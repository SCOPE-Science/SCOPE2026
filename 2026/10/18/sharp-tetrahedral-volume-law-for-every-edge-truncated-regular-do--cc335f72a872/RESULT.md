# Sharp tetrahedral-volume law for every edge-truncated regular dodecahedron

## Finding
Let \(\varphi=(1+\sqrt5)/2\). For the regular dodecahedron \(D\) described below and its uniform edge-truncation family \(P_t\), the exact largest volume of a contained tetrahedron is
\[
 M(t)=\frac{F(t)}6,\qquad F(t)=16+(32\varphi-64)t+(108-60\varphi)t^2+(36\varphi-60)t^3,
 \qquad 0\le t\le\tfrac12.
\]
This function is strictly decreasing. At each interior parameter \(0<t<1/2\), exactly 120 unordered four-element subsets of the 60 polytope vertices realize \(M(t)\). Additionally, at least 40 distinct two-dimensional families of maximizing tetrahedra occur by moving an apex through a triangular cutting face. This last assertion is an existence count, **not** an exhaustive classification of all non-vertex maximizers.

For the uniform Archimedean truncated dodecahedron, at \(t_U=(5-\sqrt5)/10\),
\[
 M(t_U)=\frac{17}{15}+\frac{37\sqrt5}{75},\qquad
 \frac{M(t_U)}{\operatorname{Vol}(P_{t_U})}=\frac{236+111\sqrt5}{3110}.
\]

## Assumptions and scope
The twenty points of \(D\subset\mathbb R^3\) consist of all eight \((\pm1,\pm1,\pm1)\) together with all twelve cyclic permutations of \((0,\pm\varphi^{-1},\pm\varphi)\). Their thirty edges are exactly their pairs at squared Euclidean distance \(8-4\varphi\). Orient every edge in both directions and write
\[
 P_t=\operatorname{conv}\{(1-t)u+tv:(u,v)\text{ is an oriented edge of }D\},
 \quad 0\le t\le\tfrac12.
\]
At interior parameters this has 60 distinct vertices, with \(P_0=D\) and \(P_{1/2}\) the rectified dodecahedron (icosidodecahedron). An arbitrary contained tetrahedron may use any points of \(P_t\), not only its vertices. Volumes are ordinary Euclidean three-volumes in these coordinates; rescaling the whole body by a factor \(s\) multiplies all stated volumes by \(s^3\).

## Proof
**Vertex reduction.** For four points \(x_1,x_2,x_3,x_4\) the signed sixfold tetrahedral volume is
\[
 \det(x_1-x_4,x_2-x_4,x_3-x_4).
\]
Holding three points fixed, its absolute value is a convex function of the remaining point. Replacing each point successively by a maximizer among the vertices of \(P_t\) cannot decrease the absolute determinant. Thus it suffices to compare all unordered quadruples of the 60 listed affine vertex paths, even at endpoints where paths coincide.

**Exact determinant certificate.** Use the deterministic ordering in `verify.cpp`: first the eight sign triples in lexicographic sign-loop order, then the twelve cyclic vertices indexed by the zero coordinate and the other two signs; list all unordered edges \(i<j\) in lexicographic order; list the 30 affine paths \(V_i\to V_j\), followed by the 30 reversed paths. Every quadruple of paths has a determinant polynomial \(p(t)\) of degree at most three with coefficients in \(\mathbb Z[\varphi]\). The program constructs each polynomial from evaluations at the four integers \(0,1,-1,2\) using exact ring arithmetic.

The quadruple with zero-based path indices \((0,10,15,20)\) gives the displayed \(F(t)\), up to its orientation sign. For each of the \(\binom{60}{4}=487635\) unordered quadruples, the program checks that all four cubic Bernstein coefficients of **both** \(F(t)-p(t)\) and \(F(t)+p(t)\) on \([0,1/2]\) are nonnegative. More precisely, if \(q(t)=c_0+c_1t+c_2t^2+c_3t^3\), the four Bernstein coefficients multiplied by 24 are
\[
 24c_0,\qquad 24c_0+4c_1,\qquad
 24c_0+8c_1+2c_2,\qquad
 24c_0+12c_1+6c_2+3c_3.
\]
Every cubic Bernstein basis function is nonnegative on the closed interval and strictly positive in its interior. Nonnegative coefficients therefore imply \(q(t)\ge0\) everywhere, and strict positivity in the interior unless \(q\equiv0\). The checker performs the complete \(487635\times 8\) coefficient-sign comparisons exactly; signs in \(\mathbb Z[\varphi]\) are decided by comparing integer squares with \(5\) where needed. It also verifies exactly 120 quadruple determinant polynomials equal \(F\) or \(-F\). Every other quadruple has strictly smaller volume at every interior parameter. Together with the explicit witness, these facts prove the formula and the interior vertex-supported equality count for a continuum of parameters, not merely a sample grid.

**Movable-apex families.** For each winning four-vertex subset, remove each vertex in turn. The same exact enumeration finds exactly 40 unordered triples of remaining fixed vertices each having three distinct compatible maximizing apex vertices, all on the three truncation edges incident to one original dodecahedral vertex. Their signed tetrahedral determinants agree. Any point in the triangle spanned by those three apex vertices is inside \(P_t\); determinant affinity in that fourth vertex makes its whole two-dimensional triangular apex region maximizing. This yields 40 distinct families when \(0<t<1/2\). The calculation makes no assertion about the exhaustiveness of non-vertex equality.

**Strict monotonicity.** Direct differentiation and \(\varphi=(1+\sqrt5)/2\) give
\[
 F'(t)=(-126+54\sqrt5)\left(t-\frac23\right)
 \left(t-2-\frac{2\sqrt5}{3}\right)<0
 \qquad(0\le t\le\tfrac12).
\]
Both linear factors are negative, and the scalar coefficient is negative. Since \(F(1/2)>0\), the maximal volume is everywhere positive and strictly decreasing.

**Uniform member.** Along a truncated pentagonal face the edge length is \((1-2t)(2/\varphi)\); along a triangular cutting face it is \(t\varphi(2/\varphi)=2t\). Equating them gives \(t_U=1/(2+\varphi)=(5-\sqrt5)/10\), with common edge length \(a=2t_U\). Inserting this into the stated cubic yields \(M(t_U)=17/15+37\sqrt5/75\). The classical uniform truncated-dodecahedron volume formula \(\operatorname{Vol}=5(99+47\sqrt5)a^3/12\) simplifies in these coordinates to \(10/3+74\sqrt5/15\), producing the quoted exact ratio.

## Verification
Compile and execute the standalone exact checker, included as `verify.cpp`, using `g++ -std=c++17 -O2 -Wall -Wextra verify.cpp -o verify && ./verify`. It asserts 30 original edges, 60 oriented truncation paths, exactly 487635 four-path configurations, nonnegative Bernstein coefficients for both signs, 120 maximizing interior path quadruples, and 40 triple-indexed movable-apex families. The exact-sign function uses integer arithmetic and an intermediate 128-bit product, with no floating-point decisions. Independently substituting \(t=1/2\) gives \(M(1/2)=(25+11\sqrt5)/24\), matching the rectified dodecahedral endpoint. The code verifies the universal polynomial inequality through an exhaustive finite certificate whose inequalities analytically govern the full interval; numerical sampling alone would not establish the theorem.

## Relationship to prior work
General work on maximum-volume simplices establishes geometric and algorithmic principles but does not directly yield the truncation-dependent exact cubic or the 120/40 interior equality structure. The regular-icosahedron truncation family has a shared rectified endpoint, but its different initial body and different vertex paths mean that its intermediate-volume profile does not imply this theorem. Similarly, exact tetrahedral-volume profiles for cube–octahedron intersections concern a distinct family. Known polyhedral descriptions supply the classical volume of the uniform truncated dodecahedron; that body-volume identity is not claimed as new.

## Limitations
The result concerns **edge-uniform truncation of this particular regular dodecahedron**, not arbitrary dodecahedral deformations. It proves the **number of vertex-supported** maximizers at interior parameters and constructs 40 moving-apex families; it does not classify every continuously varying tetrahedron or enumerate distinct endpoint maximizers. This is a mathematical proof with a complete exact finite checker, not a formal proof-assistant certification. Historical literature coverage cannot rule out an obscure equivalent previously published enumeration; independent review remains necessary.

## References
1. M. Di Summa, F. Eisenbrand, Y. Faenza, C. Moldenhauer, “On largest volume simplices and sub-determinants,” arXiv:1406.3512, version 1 posted 13 June 2014, https://arxiv.org/abs/1406.3512 .
2. A. V. Akopyan and A. A. Glazyrin, “On maximum volume simplices in polytopes,” *Periodica Mathematica Hungarica* 69 (2014), 251–256, DOI:10.1007/s10998-014-0051-2, open author PDF https://users.mccme.ru/akopyan/papers/Akopyan-Glazyrin-Maximum-Volume.pdf .
3. D. McCooey, “Truncated Dodecahedron,” polyhedral reference with explicit geometric and volume data, https://dmccooey.com/polyhedra/TruncatedDodecahedron.html .
