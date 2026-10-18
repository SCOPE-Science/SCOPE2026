# Sharp tetrahedral-volume envelope of twisted regular polygonal prisms

## Finding

For every integer \(n\ge3\), radius \(R>0\), height \(h>0\), and twist angle \(\theta\in\mathbb R\), put
\[
P_n(R)=\operatorname{conv}\{R(\cos(2\pi j/n),\sin(2\pi j/n)):0\le j<n\}
\]
and define the three-dimensional convex body
\[
K_{n,R,h,\theta}=\operatorname{conv}\bigl((P_n(R)\times\{0\})\cup
((\operatorname{Rot}_\theta P_n(R))\times\{h\})\bigr).
\]
This is a right regular polygonal prism when \(\theta=0\), and a twisted two-base prismatoid otherwise. The maximization below is over **all** Euclidean tetrahedra contained in \(K_{n,R,h,\theta}\), not merely tetrahedra whose vertices were prescribed in advance.

Define the angular lattice spacing and longest vertex-chord length by
\[
\eta_n=\begin{cases}2\pi/n,&n\text{ even},\\\pi/n,&n\text{ odd},\end{cases}
\qquad
L_n=\begin{cases}2R,&n\text{ even},\\2R\cos(\pi/(2n)),&n\text{ odd}.\end{cases}
\]
Set \(\delta_n(\theta)=\operatorname{dist}(\theta-\pi/2,\eta_n\mathbb Z)\), where the distance is ordinary distance on the real line. In particular \(0\le\delta_n(\theta)\le\eta_n/2\). Then the **exact largest tetrahedral volume** is
\[
\boxed{M_n(R,h,\theta)=\frac{hL_n^2}{6}\cos\delta_n(\theta).}
\tag{1}
\]
For every parameter choice, a maximizing tetrahedron exists with precisely two vertices on each base, and the segment joining its two vertices in each base is a longest vertex-to-vertex chord of that regular polygon. Among tetrahedra all of whose vertices are vertices of the prismatoid, every maximizer is of this two-on-each-base type for \(n\ge4\). For \(n=3\), three-on-one-base tetrahedra tie only when \(\delta_3(\theta)=\pi/6\); the assertion does **not** classify all maximizers with nonvertex points.

For fixed \(n,R,h\), as \(\theta\) ranges through a full period \(\eta_n\), the volume (1) fills precisely the interval
\[
\boxed{\frac{hL_n^2}{6}\cos(\eta_n/2)\le M_n(R,h,\theta)\le\frac{hL_n^2}{6}.}
\tag{2}
\]
Both bounds are attained. The upper endpoint occurs exactly when \(\theta-\pi/2\in\eta_n\mathbb Z\), and the lower exactly when \(\theta-\pi/2\in (\mathbb Z+1/2)\eta_n\). In particular, **untwisted bases maximize** (1) when \(4\mid n\), but **untwisted bases minimize** (1) when \(n\) is odd or \(n\equiv2\pmod4\). This twist-response reversal holds in every polygon order, including the triangular case.

## Assumptions and scope

The polygon \(P_n(R)\) is a filled regular convex polygon, rather than only its boundary or vertex set. The two copies have the same circumradius, common vertical axis, and parallel planes a distance \(h\) apart; there is no restriction on \(h/R\). The body is the convex hull of those two filled copies, and \(\operatorname{Rot}_\theta\) is planar Euclidean rotation. Tetrahedra may have any orientation and any four points of the body as vertices. Degenerate tetrahedra have zero volume and cannot maximize. Periodicity is \(\eta_n\) for the **extremal volume**, although the solid itself need not have that rotational period as a labelled object.

The theorem does not optimize the containing prismatoid's own volume, impose equal lateral edge lengths, or classify all equality configurations beyond the explicitly stated existence and vertex-supported restriction.

## Proof

**1. Reduction to four polytope vertices.** For four variable points in a fixed compact convex polytope, six times the tetrahedral volume is the absolute value of an affine determinant in each point separately. Fixing three points, its maximum in the remaining point is attained at an extreme point of the polytope (the absolute value of an affine function is convex). Repeating for the other three variables yields a maximum with all four points at polytope vertices. Every polytope vertex of \(K_{n,R,h,\theta}\) is among the specified two copies of the \(n\) polygon vertices.

**2. The only layer splits.** Four selected vertices all in one horizontal plane have volume zero. A split of one vertex versus three gives, by the pyramid formula,
\[
V_{1+3}=\frac h3 A_3,
\]
where \(A_3\) is the area of their projected triangle in the appropriate regular polygon. Every triangle whose vertices lie on the circumcircle of radius \(R\) has area at most \(3\sqrt3R^2/4\), with equality only for an equilateral triangle. Consequently
\[
6V_{1+3}\le\frac{3\sqrt3}{2}hR^2.
\tag{3}
\]
For a split of two vertices in each layer, write \(a,b\in P_n(R)\) for the lower projections and \(c,d\in\operatorname{Rot}_\theta P_n(R)\) for the upper projections. Direct expansion of the three-dimensional determinant gives
\[
6V_{2+2}=h\bigl|\det_2(b-a,d-c)\bigr|.
\tag{4}
\]

**3. The regular difference body.** For a planar convex body \(P\), its difference body \(P-P=\{x-y:x,y\in P\}\) is convex. If \(n\) is even, \(-P_n(R)=P_n(R)\), hence \(P_n(R)-P_n(R)=2P_n(R)\): it is a regular \(n\)-gon of circumradius \(2R\). If \(n\) is odd, the edge-normal directions of \(P_n(R)\) and \(-P_n(R)\) interlace at angular increments \(\pi/n\). Their Minkowski sum is therefore a regular \(2n\)-gon. Its vertices are the differences of maximally separated vertices of \(P_n(R)\), whose separation is \(2R\cos(\pi/(2n))\). Thus in both parity cases \(D_n=P_n(R)-P_n(R)\) is a regular polygon whose circumradius is \(L_n\), and whose consecutive vertex directions differ by \(\eta_n\).

Because the absolute determinant in (4) is convex in either vector separately, its maximum over the two difference bodies \(D_n\) and \(\operatorname{Rot}_\theta D_n\) is attained at a vertex of each. These vertices are exactly the vectors of the polygon's longest vertex-to-vertex chords. Such vectors have length \(L_n\), and their possible relative angles, modulo sign, are \(\theta+k\eta_n\) for integers \(k\). Therefore
\[
\max_{a,b,c,d}\bigl|\det_2(b-a,d-c)\bigr|
=L_n^2\max_{k\in\mathbb Z}|\sin(\theta+k\eta_n)|
=L_n^2\cos\delta_n(\theta).
\tag{5}
\]
The last equality uses that \(\pi\) is an integral multiple of \(\eta_n\), so the maximum absolute sine is the cosine of the distance from a right angle to the angle lattice. Equations (4)--(5) construct genuine vertex-supported tetrahedra attaining the right-hand side of (1).

**4. The three-on-one-base case never wins.** From the definition of \(\delta_n\), equation (5) is bounded below by \(L_n^2\cos(\eta_n/2)\). If \(n\) is even and at least four, then
\[
L_n^2\cos(\eta_n/2)=4R^2\cos(\pi/n)
\ge2\sqrt2 R^2>\frac{3\sqrt3}{2}R^2.
\tag{6}
\]
If \(n\) is odd, then
\[
L_n^2\cos(\eta_n/2)=4R^2\cos^3(\pi/(2n))
\ge\frac{3\sqrt3}{2}R^2,
\tag{7}
\]
with equality only at \(n=3\). When \(n=3\), the largest triangle in a base is the base itself, and its area equals \(3\sqrt3R^2/4\), so the bound (7) is also exact in the equality situation. Comparing (3), (6), (7) with (4)--(5) proves (1) for every stated parameter. The strict inequality (6) and the strict version of (7) for odd \(n\ge5\) imply that a vertex-supported maximizer cannot have a one-versus-three layer split when \(n\ge4\). In the triangular case a tie occurs precisely when \(\delta_3(\theta)=\eta_3/2=\pi/6\).

**5. Sharp angular envelope.** The distance from a point to the lattice \(\eta_n\mathbb Z\) runs through the entire interval \([0,\eta_n/2]\) as \(\theta\) runs through one period. Cosine is strictly decreasing over this interval. This proves the sharp endpoints, equality conditions, and range in (2). For \(\theta=0\), the distance \(\delta_n(0)\) is zero exactly when \(\pi/2\) is an integral multiple of \(\eta_n\), equivalent to \(4\mid n\); in all other cases it is \(\eta_n/2\). This proves the stated order-dependent reversal.

## Verification

The standalone `verify.py` constructs all \(2n\) vertices, exhaustively enumerates all distinct four-vertex choices for each \(3\le n\le13\), and calculates all determinant volumes directly. It tests five fractions of the angular period and two independent radius/height normalizations for each \(n\), making **110 complete finite enumerations**. Every enumerated maximum agrees numerically with (1), and for \(n\ge4\) no maximizing vertex quadruple has any layer split other than two-versus-two. Six exact-value specializations are additionally checked numerically:
\[
M_3(1,1,0)=\frac{\sqrt3}4,\quad M_3(1,1,\pi/6)=\frac12,
\]
\[
M_4(1,1,0)=\frac23,\quad M_4(1,1,\pi/4)=\frac{\sqrt2}3,
\]
\[
M_6(1,1,0)=\frac{\sqrt3}3,\quad M_6(1,1,\pi/6)=\frac23.
\]
The finite computations are reproducibility checks, **not** a proof of the infinite claim. The unrestricted all-parameter proof is steps 1--5 above.

## Relationship to prior work

Akopyan and Glazyrin proved qualitative structure statements about largest-volume simplices in genuine prisms, including a necessary vertical-translation segment for every vertically maximal simplex (their Theorem 4.3). Their full paper does not give an exact angle-dependent maximal-volume formula for two *relatively rotated* polygonal bases; their prism result is a motivating starting point, not an implication of (1).

The published regular-polygon translative convex-hull profile computes the single-polygon quantity \(d_P(u)w_P(u^\perp)\), and explains the regular difference body. Its formula can recover certain aligned-base benchmarks but does not optimize a determinant **between two independently rotated chord sets**. A published regular-even-polygon rectangle theorem also supplies special aligned-body area benchmarks; it does not cover arbitrary twist, odd polygon orders or the all-tetrahedra extremal claim. The genuinely additional statement here is the **entire sharp twist-angle response**, the all-order parity reversal, and the exact unrestricted tetrahedral envelope in a three-dimensional family.

## Limitations

The two-base polygons must be congruent, concentric in projection, regular, and have equal circumradius. The theorem does not address unequal radii, translated axes, nonregular polygons, or arbitrary top/bottom convex bodies. It does not claim a complete continuous classification of all maximizing tetrahedra; it establishes a vertex-supported maximizing construction and the exclusion of vertex-supported one-versus-three maximizers for \(n\ge4\). Published works may contain differently formulated special-angle instances. No independent mathematical audit has been performed.

## References

1. A. V. Akopyan and A. A. Glazyrin, *On maximum volume simplices in polytopes*, *Periodica Mathematica Hungarica* **69** (2014), 251--256, DOI: 10.1007/s10998-014-0051-2. First publicly verified publication: 26 September 2014. Author-posted full text: https://users.mccme.ru/akopyan/papers/Akopyan-Glazyrin-Maximum-Volume.pdf.
2. *Exact translative convex-hull profile of every regular polygon*, publicly indexed mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-translative-convex-hull-profile-of-every-regular-polygon--79b005afe9c0.
3. *Exact maximum-area rectangles in every regular even polygon*, publicly indexed mathematical finding, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-maximum-area-rectangles-in-every-regular-even-polygon--10bad5e59427.
