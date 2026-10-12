# Voronoi-only slack can return boundary generators in VCG
## Finding
Khademi's VCG method forms a Voronoi cell \(V_i\subseteq\mathcal X\) from affine bisector inequalities \(g_j(x)\le 0\) and chooses a restart by solving
\[
\min_{x\in\mathcal X,\,\tau\in\mathbb R}\tau
\quad\text{{subject to}}\quad g_j(x)\le\tau\quad(j\ne i).
\]
The paper's Proposition 1 states that an optimum with \(\tau^*<0\) lies in the interior of \(V_i\) relative to its affine hull. This implication is false even in one dimension.

Take the full-dimensional compact convex set \(\mathcal X=[0,1]\) and two centers \(p^1=0\), \(p^2=1\). For the cell of \(p^1\), the source formula gives \(g_2(x)=x-1/2\), hence \(V_1=[0,1/2]\). The slack problem has the unique optimum \(x^*=0\), \(\tau^*=-1/2\), but \(\operatorname{{relint}}(V_1)=(0,1/2)\). Thus \(x^*\notin\operatorname{{relint}}(V_1)\) despite \(\tau^*<0\). The second cell is symmetric: it returns \(x^*=1\), \(\tau^*=-1/2\), while \(\operatorname{{relint}}(V_2)=(1/2,1)\).

Consequently, the two VCG exploration solves can return exactly the two existing generators instead of new cell-interior restart locations. The source proof establishes strictness of the Voronoi-bisector inequalities inside \(\mathcal X\); it does not establish strictness with respect to the boundary of \(\mathcal X\).

## Assumptions and scope
The counterexample uses exactly the assumptions stated in Proposition 1: \(\mathcal X\subset\mathbb R\) is full-dimensional, compact, and convex. The center set consists of two distinct points in \(\mathcal X\). No property of the objective function, conditional-gradient step-size rule, or later VCG levels is needed, because the claim being tested concerns only the cell-restart auxiliary problem.

The finding does not claim that every VCG run fails, nor that VCG cannot work empirically. It identifies a false geometric guarantee in the restart construction and an exact level at which the proposed exploration primitive can return old generators.

## Proof
For \(p^1=0\) and \(p^2=1\), the paper defines
\[
g_2(x)=(p^2-p^1)x-\frac12(p^2-p^1)(p^2+p^1)=x-\frac12.
\]
Therefore
\[
V_1=\{{x\in[0,1]:x-1/2\le0}}\}=[0,1/2].
\]
The auxiliary problem for this cell is
\[
\min_{0\le x\le1,\,\tau\in\mathbb R}\tau
\quad\text{{subject to}}\quad x-\frac12\le\tau.
\]
At any optimum the inequality is tight, because lowering \(\tau\) until equality improves the objective. Hence minimizing \(\tau\) is equivalent to minimizing \(x-1/2\) over \([0,1]\), whose unique minimizer is \(x^*=0\). Thus \(\tau^*=-1/2<0\). Since the affine hull of \(V_1\) is \(\mathbb R\),
\[
\operatorname{{relint}}(V_1)=(0,1/2),
\]
so \(x^*=0\notin\operatorname{{relint}}(V_1)\).

For the cell of \(p^2\), the sole bisector function is \(g_1(x)=-x+1/2\). Its auxiliary problem uniquely minimizes at \(x^*=1\), again with \(\tau^*=-1/2\), while \(V_2=[1/2,1]\) has relative interior \((1/2,1)\).

The source proof uses \(g_j(x^*)<0\) to obtain a neighborhood satisfying the bisector inequalities after intersecting with \(\mathcal X\). That proves local strictness only in the topology inherited from \(\mathcal X\). A boundary point of \(\mathcal X\), such as \(0\), can have this property without lying in the relative interior of the cell in its affine hull.

A standard polyhedral repair is to maximize an inscribed-ball radius against *all* defining halfspaces of the cell, including those of \(\mathcal X\). If \(\mathcal X=\{{x:a_m^\top x\le b_m}}\), an actual Chebyshev-center formulation includes constraints \(a_m^\top x+r\lVert a_m\rVert_2\le b_m\) as well as normalized Voronoi halfspace constraints. This observation explains exactly which boundary margin is absent from the source auxiliary problem.

## Verification
The formulas above are exact rational identities. The bundled `verify.py` checks both cells with rational arithmetic, including the unique auxiliary optima, negative slack values, and failure of relative-interior membership. Its output is supplementary; the infinite/geometric statement follows directly from the analytic inequalities above.

The primary full text was inspected at the definitions of the Voronoi cells, auxiliary problem (5), Proposition 1 and its proof, and Algorithm 2. The source explicitly assumes a full-dimensional compact convex feasible set and uses \(\tau^*<0\) as the trigger for a cell restart.

## Relationship to prior work
The source paper itself asserts the opposite implication in Proposition 1; it does not contain this counterexample. Targeted searches for the source title together with “interior point,” “boundary,” “relative interior,” “slack problem,” and restart aliases did not locate a published correction or an implication-equivalent result in the searched corpus.

The classical Chebyshev-center formulation for a polyhedron treats every defining halfspace when maximizing an inscribed radius. That standard construction explains why omitting the feasible-set boundary can invalidate an interior certificate, but it does not state or imply the source-specific two-center VCG counterexample without applying it to problem (5).

## Limitations
This is a geometric counterexample to the stated interior guarantee and to the novelty of restart locations at one VCG level. It does not analyze the objective-dependent conditional-gradient trajectories after those restart points, global convergence, or the empirical benchmark results. A later revision of the preprint could change Proposition 1 or the auxiliary problem; the claim here concerns the public version inspected under the cited identifier.

## References
1. Abbas Khademi, “Voronoi Conditional Gradient Method for Constrained Nonconvex Optimization,” Optimization Online, first public record 2026-02-13, OptimizationOnline:33571, https://optimization-online.org/2026/02/voronoi-conditional-gradient-method-for-constrained-nonconvex-optimization/ .
2. S. Boyd and L. Vandenberghe, *Convex Optimization*, §4.3.1 (Chebyshev center); companion CVX example: https://cvxr.com/cvx/examples/cvxbook/Ch04_cvx_opt_probs/html/chebyshev_center_2D.html .
