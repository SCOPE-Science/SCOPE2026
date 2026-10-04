# Integral spectrum of the 85-line incidence graph on the Yu--Zhu quintic

## Finding
Let \(X=X_{-1/8}\) be the smooth quintic surface of Yu and Zhu, and let \(G\) be the graph whose vertices are the \(85\) lines \(L_1,\ldots,L_{85}\) listed in their Section 3, with two vertices adjacent exactly when the corresponding lines meet. Then \(G\) is a connected \(20\)-regular integral graph with \(850\) edges and adjacency characteristic polynomial
\[
(\lambda-20)(\lambda-3)^{46}(\lambda+1)^6(\lambda+3)^{16}(\lambda+5)^{10}(\lambda+9)^6.
\]
Equivalently, its adjacency spectrum is
\[
20^1,\quad 3^{46},\quad (-1)^6,\quad (-3)^{16},\quad (-5)^{10},\quad (-9)^6.
\]
Among adjacent vertex pairs, \(530\) have exactly three common neighbors and \(320\) have none; in particular, \(G\) has exactly \(530\) triangles.

For the divisor classes of the lines, the intersection matrix is \(A-3I\), where \(A\) is the adjacency matrix. Hence its spectrum is
\[
17^1,\quad 0^{46},\quad (-4)^6,\quad (-6)^{16},\quad (-8)^{10},\quad (-12)^6,
\]
so it has rank \(39\) and inertia \((1,38,46)\). This recovers and refines Yu--Zhu's reported computer calculation that the line intersection matrix has rank \(39\).

## Assumptions and scope
The result concerns the special smooth member \(X_{-1/8}\) and the explicit labeling of its \(85\) lines in Yu--Zhu, arXiv:2609.26862v1, Section 3. The paper proves that these are exactly all lines on \(X_{-1/8}\). No statement is made here about the incidence spectra of other members of the pencil.

## Proof
Yu--Zhu give every line by two homogeneous linear equations. All coefficients lie in
\[
K=\mathbb Q(a,b,i),\qquad a^4=2,\quad b^4=3,\quad i^2=-1.
\]
Indeed, \(\sqrt 3=b^2\), \(\sqrt[4]{12}=a^2b\), \(\sqrt[4]{18}=ab^2\), and \(\sqrt[4]{6}=ab\). Thus every incidence test can be performed exactly in the fixed number field \(K\).

If two lines are represented by pairs of linear forms \((\ell_1,\ell_2)\) and \((m_1,m_2)\), they meet in \(\mathbb P^3\) if and only if the determinant of the \(4\times4\) coefficient matrix with rows \(\ell_1,\ell_2,m_1,m_2\) is zero. Exhausting the \(\binom{85}{2}\) pairs with exact arithmetic gives \(850\) meeting pairs, and every line occurs in exactly \(20\) of them. Hence \(G\) is \(20\)-regular. The displayed line \(L_1\) has precisely the twenty neighbors \(L_2,\ldots,L_{21}\), agreeing with the source's independent decomposition into twenty lines meeting \(L_1\) and sixty-four skew to it.

For the spectrum, exact integer matrix arithmetic gives
\[
p(A)=0,
\qquad
p(z)=(z-20)(z-3)(z+1)(z+3)(z+5)(z+9),
\]
and
\[
\operatorname{tr}(A^k)=85,0,1700,3180,210644,2821740
\]
for \(k=0,1,2,3,4,5\), respectively. Since \(A\) is real symmetric, it is diagonalizable; the annihilating identity forces all eigenvalues to lie among the six distinct roots of \(p\). The six trace equations are a Vandermonde system in their multiplicities and have the unique solution
\[
(1,46,6,16,10,6),
\]
in the root order \((20,3,-1,-3,-5,-9)\). This proves the characteristic polynomial above. The multiplicity one of the valency eigenvalue \(20\) also proves that \(G\) is connected.

Finally, a line on a smooth quintic surface has self-intersection \(-3\) by adjunction, while two distinct lines have intersection number one exactly when they meet and zero when they are skew. Therefore the line intersection matrix is \(A-3I\). Shifting the spectrum by \(-3\) gives the stated rank and inertia. The common-neighbor census is obtained from the same exact adjacency matrix; summing common-neighbor counts over edges and dividing by three gives \(530\) graph triangles.

## Verification
The accompanying `verify_incidence.py` is a standalone exact-arithmetic checker using only the Python standard library. It reconstructs all \(85\) source lines over \(K\), tests every pair by an exact determinant, checks regularity and the edge/common-neighbor census, verifies the degree-six annihilating polynomial and the first six traces, and derives the shifted line-intersection rank and inertia. Its recorded output terminates with `VERIFY_OK`.

## Relationship to prior work
Yu--Zhu construct the pencil, prove that every smooth member has exactly \(85\) lines, list all \(85\) lines explicitly for \(X_{-1/8}\), and report that their intersection matrix has rank \(39\). Their paper does not state the regularity, edge count, adjacency spectrum, characteristic polynomial, common-neighbor census, or spectral explanation of that rank. Targeted searches for the paper together with “incidence graph”, “spectrum”, “20-regular”, and “characteristic polynomial” did not locate such a statement elsewhere. The new spectrum strictly refines the rank datum: the zero eigenspace of \(A-3I\) has dimension \(46\), while all nonzero eigenvalues and their multiplicities are determined.

## Limitations
The originality comparison is limited to accessible published/preprint material and does not rule out an unpublished computation. The proof depends on the correctness of Yu--Zhu's explicit list as the complete line set; that completeness is a theorem of the source and is not reproved here. The checker verifies incidence and spectral consequences of the listed equations exactly, without floating-point root finding.

## References
X. Yu and Z. Zhu, “A smooth quintic surface with 85 lines and Picard number 43,” arXiv:2609.26862v1, 22 September 2026. In particular, Theorem 1.1 and Section 3 give the surface and its lines, and the end of Section 3 reports rank \(39\) for the line intersection matrix.
