# Exact facet-distance formula for pedal-simplex volume
## Finding
Let \(A_0\ldots A_n\subset\mathbb R^n\), with \(n\ge2\), be a nondegenerate Euclidean simplex. Write \(V\) for its \(n\)-dimensional volume. For each \(i\), let \(F_i\) be the facet opposite \(A_i\), let \(S_i\) be the \((n-1)\)-dimensional volume of \(F_i\), and choose the unit normal \(u_i\) to the supporting hyperplane of \(F_i\) that points from \(F_i\) toward \(A_i\).

For any point \(P\in\mathbb R^n\), define the signed facet distance \(d_i=d_i(P)\) to be positive on the \(A_i\)-side of the hyperplane of \(F_i\). Let
\[
P_i=P-d_i u_i
\]
be the orthogonal projection of \(P\) to that hyperplane. Then the pedal simplex \(P_0\ldots P_n\) has volume
\[
\operatorname{Vol}(P_0\ldots P_n)
=
\frac{n^nV^{n-1}}{(n!)^2\prod_{k=0}^nS_k}
\left|
\sum_{i=0}^n S_i\prod_{j\ne i}d_j
\right|.
\]
Thus the pedal simplex is degenerate exactly on the algebraic locus
\[
\Phi(P):=\sum_{i=0}^n S_i\prod_{j\ne i}d_j(P)=0.
\]
At every vertex \(A_k\), the polynomial \(\Phi\) vanishes with multiplicity exactly \(n-1\).

For \(n=2\), the formula reduces to the classical signed-area formula for a pedal triangle and its zero locus is the circumcircle, recovering the Wallace--Simson phenomenon. For \(n=3\), \(\Phi=0\) is the classical cubic pedal surface; Grace explicitly records that the coplanarity locus of the four perpendicular feet is a cubic surface with nodes at the tetrahedron vertices.

## Assumptions and scope
The facets are used through their supporting hyperplanes, so \(P\) may lie inside or outside the simplex. Signed distances are essential outside the simplex. The displayed volume is unsigned; the determinant proof first gives an oriented identity and then takes absolute values.

The result is metric, not affine invariant: orthogonal projection and unit normals use the Euclidean inner product. No regularity, orthocentricity, acuteness, or interior-point hypothesis is imposed on the simplex or on \(P\).

## Proof
Let \(\lambda_i\) be the barycentric coordinate associated with \(A_i\). If \(h_i\) is the altitude from \(A_i\) to \(F_i\), then
\[
h_i=\frac{nV}{S_i},\qquad \nabla\lambda_i=\frac{u_i}{h_i}=\frac{S_i}{nV}u_i.
\]
Hence
\[
\sum_{i=0}^n S_i u_i=nV\sum_{i=0}^n\nabla\lambda_i=0.
\]
Therefore the positive vector \((S_0,\ldots,S_n)\) spans the one-dimensional kernel of the \(n\times(n+1)\) matrix whose columns are \(u_0,\ldots,u_n\).

Translate the pedal simplex by \(-P\). Its vertices become \(-d_i u_i\). Up to the fixed global orientation sign,
\[
n!\,\operatorname{Vol}_{\mathrm{or}}(P_0\ldots P_n)
=
\det
\begin{pmatrix}
-d_0u_0&\cdots&-d_nu_n\\
1&\cdots&1
\end{pmatrix}.
\]
Expanding along the final row gives a homogeneous degree-\(n\) expression in the signed distances. The signed cofactors of the normal matrix form a kernel vector, so there is one scalar \(C\) such that the cofactor obtained by deleting column \(i\) equals \(C S_i\).

To determine \(|C|\), delete column \(i\). The remaining \(n\) barycentric gradients have determinant magnitude \(1/(n!V)\). Since \(u_j=(nV/S_j)\nabla\lambda_j\),
\[
\left|\det(u_j)_{j\ne i}\right|
=
\frac{(nV)^n}{\prod_{j\ne i}S_j}\frac{1}{n!V}
=
\frac{n^nV^{n-1}}{n!\prod_{k=0}^nS_k}S_i.
\]
Substituting this common cofactor scale into the last-row expansion and dividing by \(n!\) proves
\[
\operatorname{Vol}(P_0\ldots P_n)
=
\frac{n^nV^{n-1}}{(n!)^2\prod_kS_k}
\left|\sum_iS_i\prod_{j\ne i}d_j\right|.
\]

For the vertex multiplicity, fix \(A_k\). The \(n\) signed distances \(d_j\), \(j\ne k\), vanish there and are independent local affine coordinates, while \(d_k(A_k)=h_k>0\). The lowest-degree nonzero part of \(\Phi\) at \(A_k\) is
\[
h_k\sum_{i\ne k}S_i\prod_{j\ne i,k}d_j,
\]
which has degree \(n-1\) and is not the zero polynomial because all \(S_i\) and \(h_k\) are positive. Thus the multiplicity is exactly \(n-1\).

## Verification
The bundled file `verify_pedal_simplex.py` independently constructs random nondegenerate simplices in dimensions \(2\) through \(6\), chooses both interior and exterior points, computes all facet feet directly from Euclidean projections, and compares the determinant volume with the closed formula above. It also checks the planar specialization against Euler's classical power-of-the-circumcircle pedal-area formula. The replay is deterministic.

## Relationship to prior work
Grace's 1927 paper states that, for a tetrahedron, the locus where the four perpendicular feet are coplanar is a cubic surface with nodes at the tetrahedron vertices. The present formula does not claim that qualitative tetrahedral fact as new; it supplies an explicit signed-volume polynomial with its full normalization and extends the construction to every dimension.

Yang's 2004 paper develops simplex sine laws and states an inequality for a pedal simplex. Yang and Cheng's 2006 paper defines the general pedal simplex and proves inequalities involving its radii and volume. In the public text inspected for the 2006 paper, Theorem 1.3 is an inequality obtained through earlier volume bounds; it does not state the exact facet-distance determinant identity above.

The two-dimensional specialization is classical: the pedal-triangle area is proportional to the power of \(P\) with respect to the circumcircle, and zero area gives the Wallace--Simson theorem.

## Limitations
The full text of Grace's 1927 article was not obtained during this run: an open-access search yielded the Cambridge extract, while a subsequent institutional retrieval attempt did not complete. The originality assessment therefore does not claim that Grace lacked an equivalent explicit cubic equation in dimension three; the claimed contribution is the all-dimensional exact volume formula and its immediate multiplicity statement. Earlier literature under terminology such as pedal simplex, pedal surface, trilinear coordinates, or barycentric coordinates could contain an equivalent determinant identity, so that historical risk remains.

The numerical verifier checks implementation and normalization but is not the proof. The proof is the determinant/cofactor argument above.

## References
1. J. H. Grace, “The pedal planes of a tetrahedron,” *Proceedings of the Cambridge Philosophical Society* 23 (1927), 853–858. DOI: 10.1017/S0305004100013700.
2. S. Yang, “The generalized sine law and some inequalities for simplices,” *Journal of Inequalities in Pure and Applied Mathematics* 5(4), Article 106 (2004).
3. S. Yang and S. Cheng, “Inequalities for inscribed simplex and applications,” *Journal of Inequalities in Pure and Applied Mathematics* 7(5), Article 165 (2006).
4. *Nature*, 23 July 1927, calendar notice for the Cambridge Philosophical Society meeting of 25 July 1927, listing Grace's “The Pedal Planes of a Tetrahedron.”
