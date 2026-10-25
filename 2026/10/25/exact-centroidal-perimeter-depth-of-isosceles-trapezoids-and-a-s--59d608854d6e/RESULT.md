# Exact centroidal perimeter depth of isosceles trapezoids and a sharp quarter bound

## Finding
Let \(B>b>0\) and \(h>0\), and let
\[
T=\operatorname{conv}\{(-B,0),(B,0),(b,h),(-b,h)\}.
\]
Let \(G\) be the **area centroid** of \(T\). A line through \(G\) meets \(\partial T\) at two points and divides the original perimeter into two boundary arcs (the new cutting segment is **not** counted). Denote by \(m(T)\) the least possible shorter-arc length divided by the full perimeter, with the minimum taken over all unoriented lines through \(G\).

Write
\[
\begin{aligned}
 d&=B-b,& L&=\sqrt{d^2+h^2},&
 c&=\frac{B+2b}{3(B+b)},\\
 a&=B-dc,& v&=cL,&
 z_-&=\frac{a}{1-c},\\
 z_*&=\min\{2B,\max\{z_-,a+\sqrt{av}\}\}.
\end{aligned}
\]
Then the **exact parameter-wide law** is
\[
\boxed{m(T)=\frac{\min\left\{2b+2(1-c)L,\ z_*+\frac{v z_*}{z_*-a}\right\}}{2(B+b+L)}.}
\]
There are exactly two possible geometries for a minimizing line: the horizontal line through \(G\), or one of the two reflection-paired chords cutting off a lower-corner arc, with bottom-side distance \(z_*\) from that corner. The first and second numerator terms select the relevant directions; if they tie, both types minimize.

Every genuine trapezoid in the displayed family satisfies the **strict sharp inequality**
\[
\boxed{m(T)>\tfrac14,\qquad \inf_{B>b>0,\ h>0}m(T)=\tfrac14.}
\]
The infimum is approached, and not attained, when \(B=1\), \(b=1/k\), \(h=k\) and \(k\to\infty\). Thus the sharp family-wide perimeter-depth threshold is a quarter; the full formula also resolves every finite-parameter equality direction.

## Assumptions and scope
The polytope is a nondegenerate, Euclidean, **isosceles** trapezoid with strictly unequal positive half-base lengths. Distance along the boundary is Euclidean arclength. The centroid uses planar Lebesgue area, not boundary arclength. The result does not assert a quarter bound for arbitrary quadrilaterals or arbitrary convex bodies. The limiting triangular or rectangular configurations are used only for comparisons, not as additional positive-base equality cases.

The symmetry axis is \(x=0\), and direct integration of the horizontal section length gives
\[
G=(0,ch),\qquad c=\frac{B+2b}{3(B+b)}\in(\tfrac13,\tfrac12).
\]
The perimeter is \(P=2(B+b+L)\).

## Proof
**1. Classification of intersected edges.** By reflection symmetry, an unoriented centroidal line can be written \(y=ch+tx\), \(t\ge0\), together with the vertical limit. Define
\[
t_L=\frac{ch}{B},\qquad t_R=\frac{(1-c)h}{b}.
\]
Since \(B(1-c)\ge bc\) for \(B\ge b\), we have \(0<t_L<t_R\). The line meets (i) both oblique legs for \(0\le t\le t_L\); (ii) the bottom base and right leg for \(t_L\le t\le t_R\); (iii) the bottom and top bases for \(t\ge t_R\). The transitions correspond to the lower-left and upper-right vertices, respectively. This exhausts all lines by symmetry.

**2. Both-leg regime.** Write the heights of the two leg intersections as
\[
y_L=\frac{ch-tB}{1-td/h},\qquad y_R=\frac{ch+tB}{1+td/h}.
\]
The dimensionless sum \(S(t)=(y_L+y_R)/h\) satisfies
\[
S(t)=\frac{2(c-dBt^2/h^2)}{1-d^2t^2/h^2}.
\]
Its derivative with respect to \(t^2\) has the sign of \(d(cd-B)\), which is strictly negative. The two boundary arcs are
\[
2B+LS(t)\quad\text{and}\quad 2b+L(2-S(t)).
\]
The former strictly decreases, while the latter strictly increases. Thus every shorter arc in this regime is bounded below by the smaller of the upper horizontal arc \(U=2b+2(1-c)L\) and the lower arc at \(t=t_L\).

**3. The lower-corner regime.** Use the lower-right corner \((B,0)\) as origin of unit edge rays directed left along the base and upward along the right leg. In those rays the centroid has coordinates \((a,v)\), with \(a=B-dc>0\) and \(v=cL>0\). If the chord intersects the two rays at respective distances \(z\) and \(w\) from the corner, collinearity with \(G\) gives
\[
\frac az+\frac vw=1,\qquad w=\frac{vz}{z-a}.
\]
The condition that both endpoints lie on the *actual finite edges* is exactly
\[
\frac{a}{1-c}=z_-\le z\le2B.
\]
The shorter right-corner arc candidate is therefore \(F(z)=z+vz/(z-a)\), with \(F''(z)=2av/(z-a)^3>0\). Its unique constrained minimum occurs at the clamped stationary point
\[
z_*=\min\{2B,\max\{z_-,a+\sqrt{av}\}\}.
\]
The other arc cannot produce an additional minimum: \(P-F(z)\), being concave, is minimized at an endpoint. At \(z=2B\), that complementary arc is the upper leg arc from the first regime and is at least \(U\). At \(z=z_-\), the right-corner arc is at most half the perimeter (as verified in the next regime); hence its complement is at least \(F(z_-)\ge F(z_*)\). Consequently the best value over the second regime is at least \(\min\{U,F(z_*)\}\), and the bound is attained when the corresponding term is selected.

**4. Two-base regime.** For \(t\ge t_R\), the lower and upper intercept abscissas are \(-ch/t\) and \((1-c)h/t\). The right-hand boundary arc is
\[
\frac P2-\frac{(1-2c)h}{t}.
\]
It is the shorter arc and increases strictly with \(t\), because \(c<1/2\). Its minimum is the shared boundary value \(F(z_-)\) at \(t=t_R\). Steps 1–4 therefore prove the exact formula and, by strictness and strict convexity, the stated complete minimizing-line classification.

**5. Sharp strict quarter bound.** In the horizontal candidate \(U\), compute
\[
2\left(U-\frac P4\right)=3b-B+(3-4c)L.
\]
This is positive if \(3b\ge B\). Otherwise \(L>B-b\), \(3-4c>0\), and
\[
3b-B+(3-4c)(B-b)
=\frac{2(B^2+Bb+4b^2)}{3(B+b)}>0.
\]
For any finite lower-corner chord, \(z\ge z_-=B+bc/(1-c)>B\). Also \(w=vz/(z-a)\) decreases with \(z\), so
\[
w\ge \frac{2BcL}{B+dc}\ge\frac L2.
\]
The last inequality is equivalent to \(c(3B+b)\ge B\), whose difference from equality is
\[
c(3B+b)-B=\frac{2b(2B+b)}{3(B+b)}>0.
\]
Hence \(F(z)>B+L/2>P/4\), since \(B>b\). This completes the strict lower bound for the two global candidates.

Finally, for \(B=1\), \(b=1/k\), \(h=k\), we have \(c\to1/3\), \(L\sim k\), \(a\to2/3\), and \(a+\sqrt{av}>2B\) for sufficiently large \(k\). Thus \(z_*=2\) and \(F(z_*)\sim L/2\) while \(U\sim4L/3\); dividing by \(P\sim2L\) proves \(m(T)\to1/4\).

## Verification
The standalone `trapezoid_depth_checker.py` uses only Python's standard library. It computes 204 symmetric polygon instances, compares the formula against 367404 separately generated centroidal-line/boundary intersections, and verifies the predicted minimizing chords where the direct intersection is nondegenerate. Every tested line respects the proposed lower bound. It checks the sharp family and an exact integer-side median example. To rerun, use `python trapezoid_depth_checker.py`; the resulting marker is `TRAPEZOID_DEPTH_OK`.

This is a numerical cross-check. The unlimited parameter and angle ranges are established by Steps 1–5, not inferred from sampled directions.

## Relationship to prior work
Berele and Catoiu's 2026 triangle manuscript establishes the vertex-ray W-line formula and analyzes centroidal perimeter splits for **triangles**. That ray optimization is used as a known elementary ingredient; this result instead treats every **genuine isosceles trapezoid**, where a new two-leg regime and a two-base regime must also be compared. The closed three-parameter formula, global sharp trapezoid bound and complete direction classification are not stated in that inspected manuscript.

A significant source caution is that the same manuscript's asserted universal lower bound \(3/10\) for triangles is incompatible with its own median formula. For an isosceles triangle of side lengths \(15,15,2\), a line from a base endpoint to the opposite leg midpoint passes through the centroid and cuts off the boundary fraction
\[
\frac{2+15/2}{2+2\cdot15}=\frac{19}{64}<\frac3{10}.
\]
This triangle calculation is supplied as a transparent comparison and is **not** asserted as a separately novel theorem or a new trapezoid equality case. The genuinely new claimed statement is the exact open trapezoid-family law above. Geometric dilation of isosceles trapezoids, regular-polygon centroidal perimeter depth, and quadrilateral centroidal chord *length* asymmetry address different invariants and do not imply the formula here.

## Limitations
No independent scientific review has been performed. Historical priority is provisional, especially because a general polygonal boundary-depth formula could exist under different terminology. Only centered isosceles trapezoids with Euclidean boundary arclength and *area* centroid are classified; no arbitrary quadrilateral or arbitrary convex-body extension is claimed. Parameter limiting configurations are not positive-area equality cases at \(1/4\).

## References
1. A. Berele and S. Catoiu, *The Perimeter Winternitz Theorem in a Triangle*, arXiv:2603.23653v1, publicly submitted 2026-03-24. The full arXiv-rendered text was examined, in particular Lemma 2 and Theorems 1 and 4.
2. A. Berele and S. Catoiu, *The perimeter Winternitz theorem in a triangle relative to the Nagel point*, Journal of Geometry 117 (2026), DOI:10.1007/s00022-026-00814-8. This concerns a different center, not the area centroid.
