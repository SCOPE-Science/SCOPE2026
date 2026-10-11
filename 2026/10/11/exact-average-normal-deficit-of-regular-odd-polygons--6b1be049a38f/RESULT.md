# Exact average-normal deficit of regular odd polygons
## Finding
Let \(P_n\) be a regular Euclidean \(n\)-gon with odd \(n\ge3\). For a point \(p\in P_n\), let \(n(P_n,p)\) be the number of Euclidean normals of \(P_n\) passing through \(p\), and let
\[
n(P_n)=\frac{1}{\operatorname{area}(P_n)}\int_{P_n}n(P_n,p)\,dp.
\]
Then
\[
n(P_n)=8-2\bigl(\sec(\pi/n)-1\bigr)^2
      =6+4\sec(\pi/n)-2\sec^2(\pi/n).
\]
Thus the values increase strictly along odd \(n\), with \(n(P_3)=6\), and
\[
8-n(P_n)=\frac{\pi^4}{2n^4}+O(n^{-6}).
\]
In particular, the most symmetric non-centrally-symmetric regular polygons approach the known planar value \(8\) from below at quartic order.

## Assumptions and scope
Normals and the averaged invariant are exactly those in the source definition: a normal starts at a boundary point and is perpendicular to a supporting line there. At a polygon vertex, a generic interior point determines at most one such normal line from that vertex; the measure-zero boundaries between normal cones do not affect the integral.

The proof uses the polygonal active regions \(U_F\) associated with faces \(F\). For an edge \(E\), \(U_E\) is the intersection of the polygon with the strip swept out by perpendiculars to \(E\) through points of \(E\). For a vertex, \(U_v\) is the corresponding vertex-normal wedge intersected with the polygon. Hann's planar Euler-type identity, as reproduced in the primary survey, gives
\[
\sum_v\operatorname{area}(U_v)=\sum_E\operatorname{area}(U_E).
\]
Hence
\[
n(P)=\frac{2\sum_E\operatorname{area}(U_E)}{\operatorname{area}(P)}.
\]

For even regular polygons, the known theorem for centrally symmetric cyclic polygons already yields \(n(P_n)=8\). The new calculation below concerns odd \(n\).

## Proof
Write \(n=2m+1\), put
\[
\alpha=\frac{\pi}{n},\qquad c=\cos\alpha,\qquad s=\sin\alpha,
\]
and normalize the circumradius to \(1\). Take the vertices
\[
v_j=\bigl(\cos((2j+1)\alpha),\sin((2j+1)\alpha)\bigr),
\qquad j=0,\ldots,n-1.
\]
The edge joining \(v_{n-1}=(c,-s)\) to \(v_0=(c,s)\) is vertical. Its active region is therefore
\[
U_E=P_n\cap\{(x,y):|y|\le s\}.
\]
All \(n\) edge active regions have the same area by dihedral symmetry.

The polygon area is
\[
A=\operatorname{area}(P_n)=nsc.
\]
It remains to remove the two congruent caps above and below the strip. The upper cap has vertices
\[
v_0,v_1,\ldots,v_{m-1},q,
\]
where
\[
v_{m-1}=(-\cos 2\alpha,\sin 2\alpha),\qquad
v_m=(-1,0),
\]
and the horizontal line \(y=s\) meets the edge \(v_{m-1}v_m\) at
\[
q=\left(-1+\frac{s^2}{c},s\right).
\]
Let \(C\) be the area of this cap. The shoelace sum gives
\[
2C=(m-1)\sin 2\alpha+\det(v_{m-1},q)+\det(q,v_0)
   =\frac{s}{c}\bigl(2(m-1)c^2-2c+1\bigr).
\]
Since the top and bottom caps are congruent,
\[
\begin{aligned}
\operatorname{area}(U_E)
&=A-2C\\
&=nsc-\frac{s}{c}\bigl(2(m-1)c^2-2c+1\bigr)\\
&=\frac{s}{c}\bigl(3c^2+2c-1\bigr),
\end{aligned}
\]
where the last step uses \(n=2m+1\).

The active-region integral and Hann's planar identity now give
\[
\begin{aligned}
n(P_n)
&=\frac{2n\operatorname{area}(U_E)}{A}\\
&=2\frac{3c^2+2c-1}{c^2}\\
&=6+\frac4c-\frac2{c^2}\\
&=8-2\left(\frac1c-1\right)^2.
\end{aligned}
\]
This proves the exact formula.

For odd \(n\), the quantity \(\sec(\pi/n)\) decreases strictly to \(1\), so the displayed deficit decreases strictly and \(n(P_n)\) increases strictly. Finally,
\[
\sec x-1=\frac{x^2}{2}+O(x^4),
\]
so
\[
8-n(P_n)=2(\sec(\pi/n)-1)^2
=rac{\pi^4}{2n^4}+O(n^{-6}).
\]

## Verification
The supplied `verify.py` independently reconstructs regular odd polygons for every odd \(n\) from \(3\) through \(101\), clips each polygon by the active strip \(|y|\le\sin(\pi/n)\), computes areas by shoelace, and checks the resulting average against
\[
8-2\bigl(\sec(\pi/n)-1\bigr)^2.
\]
It also checks strict increase on the tested range and prints representative values. This finite computation is only an indexing and geometry sanity check; the proof for all odd \(n\) is the symbolic cap calculation above.

## Relationship to prior work
Domokos and Lángi review Santaló's average-normal problem, reproduce Hann's Euler-type active-region identity, and note that Hug proved \(n(P)=8\) for a centrally symmetric convex polygon exactly when it is cyclic. They also emphasize that no planar convex body with average number of normals exceeding \(8\) was known at the time and pose the existence of such a body as a question. Their paper does not state an exact formula for regular odd polygons.

Nasonov, Panina, and Siersma revisit average numbers of normals for convex polytopes in a later concurrent-normals study. Their explicit planar average result treats triangles; the inspected discussion does not give a regular odd-polygon family formula.

The present theorem is not a new upper bound for arbitrary convex bodies. Its contribution is the exact full-family evaluation and the quartic approach rate to the classical value \(8\).

## Limitations
The result does not prove or disprove the existence of a planar convex body with average number of normals greater than \(8\). It treats only Euclidean regular polygons, not arbitrary cyclic or equiangular odd polygons.

The literature comparison has a historical-access limitation: Hann's 1993 article is the source of the general Euler-type identity, but its full text was not used to make a negative coverage claim here. The 2014 survey was materially inspected and supplies the exact identity and the known polygonal extremal statements used in the proof. An older unindexed explicit computation of the regular odd family remains a residual originality risk.

## References
1. G. Domokos and Z. Lángi, *On the average number of normals through points of a convex body*, arXiv:1406.0813v1, first posted 2014-06-03; later Studia Scientiarum Mathematicarum Hungarica 52 (2015), 457--476, DOI: 10.1556/012.2015.52.4.1320. Primary MSC: 52A40.
2. K. Hann, *The average number of normals through a point in a convex body and a related Euler-type identity*, Geometriae Dedicata 48 (1993), 27--55.
3. I. Nasonov, G. Panina, and D. Siersma, *Concurrent normals problem for convex polytopes and Euclidean distance degree*, arXiv:2406.01773.
