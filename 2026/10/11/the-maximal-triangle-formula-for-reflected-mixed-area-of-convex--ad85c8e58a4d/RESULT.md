# The maximal-triangle formula for reflected mixed area of convex quadrilaterals

## Finding

Let \(Q\subset\mathbb R^2\) be any nondegenerate convex quadrilateral and let \(S=\operatorname{area}(Q)>0\). Write
\[
T(Q)=\max\{\operatorname{area}(\operatorname{conv}\{x,y,z\}):x,y,z\in Q\}.
\]
For the mixed area \(V_2\), normalized by
\[
\operatorname{area}(K+tL)=\operatorname{area}(K)+2tV_2(K,L)+t^2\operatorname{area}(L),\qquad t\ge0,
\]
**the following identity is exact for every convex quadrilateral**:
\[
\boxed{V_2(Q,-Q)=2T(Q).}
\]
Consequently, for every real \(t\ge0\), the complete reflection-Minkowski polynomial is
\[
\boxed{\operatorname{area}(Q+t(-Q))=(1+t^2)S+4tT(Q).}
\]
In particular,
\[
\boxed{2S-V_2(Q,-Q)=2(S-T(Q)),\qquad
6S-\operatorname{area}(Q-Q)=4(S-T(Q)).}
\]
Thus the deficit in the sharp planar Godbersen/Rogers--Shephard inequality equals precisely twice/four times the area missed by a largest inscribed triangle. This is an **identity**, not merely a bound. In a genuine quadrilateral the deficit is positive and can tend to zero only as a vertex becomes redundant.

## Assumptions and scope

A nondegenerate convex quadrilateral is the convex hull of four distinct points in strictly convex position in \(\mathbb R^2\); collinear limits are addressed only by continuity. All areas are ordinary planar Lebesgue areas. Reflected sets are \(-Q=\{-x:x\in Q\}\), and Minkowski addition is \(K+L=\{x+y:x\in K,y\in L\}\). The claim is for *every* such quadrilateral, with no symmetry, angle, or metric assumptions. It is affine invariant and translation invariant. The maximum in \(T(Q)\) runs over all triangles contained in \(Q\), not merely a chosen triangulation.

## Proof

**1. Inscribed maximal triangles use vertices.** For fixed \(y,z\in Q\), the area \(\tfrac12|\det(y-x,z-x)|\) is the absolute value of an affine function of \(x\) and hence convex in \(x\). Its maximum on a polygon occurs at a vertex. Repeating this maximization successively in the \(y\) and \(z\) variables shows that a largest-area inscribed triangle is obtained from three vertices. (An inscribed triangle is the convex hull of three points; conversely every such triangle lies in \(Q\).) Thus it suffices to compare the four vertex-deletion triangles.

**2. Complete affine normalization.** Let \(A,B,C,D\) be the cyclically ordered vertices and let the diagonals \(AC\) and \(BD\) intersect at \(O\). Their directions are linearly independent. Translate \(O\) to the origin and apply the invertible linear map taking \(C\) to \((-1+a,0)\), \(A\) to \((a,0)\), \(D\) to \((0,b-1)\), and \(B\) to \((0,b)\). The parameters \(a,b\) lie strictly between \(0\) and \(1\). Indeed the map uses the full diagonal vectors as coordinate axes, so \(A-C=(1,0)\) and \(B-D=(0,1)\). Swapping endpoints of either diagonal replaces that parameter by its complement, and exchanging the two diagonal axes interchanges \(a,b\). Since both sides of the asserted identity are affinely covariant with the same determinant factor, we may assume without loss of generality that
\[
0<a\le b\le\tfrac12.
\]
In these coordinates the four vertices are
\[
A=(a,0),\quad B=(0,b),\quad C=(a-1,0),\quad D=(0,b-1).
\]
The shoelace or diagonal determinant formula gives \(S=\tfrac12\). The four vertex triangles have respective areas
\[
\frac a2,\quad\frac{1-a}{2},\quad\frac b2,\quad\frac{1-b}{2}.
\]
Because \(a\le b\le\tfrac12\), the largest is \(T(Q)=(1-a)/2\).

**3. Determine the entire difference polygon.** The difference body \(Q-Q\) is the convex hull of the sixteen vectors \(X-Y\), with \(X,Y\in\{A,B,C,D\}\). Four are zero. The diagonal differences supply \((\pm1,0)\) and \((0,\pm1)\), whose convex hull is the diamond \(\{|x|+|y|\le1\}\). The other differences are precisely the negatives and positives of
\[
(a,-b),\quad(a,1-b),\quad(a-1,-b),\quad(a-1,1-b).
\]
The pairs \(\pm(a,-b)\) and \(\pm(a,1-b)\) lie in the diamond because \(a+b\le1\) and \(a+(1-b)\le1\), respectively. Accordingly, they cannot enlarge the hull already containing the four diagonal differences. The other four nondiamond candidates, together with the four diagonal differences, form the polygon given in cyclic order by
\[
(-1,0),\ (a-1,-b),\ (0,-1),\ (1-a,b-1),\ (1,0),\ (1-a,b),\ (0,1),\ (a-1,1-b).
\]
To justify that this ordered eight-point list is indeed convex, compute successive oriented edge-pair determinants. They are, cyclically,
\[
b-a,\quad1-a,\quad1-a-b,\quad a,\quad b-a,\quad1-a,\quad1-a-b,\quad a,
\]
all nonnegative for \(0<a\le b\le1/2\). The list is simple (its points proceed through the four coordinate quadrants in order), hence determines a convex polygon; zero determinants allow redundant collinear vertices, without changing the hull. We have therefore identified \(Q-Q\) exactly, including parameter-equality boundaries.

**4. Shoelace evaluation and polarization.** Applying the shoelace identity to that eight-point polygon gives
\[
\operatorname{area}(Q-Q)=3-2a.
\]
The verification is purely algebraic: the oriented double-area sum of the eight cyclic pairs equals \(6-4a\), and the \(b\)-terms cancel. Since \(2S=1\) and \(T(Q)=(1-a)/2\),
\[
V_2(Q,-Q)=\frac{\operatorname{area}(Q-Q)-2S}{2}
=\frac{(3-2a)-1}{2}=1-a=2T(Q).
\]
Both mixed area and maximal triangle area are multiplied by \(|\det M|\) under every nonsingular affine-linear change of coordinates; their equality is therefore valid for the original quadrilateral. The polynomial and deficit formulas follow from the mixed-area normalization stated above.

**5. Sharp endpoint behavior.** The parameter \(a\) is strictly positive for a strict quadrilateral and can be arbitrarily close to zero, proving that \(2S-V_2(Q,-Q)>0\) with no positive uniform area-normalized lower bound. The maximal possible relative deficit within quadrilaterals is \(1\), attained exactly for parallelograms: \(a=\tfrac12\) and \(a\le b\le\tfrac12\) force \(a=b=\tfrac12\). In normalized form, \((2S-V_2(Q,-Q))/S=2a\in(0,1]\).

## Verification

The standalone program `verify.py` uses exact rational arithmetic and an independent monotone-chain convex-hull implementation, not the explicit eight-vertex hull used in the proof. It checks every parameter pair with positive numerators below denominators \(7,11,13,17\), plus affine images with determinant \(13\). It confirms the difference-body area, the largest of all four vertex triangles, the mixed-area identity, and the affine scaling. Executing it yielded `VERIFY_OK 642 exact-rational quadrilaterals`. Its finite regression tests are not used to infer the universal quantifier; that depends on steps 1--5.

## Relationship to prior work

Kotrbatý and Mouamine, *Godbersen's conjecture and the \(L_p\)-Rogers--Shephard inequality*, arXiv:2607.20387v2, prove the sharp mixed-volume bound \(V_2(K,-K)\le2\operatorname{area}(K)\) and polytope equality only for triangles. Friedland, Putterman and Szusterman, *Equality case in the Kotrbatý-Mouamine inequality*, arXiv:2610.04527v1 (first posted 3 October 2026), extend the equality characterization to arbitrary convex bodies. Bianchini and Colesanti, *A sharp Rogers & Shephard type inequality for the p-difference body of planar convex bodies*, arXiv:math/0702102v1, study global sharp constants and shadow-system reductions. These are broader **inequalities** or equality criteria. Their inspected arguments do not supply an exact formula for the Godbersen deficit in terms of the largest inscribed triangle on the whole four-vertex class. In particular, knowing strictness for each quadrilateral does not determine the coefficient \(2\) in the present identity or the full reflection polynomial.

## Limitations

The identity is proved only for four-vertex planar convex polytopes (and their degenerate triangular limits). It does **not** extend by the same formula to arbitrary convex bodies or arbitrary higher-vertex polygons; for example, a unit disk has \(V_2(B,-B)=\pi\), whereas twice the area of its largest inscribed triangle equals \(3\sqrt3/2\). No dimension-independent Godbersen stability bound, proof of publication-level novelty, or independent validation is claimed. Historical unindexed instances of this elementary-looking quadrilateral identity remain a literature risk.

## References

1. J. Kotrbatý and M. A. Mouamine, *Godbersen's conjecture and the \(L_p\)-Rogers--Shephard inequality*, arXiv:2607.20387v2 (14 September 2026), https://arxiv.org/html/2607.20387v2.
2. O. Friedland, E. Putterman and M. Szusterman, *Equality case in the Kotrbatý-Mouamine inequality*, arXiv:2610.04527v1 (3 October 2026), https://arxiv.org/html/2610.04527v1.
3. C. Bianchini and A. Colesanti, *A sharp Rogers & Shephard type inequality for the p-difference body of planar convex bodies*, arXiv:math/0702102v1 (5 February 2007), https://arxiv.org/pdf/math/0702102.
4. C. A. Rogers and G. C. Shephard, *The difference body of a convex body*, Archiv der Mathematik 8 (1957), 220--233 (classical difference-body inequality).
