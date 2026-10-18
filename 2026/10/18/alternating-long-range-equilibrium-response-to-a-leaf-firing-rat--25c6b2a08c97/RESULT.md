# Alternating long-range equilibrium response to a leaf firing rate on every finite tree

## Finding
Let \(T=(V,E)\) be any finite tree with at least one edge, with arbitrary vertex firing rates \(p_v>0\), and fix \(0<\alpha<1\). For each edge \(e\), the positive weakly reinforced edge equilibrium is the solution of
\[
\mu_e=\sum_{v\in e}p_v\frac{\mu_e^\alpha}{\sum_{f\ni v}\mu_f^\alpha}.
\]
Choose a leaf \(r\) and root the tree there. Define the depth \(d_T(r,e)\) of an edge to be zero for the edge adjoining \(r\), and to increase by one per successive edge away from \(r\). Then the unique positive equilibrium depends smoothly on all positive firing rates and satisfies, simultaneously for every edge,
\[
\boxed{(-1)^{d_T(r,e)}\frac{\partial\mu_e}{\partial p_r}>0.}
\]
In particular, increasing a single leaf firing rate *strictly increases* the equilibrium weight of every edge at even depth and *strictly decreases* that of every edge at odd depth; this holds after arbitrarily large positive changes to that firing rate, not just locally. A bottom-up recursion in the proof computes every derivative. The result concerns the deterministic equilibrium, which is the almost-sure limiting reinforcement rate in the model of Qin [1].

## Assumptions and scope
The graph is finite, connected, loop-free and acyclic, with at least two vertices. The leaf \(r\) has one incident edge. Every firing rate is strictly positive; the reinforcement exponent lies in \((0,1)\). The equilibrium components are strictly positive. The root edge has depth zero; at a branching vertex, all outgoing child edges have depth one greater than their parent edge. The derivative treats every other vertex firing rate and \(\alpha\) as fixed. There are no uniformity assumptions on the sizes or ratios of positive firing rates.

## Proof
**1. Existence, uniqueness and smoothness.** Make the change of variables \(z_e=\mu_e^\alpha\), let \(S_v=\sum_{f\ni v}z_f\), and define, for positive \(z\),
\[
\mathcal F(z;p)=\alpha\sum_{e\in E}z_e^{1/\alpha}-\sum_{v\in V}p_v\log S_v.
\]
Its gradient in edge coordinate \(e=\{u,v\}\) is
\[
\partial_e\mathcal F=z_e^{1/\alpha-1}-p_u/S_u-p_v/S_v.
\]
Thus \(\nabla\mathcal F=0\) is exactly the displayed urn-equilibrium equation after multiplication by \(z_e\). The Hessian is
\[
H_{ef}=D_e\,\mathbf1_{e=f}+\sum_{v:e,f\ni v}w_v,\qquad
D_e=\frac{1-\alpha}{\alpha}z_e^{1/\alpha-2}>0,
\quad w_v=\frac{p_v}{S_v^2}>0.
\]
For every nonzero real edge vector \(h\),
\[
h^{\mathsf T}Hh=\sum_e D_eh_e^2+\sum_v w_v\bigl(\sum_{e\ni v}h_e\bigr)^2>0.
\]
The potential is coercive as \(\|z\|\to\infty\), because the superlinear powers dominate all logarithms. A minimizing sequence cannot make any \(S_v\) tend to zero, since the corresponding term \(-p_v\log S_v\) diverges, while the other terms remain bounded below on bounded sets. If a candidate minimizer has \(z_e=0\) with all vertex sums positive, its one-sided directional derivative on increasing that coordinate is \(-p_u/S_u-p_v/S_v<0\), so it cannot minimize. Consequently the potential has a strictly positive global minimizer. Positive definiteness of its Hessian proves uniqueness. The implicit-function theorem gives smooth dependence of \(z\), and hence of \(\mu\), on the rates.

**2. Derivative as a positive-root Green vector.** Differentiate the stationarity equations with respect to the leaf rate \(p_r\). If \(e_0\) denotes the sole edge incident to \(r\), then \(S_r=z_{e_0}\) and
\[
H\frac{\partial z}{\partial p_r}=\frac{\mathbf e_{e_0}}{z_{e_0}}.
\]
It suffices to determine the signs of the unique vector \(x\) solving \(Hx=\mathbf e_{e_0}\), because
\[
\frac{\partial\mu_e}{\partial p_r}=
\frac{z_e^{1/\alpha-1}}{\alpha z_{e_0}}x_e.
\]
All prefactors are strictly positive.

**3. Exact tree elimination.** The vector \(x\) uniquely minimizes the strictly convex quadratic function
\[
Q(x)-2x_{e_0},\qquad
Q(x)=\sum_e D_ex_e^2+\sum_vw_v(\sum_{e\ni v}x_e)^2.
\]
Root the tree at leaf \(r\). Each oriented edge \(e=(u,v)\) points away from \(r\), with \(v\) the child vertex. Write \(\mathcal C(v)\) for the child edges of \(v\). Starting at terminal edges and proceeding toward the root, define strictly positive *cavity coefficients*
\[
C_e=D_e+\frac{w_v}{1+w_v\sum_{f\in\mathcal C(v)}C_f^{-1}}.
\]
The empty sum is zero. To verify this recursion, fix \(x_e=a\), retain the quadratic contributions on the downward subtree of \(v\), and minimize over all descendant edges. By induction each child subtree contributes \(C_fx_f^2\); the only remaining joint term at \(v\) is \(w_v(a+\sum_fx_f)^2\). Its unique minimizer is
\[
x_f=-\frac{w_v/C_f}{1+w_v\sum_{g\in\mathcal C(v)}C_g^{-1}}\,a,
\qquad f\in\mathcal C(v),
\]
and substitution gives the recursion for \(C_e\). Every factor multiplying \(-a\) is strictly positive. At the root, after eliminating every descendant edge, the objective becomes \((w_r+C_{e_0})x_{e_0}^2-2x_{e_0}\). Hence
\[
x_{e_0}=\frac1{w_r+C_{e_0}}>0.
\]
The child response formula now shows by induction that every edge response is nonzero and changes sign exactly once along each outward step. It follows that \((-1)^{d_T(r,e)}x_e>0\), yielding the claimed strict signed derivative. The same recursions yield its exact positive magnitude on each edge.

**4. Global monotonicity and boundary exponent.** For any two positive leaf rates with all other rates fixed, integrate the derivative along the closed interval joining them. Since its sign is strict and constant throughout the positive-rate domain, the finite difference has the same alternating sign. At \(\alpha=0\), choices at each vertex are uniform across its incident edges, so \(\mu_e=\sum_{v\in e}p_v/\deg(v)\); raising the leaf rate then changes only \(\mu_{e_0}\), establishing the stated sharp distinction from \(\alpha>0\).

## Verification
The standalone `verify_tree_sensitivity.py` uses only the Python standard library. It computes positive equilibria by damped Newton iteration, constructs the Hessian independently, evaluates the cavity recursion, compares it with a direct linear solve, checks centered finite differences and finite increases of the root firing rate, and verifies the exact mass identity \(\sum_e\mu_e=\sum_v p_v\). Run it with `python3 verify_tree_sensitivity.py`. In the packaged run, all **1,440** explicit finite checks passed across 180 deterministic path, star, balanced and irregular tree instances, with reinforcement exponents ranging from \(0.12\) to \(0.94\). These checks are supplementary; the proof above handles all finite trees and all real \(0<\alpha<1\).

## Relationship to prior work
Qin [1] proves almost-sure homogenization to a unique positive equilibrium under arbitrary positive vertex firing rates, on far more general graphs. The new statement concerns an additional comparative-static question: the sign and explicit magnitude of every response to a *single leaf firing rate*, and its strict alternating propagation to arbitrarily remote branches of every finite tree. The existence of a unique limiting equilibrium alone does not determine these cross-edge derivative signs. Couzinié and Hirsch [2] study weak reinforcement with unit firing rates and convergence on countable graphs, not variation of a leaf rate. Van der Hofstad and coauthors [3] analyze strong reinforcement and stability, including finite path/whisker examples; their parameter regime and conclusions do not give this weak-reinforcement tree susceptibility formula. The quadratic subtree-elimination step uses standard convex-analysis ideas, but the strictly signed WARM response and global finite-increment conclusion are the result asserted here.

## Limitations
This result does not assert the alternating law for cycles, infinite trees, perturbations at an internal vertex, or varying several firing rates simultaneously. At \(\alpha=0\), remote derivatives vanish and thus do not obey a strict sign law. The recursion applies to the deterministic equilibrium, not the finite-time random fluctuation field. The reported literature comparison is evidence-based, not a proof of worldwide novelty; earlier comparative-statics work under another model name could implicitly contain an equivalent special case. No independent audit has been carried out.

## References
[1] Shuo Qin, *Homogenization of weakly reinforced Pólya urns on countable networks*, arXiv:2610.11780v1, first posted 2026-10-08, https://arxiv.org/abs/2610.11780.

[2] Yannick Couzinié and Christian Hirsch, *Weakly reinforced Pólya urns on countable networks*, arXiv:2010.03347v1 (2020), https://arxiv.org/abs/2010.03347.

[3] Remco van der Hofstad, Mark Holmes, Alexey Kuznetsov and Wioletta Ruszel, *Strongly reinforced Pólya urns with graph-based competition*, arXiv:1406.0449v1 (2014); *Annals of Applied Probability* 26 (2016), 2494–2539, https://arxiv.org/abs/1406.0449.
