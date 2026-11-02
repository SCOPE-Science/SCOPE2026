# Dyadic collapse and the thirty-one marked points of the icosahedral mirror arrangement

## Finding

Let \(\varphi\) satisfy \(\varphi^2=\varphi+1\) and set \(R=\mathbb Z[\varphi]\). The following fifteen primitive lines in \(\mathbb P^2_R\) define an integral coordinate model of the icosahedral \(H_3\) reflection arrangement: the three coordinate lines \(X,Y,Z\), together with the twelve lines obtained by cyclically permuting the coefficients of
\[
X+\epsilon\varphi Y+\delta(\varphi-1)Z,
\qquad \epsilon,\delta\in\{1,-1\}.
\]
The model is projectively equivalent, after interchange of two coordinates, to the reflection-hyperplane orbit in Calvo [1, Section 2.2]. For this fixed integral model:

**(i) Complete exceptional-prime classification.** Every prime of \(R\) not above \(2\) preserves all fifteen distinct geometric lines and their complete incidence lattice: fifteen double, ten triple, and six quintuple intersection points. At the unique prime above \(2\), with \(R/(2)=\mathbb F_4\), writing \(\omega=\overline\varphi\), the divisorial special fiber is
\[
\boxed{\;XYZ\,(X+\omega Y+\omega^2Z)^{12}=0.\;}
\]
Its reduced support consists of four lines in general position, with six ordinary double intersections.

**(ii) Complete specialization of the thirty-one individually marked generic intersection points.** A generic intersection is extended by its primitive projective cross product of incident line coefficients. Their thirty-one sections have exactly eight distinct specializations in \(\mathbb P^2(\mathbb F_4)\). Writing \(L=X+\omega Y+\omega^2Z\), these consist of the three coordinate vertices, of weight \(1\) each, and all five \(\mathbb F_4\)-rational points on \(L\): its three coordinate-axis intersections of weight \(4\) each, \([1:1:1]\) of weight \(4\), and \([1:\omega:\omega^2]\) of weight \(12\). At a vertex, the single marked point was formerly double; at each \(L\)-axis intersection, two formerly quintuple and two formerly triple points meet; at \([1:1:1]\), four formerly triple points meet; at \([1:\omega:\omega^2]\), twelve formerly double points meet. These weights count labeled specializations, **not** local lengths of a flat singular scheme.

**(iii) A derived interpolation formula for the reduced eight-point limit.** Let \(Z_8\) be its reduced support over an algebraic closure of \(\mathbb F_2\). Then for each integer \(m\ge1\),
\[
\boxed{\alpha(I_{Z_8}^{(m)})=\left\lceil\frac{7m}{3}\right\rceil,\qquad
\widehat\alpha(I_{Z_8})=\frac73.}
\]
The abstract eight-point Waldschmidt constant \(7/3\) is **already implied by** Huynh–Linh–Long [2, Corollary 2.3]; it is included to identify the arithmetic limit, not claimed as a new abstract invariant. The newly assessed assertion is the full reduction and thirty-one-section collision classification in (i)–(ii), with the characteristic-two exact initial-degree sequence as a transparent consequence.

## Assumptions and scope

All assertions concern the explicitly given scheme of fifteen hyperplanes over \(R\), its base changes to algebraically closed residue fields, and the individually marked intersections of the generic arrangement. The ring \(R\) is the full ring of integers in \(\mathbb Q(\sqrt5)\); \(2\) is inert and the unique residue field is \(\mathbb F_4\). For each generic intersection incident with at least two lines, select any two incident normals, take their cross product in \(R^3\), and remove a maximal common power of \(2\). The resulting vector defines a projective integral section over the localization \(R_{(2)}\), and its specialization is independent of the selected incident pair. No assertion is made that this specialization is the schematic limit of a family of singular loci; it is the limit of the chosen *marked points*.

For a reduced set \(T\subset\mathbb P^2\), \(I_T^{(m)}\) denotes the intersection of the \(m\)-th powers of its homogeneous point ideals, and \(\alpha\) is the minimum nonzero homogeneous degree. An equivalent geometric formulation is the least degree of a plane curve having multiplicity at least \(m\) at every point of \(T\).

## Proof

**1. Identification with the icosahedral reflection orbit.** The displayed fifteen normals are the coordinate vectors and cyclic permutations of \((1,\pm\varphi,\pm(\varphi-1))\). Start with the normal of Calvo's line \(X=0\). Apply his three matrices from Section 2.2, including the two diagonal sign changes and the symmetric involution with entries in \(\mathbb Q(\varphi)\); projective normalization gives fifteen elements. These coincide exactly with the displayed normals after exchanging the first two coordinates. This equality was independently reconstructed with exact quadratic arithmetic; no appeal to a mere count of lines is needed.

**2. Exhaustive integral determinant certificate and all odd primes.** Represent an element \(a+b\varphi\) by \((a,b)\in\mathbb Z^2\); multiplication is
\[
(a,b)(c,d)=(ac+bd,\ ad+bc+bd),
\quad N(a+b\varphi)=a^2+ab-b^2.
\]
Evaluate the determinants of every triple among the fifteen explicit normal vectors. Exactly \(70\) vanish. For the \(385\) nonzero determinants, the distribution of their absolute field norms is
\[
\begin{array}{c|rrrr}
|N(\det)|&1&4&16&64\\\hline
\#\text{triples}&37&156&188&4
\end{array}.
\]
This is a complete \(\binom{15}{3}=455\)-triple calculation, reproduced from the formulas in `verify_icosahedral.py`. There are fifteen maximal incidence sets of size two, ten of size three, and six of size five; they exhaust all \(\binom{15}{2}=105\) pairs. Since every nonzero determinant is a unit at every prime away from \(2\), no new concurrence occurs in any such residue characteristic. Distinct lines are preserved there as well: were two normals proportional modulo a prime, every determinant using them would vanish modulo that prime, contrary to a nonzero determinant of norm a power of two. Thus the complete incidence lattice is unchanged outside characteristic two.

**3. The fiber at two.** The minimal polynomial of \(\varphi\) is \(T^2-T-1\), which modulo two is the irreducible polynomial \(T^2+T+1\). Hence \(R/(2)=\mathbb F_4\). In this field signs coincide and \(\omega-1=\omega+1=\omega^2\). All twelve non-coordinate normals therefore reduce, up to projective scalar, to \((1,\omega,\omega^2)\), while the coordinate normals remain distinct. Multiplying the fifteen reduced linear factors proves the scheme-theoretic polynomial identity in (i). The line \(L\) does not contain a coordinate vertex, so these four reduced lines are in general position and have six transverse double points.

**4. Marked collisions.** The exact pairwise-cross-product procedure in the attached verifier groups the \(105\) pairs into their \(31\) maximal incident-line subsets; for each, it divides a common power of \(2\) from the cross product and reduces to \(\mathbb F_4\). Independence of the chosen pair is checked for *every* pair of every subset. The complete table is
\[
\begin{array}{c|r|rrr}
\text{specialization}&\text{weight}&\text{old double}&\text{old triple}&\text{old quintuple}\\\hline
[1:0:0],[0:1:0],[0:0:1]\ \text{(each)}&1&1&0&0\\
L\cap\{X=0\},L\cap\{Y=0\},L\cap\{Z=0\}\ \text{(each)}&4&0&2&2\\
[1:1:1]&4&0&4&0\\
[1:\omega:\omega^2]&12&12&0&0
\end{array}.
\]
Each weight and type follows from exact integer-pair arithmetic, including the divisibility by \(2\) before reduction; the table totals \(3+12+4+12=31\) old intersections, with \(15\) double, \(10\) triple, and \(6\) quintuple labels. The three \(L\)-axis intersections together with the two additional points exhaust the five \(\mathbb F_4\)-rational points on \(L\).

**5. Exact symbolic initial degrees.** Denote the coordinate vertices by \(A\), the three intersections of \(L\) with the coordinate axes by \(B\), and the two additional points by \(C\). The conic
\[
Q=XY+\omega XZ+\omega^2YZ
\]
passes through all three points \(A\) and both points \(C\), but none of \(B\). Its partial derivatives have no common zero on the conic, so it is smooth. The curves \(LQ\), \(L^2XYZ\), and \(L^2XYZQ\) have respective degrees \(3,5,7\) and multiplicity at least \(1,2,3\) at all eight points. Products of these curves give
\(\alpha(I_{Z_8}^{(m)})\le\lceil7m/3\rceil\) for all \(m\), according as \(m\equiv0,1,2\pmod3\).

For the reverse inequality, blow up the eight points. Let \(H\) denote the pullback of a line, with \(E_A,E_B,E_C\) the sums of exceptionals in the respective groups. The divisor
\[
N=9H-4E_A-E_B-3E_C
\]
is nef. Indeed, its intersections with each exceptional curve are positive and with the strict transforms of \(L\), \(Q\), and all three coordinate axes are zero. For any other irreducible plane curve of degree \(d\), write \(x,y,z\) for its summed multiplicities along \(A,B,C\) respectively. Bézout with the three axes, \(L\), and \(Q\) yields respectively
\[
2x+y\le3d,\quad y+z\le d,\quad x+z\le2d.
\]
Take \(2/3\), \(1/3\), and \(8/3\) times these inequalities and add:
\[
4x+y+3z\le\frac{23}{3}d<9d.
\]
This proves nefness, including for arbitrary effective divisors by decomposition into irreducible components. Thus a degree-\(d\) curve vanishing to order at least \(m\) at every point satisfies
\[
0\le N\cdot\widetilde C\le9d-(4\cdot3+1\cdot3+3\cdot2)m=9d-21m,
\]
and hence \(d\ge\lceil7m/3\rceil\). This is a characteristic-two argument on the actual eight-point limit; it does not deduce the finite-characteristic conclusion from a characteristic-zero theorem.

## Verification

Run `python3 verify_icosahedral.py` in the directory containing this file. It uses only standard-library Python and constructs its data from the fifteen displayed normals. It first verifies equality with the reflection-generator orbit in Calvo, then checks all \(455\) triple determinants, all \(105\) pairs, the complete generic incidence lattice, the special-fiber line multiset, all \(31\) primitive marked intersections (with all pair-choice comparisons), and the conic point incidences. Expected final status is `ICOSAHEDRAL_15_MODULAR_COLLISIONS_AND_NEFDIVISOR_OK`. The infinite symbolic-degree assertion is proved via the nef divisor and explicit products, not by extrapolating finite numerical tests. The script certifies the finite identities used in that proof, not the abstract cone-of-curves argument.

## Relationship to prior work

Calvo [1, Section 2 and Main Result] introduced and analyzed the complex fifteen-line icosahedral configuration, including its \(15/10/6\) intersection multiplicities and Waldschmidt constant \(11/2\) for the 31 complex points. Those results, and the underlying reflection-hyperplane equations, are prior knowledge. The present result concerns their explicitly integral arithmetic incarnation, the unique dyadic degeneration, and the specialization of every one of the 31 labeled points.

Huynh, Linh, and Long [2, Corollary 2.3] prove a Waldschmidt constant \(7/3\) for the abstract eight-point collinearity pattern of five points on a line and three off-line vertices with three points on their connecting sides. Their setting assumes characteristic zero in the surrounding paper; their abstract \(7/3\) value and degree-seven construction are **not** claimed to be original here. The geometric identification of this pattern as the marked limit of Calvo's 31-point configuration, along with the full collision stratification and complete good/bad reduction classification, is the separate statement evaluated as new.

## Limitations

The integral presentation is fixed: a different lattice for the generic hyperplanes can yield a different special fiber. A point-section weight is a count of marked generic points, not an intrinsic length of the singular scheme of the specialized arrangement. The exact symbolic initial degrees apply to the **reduced eight-point support** in the characteristic-two fiber; they do not describe the scheme of all colliding marked sections or the singular scheme of the nonreduced divisor. The priority assessment is based on the accessible primary sources and targeted mathematical-record searches, not on a proof of bibliographic uniqueness. No independent mathematical validation has been performed.

## References

[1] Sebastian Calvo, *The icosahedral line configuration and Waldschmidt constants*, arXiv:2209.01499 (first posted 2022-09-03), especially Sections 2–5. https://arxiv.org/abs/2209.01499

[2] Dinh Tuan Huynh, Tran N. K. Linh, and Le Ngoc Long, *Some line and conic arrangements and their Waldschmidt constants*, arXiv:2410.05029 (first posted 2024-10-07), especially Corollary 2.3 and its proof. https://arxiv.org/abs/2410.05029
