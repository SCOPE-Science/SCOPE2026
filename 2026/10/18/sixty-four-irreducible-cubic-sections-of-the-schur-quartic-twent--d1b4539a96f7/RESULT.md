# Sixty-four irreducible cubic sections of the Schur quartic twenty-four-line divisor

## Finding
Let \(X\subset\mathbb P^3_{\mathbb C}\) be the smooth Schur quartic
\[
X_0^4-X_0X_1^3-X_2^4+X_2X_3^3=0,
\]
and let \(H\) be its hyperplane class. Label \(L_1,\ldots,L_{24}\) by the explicit parameter table in Naskręcki--Pokora [1, Appendix A], and set \(D=\sum_{i=1}^{24}L_i\).

**Theorem.** There are **exactly 64** subsets \(S\subset\{1,\ldots,24\}\) such that the reduced divisor \(E_S=\sum_{i\in S}L_i\) is linearly equivalent to \(3H\). Every such subset contains exactly twelve lines, and exactly one cubic hypersurface in \(\mathbb P^3_{\mathbb C}\), up to multiplying its equation by a nonzero scalar, has scheme-theoretic intersection \(E_S\) with \(X\). **All 64 cubic hypersurfaces are irreducible over \(\mathbb C\)**. The 64 subsets form exactly **32 unordered complementary pairs** \(\{S,S^c\}\); each pair gives a decomposition \(D=E_S+E_{S^c}\) into two cubic sections.

Furthermore, the integral sublattice \(\Lambda=\langle[L_1],\ldots,[L_{24}]\rangle\subset\operatorname{NS}(X)\) has rank 16, signature \((1,15)\), discriminant magnitude \(1728\), and discriminant group \((\mathbb Z/2\mathbb Z)^4\oplus\mathbb Z/6\mathbb Z\oplus\mathbb Z/18\mathbb Z\). The hyperplane class satisfies \(H\notin\Lambda\) but \(3H\in\Lambda\), so \([\Lambda+\mathbb ZH:\Lambda]=3\). The lattice \(\Lambda+\mathbb ZH\) has discriminant magnitude \(192\) and discriminant group \((\mathbb Z/2\mathbb Z)^5\oplus\mathbb Z/6\mathbb Z\). These statements concern the **line-generated sublattice**, not an assertion that it is primitive in \(\operatorname{NS}(X)\).

For example, one cubic-section divisor is the sum of lines with labels
\[
S_0=\{1,3,4,8,9,10,11,12,13,15,17,24\}.
\]
Its complement supplies the matching cubic section.

## Assumptions and scope
The ground field is \(\mathbb C\). The Schur quartic is smooth, hence a complex K3 surface. All lines are the specified 24 components of the distinguished \((24_4,32_3)\)-configuration [1]; no statement is made about arbitrary 24-line sets or all 64 lines of \(X\). A *cubic section supported on* \(D\) means an effective reduced subdivisor of \(D\) linearly equivalent to \(3H\); cubic hypersurfaces with intersections involving other components, or nonreduced intersections, are not being classified.

## Proof
**1. Exact incidence matrix.** For every parameter quadruple \((a,b;c,d)\) in [1, Appendix A], use the line \([s:t]\mapsto[s:t:as+ct:bs+dt]\) over \(K=\mathbb Q(\tau)\), \(\tau^2=-3\). The five coefficients of the quartic restricted to each line vanish. Two graph lines meet exactly when
\[
(a_i-a_j)(d_i-d_j)-(b_i-b_j)(c_i-c_j)=0.
\]
Exact arithmetic gives 96 intersecting pairs, all organized into the 32 concurrent triples listed in [1, Appendix B], with no fourth selected line at a point and no other intersections. The attached standalone checker reconstructs these statements from the printed parameter data (including concurrency and distinctness), without floating-point comparisons. A smooth rational line on a K3 surface has self-intersection \(-2\) by adjunction. Thus the intersection matrix \(M\) has diagonal entries \(-2\) and off-diagonal entries \(1\) exactly for the 96 pairs. Every row of \(M\) sums to \(6\). Exhaustive inspection of the \(\binom{24}{4}=10626\) quadruples shows the line-intersection graph contains no clique on four vertices.

**2. Divisors are cubic sections precisely when a binary linear system holds.** For \(x=(x_i)\in\{0,1\}^{24}\), write \(E_x=\sum_i x_iL_i\). If \(E_x\sim3H\), then \(Mx=3\mathbf 1\), since \(H\cdot L_i=1\). Conversely, suppose \(Mx=3\mathbf 1\). Multiplying by \(\mathbf1^\mathsf T\) and using the row sums forces \(\sum x_i=12\). Hence \(E_x\cdot H=12\) and \(E_x^2=x^\mathsf TMx=36\). Since \(H^2=4\), the Hodge index equality gives \(E_x\equiv3H\) numerically; numerical and linear equivalence agree on a complex K3 surface. Therefore
\[
E_x\sim3H\quad\Longleftrightarrow\quad x\in\{0,1\}^{24},\ Mx=3\mathbf1.
\]
The same argument applied to \(D\), using \(D\cdot H=24\) and \(D^2=144\), yields \(D\sim6H\), independently of the divisor identity already established in [1].

**3. Exhaustive count.** Choose the 16 line indices
\[
I=(1,2,3,4,5,7,8,9,10,11,12,13,14,15,16,17)
\]
and let \(J=(6,18,19,20,21,22,23,24)\). The principal matrix \(B=M_{I,I}\) has determinant \(-1728\), so is invertible. For every binary assignment on the eight indices \(J\), the first 16 coordinates are forced to be
\[
x_I=B^{-1}(3\mathbf1-M_{I,J}x_J).
\]
There are precisely \(2^8=256\) assignments to inspect. Exact rational elimination gives 64 for which all 16 forced coordinates belong to \(\{0,1\}\); each of the 64 also satisfies the remaining eight equations. This is an exhaustive finite classification, not sampling. Complementation \(x\mapsto\mathbf1-x\) preserves the equation because \(M\mathbf1=6\mathbf1\), and has no fixed binary vector. Hence there are 32 unordered complement pairs.

**4. Cubic hypersurfaces and irreducibility.** For each reduced effective \(E_x\sim3H\), its canonical section of \(\mathcal O_X(3H)\) is unique up to scalar. The restriction map \(H^0(\mathbb P^3,\mathcal O(3))\to H^0(X,\mathcal O_X(3H))\) is an isomorphism: use the quartic hypersurface sequence with kernel \(\mathcal O_{\mathbb P^3}(-1)\), whose zeroth and first cohomology vanish. Thus there is exactly one cubic hypersurface cutting out \(E_x\). If its cubic equation were reducible over \(\mathbb C\), it would have a linear factor. Its plane section on \(X\) would then be an effective degree-four subdivisor of the *reduced* twelve-line divisor \(E_x\), hence a sum of four distinct selected lines in one plane. Any four coplanar lines pairwise meet, contradicting the no-four-clique computation in Step 1. Every cubic is therefore irreducible. Distinct subdivisors give distinct cubics.

**5. Integral lattice and polarization defect.** The same exact matrix has rank 16; the 16 selected classes indexed by \(I\) generate all 24 classes integrally. Indeed, solving their 16 intersection equations expresses each of the remaining eight lines with integer coefficients, and all 24 intersection pairings are verified. The Hodge index theorem and \(D\sim6H\) show that a rational combination of the 24 line classes orthogonal to all 24 is zero: it has zero intersection with \(H\) and with itself. Consequently the 16 selected line classes are an integral basis of \(\Lambda\), with Gram matrix \(B\). Its determinant, signature and Smith invariants are respectively \(-1728\), \((1,15)\), and ten 1's, four 2's, 6, 18.

In this basis, \(3H\) is the integral class
\[
3H\sim2L_1-L_2+L_3+L_5+\sum_{j=7}^{15}L_j,
\]
verified by intersecting both sides with all 24 line classes and applying Hodge index. The unique rational coordinates of \(H\) in that basis have denominator 3, so \(H\notin\Lambda\) while \(3H\in\Lambda\). Adjoining \(H\) produces an index-three overlattice with discriminant \(1728/9=192\); its exact Smith form has ten 1's, five 2's and 6. This proves the further lattice assertions.

## Verification
Run `python3 verify_schur_cubics.py` with Python 3 and its standard library; no extra packages or remote data are needed. The script checks all 24 quartic-line containment identities, all 276 pair determinants, 32 triple concurrences and distinctness, the absence of four-cliques, the exact determinant and Smith reductions, integral line-basis relations, the index-three hyperplane class, and all 256 binary assignments. Expected output includes `precisely 64 twelve-line cubic sections, 32 complementary pairs`. The script and its input table are embedded alongside this document.

## Relationship to prior work
Naskręcki and Pokora [1] constructed the 24-line configuration, its exact incidence table, the relation \(D\sim6H\), and the logarithmic Chern-slope counterexample. The present theorem adds the complete classification of *reduced cubic subdivisors* of that degree-six divisor, irreducibility of their cubic hypersurfaces, and the integral hyperplane-defect and discriminant data. The 24-line case is not obtained merely by substituting a parameter in a more general published cubic-section count identified in the searches.

Höhn [2] subsequently described the projective automorphism group and a \(D_4\)-root model for the same arrangement; these are relevant to the combinatorial symmetry, but the accessible abstract does not assert a count of 64 cubic sections or the stated lattice index. A published indexed analysis of the full 64-line intersection graph [3] provides a rank-20 full-graph spectrum, not the 24-line cubic-subdivisor classification. The full text of [2] could not be inspected, so a hidden equivalent enumeration remains a bibliographic risk.

## Limitations
The classification includes only reduced subdivisors of this labelled 24-line divisor and uses complex K3 intersection theory. It does not classify every cubic hypersurface through any twelve Schur lines, does not determine the singularities or automorphism orbits of the 64 cubics, and does not claim \(\Lambda\) is primitive in the full Néron--Severi lattice. The available comparison of [2] is limited to its abstract and secondary discussion; another unindexed cubic-section enumeration is possible. The proof and computation are exact, but independent audit has not been performed.

## References
[1] B. Naskręcki and P. Pokora, *A \((24_4,32_3)\)-configuration on the Schur quartic with logarithmic Chern slope \(14/5\)*, arXiv:2607.07898v1 (first public July 8, 2026), https://arxiv.org/abs/2607.07898.

[2] G. Höhn, *Automorphisms of a \((24_4,32_3)\)-configuration on the Schur quartic*, arXiv:2607.10090v1 (July 11, 2026), https://arxiv.org/abs/2607.10090.

[3] *Spectrum and common-transversal profile of the 64 Schur lines*, public indexed research record `2026/10/4/SCOPE-spectrum-and-common-transversal-profile-of-the-64-schur-lines--76e63f54b379`, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-spectrum-and-common-transversal-profile-of-the-64-schur-lines--76e63f54b379.
