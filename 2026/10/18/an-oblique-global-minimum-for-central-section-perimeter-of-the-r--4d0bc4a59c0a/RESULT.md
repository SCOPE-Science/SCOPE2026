# An oblique global minimum for central-section perimeter of the regular cuboctahedron

## Finding
Let
\[
C=[-1,1]^3\cap\{(x_1,x_2,x_3):|x_1|+|x_2|+|x_3|\le2\}.
\]
This is the regular cuboctahedron with edge length \(\sqrt2\). For a unit vector \(u\), let \(P(u)\) be the intrinsic Euclidean perimeter of the central polygon \(C\cap u^\perp\).

Let \(t_*\in(0,1)\) be the unique zero of
\[
-1+\frac{t-1}{(1+t)^2\sqrt{1+t^2}}+
\frac{2+3t+5t^2+2t^3}{(1+t)^2\sqrt{2(1+t+t^2)}}=0.
\]
Then the exact sharp global minimum and its complete equality set are
\[
\min_{u\in S^2}P(u)=4(1-t_*)+\frac4{1+t_*}
\left(\sqrt{1+t_*^2}+t_*\sqrt{2(1+t_*+t_*^2)}\right),
\]
\[
t_*=0.5150605280531426445\ldots,\qquad
\min P=7.4755344540607439843\ldots.
\]
Equality holds if and only if \(u\) is a signed coordinate permutation of \((1,t_*,0)/\sqrt{1+t_*^2}\). In particular, no coordinate-axis, face-diagonal or body-diagonal normal minimizes the perimeter.

There is also a global transverse stability estimate: for a normal proportional to \((1,b,c)\), with \(0\le c\le b<1\),
\[
P(1,b,c)-P(1,b,0)\ge
\frac{4c^2(1-b)}{1-c^2}
\left(\sqrt2-\frac{1+2b}{\sqrt{2(1+b+b^2)}}\right),
\]
where \(P(1,b,c)\) denotes the perimeter for the corresponding normal direction. The right-hand side is strictly positive for \(0<c\le b<1\).

## Assumptions and scope
All sections are through the center, not arbitrary affine sections. Perimeter is measured within each section plane in the ambient Euclidean metric. Homogeneity of the normal permits using \((1,b,c)\) without normalization. Symmetry under independent sign changes and coordinate permutations reduces all normals to \(1\ge b\ge c\ge0\). Degenerate normal chambers are included by continuity.

## Proof
**Exact directional formula.** The polyhedron has twelve vertices, all signed permutations of \((0,1,1)\), and twenty-four edges, each of length \(\sqrt2\). For generic \(0<c<b<1\), intersect the plane \(x_1+bx_2+cx_3=0\) with the six square and eight triangular support facets. The resulting central octagon has paired chords of lengths
\[
\ell_y=\frac{2(1-b)\sqrt{1+c^2}}{1-c^2},
\qquad
\ell_z=\frac{2\sqrt{1+b^2}}{1+b},
\]
\[
\ell_+=\frac{(b+c)R_+}{(1+b)(1+c)},
\qquad
\ell_-=\frac{(b-c)R_-}{(1+b)(1-c)},
\]
where
\[
R_+=\sqrt{(b-c)^2+(1+b)^2+(1+c)^2},
\quad
R_-=\sqrt{(b+c)^2+(1+b)^2+(1-c)^2}.
\]
Each length occurs twice, so \(P(b,c)=2(\ell_y+\ell_z+\ell_++\ell_-)\). These expressions follow by solving the two linear plane equations on each supporting facet and taking the distance of the resulting edge endpoints. In particular, the formula extends continuously to \(c=0\), \(c=b\), and \(b=1\).

Put \(M=(R_++R_-)/2\) and \(R_0=\sqrt{2(1+b+b^2)}\). The identity \(R_+^2-R_-^2=4c(1-b)\), together with the chord sum, gives
\[
P(b,c)=\frac{4\sqrt{1+b^2}}{1+b}
+\frac4{1-c^2}\left[
(1-b)\sqrt{1+c^2}+
\frac{(b-c^2)M+(1-b)^2c^2/M}{1+b}\right].\tag{1}
\]
This equation is used for \(b<1\); its boundary value is taken by continuity.

**Transverse comparison.** Both \(R_+\) and \(R_-\) are Euclidean norms of vectors whose mean equals \((1+b,1,b)\). Convexity of the Euclidean norm gives \(M\ge R_0\). For \(0\le c\le b<1\), the map
\[
H(M)=(b-c^2)M+\frac{(1-b)^2c^2}{M}
\]
is nondecreasing on \([R_0,\infty)\): indeed \(b-c^2\ge b(1-b)\), whereas \((1-b)^2c^2/M^2\le(1-b)^2b^2/[2(1+b+b^2)]\le b(1-b)\). Also, concavity of the square root on the unit interval gives the chord inequality
\(\sqrt{1+c^2}\ge1+(\sqrt2-1)c^2\).

Substitute these two bounds into (1), subtract its \(c=0\) value and simplify. The result is precisely the stated quantitative transverse inequality. Its bracket is positive because
\[
4(1+b+b^2)-(1+2b)^2=3>0.
\]
Thus every normal with \(0<c\le b<1\) has strictly greater perimeter than \((1,b,0)\). For the remaining face \(b=1\), direct substitution into the chord formulas gives
\[
P(1,c)=2\sqrt2+2\sqrt{6+2c^2}>2\sqrt2+2\sqrt6=P(1,0)
\quad(0<c\le1).
\]
Consequently **every global minimizer has its smallest absolute normal coordinate equal to zero**.

**One-dimensional sharp minimization.** On that boundary,
\[
P(b,0)=4F(b),\qquad
F(b)=1-b+\frac{\sqrt{1+b^2}+b\sqrt{2(1+b+b^2)}}{1+b},
\quad0\le b\le1.\tag{2}
\]
Set \(r(b)=\sqrt{1+b^2}/(1+b)\) and \(s(b)=b\sqrt{2(1+b+b^2)}/(1+b)\). Direct differentiation gives
\[
r''(b)=\frac{-2b^3+3b^2+3}{(1+b)^3(1+b^2)^{3/2}},
\]
\[
s''(b)=\frac{\sqrt2\,(7b^3+6b^2+3b-4)}
{4(1+b)^3(1+b+b^2)^{3/2}}.
\]
For \(3/5\le b\le1\), both terms are strictly positive. For \(0\le b\le3/5\),
\[
F''(b)\ge\frac{3/(34/25)^{3/2}-\sqrt2}{(1+b)^3}>0.
\]
(The first numerator is at least three; the second numerator is at least minus four, and its other denominator factors are at least one.) Therefore \(F\) is strictly convex on \([0,1]\). Its endpoint derivatives are
\[
F'(0)=\sqrt2-2<0,\qquad F'(1)=\sqrt6/2-1>0.
\]
Exactly one critical point \(t_*\in(0,1)\) exists. Differentiating (2) yields its defining equation in the finding. Strict convexity makes this point the unique minimum in the symmetry chamber. Restoring all signed coordinate permutations proves the sharp equality classification. Every statement holds at the chamber walls because the original perimeter is continuous in the section normal.

## Verification
The standalone checker `cuboctahedron_perimeter_checker.py` reconstructs all twelve vertices and twenty-four edges and computes section polygons by plane-edge intersections followed by an independent planar convex-hull algorithm. It compares the exact directional expression with 2,400 such independent constructions and representative boundary cases. It also checks the symbolic second-derivative identities, rational inequalities used in the global argument, the transverse certificate and a numerical enclosure of the unique critical point. The analytic proof above, not the finite computations, establishes the all-normal assertions.

Run in an environment with Python 3.10 or later and SymPy: `python cuboctahedron_perimeter_checker.py`. The expected last line is `ALL_CUBOCTAHEDRON_SECTION_PERIMETER_CHECKS_OK`.

## Relationship to prior work
Kovič's 2013 classification identifies the cuboctahedron among centrally symmetric Archimedean polyhedra with regular polygonal faces, but its theorems concern antipodal incidence structures, flag graphs and related classification rather than optimization of Euclidean perimeters of central sections. Koenig and Koldobsky prove a maximum-perimeter theorem for central sections of **cubes**, not a minimum-perimeter theorem for **cuboctahedra**. Previously studied cuboctahedral central **areas** and affine-section vertex counts do not imply an exact minimum-perimeter value or an oblique equality set. In particular, neither area extrema nor polygon side counts fix perimeter. The prior comparisons support a distinct result, but do not constitute a proof of universal historical priority.

## Limitations
The theorem concerns central sections of the regular, unscaled cuboctahedron only. It does not determine minimum perimeter among all translated planes, arbitrary affine deformations, or other Archimedean solids. The stability inequality is quantitative but its coefficient is not claimed optimal. The numerical constants are approximate evaluations of exactly characterized quantities. Independent mathematical validation and exhaustive historical-priority determination have not been performed.

## References
- Jurij Kovič, “Centrally symmetric convex polyhedra with regular polygonal faces,” *Mathematical Communications* **18** (2013), 429–440, public 19 November 2013. https://hrcak.srce.hr/110844
- Hermann Koenig and Alexander Koldobsky, “On the maximal perimeter of sections of the cube,” arXiv:1806.08659 (22 June 2018). https://arxiv.org/abs/1806.08659
