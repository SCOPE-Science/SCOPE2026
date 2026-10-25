# Sharp area-halving chord lengths and their directional profile in regular odd polygons

## Finding
Let \(P_n\) be a regular convex Euclidean polygon with odd \(n\ge3\), circumradius \(R>0\), and center \(o\). For an unoriented normal line direction \(\theta\in\mathbb R/\pi\mathbb Z\), a unique line with normal \(\theta\) divides the area of \(P_n\) into equal halves; its intersection with the polygon is denoted \(C_\theta\). Set \(L_n(\theta)=|C_\theta|\) and \(\delta=\pi/(2n)\). Let \(\phi\in[0,\delta]\) be the smallest angle between the normal line and a reflection-axis line of \(P_n\), modulo unoriented lines. Then
\[
L_n(\theta)=\frac{2R\cos\delta\sqrt{\cos(2\delta)}}{\sqrt{\cos^2\phi-\tan^2\delta\,\sin^2\phi}}.
\]
The right-hand side increases strictly with \(\phi\), giving
\[
h_A(P_n)=2R\cos\delta\sqrt{\cos(2\delta)},\qquad H_A(P_n)=2R\cos^2\delta=R(1+\cos(\pi/n)).
\]
Every minimum and maximum occurs in the indicated dihedral classes: a minimizing chord has its normal parallel to a reflection axis; a maximizing chord itself lies along a reflection axis and goes from a vertex to the midpoint of the opposite side. As odd \(n\to\infty\), \(H_A-h_A\sim R\pi^2/(4n^2)\). This statement concerns **area**, not perimeter, bisection.

## Assumptions and scope
The polygon is nondegenerate and geometrically regular in the Euclidean plane. An area-halving line means a complete supporting line cutting polygon area into two equal portions; the associated chord is its segment inside \(P_n\). Directions are **unoriented** and are parametrized by normals rather than tangents. Reflection axes of odd regular polygons are the lines through a vertex and the midpoint of its opposite side. Since their unoriented directions form a lattice of spacing \(\pi/n=2\delta\), every normal has a nearest reflection axis at angle \(\phi\in[0,\delta]\).

## Proof
**Existence and uniqueness.** For a fixed unit normal \(u\), the area \(A(t)=\operatorname{area}(P_n\cap\{x:u\cdot x\le t\})\) varies continuously from zero to the full area as \(t\) crosses the polygon. It is strictly increasing when the cutting line meets the interior. Thus there is one and only one area-bisecting line for each normal direction.

**Reduction and the anchor.** Dihedral reflections reduce normal directions to the closed sector \(0\le\phi\le\delta\), measured from a chosen reflection-axis line. At its upper endpoint \(\phi=\delta\), the *chord direction*, perpendicular to its normal, is a reflection-axis line of the odd polygon. That line itself bisects area by reflection and joins a vertex to the midpoint of the opposite edge. Its length is the distance between the opposite vertex and side midpoint. The inradius is \(R\cos(\pi/n)=R\cos(2\delta)\), so this length is
\[
L_* = R+R\cos(2\delta)=2R\cos^2\delta.
\]
Choose as \(E_+\) and \(E_-\) the two polygon edges met by the chord for the interior directions of the sector. These are mirror images under reflection in its lower-endpoint axis. Their extended supporting lines intersect in a point \(O\) on that axis, and the rays from \(O\) toward the edge interiors make angles \(+\delta\) and \(-\delta\) with the axis. This includes the triangular case, in which \(O\) is a polygon vertex. The two rays have identical allowed radial intervals because the edges are reflected copies.

**Equal-area product law.** Represent the cutting endpoints on these rays by \(p=O+a(\cos\delta,\sin\delta)\) and \(q=O+b(\cos\delta,-\sin\delta)\), with \(a,b>0\), after a rigid motion. While they remain in \(E_+\), \(E_-\), the area cut off between the two edges and the cutting chord differs from the wedge-triangle area \(ab\sin(2\delta)/2\) by a fixed area independent of \(a,b\). Consequently two such chords divide the polygon into the same two areas if and only if their endpoint products \(ab\) agree. Let \(c=a_*b_*\) be the positive product for the already known area-bisecting anchor chord. The equal-area chords in this edge pair therefore satisfy \(ab=c\).

At \(\phi=0\), the mirror-symmetric chord has endpoints at equal ray distance, hence \(a=b=\sqrt c\). At \(\phi=\delta\), the anchored chord has endpoints at the two admissible ray distances \(a_*,b_*\), with product \(c\). Along the interpolation \(a=\sqrt c\,e^s\), \(b=\sqrt c\,e^{-s}\) for \(s\) between zero and the anchor parameter, both endpoints stay inside their respective edges: their radial distances lie between \(a_*\) and \(b_*\), which both belong to the common permissible radial interval of the mirrored edges. Hence this construction never crosses an edge boundary. It joins both endpoint directions continuously with area exactly halved.

**Angular relation and length.** The chord displacement is \(p-q=((a-b)\cos\delta,(a+b)\sin\delta)\), up to reversing signs. A normal to that line makes an angle \(\phi\) with the horizontal reflection axis, where
\[
\tan\phi=\cot\delta\,|\tanh s|.
\]
Along the interpolation this is strictly monotone, and reaches the sector endpoint \(\delta\) at the anchor. Thus it describes every normal in the fundamental sector; by area-bisector uniqueness there are no other chords to consider. The Euclidean cosine rule gives
\[
\begin{aligned}
L_n(\theta)^2&=a^2+b^2-2ab\cos(2\delta)\\
&=4c\bigl(\sinh^2s+\sin^2\delta\bigr)\\
&=\frac{4c\sin^2\delta}{\cos^2\phi-\tan^2\delta\,\sin^2\phi}.
\end{aligned}
\]
At \(\phi=\delta\), the denominator equals \(\cos(2\delta)/\cos^2\delta\), which is positive because \(\delta\le\pi/6\). Matching the anchor length \(L_*=2R\cos^2\delta\) yields \(4c\sin^2\delta=4R^2\cos^2\delta\cos(2\delta)\); substitution proves the formula for every normal.

**Extremality, equality and limit.** The denominator is \(1-(1+\tan^2\delta)\sin^2\phi\), strictly decreasing for \(0<\phi<\delta\), and positive even at \(\phi=\delta\). Therefore the chord length strictly increases with \(\phi\), and the two endpoints give all equality orientations in the full normal circle. Finally Taylor expansion at \(\delta=0\) gives \(2R\cos^2\delta-2R\cos\delta\sqrt{\cos 2\delta}=R\delta^2+O(R\delta^4)=R\pi^2/(4n^2)+O(Rn^{-4})\).

## Verification
The attached `verify_halving.py` is a standalone numerical cross-check. For odd \(n\in\{3,5,7,9,11,13,19,31,51\}\), it constructs \(P_n\), numerically clips it by a line in each of 37 equally spaced sector directions, solves for the exactly half-area offset by bisection, measures the resulting segment length, and compares with the analytic formula. The maximum absolute discrepancy for unit circumradius was below \(4\times10^{-13}\). These finite checks illustrate boundary behavior but do **not** prove the theorem; the wedge-area argument above proves the assertion for all odd \(n\ge3\) and all directions.

## Relationship to prior work
Grüne, Klein, Miori, and Segura Gomis (2007) defined area-halving distance \(h_A(v)\) and its extrema \(h_A,H_A\) for arbitrary planar convex bodies and proved general inequalities, but the inspected full work does not state this all-odd-regular-polygon directional identity or its equality classes. Esposito et al.'s 2010/2012 shortest-fence work studies optimized area-partition interfaces rather than the full direction-fixed profile of regular odd polygons. Distinct prior geometric studies of regular polygon *center-passing* chords cannot imply the formula by replacing the center cut with an area cut: except for symmetry axes, an odd regular polygon's center cut is generally not area-halving. Marques da Silva and Craizer (2024) study envelopes of bisecting lines and explicitly describe hyperbolic arc envelopes of regular pentagons, but do not state these chord-length extrema or the entire all-odd-\(n\) law in the material examined. Literature comparison remains nonexhaustive; a relevant 2022 bisecting-envelope paper was not accessible in full.

## Limitations
The result is restricted to Euclidean *regular odd* polygons. It makes no new claim for arbitrary convex polygons, even-sided regular polygons, or perimeter bisection. The attached numerical verifier is finite sampling, not computer proof. The historical bibliographic comparison is best-effort: an unindexed equivalent formula or implicit consequence of unavailable full papers cannot be excluded. The finding has undergone self-review only; no independent audit or certification is claimed.

## References
1. A. Grüne, R. Klein, C. Miori, S. Segura Gomis, “Chords halving the area of a planar convex set,” *Mathematical Inequalities & Applications* **10** (2007), 205–216. DOI: 10.7153/mia-10-17.
2. L. Esposito, C. Nitsch, C. Trombetti, “The longest shortest fence and sharp Poincaré–Sobolev inequalities,” arXiv:1011.6248, first submitted 2010-11-29; subsequent journal version.
3. J. A. Marques da Silva and M. Craizer, “Envelopes of Bisection Lines of Polygons,” *International Electronic Journal of Geometry* **17** (2024), 421–436. DOI: 10.36890/iejg.1512613.
4. A. Berele and S. Catoiu, “Bisecting envelopes of convex polygons,” *Advances in Applied Mathematics* **137** (2022), 102342. DOI: 10.1016/j.aam.2022.102342 (abstract/metadata consulted; full text unavailable during comparison).
