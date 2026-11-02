# The integral order-two defect of the Burkhardt node–Jacobi-plane incidence lattice

## Finding
Let \(k=\overline{\mathbb F}_2\), and let \(B\subset\mathbb P^5_k\) be the Burkhardt quartic threefold in its symmetric model
\[
 B=\{\sigma_1(X_0,\ldots,X_5)=\sigma_4(X_0,\ldots,X_5)=0\}.
\]
Its \(45\) geometric nodes form a set \(\mathcal N\). The \(40\) Jacobi planes form a set \(\mathcal J\), each plane containing exactly \(9\) nodes. Define the integral, unoriented incidence map
\[
 I:\mathbb Z^{\mathcal J}\longrightarrow\mathbb Z^{\mathcal N},
 \qquad e_J\longmapsto\sum_{P\in J\cap\mathcal N}e_P.
\]
**Theorem.** The nonzero Smith factors of \(I\) are \(1\) with multiplicity \(15\) and \(2\) with multiplicity \(10\). In particular,
\[
 \ker(I)\cong\mathbb Z^{15},\qquad
 \operatorname{coker}(I)\cong\mathbb Z^{20}\oplus(\mathbb Z/2\mathbb Z)^{10}.
\]
This describes the integral saturation of the canonical node–plane incidence lattice, which cannot be recovered from the rational rank alone.

## Assumptions and scope
All coordinates are in characteristic \(2\); incidence counts geometric points over the algebraic closure. The source module is free on the \(40\) distinct Jacobi planes and the target is free on the \(45\) distinct singular nodes. There are no orientation signs and no identifications of geometric Galois conjugates. The claimed abelian group is the cokernel of the **combinatorial incidence map**, not the divisor class group, a Chow group, or the Picard group of the quartic. The classical complex Burkhardt configuration provides context, but the theorem is verified on the displayed characteristic-two model.

## Proof
Write \(s=\sigma_2(X_0,\ldots,X_5)\). On \(\sigma_1=0\), the gradient coordinates of \(\sigma_4\) agree exactly when, for all pairs of indices, 
\[
 (X_i+X_j)(s+X_i^2+X_iX_j+X_j^2)=0.
\]
For any fixed coordinate value, the second factor is quadratic in the other coordinate. Hence a singular point has at most three distinct coordinate values. With one repeated value, \(\sigma_4\ne0\) in projective space. With two distinct values, \(\sigma_1=0\) forces both multiplicities even, and the gradient equation forces the multiplicity-four value to vanish: these yield the \(\binom62=15\) projective points with two equal nonzero coordinates. With three distinct values, the gradient equation for three pairs gives that the values sum to zero; \(\sigma_1=0\) then forces multiplicities \((2,2,2)\), and \(s=0\) makes the values proportional to \(1,\omega,\omega^2\), where \(\omega^2+\omega+1=0\). These give \(30\) additional projective points. Substitution into \(\sigma_4\) shows that all \(45\) lie on \(B\), and the exhaustive cases show there are no further singular points. To check the singularity type, at a two-support point the quadratic part on a four-dimensional affine slice is \(q=\sum_{1\le i<j\le4}z_i z_j\), whose alternating polar form has invertible matrix with zero diagonal and unit off-diagonal. At a paired-root point \((a,a,b,b,c,c)\), the quadratic polar form on the six-coordinate vector space is the direct sum of the three nondegenerate pair blocks with coefficients \(a^2,b^2,c^2\). Its restriction to \(\sum \delta X_i=0\) has radical exactly the radial line spanned by \((a,a,b,b,c,c)\), since \(a^3=b^3=c^3\). Removing that scaling direction gives a nondegenerate four-dimensional projective tangent quadratic form. Thus all \(45\) singularities are ordinary nodes.

All \(45\) nodes are therefore defined over \(\mathbb F_4\). The standalone exact checker constructs their normalized six-coordinate vectors. It enumerates every noncollinear triple of nodes, retains the distinct planes containing exactly nine of the nodes, and obtains exactly \(40\) planes. No line contains more than three nodes, so every nine-node plane is spanned by one of the triples. The checker expands the restriction of \(\sigma_4\) to each of the \(40\) three-dimensional vector subspaces as a homogeneous polynomial of degree \(4\) over \(\mathbb F_4\) and verifies every coefficient is zero. Thus these are actual planes on \(B\), rather than fortuitous finite-field point collections, and they coincide with the classical Jacobi planes described in the cited sources.

Order the normalized vectors lexicographically, then order the nine-node subsets lexicographically; let \(M\) be the resulting \(45\)-by-\(40\) integral incidence matrix. The checker verifies row sums \(8\), column sums \(9\), and that any two distinct rows have either zero or two shared columns. Consequently
\[
 MM^{\mathsf T}=8\mathbf1+2A,
\]
where \(A\) is the adjacency matrix of a strongly regular graph with parameters \((45,32,22,24)\). Indeed, each node has \(32\) neighbors, adjacent nodes have \(22\) common neighbors and nonadjacent nodes have \(24\). Thus \(A^2=8\mathbf1-2A+24J\), with \(J\) the all-ones matrix. As \(A\) is symmetric, its eigenvalues are \(32\) once, \(2\) twenty-four times, and \(-4\) twenty times. The eigenvalues of \(MM^{\mathsf T}\) are therefore \(72\) once, \(12\) twenty-four times, and \(0\) twenty times, proving \(\operatorname{rank}_{\mathbb Q}M=25\).

Exact binary row elimination gives \(\operatorname{rank}_{\mathbb F_2}M=15\). Finally, the explicit \(25\)-by-\(25\) minor at zero-based row indices

`[18,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,21,22,23,24,25,27,28]`

and column indices

`[0,1,2,3,4,5,6,8,9,10,11,12,14,15,16,17,18,20,21,22,24,25,28,29,32]`

has determinant \(-1024=-2^{10}\), verified by exact fraction-free integer elimination. Because the rank is \(25\) and the binary rank is \(15\), exactly ten nonzero Smith factors are even. Their product divides the determinant of every maximal minor, hence divides \(2^{10}\); all ten must be \(2\), and the other fifteen must be units. The kernel and cokernel follow from the Smith decomposition.

## Verification
Execute `python3 burkhardt_incidence_verify.py` with a standard Python 3 interpreter; no additional packages or datasets are required. The program performs exact arithmetic in \(\mathbb F_4\) and \(\mathbb Z\), enumerates the finite configurations, checks the plane equations, certifies the strongly regular Gram structure and binary rank, and computes the displayed maximal minor using Bareiss elimination. The expected terminal line is `VERIFY_OK`. The checker additionally observes \(15\) rational nodes and \(15\) Frobenius pairs of nodes, and \(20\) Frobenius pairs of Jacobi planes; this arithmetic splitting is supporting context and is not the claimed new invariant.

## Relationship to prior work
Cheltsov–Przyjalkowski–Shramov give the symmetric \(\sigma_1=\sigma_4=0\) model, the \(45\)-node configuration, explicit Jacobi planes, and divisor-class intersection calculations. Bruin–Nasserden describe the \(40\) Jacobi planes, their nine-node incidences, and their Galois behavior for the symmetric twist. Szemberg–Szpond give a Pascal-type realization of the configuration and explicit complementary Jacobi planes. The new statement here is the **full integral Smith invariant** of the node-to-Jacobi-plane incidence map, in particular its ten independent order-two torsion classes. Neither the mere incidence parameters nor the rational ranks of other intersection matrices determine these Smith factors. The cited sources encode enough geometric information to permit a separate calculation, so historical priority of the exact integral invariant remains a limitation; no novelty is inferred merely from an unsuccessful search.

## Limitations
The result is finite and exact for the specified incidence map. It does not compute \(\operatorname{Cl}(B)\) or describe all linear spaces on arbitrary Burkhardt twists. In particular the \(2\)-torsion in the displayed cokernel should not be interpreted as divisor-class torsion without a separate comparison. We have not proved that no earlier source computes the same Smith form under a different name. The 1990 original paper of de Jong, Shepherd-Barron and van de Ven was not accessible in complete form for this review. The arXiv 2026 treatment gives explicit coordinate incidence data from which the Smith form could be independently reconstructed.

## References
1. I. Cheltsov, V. Przyjalkowski and C. Shramov, *Burkhardt quartic, Barth sextic, and the icosahedron*, arXiv:1606.04372, first posted 2016-06-14, especially Section 2.
2. N. Bruin and B. Nasserden, *Arithmetic aspects of the Burkhardt quartic threefold*, arXiv:1705.09006, first posted 2017-05-25, Sections 3–5.
3. T. Szemberg and J. Szpond, *From a Pascal construction to the Burkhardt quartic*, arXiv:2606.30772, first posted 2026-06-29, Sections 3–7.
4. I. Cheltsov et al., *Equivariant geometry of the Segre cubic and the Burkhardt quartic*, Selecta Mathematica, DOI 10.1007/s00029-024-01001-w.
5. A. J. de Jong, N. I. Shepherd-Barron and A. Van de Ven, *On the Burkhardt quartic*, Math. Ann. 286 (1990), 309–328, DOI 10.1007/BF01453578 (historical background; complete text not inspected).
