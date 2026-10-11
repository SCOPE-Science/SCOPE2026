# Complete area spectrum of maximum-perimeter diameter-one nonagons
## Finding
Consider convex Euclidean nonagons of diameter \(1\). Among those attaining the maximum possible perimeter, the area takes exactly two values:
\[
A_{\mathrm{tri}}
=
\frac92\sin\!\left(\frac{\pi}{9}\right)-\frac{\sqrt3}{2},
\]
and
\[
A_{\mathrm{reg}}
=
9\sin^2\!\left(\frac{\pi}{18}\right)
\cot\!\left(\frac{\pi}{9}\right).
\]
Numerically,
\[
A_{\mathrm{tri}}=0.673065241181070\ldots,
\qquad
A_{\mathrm{reg}}=0.745619231777417\ldots .
\]

The smaller value belongs to the Reinhardt class with periodic composition \([(3)^3]\), whose underlying constant-width curve is the Reuleaux triangle. The larger value belongs to the regular nonagon, with composition \([(1)^9]\).

Both classes have the same extremal perimeter
\[
P_{\max}=18\sin\!\left(\frac{\pi}{18}\right).
\]
Their exact area gap is
\[
A_{\mathrm{reg}}-A_{\mathrm{tri}}
=
\frac{\sqrt3-9\tan(\pi/18)}2
=
0.072553990596346\ldots>0.
\]

## Assumptions and scope
A polygon is normalized to diameter \(1\), meaning the greatest Euclidean distance between two of its vertices is \(1\). A Reinhardt polygon is used in the standard sense: an equilateral convex polygon inscribed in a Reuleaux polygon of the same diameter, with every vertex of the Reuleaux polygon also a polygon vertex.

The result concerns the complete set of perimeter-maximizing convex nonagons under this normalization. It is a secondary optimization statement: after the perimeter objective has tied, area distinguishes the two possible congruence classes.

No claim is made here about even-sided small polygons or about the full area spectrum away from maximum perimeter.

## Proof
The inspected Reinhardt-polygon classification gives two facts needed for completeness.

First, every diameter-normalized convex \(n\)-gon that is extremal for perimeter belongs to the Reinhardt family when \(n\) is not a power of \(2\). Second, every Reinhardt polygon with fewer than \(30\) sides is periodic. A periodic Reinhardt composition has the form
\[
[(k_1,\ldots,k_s)^d],
\]
where \(d>1\) divides \(n\), the integers \(s,d\) are odd, and the positive block entries sum to \(n/d\).

For \(n=9\), only \(d=3\) and \(d=9\) are possible. If \(d=9\), the block sum is \(1\), giving only \([(1)^9]\). If \(d=3\), the block sum is \(3\). Since \(s\) is odd and the entries are positive, either \(s=1\), giving \([(3)^3]\), or \(s=3\), forcing the block \((1,1,1)\), which again gives \([(1)^9]\). Hence exactly two dihedral, and therefore congruence, classes occur.

In any diameter-one Reinhardt nonagon, each side is a chord of a unit-radius Reuleaux arc whose central angle is
\[
\frac{\pi}{9}.
\]
Thus every side has length
\[
2\sin\!\left(\frac{\pi}{18}\right),
\]
and both classes have perimeter
\[
P_{\max}=18\sin\!\left(\frac{\pi}{18}\right).
\]

For the class \([(3)^3]\), the underlying star polygon is an equilateral triangle of side \(1\). Each of the three \(60^\circ\) boundary arcs of its Reuleaux triangle is subdivided into three equal \(20^\circ\) subarcs. The polygonal cap over one side of the equilateral triangle is the difference between three unit-radius isosceles triangles of apex angle \(20^\circ\) and the equilateral triangle. Its area is therefore
\[
\frac32\sin\!\left(\frac{\pi}{9}\right)-\frac{\sqrt3}{4}.
\]
Adding the three caps to the equilateral triangle gives
\[
\begin{aligned}
A_{\mathrm{tri}}
&=
\frac{\sqrt3}{4}
+
3\left(
\frac32\sin\!\left(\frac{\pi}{9}\right)
-\frac{\sqrt3}{4}
\right)\\
&=
\frac92\sin\!\left(\frac{\pi}{9}\right)
-\frac{\sqrt3}{2}.
\end{aligned}
\]

For the regular diameter-one nonagon, the side length is the same value
\[
s=2\sin\!\left(\frac{\pi}{18}\right).
\]
The standard regular-polygon area formula yields
\[
A_{\mathrm{reg}}
=
\frac94s^2\cot\!\left(\frac{\pi}{9}\right)
=
9\sin^2\!\left(\frac{\pi}{18}\right)
\cot\!\left(\frac{\pi}{9}\right).
\]

Put \(x=\pi/18\). Since \(\sin(\pi/9)=2\sin x\cos x\),
\[
A_{\mathrm{reg}}-A_{\mathrm{tri}}
=
\frac{\sqrt3-9\tan x}{2}.
\]
This is positive. Indeed, set
\[
t_0=\frac{1}{3\sqrt3}.
\]
Then
\[
\tan\!\bigl(3\arctan t_0\bigr)
=
\frac{10\sqrt3}{27}
>
\frac{\sqrt3}{3}
=
\tan\!\left(\frac{\pi}{6}\right).
\]
Both compared angles lie in \((0,\pi/2)\), so
\[
\arctan t_0>\frac{\pi}{18},
\]
and consequently
\[
9\tan\!\left(\frac{\pi}{18}\right)<\sqrt3.
\]
Therefore \(A_{\mathrm{reg}}>A_{\mathrm{tri}}\), completing the two-value spectrum.

## Verification
The supplied `verify.py` is an exact symbolic replay in SymPy. It constructs the nine vertices of the \([(3)^3]\) class from the three \(60^\circ\) unit-circle arcs, computes its shoelace area, and proves symbolically that the result equals
\[
\frac92\sin\!\left(\frac{\pi}{9}\right)-\frac{\sqrt3}{2}.
\]
It independently reconstructs the regular diameter-one nonagon, checks its side length, diameter normalization, and area formula, and verifies the exact gap identity.

The script also enumerates the positive odd-length blocks of total \(9/d\) for \(d=3,9\), confirming that the periodic-composition reduction produces only \([(3)^3]\) and \([(1)^9]\). This finite enumeration is exhaustive only because the published classification first proves that every Reinhardt nonagon is periodic; the script is not used as a substitute for that theorem.

## Relationship to prior work
Reinhardt's classical diameter problem asks for maximal perimeter among convex \(n\)-gons of fixed diameter. Hare and Mossinghoff's archive-era treatment states that Reinhardt polygons are precisely the relevant extremal family, describes them by dihedral compositions, and records that every Reinhardt polygon with fewer than \(30\) sides is periodic. Those results imply the two-class reduction for \(n=9\), but the inspected paper does not compute or compare the two nonagon areas.

The later area literature records Reinhardt's classical theorem that, for odd \(n\), the regular diameter-one \(n\)-gon is the unique maximum-area small \(n\)-gon. That broader theorem implies the ordering
\[
A_{\mathrm{reg}}>A_{\mathrm{tri}},
\]
but it does not supply the exact area of the nonregular perimeter maximizer, the exact gap, or the complete secondary area spectrum of the perimeter-extremal set.

Targeted searches using the terms “Reinhardt nonagon,” “maximum-perimeter nonagon,” the composition \([(3)^3]\), both exact area expressions, their decimal values, and the exact gap did not locate a prior statement of the two-value spectrum.

## Limitations
The classification step depends on the published theorem that every Reinhardt polygon with fewer than \(30\) sides is periodic. The geometric area computations themselves are elementary and independently reproduced.

The result does not strengthen the classical theorem that the regular odd polygon maximizes area among all diameter-one odd polygons; it refines the different perimeter problem by resolving area on its full nonagon optimizer set.

Historical indexing of old isodiametric geometry is incomplete. An unindexed exercise or note could contain the same nonregular area calculation, although no such statement was located in the inspected primary and secondary sources.

## References
1. K. G. Hare and M. J. Mossinghoff, *Sporadic Reinhardt Polygons*, Discrete & Computational Geometry 49 (2013), 540--557. DOI: 10.1007/s00454-012-9479-4. First public preprint: arXiv:1203.4107v1, 2012-03-19.
2. M. J. Mossinghoff, *Enumerating isodiametric and isoperimetric polygons*, Journal of Combinatorial Theory, Series A 118 (2011), 1801--1815. DOI: 10.1016/j.jcta.2011.03.004.
3. C. Bingane and M. J. Mossinghoff, *Small polygons with large area*, arXiv:2204.04547v1, 2022-04-09; Journal of Global Optimization 88 (2024), 1035--1050.
4. K. Reinhardt, *Extremale Polygone gegebenen Durchmessers*, Jahresbericht der Deutschen Mathematiker-Vereinigung 31 (1922), 251--270.
