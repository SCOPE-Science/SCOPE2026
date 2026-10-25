# An unbounded LP gap for homological edge cuts on planar annulus wedges

## Finding

For every integer \(m\ge2\), there is a finite planar simplicial \(2\)-complex \(K_m\) and a primitive integral \(1\)-cycle \(c_m\), with every nonzero edge coefficient equal to \(\pm1\), for which
\[
\operatorname{MHC}(K_m,[c_m],1)\ge m,
\qquad
\operatorname{LP}(K_m,c_m)\le \frac{2m-1}{m}<2.
\]
Here \(\operatorname{MHC}\) is the minimum cardinality of an edge set \(C\) for which \([c_m]\) is not in the image of \(H_1(K_m-C;\mathbb R)\to H_1(K_m;\mathbb R)\), and
\[
\operatorname{LP}(K,c)=\min_{\phi\in C^1(K;\mathbb R)}\{\|\phi\|_1:\delta\phi=0,\ \phi(c)=1\}.
\]
Consequently, \(\operatorname{MHC}(K_m,[c_m],1)/\operatorname{LP}(K_m,c_m)>m/2\). In particular, the integrality gap of this \(\ell^1\) relaxation is unbounded even on finite planar complexes and for primitive integral cycle chains.

## Assumptions and scope

All complexes are finite and simplicial; homology and cohomology are over \(\mathbb R\). An edge cut removes the chosen edges and all simplices containing them, as in the minimum homological edge-cut problem. The norm \(\|\phi\|_1\) is the unweighted sum of absolute values of the edge-cochain coefficients. The conclusion concerns this LP objective as a surrogate for the cardinality of a homological edge cut; it does not assert that every LP-based algorithm or every strengthened relaxation has the same gap.

## Proof

For each \(m\), take a triangulated annulus \(A_m\) with \(m\) pairwise edge-disjoint parallel essential cycles \(C_0,\ldots,C_{m-1}\). Label the vertices of ring \(j\) by \(v_{j,0},v_{j,1},v_{j,2}\), cyclically. For each strip between rings \(j\) and \(j+1\), triangulate its three quadrilaterals with triangles \([v_{j,i},v_{j,i+1},v_{j+1,i+1}]\) and \([v_{j,i},v_{j+1,i},v_{j+1,i+1}]\), with indices modulo \(3\). Orient each ring cyclically. Let \(e_j=[v_{j,2},v_{j,0}]\) be its wraparound edge and \(d_j=[v_{j,2},v_{j+1,0}]\) the corresponding diagonal in strip \(j\). Define the cochain \(\eta_m\) to equal \(1\) on the \(m\) edges \(e_j\), equal \(1\) on the \(m-1\) diagonals \(d_j\), and zero on every other edge. The only triangles containing a nonzero cochain edge are the two triangles on either side of each \(d_j\); in each, the two nonzero boundary contributions have opposite signs. Thus \(\delta\eta_m=0\), \(\eta_m(C_j)=1\) for every \(j\), and \(\|\eta_m\|_1=2m-1\). Each ring represents the same generator \(\gamma\in H_1(A_m;\mathbb R)\).

Let \(K_m\) be the wedge at one vertex of two copies \(A_m^{(1)}\) and \(A_m^{(2)}\). Write \(C_j^{(i)}\) for the rings in copy \(i\), and set
\[
c_m=C_1^{(1)}+\sum_{j=1}^{m}C_j^{(2)}.
\]
The rings have disjoint edge supports, so this is an integral cycle whose nonzero coefficients are \(\pm1\). Its homology class is \([\gamma_1]+m[\gamma_2]\), where \([\gamma_i]\) generates the first homology of the corresponding annulus. Since \(H_1(K_m;\mathbb Z)\cong\mathbb Z^2\) and \(\gcd(1,m)=1\), the class itself is primitive and nonzero.

If an edge set \(C\) has fewer than \(m\) edges, it cannot meet all \(m\) edge-disjoint rings in either annulus. Thus some ring in each annulus survives in \(K_m-C\). Since the rings in each annulus are homologous, the surviving first-annulus ring plus \(m\) times a surviving second-annulus ring represents \([c_m]\) in \(H_1(K_m;\mathbb R)\). Therefore \([c_m]\) remains in the image from \(K_m-C\), so \(\operatorname{MHC}(K_m,[c_m],1)\ge m\).

For the LP upper bound, extend \(m^{-1}\eta_m\) from the second annulus by zero on the first annulus, obtaining \(\phi_m\in C^1(K_m;\mathbb R)\). It is a cocycle, and
\[
\phi_m(c_m)=m^{-1}\sum_{j=1}^{m}\eta_m(C_j^{(2)})=1,
\qquad
\|\phi_m\|_1\le\frac{2m-1}{m}<2.
\]
Thus \(\operatorname{LP}(K_m,c_m)\le(2m-1)/m\). Combining this with the cut lower bound gives
\[
\frac{\operatorname{MHC}(K_m,[c_m],1)}{\operatorname{LP}(K_m,c_m)}\ge\frac{m}{(2m-1)/m}>\frac m2.
\]
The bound grows without limit as \(m\to\infty\), proving the claim.

## Verification

The included verification.py constructs the explicit annulus triangulation and checks the cocycle equations, ring pairings, and support count for m=2 through 10. These finite checks audit the cochain formula only; the all-m cut lower bound and unbounded ratio follow from the analytic arguments in RESULT.md. No claim is made that the displayed cochain is LP-optimal; an upper bound below \(2\) is sufficient for the unbounded-gap conclusion.

## Relationship to prior work

Hoefgeest and Slot formulate the minimum homological edge-cut problem as minimizing the support size of a cocycle with \(\phi(c)=1\), and relax the support objective to \(\|\phi\|_1\). Their Example 6.3 gives a specific non-tight instance with minimum cut size \(3\) and LP value \(3/2\). The present family strengthens that finite separation to an unbounded multiplicative gap while retaining a primitive integral cycle chain. Earlier generalized flow/cut results for simplicial complexes distinguish topological cuts from combinatorial cuts and treat a different flow formulation; they do not imply the stated bound for this nonzero \(H_1\)-class edge-cut problem.

## Limitations

The result rules out a universal constant-factor guarantee based solely on the raw \(\ell^1\) objective for this cut problem. It does not classify all instances, give a polynomial-time approximation algorithm, or establish an unbounded gap for every restricted geometric or manifold subclass. The construction is a finite planar simplicial complex and need not be a 2-manifold at the wedge vertex.

## References

1. P. R. Hoefgeest and L. Slot, *Robustness of Persistent Topological Features and Minimum Homological Cuts*, arXiv:2602.23154v1 (first public version, 26 February 2026); also LIPIcs SoCG 2026, DOI 10.4230/LIPIcs.SoCG.2026.87. See the minimum-cut/cocycle formulation and Section 6, especially Proposition 6.2 and Example 6.3.
2. W. Maxwell and A. Nayyeri, *Generalized Max-Flows and Min-Cuts in Simplicial Complexes*, LIPIcs ESA 2021, DOI 10.4230/LIPIcs.ESA.2021.69. Its definitions distinguish topological and combinatorial cuts and use a different flow formulation.
3. E. W. Chambers, J. Erickson, and A. Nayyeri, *Homology Flows, Cohomology Cuts*, SIAM Journal on Computing 41 (2012), 1605–1634, DOI 10.1137/090766863.
