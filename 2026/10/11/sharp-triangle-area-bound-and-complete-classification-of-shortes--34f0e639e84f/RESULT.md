# Sharp triangle area bound and complete classification of shortest perimeter-halving chords

## Finding
For every nondegenerate Euclidean triangle \(T\), let \(s>0\) be its semiperimeter and \(\alpha\in(0,\pi/3]\) its smallest interior angle. A *perimeter-halving chord* connects two boundary points such that either of the two boundary arcs between them has length \(s\). Let \(h(T)\) be the minimum Euclidean length of these chords. Then
\[
h(T)=s\sin(\alpha/2),\qquad \frac{A(T)}{h(T)^2}\ge\frac{4}{3\sqrt3}.
\]
The area inequality is sharp, with equality exactly for equilateral triangles. All shortest halving chords are precisely the chords from a vertex of smallest angle joining the two points at arclength \(s/2\) from that vertex along its incident edges. The number of such chords equals the number of minimum-angle vertices (one, two, or three).

## Assumptions and scope
\(T\) is any planar triangle with strictly positive area, and its boundary is equipped with the ordinary Euclidean arclength. Endpoints can be vertices or interior points of edges, with repeated boundary points identified geometrically. The chord length is Euclidean distance, *not* distance along the boundary. The result does not concern chords halving *area*, or general smooth convex cycles. Write side lengths \(a\le b\le c\) opposite interior angles \(\alpha\le\beta\le\gamma\), respectively. The strict triangle inequalities hold.

## Proof
**1. Exact shortest-chord formula and complete minimizers.** No side of a nondegenerate triangle can contain both endpoints of a perimeter-halving pair: their shortest arc along that side has length at most the side length, which is strictly less than \(s\) because each side is less than the sum of the other two. Thus a pair lies on distinct edges, which share a unique vertex \(V\). Choose the arc between endpoints passing through \(V\). Its length is \(s\), since both arcs are halving arcs. If its two subarc lengths from \(V\) are \(u,v\ge0\), then \(u+v=s\). Writing \(\theta_V\) for the angle at \(V\) and applying the cosine law to the triangle spanned by these two endpoints and \(V\),
\[
|pq|^2=u^2+v^2-2uv\cos\theta_V
=s^2\sin^2(\theta_V/2)+(u-v)^2\cos^2(\theta_V/2)
\ge s^2\sin^2(\alpha/2).
\]
The two edges incident at any smallest-angle vertex have lengths \(b,c\), the two longer sides. Since \(c<a+b\), we have \(s=(a+b+c)/2<a+b\le2b\), hence \(b>s/2\). Also \(c\ge b>s/2\). Therefore the points at distance \(s/2\) along each incident edge exist strictly inside the edges. They give a halving pair with \(u=v=s/2\), attaining the universal lower bound. Equality in the cosine-law bound requires both \(\theta_V=\alpha\) and \(u=v=s/2\), because \(\cos(\theta_V/2)>0\); this proves the classification.

**2. Sharp area bound.** Put \(x=s-a\), \(y=s-b\), \(z=s-c\); the triangle inequalities are equivalent to \(x\ge y\ge z>0\). Then \(s=x+y+z\), \(b=x+z\), \(c=x+y\). Heron's formula gives \(A(T)=\sqrt{sxyz}\). The standard half-angle identity gives
\[
\sin^2(\alpha/2)=\frac{(s-b)(s-c)}{bc}=
\frac{yz}{(x+z)(x+y)}.
\]
Consequently the exact dimensionless area/halving-distance ratio is
\[
\frac{A(T)}{h(T)^2}
=\frac{(x+y)(x+z)}{s^2}\sqrt{\frac{sx}{yz}}.
\]
Since \(x\ge y\ge z>0\), one has \(x/y\ge1\) and \(s/z\ge3\), hence \(sx/(yz)\ge3\). Also \(y\le(s-z)/2\) and \(z\le s/3\), so
\[
(x+y)(x+z)=(s-y)(s-z)
\ge \frac{(s+z)(s-z)}2
=\frac{s^2-z^2}2\ge\frac49s^2.
\]
Multiplying the inequalities proves \(A(T)/h(T)^2\ge(4/9)\sqrt3=4/(3\sqrt3)\). Equality forces \(x=y=z\), and therefore \(a=b=c\). Conversely, for an equilateral triangle of side length \(\ell\), \(s=3\ell/2\), \(h=3\ell/4\), and \(A=\sqrt3\ell^2/4\), giving exactly the displayed constant.

## Verification
The companion self-contained standard-library `verify.py` performs 1,771 exact-rational tangent-length checks, including equality and a polynomial nonnegative-defect identity; it independently minimizes the piecewise-quadratic boundary-halving chord lengths for 1,206 Euclidean triangles, checking the analytic formula and area ratio. Run `python verify.py`; the observed output was `VERIFY_OK 1771 exact-rational triples; 1206 independent halving-chord minimizations`. These finite checks are supplementary: the proof above covers all nondegenerate triangles without reliance on enumeration. The boundary cases of zero area are excluded because the theorem assumes strict triangle inequalities.

## Relationship to prior work
Dumitrescu, Ebbers-Baumann, Grüne, Klein and Rote introduced and studied the minimum perimeter-halving distance, including the universal convex-cycle inequality \(A\ge h^2/\sqrt3\), and explicitly calculated the equilateral-triangle ratio \(A/h^2=4/(3\sqrt3)\). Their broad convex-cycle conjectural comparison does not, in the inspected primary material, prove the sharp inequality for all triangles or classify every minimizing triangle chord. The present triangle-only result strengthens that universal bound on a precisely delimited natural class, with a rigid equality case. It does not establish the conjectured bound for general convex cycles. Research on triangle roundness and minimum width addresses different invariants and does not directly imply this sharp area/halving-chord ratio.

## Limitations
The result concerns a nondegenerate Euclidean triangle, not arbitrary convex polygons, convex cycles, or perimeter-halving chords in other norms. The full 2008 thesis *Geometric Dilation and Halving Distance* by Ansgar Grüne could not be inspected through available public full-text mirrors, so historically equivalent assertions remain a residual priority risk. Finite checks are not an independent validation or an infinite proof.

## References
1. Adrian Dumitrescu, Annette Ebbers-Baumann, Ansgar Grüne, Rolf Klein, and Günter Rote, *On the geometric dilation of closed curves, graphs, and point sets*, arXiv:math/0407135v1 (first public 2004-07-08); *Computational Geometry* 36 (2006), 16–38. https://arxiv.org/abs/math/0407135 ; https://doi.org/10.1016/j.comgeo.2005.07.004 .
2. The same authors, *On Geometric Dilation and Halving Chords*, WADS 2005, DOI:10.1007/11534273_22. https://page.mi.fu-berlin.de/rote/Papers/pdf/On+geometric+dilation+and+halving+chords.pdf .
3. Ansgar Grüne, *Geometric Dilation and Halving Distance*, doctoral thesis, University of Bonn, 2008; https://bonndoc.ulb.uni-bonn.de/xmlui/handle/20.500.11811/3563 (bibliographic/limited preview only; full text not inspected).
