# Universal edge-support threshold in Kirchhoff-index design of clique windmills

## Finding
Fix integers \(s,r\ge 2\), a total conductance-cost budget \(B>0\), and positive unit prices \(P,Q\). Form the clique windmill \(W_{s,r}=K_1\vee(sK_r)\), with \(M=sr\) peripheral vertices and \(N=M+1\) total vertices. A spoke from the common hub costs \(P\) per unit conductance and an edge internal to a peripheral clique costs \(Q\) per unit conductance. All individual conductances may be chosen independently, including zero, subject to connectivity and budget \(B\). Minimize the Kirchhoff index \(\mathcal K=\sum_{u<v}R_{\mathrm{eff}}(u,v)=N\operatorname{tr}(L^\dagger)\).

**Universal support transition.** Write \(\Theta=2N/M=2+2/(sr)\). The unique global optimizer assigns strictly positive conductance to every clique-internal edge if and only if \(Q/P<\Theta\). At \(Q/P\ge\Theta\), every internal clique-edge conductance is zero, all \(M\) spoke conductances are \(B/(MP)\), and \(\mathcal K_*=M^3P/B\). This threshold depends on \(s,r\) only through their product \(sr\), even though the optimal positive internal conductances depend separately on the clique geometry.

For \(Q/P<\Theta\), let
\[
A=s(r-1),\quad C=s-1+\frac1N,\quad E=MP,\quad F=\frac{s(r-1)Q}{2},\quad
z=\sqrt{\frac{A(E-F)}{CF}}>1.
\]
The unique optimum has a common spoke conductance \(a_*\) and a common internal edge conductance \(b_*\) given by
\[
a_* = \frac{B}{E+F(z-1)},\qquad b_* = \frac{a_*(z-1)}r,
\]
with exact optimal value
\[
\boxed{\mathcal K_* = \frac{N}{B}\big(\sqrt{C(E-F)}+\sqrt{AF}\big)^2.}
\]
At the threshold equality \(Q/P=\Theta\), the unique optimum is the all-spoke star, with no coexistence of distinct optimal supports.

## Assumptions and scope
A finite simple undirected graph has one central vertex, \(s\) pairwise disjoint peripheral cliques each of size \(r\), all spokes connecting every peripheral vertex to the central vertex, and no edges between peripheral cliques. For each graph edge choose a real, nonnegative conductance. Prices are \(P\) per unit on each spoke and \(Q\) per unit on each internal edge, so the total cost is at most \(B\). The positive-conductance subgraph must be connected. The effective resistance is computed using the weighted combinatorial Laplacian; \(L^\dagger\) denotes its Moore--Penrose pseudoinverse. The result concerns the Kirchhoff index, not maximum resistance, consensus leader placement, or a fastest-mixing chain. Distinct clique edges and spokes are independently adjustable; no symmetry is assumed of candidate allocations.

## Proof
**Step 1: existence and uniqueness.** The feasible weights are in a compact nonnegative budget simplex. Every sequence approaching a disconnected weighted graph has an additional Laplacian eigenvalue tending to zero and hence Kirchhoff index tending to \(+\infty\). A connected feasible point exists (uniform positive spokes). Thus a minimum exists and is connected. Its budget constraint is active: scaling all positive weights by any factor greater than one decreases all effective resistances by the reciprocal factor.

On the orthogonal complement \(\mathbf1^\perp\), the weighted Laplacian is positive definite. The map \(X\mapsto\operatorname{tr}(X^{-1})\) is strictly convex over positive-definite matrices, since for a nonzero symmetric perturbation \(H\) the second derivative is \(2\operatorname{tr}(X^{-1}HX^{-1}HX^{-1})>0\). Here the symmetric matrix \(X^{-1/2}HX^{-1/2}\) is nonzero, so the derivative is strictly positive. On a simple graph the map from edge conductances to the restricted Laplacian is injective: vanishing on \(\mathbf1^\perp\), together with zero row sums, would force the entire Laplacian difference to vanish; distinct off-diagonal entries recover every edge weight. Consequently \(\operatorname{tr}(L^\dagger)\) is strictly convex along distinct feasible connected weight assignments and the minimizer is unique.

The graph's automorphism group acts transitively on all spokes and also on all edges inside peripheral cliques; these permutations preserve both prices and objective. Uniqueness therefore forces a common spoke weight \(a\) and common internal weight \(b\). Since \(s\ge2\), a connected symmetric allocation has \(a>0\), while \(b\ge0\).

**Step 2: exact spectrum.** For the symmetric weights the Laplacian spectrum, including multiplicities, is
\[
0\ (1),\quad a+rb\ (s(r-1)),\quad a\ (s-1),\quad Na\ (1).
\]
Within each clique, zero-sum fluctuations give the first positive eigenvalue; contrasts of constant clique values give the second; the final hub-against-all-peripheral mode gives the last. Thus
\[
\operatorname{tr}(L^\dagger)=\frac{A}{a+rb}+\frac Ca,
\quad A=s(r-1),\quad C=s-1+\frac1N.
\]
The exact budget identity is \(MPa+sr(r-1)Qb/2=B\).

**Step 3: optimize globally in the symmetric slice.** Put \(u=a\), \(v=a+rb\), \(E=MP\), and \(F=s(r-1)Q/2\). Then \(0<u\le v\), the cost constraint becomes \((E-F)u+Fv=B\), and the objective is \(C/u+A/v\). If \(Q/P<2N/M\), then \(E-F>0\) and the interior first-order condition from the multiplier for the budget is
\[
\frac vu=\sqrt{\frac{A(E-F)}{CF}}=:z.
\]
The stated price inequality is *equivalent* to \(z>1\) (use \(A+C=M^2/N\)). Cauchy--Schwarz gives, for all positive \(u,v\) on this budget hyperplane,
\[
\frac Cu+\frac Av\ge\frac{(\sqrt{C(E-F)}+\sqrt{AF})^2}{B},
\]
with equality exactly at the displayed ratio and the stated optimal conductances.

At the constrained boundary \(b=0\), write \(a=(B-sr(r-1)Qb/2)/(MP)\). Direct differentiation of the objective at \(b=0^+\) gives
\[
\left.\frac{d}{db}\operatorname{tr}(L^\dagger)\right|_{b=0^+}
=\frac{M(r-1)}{a^2}\left(\frac{MQ}{2NP}-1\right).
\]
This is nonnegative exactly when \(Q/P\ge2N/M\). Convexity then makes \(b=0\) the global optimum of the symmetric slice; global strict convexity makes it the *unique* optimizer over every asymmetric feasible allocation. The star value follows from \(A+C=M^2/N\) and \(a=B/(MP)\): \(N(A+C)/a=M^3P/B\). This also proves all boundary and equality cases.

## Verification
A standalone finite checker, `verify.py`, uses exact symbolic inverses and numerical optimization to corroborate this proof. Its recorded completed run is `verification_run.txt`. It performs 81 exact-rational pseudoinverse-trace comparisons, 81 positive eigenspace-multiplicity checks, 30 unrestricted edgewise numerical optimizations, 3,000 independently chosen asymmetric budget-feasible resistance comparisons, and 48 support-boundary tests. The infinite theorem is established by the strict-convexity and spectral derivation above, not by finite testing.

## Relationship to prior work
Ghosh, Boyd, and Saberi developed convex effective-resistance minimization with budgeted conductances and analyzed several special graph families, including trees and a barbell. Their inspected conference paper and longer account provide the underlying optimization framework but do not state the present clique-windmill global support transition. Sardar and Xu study resistance distance and Kirchhoff index of windmill graphs with fixed unit edge resistances, a different optimization question; only the abstract was available for material comparison. Johnson and Chertkov study broad network-design objectives rather than this all-budget exact class-dependent price transition. The theorem refines the general framework by providing a complete support classification and explicit conductances for independently adjustable windmill networks.

## Limitations
The result requires equal costs within the spoke class and within the internal-edge class, and exact undirected conductance allocation. It does not classify nonuniform price vectors or objectives other than total effective resistance. A specialized prior exact windmill design theorem may exist outside the primary material examined; the 2024 fixed-weight windmill article's full text was not accessible and absolute literature priority is unverified. Computational checks cover finite cases only. No independent mathematical audit has been performed.

## References
1. A. Ghosh, S. Boyd, and A. Saberi, *Minimizing Effective Resistance of a Graph*, 17th International Symposium on Mathematical Theory of Networks and Systems (2006), https://web.stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf ; later expanded account in *SIAM Review*, 50(1) (2008), https://studyres.com/doc/19597605/minimizing-effective-resistance-of-a-graph .
2. Z. Sardar and X. Xu, *Resistance Distance and Kirchhoff Index in Windmill Graphs* (2024), https://doi.org/10.2174/0115701794299562240606054510 . Full article not reviewed.
3. J. K. Johnson and M. Chertkov, *A Majorization-Minimization Approach to Design of Power Transmission Networks* (2010), https://arxiv.org/abs/1004.2285 .
