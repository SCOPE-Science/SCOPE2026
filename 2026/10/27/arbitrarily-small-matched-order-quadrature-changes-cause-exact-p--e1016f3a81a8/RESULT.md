# Arbitrarily small matched-order quadrature changes cause exact policy cycles in a one-node HJB finite element method

## Finding
Fix the smooth control data and single-hat finite element space in the next section. For **every** \(0<\varepsilon<1/16\), the two positive cellwise quadrature rules \(Q_0\) (midpoint) and \(Q_\varepsilon\) (equal-weight symmetric points at distance \(\varepsilon\) from the midpoint) both integrate every affine polynomial exactly. Their difference on smooth integrands is \(O(\varepsilon^2)\). Nevertheless, if \(Q_0\) assembles the policy-evaluation operator and \(Q_\varepsilon\) assembles the right-hand side, the nonresidual policy iteration has the globally reached exact two-cycle
\[
 a_-=1-\frac{\varepsilon^2}{3},\qquad
 a_+=1+\frac{\varepsilon^2}{2},\qquad
 a_+-a_-=\frac{5\varepsilon^2}{6}.
\]
It never converges for any initial scalar coefficient, including an initial exact solution (with either tie policy). The consistent-midpoint discrete HJB equation is nevertheless strictly increasing and has the unique root \(a=1\); with matching quadrature both versions of policy iteration attain it in one step.

For the **same** mismatched pair of rules, residual-form policy iteration becomes, after at most one update, a linear contraction of exact factor \(2\varepsilon^2/3\) to the different limit
\[
 a_* = 1+\frac{\varepsilon^2}{3-2\varepsilon^2}.
\]
The first conclusion is a zero-tolerance obstruction: no positive quadrature-difference tolerance alone guarantees convergence of nonresidual policy iteration even for this fixed smooth problem, positive rules of the same affine exactness, one interior degree of freedom and a strongly monotone consistent discrete equation. The contrasting residual-form behavior explains the qualitative difference between the two assembly forms without asserting that either mismatched form solves the original consistent discrete equation.

More generally, for any replacement quadrature \(\widetilde Q\) on the right, put \(p=\widetilde Q(f_0\phi)\) and \(q=\widetilde Q(b_1\phi)\). When the two inequalities are strict, its nonresidual iteration has a two-cycle **if and only if** \(p>2\) and \(p+q<3\); it has two distinct fixed points with separate basins if and only if \(p<2\) and \(p+q>3\). Both phase regimes follow from exact two-branch dynamics rather than finite iterate tests.

## Assumptions and scope
Let \(\Omega=(0,2)\) have the two unit cells \((0,1)\) and \((1,2)\), and impose zero Dirichlet boundary values. Let \(V_h=\operatorname{span}\{\phi\}\), where
\[
 \phi(x)=\begin{cases}x,&0\le x\le1,\\2-x,&1\le x\le2.\end{cases}
\]
Choose fixed smooth functions \(\chi_L,\chi_R\in C_c^\infty(\Omega)\), taking values in \([0,1]\), supported respectively inside \((1/4,3/4)\) and \((5/4,7/4)\), and equal to one when \(|x-1/2|\le1/8\) and \(|x-3/2|\le1/8\), respectively. Such standard smooth cutoffs exist. Define
\[
 d(x)=\chi_L(x)(x-1/2)^2+\chi_R(x)(x-3/2)^2,
 \qquad b_1(x)=2\chi_L(x)\bigl(1-2(x-1/2)^2\bigr).
\]
Then \(b_1\ge0\), \(b_1\) is supported strictly inside the left cell, and all the following coefficients are fixed and smooth independently of \(\varepsilon\):
\[
 b(x,0)=0,\quad b(x,1)=b_1(x),\qquad
 f(x,0)=f_0(x)=2+d(x),\quad f(x,1)=f_1(x)=f_0(x)+b_1(x).
\]
The control set is \(\{0,1\}\). The semilinear HJB weak residual for trial \(u=a\phi\) and test \(\phi\) is
\[
 \mathcal F(a)=\int_\Omega\bigl(a|\phi'|^2+H(x,a\phi')\phi\bigr)\,dx,\qquad
 H(x,z)=\max_{\alpha\in\{0,1\}}\{b(x,\alpha)z-f(x,\alpha)\}.
\]
On each unit cell, \(Q_0\) is the midpoint rule of weight one. On each cell, \(Q_\varepsilon\) uses the two nodes midpoint \(\pm\varepsilon\), each of weight \(1/2\). The left bilinear form in **both** policy iterations is assembled with \(Q_0\), while the nonresidual right-hand forcing or residual-form nonlinear residual is assembled with \(Q_\varepsilon\). Computation is in exact arithmetic. At a policy tie, either control is permitted. A smooth continuum solution is not assumed to lie in \(V_h\).

## Proof
**1. Pointwise policy and consistent residual.** On the support of \(b_1\), \(\phi'=1\), and
\[
 b(x,1)a\phi'-f(x,1)-\bigl(b(x,0)a\phi'-f(x,0)\bigr)=b_1(x)(a-1).
\]
Thus the maximizing policy is control zero for \(a<1\) and control one for \(a>1\) wherever the controls differ; outside this support the controls are identical. The midpoint stiffness is \(Q_0(|\phi'|^2)=2\). The midpoint drift contribution in policy one is \(Q_0(b_1\phi'\phi)=2(1/2)=1\), and the midpoint forcing terms are \(Q_0(f_0\phi)=2\) and \(Q_0(f_1\phi)=3\). Therefore the midpoint-discretized nonlinear residual is exactly
\[
 F_0(a)=2(a-1)+(a-1)_+.
\]
Its slopes are \(2\) and \(3\), so it is strictly increasing with unique zero \(1\). Under matching midpoint quadrature, either frozen-policy equation is solved at \(a=1\), from every initial value, for both formulations.

**2. All quadrature moments.** Since \(0<\varepsilon<1/16\), every shifted node lies in a region where the cutoffs are exactly one (near the corresponding midpoint). At those nodes, \(d=\varepsilon^2\), while at left nodes \(b_1=2-4\varepsilon^2\) and at right nodes \(b_1=0\). Symmetry gives \(Q_\varepsilon(\phi)=1\), and each cell contributes \(1/2\) to this sum. Consequently
\[
 p_\varepsilon=Q_\varepsilon(f_0\phi)=2+\varepsilon^2,
 \qquad q_\varepsilon=Q_\varepsilon(b_1\phi)=1-2\varepsilon^2.
\]
Each quadrature has positive weights and is exact on cellwise affine polynomials. Taylor's theorem implies for any \(C^2\) test integrand \(g\) on either cell
\[
 |Q_\varepsilon(g)-Q_0(g)|\le\frac{\varepsilon^2}{2}\|g''\|_\infty;
\]
thus the two rules approach each other on all fixed smooth data despite producing distinct dynamics.

**3. Nonresidual update and phase test.** The fixed-control policy equations use the midpoint matrix scalars \(2\) and \(3\), but the right-hand scalars \(p_\varepsilon\) and \(p_\varepsilon+q_\varepsilon\). Hence, for \(a\ne1\),
\[
 T_{\rm nr}(a)=\begin{cases}
 p_\varepsilon/2=1+\varepsilon^2/2,&a<1,\\
 (p_\varepsilon+q_\varepsilon)/3=1-\varepsilon^2/3,&a>1.
 \end{cases}
\]
The two images lie strictly on opposite sides of the switching threshold in reversed order. They therefore map into one another, and every starting value enters this exact primitive two-cycle after one update. At \(a=1\), the available tie policies produce one of these two points. The cycle length is \(5\varepsilon^2/6\). The residual of the **consistent** discrete equation alternates between \(F_0(a_-)=-2\varepsilon^2/3\) and \(F_0(a_+)=3\varepsilon^2/2\), so neither the iterates nor their consistent residuals converge. For a general right-hand rule \(\widetilde Q\), the images are \(p/2\) and \((p+q)/3\); comparing each with one proves the strict cycle and two-fixed-point criteria stated above. The remaining strict cases reach a single fixed point in at most two updates.

**4. Residual-form update.** With the nonlinear residual assembled under \(Q_\varepsilon\) but frozen-policy derivative under \(Q_0\), the exact sampled residual is
\[
 F_\varepsilon(a)=2(a-1)-\varepsilon^2+(1-2\varepsilon^2)(a-1)_+.
\]
The residual update is \(T_{\rm r}(a)=a-F_\varepsilon(a)/2\) for \(a<1\) and \(T_{\rm r}(a)=a-F_\varepsilon(a)/3\) for \(a>1\). Below the switch it lands exactly at \(1+\varepsilon^2/2>1\); at a tie, either denominator yields a value above one. Above the switch, the map is
\[
 T_{\rm r}(a)=1+\frac{\varepsilon^2}{3}+\frac{2\varepsilon^2}{3}(a-1).
\]
It preserves the half-line \(a>1\) and contracts there by the positive factor \(2\varepsilon^2/3<1\). Its unique fixed point is \(a_*=1+\varepsilon^2/(3-2\varepsilon^2)\). The consistent residual at this point is \(F_0(a_*)=3\varepsilon^2/(3-2\varepsilon^2)>0\), so convergence is to a biased sampled-residual solution, not the consistent midpoint Galerkin solution.

## Verification
The standalone `checks.py` evaluates the two cell quadratures using exact rational numbers (not rounded integrals). It reconstructs the moments, policy matrices, period-two orbit, consistent and mismatched residuals, fixed point, and exact linear contraction identity for eight rational node offsets between \(1/32\) and \(1/4096\). Run with `python3 checks.py`; it uses only the Python standard library. The infinite-iteration and every-\(\varepsilon\) statements follow from the preceding two-branch identities, not from the finite checks.

## Relationship to prior work
Hall, Smears, Süli and Wells (2026) establish and illustrate that nonmatching quadrature in finite-element policy iteration can destroy convergence of the nonresidual form and reduce the residual form to linear convergence; their equations (8) and (9) are the algorithms specialized here. The new claim is **not** the general existence of quadrature sensitivity. It is the simultaneous *fixed smooth PDE / one-degree-of-freedom / positive same-affine-order symmetric rules / arbitrarily small quadrature perturbation* construction, together with exact global period-two behavior, its amplitude and residual floor, a strict two-moment phase criterion, and the contrasting exact biased residual-iteration rate. The source's numerical examples and generic observation do not logically imply this uniform zero-tolerance construction or these formulas.

Bokanowski, Maroso and Zidani (2009) analyze exact Howard iterations in terms of a consistent family of policy residuals, with finite termination under suitable monotonicity and finite-control assumptions. Here the policy choice uses the midpoint residual while the nonresidual policy solve uses a *different* sampled forcing; thus it is not an exact Howard iteration for a single Bellman system. Their exact-evaluation convergence theorem does not cover this mismatch. This observation uses the mathematical hypotheses, not merely differing titles or years.

## Limitations
The result is about a specific smooth, fixed one-dimensional two-control HJB model, one interior piecewise-linear degree of freedom, and its two precisely defined quadrature assembly conventions. The consistent discrete root lies at a policy tie, which is the mechanism allowing arbitrarily small perturbations to create chattering; no conclusion is drawn for all strictly complementary solutions, other nonlinear discretizations, or fully integrated continuum solutions. The residual-form limit solves the sampled nonlinear residual, not the original midpoint discrete equation. Rates and cycles are exact-arithmetic statements and make no claim about implementation stopping tests or floating-point rounding. Historical equivalence in literature not indexed or materially accessible remains possible.

## References
1. T. Hall, I. Smears, E. Süli, H. Wells, *The Effect of Quadrature on the Convergence of Policy Iteration for Hamilton-Jacobi-Bellman Equations*, arXiv:2606.24806v1, first public version 2026-06-23. https://arxiv.org/abs/2606.24806
2. O. Bokanowski, S. Maroso, H. Zidani, *Some Convergence Results for Howard's Algorithm*, SIAM Journal on Numerical Analysis 47 (2009), 3001–3026, DOI:10.1137/08073041X; public INRIA manuscript dated 2007-10-15. https://www.researchgate.net/publication/29647850_Some_Convergence_Results_for_Howard%27s_Algorithm
