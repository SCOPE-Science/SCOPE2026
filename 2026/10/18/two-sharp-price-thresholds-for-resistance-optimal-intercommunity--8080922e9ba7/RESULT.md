# Two sharp price thresholds for resistance-optimal intercommunity designs

## Finding
Let \(p\ge q\ge2\) be integers, \(N=p+q\), \(B>0\), and \(t>0\). Partition \(N\) labeled vertices into groups of sizes \(p\) and \(q\). Every vertex pair is an available undirected edge. Each cross-group edge costs one unit per unit conductance; each edge internal to either group costs \(t\) units per unit conductance. Independently choose nonnegative conductances with total cost \(B\), minimizing the sum \(J\) of all pairwise effective resistances; disconnected positive-conductance supports have objective \(+\infty\).

Set
\[
H=\frac{p-1}{q}+\frac{q-1}{p}+\frac1N,\qquad
H_q=\frac{q-1}{p}+\frac1N,
\]
\[
t_{\mathrm{on}}=\frac{2p}{qH},\qquad
t_{\mathrm{fill}}=\frac{2pN}{2pN-2p-q}.
\]
There is **exactly one global optimum**, even though all edges are independently adjustable. At that optimum all edges within the larger group have the same conductance \(x\), all edges within the smaller group have the same conductance \(y\), and all cross-group edges have the same conductance \(z>0\). Its **complete classification** is as follows.

1. For \(t\ge t_{\mathrm{on}}\):
\[
x=y=0,\qquad z=\frac{B}{pq}.
\]
Only cross-group connections are used.

2. When \(p>q\) and \(t_{\mathrm{fill}}\le t<t_{\mathrm{on}}\), put
\[
D_1=pq-\frac{(p-1)qt}{2},\qquad
r=\sqrt{\frac{2D_1}{tH_q}}.
\]
Then
\[
z=\frac{B}{D_1+\frac12(p-1)tr},\qquad
x=\frac{(r-q)z}{p},\qquad y=0.
\]
Precisely the larger group's internal edges are used, in addition to all cross-group edges. At the lower threshold \(t=t_{\mathrm{fill}}\), the smaller group's internal conductances remain zero.

3. For \(0<t<t_{\mathrm{fill}}\), put
\[
D_2=pq-\frac t2\big((p-1)q+(q-1)p\big),\qquad
f=\sqrt{\frac{2ND_2}{t}}.
\]
Then
\[
z=\frac{B}{D_2+\frac12(N-2)tf},\qquad
x=\frac{(f-q)z}{p},\qquad y=\frac{(f-p)z}{q}.
\]
All three edge classes have strictly positive conductance.

When \(p=q\), the two thresholds coincide at \(4p/(4p-3)\), and the one-internal-group phase disappears. When \(p>q\), \(t_{\mathrm{fill}}<t_{\mathrm{on}}\), so the middle phase has strictly positive width. The limits with \(q\) fixed and \(p\to\infty\) are \(t_{\mathrm{on}}\to2\) and \(t_{\mathrm{fill}}\to1\).

The minimum **total** effective resistance (not the average and not the trace alone) is, in the three respective regimes,
\[
J^*=\frac{NpqH}{B},
\]
\[
J^*=\frac{\big((p-1)\sqrt{Nt/2}+\sqrt{NH_qD_1}\big)^2}{B},
\]
\[
J^*=\frac{\big((N-2)\sqrt{Nt/2}+\sqrt{D_2}\big)^2}{B}.
\]
The formulas extend continuously to the applicable price boundaries.

## Assumptions and scope
The vertex partition is fixed, the graph is simple and complete as a *set of available edges*, the budget is exactly spent, and every conductance is nonnegative. Prices are homogeneous within each of the three edge orbits, but the optimization imposes **no orbit symmetry**: that symmetry is a conclusion. The Laplacian uses each conductance once in the standard convention \(L_{uv}=-w_{uv}\) for distinct vertices; for a connected network, \(J=N\operatorname{tr}L^+\), where \(L^+\) is the Moore–Penrose pseudoinverse. Edges having zero optimal conductance are absent from the operational support. Both threshold equalities are included.

## Proof
**Existence, strict convexity, and symmetry.** Write \(L(w)=\sum_e w_e b_e b_e^{\mathsf T}\), with \(b_e\) the unsigned-choice incidence difference. For connected support the matrix \(A=L(w)+\mathbf1\mathbf1^{\mathsf T}/N\) is positive definite, and \(J=N(\operatorname{tr}A^{-1}-1)\). On the affine budget hyperplane, the feasible weights are bounded. As connectivity is lost, a nonzero Laplacian eigenvalue approaches zero and \(J\to+\infty\); a connected feasible allocation exists, so the minimum is attained. For every nonzero symmetric Laplacian perturbation \(H\),
\[
\frac{d^2}{ds^2}\operatorname{tr}(A+sH)^{-1}\bigg|_{s=0}
=2\operatorname{tr}(A^{-1}HA^{-1}HA^{-1})>0.
\]
The inequality follows by writing the trace as the squared Frobenius norm of \(A^{-1/2}HA^{-1}\). Distinct edge weights produce distinct Laplacians because their off-diagonal entries recover each weight. Thus \(J\) is strictly convex in all independently adjustable conductances and the optimum is unique. Permutations within either group preserve cost and objective; uniqueness forces a common weight \(x\) on its \(\binom p2\) edges, a common weight \(y\) on the other \(\binom q2\) edges, and a common weight \(z\) on the \(pq\) cross edges. Finite objective forces \(z>0\).

**Exact spectrum.** The nonzero eigenvalues of this three-class Laplacian are
\[
px+qz\quad(p-1\text{ times}),\qquad qy+pz\quad(q-1\text{ times}),\qquad Nz\quad(1\text{ time}).
\]
These follow by decomposing vertex functions into the zero-sum subspaces within each group and the one-dimensional group-contrast subspace. Consequently the entire independent-edge problem reduces *without loss* to
\[
J=N\left(\frac{p-1}{px+qz}+\frac{q-1}{qy+pz}+\frac1{Nz}\right),
\]
subject to
\[
\frac{tp(p-1)}2x+\frac{tq(q-1)}2y+pqz=B,
\qquad x,y\ge0,\quad z>0.
\]

**Optimality conditions.** Set \(U=px+qz\) and \(V=qy+pz\). The magnitudes of the objective derivatives *per unit price* for the three classes are respectively
\[
\frac{2N}{tU^2},\qquad \frac{2N}{tV^2},\qquad
\frac{N}{pq}\left(\frac{(p-1)q}{U^2}+\frac{(q-1)p}{V^2}+\frac1{Nz^2}\right).
\]
At an active class these equal a common positive multiplier; at an inactive class its derivative magnitude cannot exceed the multiplier. Strict convexity makes these conditions necessary and sufficient.

If \(x=y=0\), then \(U=qz\), \(V=pz\), and the inactive-class inequalities reduce to
\[
t\ge\frac{2p}{qH},\qquad t\ge\frac{2q}{pH}.
\]
Since \(p\ge q\), both hold exactly when \(t\ge t_{\mathrm{on}}\), yielding case 1.

If \(x>0\), \(y=0\), equating the first and third marginal ratios gives
\[
\frac Uz=r(t)=\sqrt{\frac{2pq-(p-1)qt}{tH_q}}.
\]
Here \(x>0\) is exactly \(r>q\). The inactive-class inequality for \(y\) is \(U\le pz\), or \(r\le p\). The function \(r(t)^2=2pq/(tH_q)-(p-1)q/H_q\) is strictly decreasing on its positive domain. Its crossings of \(q\) and \(p\) occur at \(t_{\mathrm{on}}\) and \(t_{\mathrm{fill}}\), respectively (direct substitution gives both identities). Thus the unique one-sided interval is case 2. Solving the budget equation after substituting \(U=rz\) gives the stated formulas. When \(p=q\), the two crossings coincide and there is no interval with only one group active; symmetry under swapping groups independently confirms this.

If \(x,y>0\), equality of the first two marginal ratios gives \(U=V\). Equating them with the cross-class ratio then gives
\[
\frac Uz=\frac Vz=f(t)=\sqrt{\frac{2Npq}{t}-N\big((p-1)q+(q-1)p\big)}.
\]
Since \(p\ge q\), both internal classes are positive exactly when \(f>p\), which is equivalent to \(0<t<t_{\mathrm{fill}}\). Solving \(U=V=fz\) and the budget gives case 3. The displayed positive-domain formulas follow directly from \(r\ge q\) or \(f>p\), so all square roots are real wherever used. The three regimes cover all positive prices and satisfy their respective complementary slackness inequalities. Uniqueness establishes that no asymmetric optimum or omitted phase exists.

**Optimum values and asymptotics.** Substitute each allocation into the exact spectral objective. Alternatively, in case 2 use Cauchy–Schwarz on \(N(p-1)/U+NH_q/z\) under \((p-1)tU/2+D_1z=B\); in case 3 use it on \(N(N-2)/U+1/z\) under \((N-2)tU/2+D_2z=B\). This yields the three displayed square formulas. At \(p=q\), direct simplification of either price threshold gives \(4p/(4p-3)\). With fixed \(q\), division by the highest power of \(p\) in their rational definitions gives the limits \(2\) and \(1\). Both threshold equality cases inherit strict global uniqueness.

## Verification
Run `python verify.py` with Python 3 and SymPy installed. The script reconstructs weighted Laplacian matrices directly from all edges, computes the trace of the exact-rational inverse of \(L+\mathbf1\mathbf1^{\mathsf T}/N\), compares it with the three-eigenvalue formula, checks budgets and edgewise full-matrix Karush–Kuhn–Tucker inequalities, checks optimal-value formulas, tests both exact price boundaries, and verifies the symbolic large-group limits. Its current run completed 752 exact assertions across five part-size pairs. Parameters are chosen so the matrix calculations are exact rational; they do not substitute for the all-size proof.

## Relationship to prior work
Ghosh, Boyd, and Saberi (2006 conference version; 2008 expanded article) established convex allocation of conductances to minimize total effective resistance, uniqueness and symmetry, and solved trees, wheels and a single-bridge barbell example. This result uses that framework but addresses a different priced complete two-part design and identifies two explicit, unequal-size support transitions. Tovar et al. (2026) study resistance-optimal architecture across nonlinear resource exponents and discuss the linear-cost marginal balance; their studied topology/cost regimes do not state this all-order two-part price classification. Bhoite et al. (2026) treat fixed-base, exact-cardinality, cost-aware graph augmentation, which is not an unrestricted allocation over all edges with simultaneous reallocation of cross-group and internal weights. None of those broader optimization frameworks by itself gives the two threshold values or the intermediate larger-part-only support without solving this specialized KKT system.

## Limitations
Only two prescribed groups with a **common** internal-edge unit price and a unit cross-edge price are treated. No claim is made for multiple groups, heterogeneous prices within each orbit, different objective functions, network reliability under discrete failures, or nonlinear power-law budgets. The result concerns total effective resistance, not spectral-gap maximization or spanning-tree determinant maximization. Analytic correctness follows from the proof; computations are finite corroboration. Equivalence with an unindexed or inaccessible existing specialization cannot be categorically excluded without independent literature review.

## References
1. A. Ghosh, S. Boyd, A. Saberi, *Minimizing Effective Resistance of a Graph*, MTNS 2006, Kyoto, July 24–28, 2006, pp. 1185–1196, https://web.stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf ; expanded SIAM Review 50 (2008), 37–66, https://doi.org/10.1137/050645452 .
2. H. Tovar, G. Vázquez-Victorio, E. Hernández-Lemus, A. Cervera, D. Pérez-Calixto, *Cost convexity controls the architecture of resistance-optimal networks*, arXiv:2610.03627 (2026), https://arxiv.org/abs/2610.03627 .
3. O. Bhoite, V. S. Dhuli, S. Werner, K. Kansanen, *Budget-Constrained Graph Augmentation for Robust Network Design via Kirchhoff Index Minimization*, arXiv:2609.29790 (2026), https://arxiv.org/abs/2609.29790 .
