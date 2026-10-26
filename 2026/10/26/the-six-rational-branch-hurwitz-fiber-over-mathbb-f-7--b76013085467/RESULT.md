# The six-rational-branch Hurwitz fiber over \(\mathbb F_7\)

## Finding
Let \(k=\mathbb F_7\). Consider separable degree-three morphisms \(\pi:C\to\mathbb P^1_k\) with \(C\) a smooth, projective, geometrically connected genus-one curve, and suppose their geometric branch divisor consists of **six distinct \(k\)-rational points**. Every such cover is isomorphic, allowing a \(k\)-automorphism of the target \(\mathbb P^1\), to the projection
\[
\pi_0:E\to\mathbb P^1,\qquad E:\ Z^3+X^2Z+2Y^3=0,\qquad [X:Y:Z]\longmapsto[X:Y].
\]
Thus the unmarked arithmetic Hurwitz fiber contains exactly **one** isomorphism class. Its source has \(\#E(\mathbb F_7)=13\), the Hasse upper bound for a genus-one curve over this field.

More precisely, after the six branch points are *fixed pointwise* on the target as \(\mathbb P^1(\mathbb F_7)\setminus\{[0:1],[1:0]\}\), there are exactly **two** isomorphism classes of covers over the fixed target. They are represented by \(\pi_0\) and
\[
\pi_1:E_1\to\mathbb P^1,\qquad E_1:\ Z^3+Y^2Z+2X^3=0,\qquad [X:Y:Z]\longmapsto[X:Y].
\]
The target involution \([X:Y]\mapsto[Y:X]\) identifies these two classes.

## Assumptions and scope
All morphisms, curve isomorphisms, and target automorphisms are defined over \(\mathbb F_7\). A branch point means a geometric branch point of the separable finite degree-three morphism. Six distinct rational branch points are necessarily all simply ramified: the tame Riemann--Hurwitz different for a genus-one degree-three map to genus zero has total degree six. The **fixed-target** count differs from the count allowing base automorphisms. No assertion is made about covers whose branch points have other residue degrees or about arbitrary characteristic.

## Proof
**1. Every cover has a projected plane-cubic model.** Set \(L=\pi^*\mathcal O_{\mathbb P^1}(1)\), of degree three. On a genus-one curve, Riemann--Roch gives \(h^0(C,L)=3\), and every degree-three line bundle is very ample. The two sections defining \(\pi\) extend to a basis of \(H^0(C,L)\), embedding \(C\) as a smooth plane cubic with coordinates \([X:Y:Z]\) and \(\pi=[X:Y]\). The point \([0:0:1]\) is outside this cubic, because the two sections defining \(\pi\) have no common zero. Hence its homogeneous cubic equation has nonzero \(Z^3\)-coefficient, which can be normalized to one. As \(3\) is invertible in \(k\), an \(\mathbb F_7\)-linear translation of \(Z\) removes the \(Z^2\)-term. We obtain
\[
Z^3+Q(X,Y)Z+R(X,Y)=0,
\]
with \(Q\) a binary quadratic and \(R\) a binary cubic. After depressing, any isomorphism of covers **over the same fixed target** must send \(Z\) to \(sZ+\ell(X,Y)\), where \(s\in k^\times\) and \(\ell\) is linear, because it acts linearly on the complete three-dimensional section space of \(L\). Comparison of \(Z^2\)-coefficients forces \(\ell=0\). Accordingly the remaining equivalence is \((Q,R)\sim(s^{-2}Q,s^{-3}R)\).

**2. Fixing the branch divisor.** The group \(\operatorname{PGL}_2(k)\) acts transitively on the unordered pairs of rational points of \(\mathbb P^1(k)\). Since \(\#\mathbb P^1(k)=8\), we may normalize the complementary two nonbranch points to \([0:1]\) and \([1:0]\). The binary branch sextic is then a nonzero multiple of
\[
\prod_{t\in k^\times}(X-tY)=X^6-Y^6.
\]
For a depressed cubic, the usual discriminant \(-4Q^3-27R^2\) becomes \(3Q^3+R^2\) modulo seven. Thus every sought cover satisfies the exact coefficient identity
\[
3Q(X,Y)^3+R(X,Y)^2=\kappa(X^6-Y^6),\qquad\kappa\in k^\times.
\tag{1}
\]
This is a complete reduction; there are no unaccounted forms or rational descent assumptions.

**3. Exact finite classification of (1).** Write
\[
Q=a_0X^2+a_1XY+a_2Y^2,\qquad
R=b_0X^3+b_1X^2Y+b_2XY^2+b_3Y^3.
\]
There are exactly \(7^3\cdot7^4=823543\) coefficient septuples. Exhaustively expanding \(3Q^3+R^2\) and comparing all seven coefficients in (1) gives precisely the following twelve septuples:

| \(\kappa\) | \(Q\) | \(R\) | Coefficient pairs |
|---|---|---|---|
| \(3\) | \(aX^2\) | \(bY^3\) | \(a\in\{1,2,4\}\), \(b\in\{2,5\}\) |
| \(4\) | \(aY^2\) | \(bX^3\) | \(a\in\{1,2,4\}\), \(b\in\{2,5\}\) |

The finite universal quantifier over septuples is established by `verify.cpp`, which checks every septuple without sampling; a separate evaluation-based enumeration (`check_evaluation.py`) independently verifies the same complete list using the six rational branch slopes instead of coefficient convolution. The checker files are included with this proof and provide their loop bounds, field arithmetic, and exact expected solution sets. No general algebraic closure statement is inferred from finite sampling.

For \(s\in k^\times\), multiplication by \(s^{-2}\) cycles through \(\{1,2,4\}\) and multiplication by \(s^{-3}\) supplies both signs of \(2\), with their combined six values forming the entire first row as one orbit. The second row likewise forms one orbit. These two orbits have different \(\kappa\), and \(s^6=1\) over \(k^\times\), so they are distinct over the **fixed target**. Swapping \(X,Y\) identifies the two and proves the unmarked uniqueness.

**4. Smoothness, branching, and point count.** The equation \(Z^3+X^2Z+2Y^3=0\) is smooth over the algebraic closure: the partial derivative in \(Y\) is \(6Y^2\), hence a singular point must have \(Y=0\); the derivatives in \(X\) and \(Z\), together with the equation, then exclude any projective singular point. Its branch discriminant is \(3(X^6-Y^6)\), a separable sextic in characteristic seven, so the indicated projection has exactly the required six branch points.

For \([X:Y]=[t:1]\) with \(t\in k^\times\), the fiber polynomial \(z^3+t^2z+2\) has one double and one distinct simple \(k\)-root (the double root is \(-3t^4\), using \(t^6=1\)); thus each of the six branch fibers has two distinct rational points. At \(t=0\), the equation \(z^3+2=0\) has no rational root, because nonzero cubes in \(k\) are \(\{1,-1\}\). At \([1:0]\), the equation \(z^3+z=0\) has exactly one rational root because \(-1\) is a nonsquare in \(k\). Therefore
\[
\#E(k)=6\cdot2+0+1=13.
\]
The genus is one by the plane-cubic formula. The Hasse bound gives \(\#E(k)\le\lfloor 7+1+2\sqrt 7\rfloor=13\), so this curve is maximal over \(k\).

## Verification
From the folder containing the supplementary files, execute `c++ -O2 -std=c++17 verify.cpp -o verify && ./verify` and `python check_evaluation.py` (Python requires NumPy). The expected terminal markers are `VERIFY_OK` and `INDEPENDENT_VERIFY_OK`. Both exact enumerations produced twelve coefficient solutions, six at each scalar \(\kappa=3,4\); the normalized cover count is two and the unmarked count is one. Both separately computed thirteen rational source points. The proof does not rely on the numerical genus-one point count for the cover classification.

## Relationship to prior work
Agostini, Markwig, Nollau, Schleis, Sendra-Arranz, and Sturmfels [1] develop the inverse discriminant problem for plane cubics over characteristic zero and study the generic forty-solution plane Hurwitz fiber and real solutions. Their general discriminant framework motivates the problem, but the six-point **finite-field arithmetic fiber**, its two fixed-target classes, and source point count are not provided in their inspected statements, tables, or cubic-recovery algorithms. Weir [2] develops more general algorithms for cubic function fields with prescribed discriminant and tabulates aggregate finite-field counts; his algorithms are closely relevant, but the inspected numerical tables do not identify these twelve coefficient models or the unique six-rational-branch class. The result concerns a natural maximal-rationality branch configuration, not a new generic complex Hurwitz number.

## Limitations
The classification is only for separable genus-one covers of degree three over \(\mathbb F_7\) with **all six geometric branch points distinct and rational**. It distinguishes covers over a fixed target from covers permitting target reparameterization. It neither classifies every elliptic degree-three cover nor computes the geometric Hurwitz fiber of the special sextic over an algebraic closure. The finite enumeration is exact and exhausts only the specified coefficient set. Potential overlap remains with any unpublished parameter-specific output of older discriminant-table algorithms. No independent external audit has been performed.

## References
1. D. Agostini, H. Markwig, C. Nollau, V. Schleis, J. Sendra-Arranz, B. Sturmfels, *Recovery of Plane Curves from Branch Points*, arXiv:2205.11287, first posted 2022-05-23; Discrete & Computational Geometry 72 (2024), 451–475. https://arxiv.org/abs/2205.11287 ; https://link.springer.com/article/10.1007/s00454-023-00538-5
2. C. Weir, *Constructing and Tabulating Dihedral Function Fields*, PhD thesis, University of Calgary, August 2013, Chapters 3–4 and 6. https://doczz.net/doc/8044433/my-thesis---colin-weir
3. R. Scheidler and C. Weir, *Constructing and tabulating dihedral function fields*, ANTS-X (2012). https://mathweb.ucsd.edu/~kedlaya/ants10/paper-scheidler.html
