# The marked five–ten–thirty Eckardt incidence of the characteristic-two Clebsch cubic

## Finding

For the diagonal Clebsch surface in characteristic two, the standard five-coordinate marking breaks the \(45\) geometric Eckardt points into three orbits under its coordinate-permutation group \(S_5\), of sizes \(5,10,30\), and its \(27\) lines into orbits of sizes \(15,12\). The following is the **complete point–line incidence quotient**, with entries counting points of each class on one line of the indicated class:

| Line orbit | Point orbit of size \(5\) | Point orbit of size \(10\) | Point orbit of size \(30\) |
| --- | ---: | ---: | ---: |
| \(L_{15}\) (\(\mathbb F_2\)-rational lines) | 1 | 2 | 2 |
| \(L_{12}\) (\(\mathbb F_4\)-rational, not \(\mathbb F_2\)) | 0 | 0 | 5 |

All \(45\) points are \(\mathbb F_4\)-rational, whereas exactly \(15\) are \(\mathbb F_2\)-rational. The incidence of the \(15\) rational points and lines is the symplectic generalized quadrangle \(W(3,2)\), with a distinguished \(S_5\)-invariant five-point ovoid. The remaining twelve lines form a classical double-six; their intersection graph is the crown graph \(K_{6,6}\) minus a perfect matching. Each of its \(30\) edge intersections is a non-rational Eckardt point lying on a unique rational line.

## Assumptions and scope

Work over the algebraic closure \(k=\overline{\mathbb F}_2\). The surface and its five-coordinate marking are
\[
X=V\left(\sum_{i=0}^{4}x_i,\ \sum_{i=0}^{4}x_i^3\right)\subset\mathbb P^4_k.
\]
All references to rationality of points and lines mean descent to the indicated *finite field*, not merely rationality as an abstract algebraic curve. An Eckardt point is a common point of three distinct lines on a smooth cubic surface. All assertions concern the reduced sets of geometric Eckardt points and geometric lines. No scheme structure on the relative Eckardt locus in mixed characteristic is asserted.

For \(\mathbb F_4=\mathbb F_2(\omega)\), with \(\omega^2+\omega+1=0\), define the point types from their five homogeneous coordinates, up to scalar: \(P_{10}\) consists of permutations of \([1:1:0:0:0]\), \(P_5\) of permutations of \([0:1:1:1:1]\), and \(P_{30}\) of permutations of \([0:1:1:\omega:\omega]\) and their projectively equivalent scalar multiples. The two line types are \(L_{15}\), those defined over \(\mathbb F_2\), and \(L_{12}\), the others. The subscripts give the precise sizes of the respective \(S_5\)-orbits.

## Proof

**1. Hermitian structure and completeness.** Eliminate the zeroth coordinate by \(x_0=x_1+x_2+x_3+x_4\). The cubic becomes
\[
F(x_1,\ldots,x_4)=\sum_{i\ne j}x_i^2x_j=x^{[2]T}Ax,
\qquad A=J_4+I_4\quad(\operatorname{char}k=2),
\]
where \(J_4\) is the all-ones matrix. The matrix has zero diagonal and ones elsewhere; as \(J_4^2=4J_4=0\), \(A^2=I_4\), so \(A\) is invertible. It is Hermitian over \(\mathbb F_4\), and \(X\) is a smooth nondegenerate Hermitian cubic, projectively equivalent over \(\mathbb F_4\) to the Fermat cubic. In particular, the classical theorem on lines on a smooth cubic gives exactly \(27\) geometric lines. The standard Hermitian plane geometry, or the direct exhaustive line enumeration described below, gives all of them over \(\mathbb F_4\). There are precisely \(45\) points of \(X(\mathbb F_4)\), with three distinct contained lines through each; hence each is Eckardt. A smooth cubic has exactly \(45\) tritangent planes, each supporting at most one Eckardt point, so this exhausts all geometric Eckardt points. These broad Hermitian facts are known and are not asserted here as original.

**2. Marked point orbits.** For a nonzero \(a\in\mathbb F_4\), \(a^3=1\). The equation \(\sum_i x_i^3=0\) therefore says that the number of nonzero coordinates is even. Nonzero points have support size \(2\) or \(4\). If the support is two, the linear equation forces the two entries to be equal, producing \(\binom52=10\) points. For support size four, the nonzero entries either all agree or consist of two copies of each of two distinct values. This follows by writing \(\mathbb F_4\) additively as a two-dimensional \(\mathbb F_2\)-vector space and reducing the three nonzero-element frequencies modulo two. The all-equal case gives five points, one per zero-coordinate position. In the two-pair case there are \(5\) choices of the zero position, \(3\) pair partitions of the remaining coordinates and \(2\) choices of the nontrivial ratio, hence \(30\) points. These are the three transitive permutation orbits, with \(\mathbb F_2\)-rational locus exactly the first two. Thus the known ten characteristic-zero Eckardt points reduce into \(P_{10}\), while \(P_5\cup P_{30}\) gives precisely \(35\) extra ones.

**3. The symplectic rational subgeometry.** Put \(V=\{u\in\mathbb F_2^5:\sum_i u_i=0\}\), a four-dimensional vector space. The dot product \(B(u,v)=\sum_i u_iv_i\) restricts to a nondegenerate alternating form on \(V\): \(B(u,u)=\sum_i u_i=0\), and its radical is zero because the perpendicular complement of \(V\) in \(\mathbb F_2^5\) is spanned by the all-ones vector, which is not in \(V\). For independent \(u,v\in V\), the cubic along their projective line is exactly
\[
\sum_i (su_i+tv_i)^3=st(s+t)B(u,v).
\]
Thus an \(\mathbb F_2\)-line belongs to \(X\) exactly when its two-dimensional subspace is totally isotropic for \(B\). There are \((2+1)(2^2+1)=15\) such lines, and the corresponding \(15\) points and \(15\) lines form \(W(3,2)\). Each line contains three rational points, two of support two and one of support four: explicitly it corresponds to a missing index and an unordered partition of the remaining four indices into two pairs. Its other two \(\mathbb F_4\)-points are in \(P_{30}\). Hence one line of \(L_{15}\) contains \((1,2,2)\) points of \((P_5,P_{10},P_{30})\). In particular the five support-four rational points each meet every rational line in exactly one point: they form an ovoid of \(W(3,2)\).

**4. The twelve other lines and all mixed incidences.** The fifteen lines above are precisely the lines rational over \(\mathbb F_2\). Since all \(27\) geometric lines are \(\mathbb F_4\)-rational, the other twelve form \(L_{12}\). No line in \(L_{12}\) can contain an \(\mathbb F_2\)-point: every rational point already lies on the three lines of \(W(3,2)\), which are the three geometric lines through it. Two distinct \(\mathbb F_2\)-rational lines cannot intersect at a non-rational point, because their intersection is then an \(\mathbb F_2\)-rational subspace. Consequently the \(15\) rational lines have \(30\) distinct non-rational point incidences, exhausting \(P_{30}\). Each point of \(P_{30}\) lies on one rational line and, by the Hermitian three-line property, on two lines of \(L_{12}\). It follows that every \(L_{12}\)-line contains five points, all in \(P_{30}\), yielding the displayed incidence matrix and the reciprocal point profile. The twelve lines form the classical Clebsch double-six, which persists as the surface is smooth in characteristic two. Hence their graph of pairwise intersection is \(K_{6,6}\) with a perfect matching removed. The thirty edges correspond bijectively to \(P_{30}\). These conclusions also follow directly by the finite computation below.

**5. Transitivity under the marked action.** The point orbit descriptions are manifestly transitive under \(S_5\). The \(15\) rational lines correspond to a missing index and a partition into two pairs, so form one orbit. The remaining \(12\) form one orbit: for example, over an extension containing a primitive fifth root of unity \(\zeta\), the classical line spanned by \((\zeta^i)_{i=0}^{4}\) and \((\zeta^{-i})_{i=0}^{4}\) is defined over \(\mathbb F_4\) (fourth-power Frobenius interchanges the two spanning vectors), but not over \(\mathbb F_2\); its \(S_5\)-orbit has size \(12\). The orbit and non-descent are alternatively checked exhaustively in the attached stand-alone checker using no fifth-root calculations.

## Verification

`CHECKER.py` uses only the Python standard library and represents \(\mathbb F_4\) by \(\mathbb F_2[\omega]/(\omega^2+\omega+1)\). It enumerates all \(85\) points of \(\mathbb P^3(\mathbb F_4)\), selects the \(45\) on \(X\), enumerates all projective lines through pairs of selected points and retains the \(27\) fully contained in \(X\). It checks the point and line orbit partitions under all \(120\) permutations, verifies the entire incidence matrix, and confirms the twelve-line crown graph. Running `python CHECKER.py` returns four PASS lines. These finite checks corroborate the calculations; geometric exhaustion relies additionally on the smooth-cubic \(27\)-line theorem and the tritangent bound described in the proof.

## Relationship to prior work

Homma–Kim (arXiv:1304.0302) give the general nonsingular Hermitian-surface framework and its finite-field point count. Dolgachev–Duncan (arXiv:1712.01167), especially Lemma 5.3, Lemma 12.4 and Remark 13.3, **already** identify the characteristic-two Clebsch surface with the Fermat cubic and state the \(45\) Eckardt points, \(27\) lines, the classical double-six and new face concurrence. Saniga and collaborators (arXiv:0903.0715) discuss the generalized quadrangle and double-six geometry. Those ingredients are not new here. The narrowly assessed statement is the **complete incidence quotient for the specific five-coordinate \(S_5\)-marking**, including the three point-orbit types, their field-of-definition split, the ovoid, and the precise attachment of the thirty non-rational Eckardt points to the rational lines and double-six. The inspected sources did not explicitly state this marked incidence classification; related finite-geometric equivalences could nonetheless make it a previously known corollary.

## Limitations

This classifies a special fiber and its reduced incidence sets only. It does not calculate a relative Eckardt scheme, infinitesimal multiplicities, or integral deformation data. It does not establish a general new Hermitian-surface theorem, and the two leading global counts are published. The complete historical literature on marked subconfigurations of \(\mathrm{GQ}(4,2)\) was not exhaustively inspected. Independent scientific validation is outstanding.

## References

1. M. Homma and S. J. Kim, *The characterization of Hermitian surfaces by the number of points*, arXiv:1304.0302 (first submitted 1 April 2013), especially pp. 1–2.
2. I. Dolgachev and A. Duncan, *Automorphisms of cubic surfaces in positive characteristic*, arXiv:1712.01167 (first submitted 4 December 2017), especially §§5.1, 12.1, 13.1.
3. M. Saniga, R. M. Green, P. Lévay, P. Pracna and P. Vrana, *The Veldkamp Space of GQ(2,4)*, arXiv:0903.0715 (first submitted 4 March 2009), especially §§2–3.
