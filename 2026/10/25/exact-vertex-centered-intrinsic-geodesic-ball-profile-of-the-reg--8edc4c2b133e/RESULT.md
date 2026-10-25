# Exact vertex-centered intrinsic geodesic ball profile of the regular tetrahedron

## Finding
Let \(T\) be the boundary of a Euclidean regular tetrahedron of edge length \(1\), endowed with its intrinsic shortest-path metric \(d_T\). Fix any vertex \(v\), and let \(X\) be distributed uniformly in surface area. The exact cumulative distribution function of \(R=d_T(v,X)\) is
\[
F(r)=\begin{cases}
0,&r<0,\\
\pi r^2/(2\sqrt3),&0\le r\le1,\\
\sqrt3\left[r^2\left(\pi/6-\arccos(1/r)\right)+\sqrt{r^2-1}\right],&1<r<2/\sqrt3,\\
1,&r\ge2/\sqrt3.
\end{cases}
\]
Consequently the area of the geodesic disk \(B_T(v,r)\) equals \(\sqrt3 F(r)\). The intrinsic eccentricity of \(v\) is \(2/\sqrt3\), attained at exactly one point: the centroid of the opposite face. The length of the intrinsic distance level set, for all regular radii, equals
\[
L(r)=\begin{cases}
\pi r,&0<r<1,\\
r\left(\pi-6\arccos(1/r)\right),&1<r<2/\sqrt3,\\
0,&r>2/\sqrt3.
\end{cases}
\]
The disk-area function is \(C^1\) across \(r=1\) but its second right derivative tends to \(-\infty\); in particular its profile has a genuine fractional-power boundary transition, even though the first derivative is continuous.

## Assumptions and scope
All lengths are intrinsic shortest-path lengths measured *along the tetrahedral surface*, not Euclidean ambient chords, and probabilities are normalized by its total area \(\sqrt3\). Boundary and cut-locus sets have area zero, so the distinction between open and closed disks does not affect \(F\). For tetrahedra of arbitrary edge length \(\ell>0\), substitute \(r/\ell\) for \(r\) in the unit-edge probability formula.

## Proof
**1. Reduction to four flat regions.** Label the vertices \(v,B,C,D\), where \(BCD\) is the face opposite \(v\), and put \(h=\sqrt3/2\). On each of the three faces incident with \(v\), straight Euclidean segments from \(v\) stay in that triangular face. Because any surface curve has length at least the ambient Euclidean endpoint distance, the intrinsic distance on these faces is exactly the within-face Euclidean distance.

Develop the opposite face into the plane with \(B=(0,0)\), \(C=(1,0)\), and \(D=(1/2,h)\). Reflect the remaining vertex across each side of this triangle. Its three developed images are
\[
Z_0=(1/2,-h),\qquad Z_1=(3/2,h),\qquad Z_2=(-1/2,h).
\]
For \(P\in BCD\), any path from \(v\) to \(P\) has a *last entry* into \(BCD\) across one of its sides. If that entry occurs at \(Q\) on side \(e\), the preceding part of the path has length at least \(|v-Q|\), which is attained inside the face adjacent to \(e\) and containing \(v\). The remaining segment inside \(BCD\) is at least \(|Q-P|\). Minimizing over crossing points \(Q\in e\) and over the three sides yields
\[
d_T(v,P)=\min\{|P-Z_0|,|P-Z_1|,|P-Z_2|\}.
\]
Indeed, for each side the straight segment joining its reflected image to \(P\) meets that side within its segment, so the planar straight-line lower bound is realizable as a two-face path. Any path with repeated face crossings is included in the lower bound and cannot beat it.

**2. Voronoi division of the opposite face.** The three planar nearest-image regions are the triangles \(BCG\), \(CDG\), \(DBG\), where \(G=(1/2,h/3)\) is the centroid. Each has area \(\sqrt3/12\). On \(BCG\), distance is \(|P-Z_0|\). Its unique farthest point from \(Z_0\) is \(G\), whose distance is \(4h/3=2/\sqrt3\); all three incident faces have maximal distance \(1\). This proves the exact eccentricity and uniqueness statement.

**3. Polar integration.** Define \(I(r)\) as the area within distance \(r\) on one incident face, and \(J(r)\) as the corresponding area in \(BCG\). Use a polar angle \(\phi\in[-\pi/6,\pi/6]\) around \(v\) (for \(I\)) and \(Z_0\) (for \(J\)), measured from the symmetry axis. An incident face fills radii from \(0\) to \(h/\cos\phi\). Therefore
\[
I(r)=\begin{cases}
\pi r^2/6,&0\le r\le h,\\
h\sqrt{r^2-h^2}+r^2\bigl(\pi/6-\arccos(h/r)\bigr),&h<r<1,\\
\sqrt3/4,&r\ge1.
\end{cases}
\]
The opposite-face Voronoi triangle fills the polar annulus from radius \(h/\cos\phi\) to radius \(1/\cos(\pi/6-|\phi|)\). Thus
\[
J(r)=\int_0^{\pi/6}\Bigl[\min\!\left\{r^2,\sec^2(\pi/6-\phi)\right\}-h^2\sec^2\phi\Bigr]_+\,d\phi,
\]
where the positive part ensures the inner boundary has been reached. Evaluating at the break angles \(\arccos(h/r)\) for \(h<r\le1\) and \(\pi/6-\arccos(1/r)\) for \(1<r<2/\sqrt3\), we obtain
\[
J(r)=\begin{cases}
0,&0\le r\le h,\\
r^2\arccos(h/r)-h\sqrt{r^2-h^2},&h<r\le1,\\
r^2\bigl(\pi/6-\arccos(1/r)\bigr)+\sqrt{r^2-1}-\sqrt3/4,&1<r<2/\sqrt3,\\
\sqrt3/12,&r\ge2/\sqrt3.
\end{cases}
\]
The full geodesic disk is the area-disjoint union of three incident-face pieces and three congruent opposite-face Voronoi pieces, so \(\operatorname{area}B_T(v,r)=3(I(r)+J(r))\). On \(h<r\le1\), the radical and inverse-cosine terms cancel *exactly*, yielding \(\pi r^2/2\) throughout \(0\le r\le1\). For \(1<r<2/\sqrt3\), substitution gives
\[
\operatorname{area}B_T(v,r)=3\left[r^2\bigl(\pi/6-\arccos(1/r)\bigr)+\sqrt{r^2-1}\right].
\]
Divide by total area \(4(\sqrt3/4)=\sqrt3\) to obtain \(F\).

**4. Perimeter and transition.** Differentiate the area expression for \(1<r<2/\sqrt3\). The derivative of the inverse-cosine term cancels the derivative of \(\sqrt{r^2-1}\), giving \(L(r)=r(\pi-6\arccos(1/r))\). This agrees at \(r=1\) with the left derivative \(\pi r\), and vanishes at \(2/\sqrt3\). But as \(r\downarrow1\) from above,
\[
\operatorname{area}B_T(v,r)-\pi r^2/2=-4\sqrt2\,(r-1)^{3/2}+O((r-1)^{5/2}),
\]
so the second derivative does not extend continuously to that radius. The exact full support and endpoint value follow also from the Voronoi decomposition.

## Verification
The accompanying executable `check_profile.py` numerically and independently integrates the two polar-face regions at eleven named test radii, including both nonanalytic boundary radii, and checks the stated closed formula against that direct integral at absolute tolerance \(10^{-9}\). It checks the total surface area, monotonicity on a finite grid, and one-sided derivative agreement at the transition. These finite numerical tests are consistency checks: the all-radius statement is established by the preceding exact planar-geometry and integral evaluations, not by enumeration.

## Relationship to prior work
Davis–Dods–Traub–Yang, *Geodesic trajectories on regular polyhedra* (2015), classifies geodesics from a tetrahedral vertex to a point (including non-minimizing geodesic trajectories), but does not tabulate the vertex-centered geodesic-ball area or random-distance distribution. Fontenot and collaborators (2022), *Landscapes of the Tetrahedron and Cube*, furnish pointwise shortest-path formulas via polyhedral developments; these permit computing distances but are not the closed radial distribution derived here. Donald M. Davis (2023) describes the regular tetrahedron's geodesic cut locus, consistent with the Voronoi-centroid farthest-point description. Freitas–Krejčiřík (2014) relates areas, diameters and cut loci of convex surfaces; it does not evaluate the explicit vertex-centered tetrahedral disk-area profile. An equivalent formula in a different literature may remain unindexed.

## Limitations
The claim is exclusively about vertex-centered balls on regular tetrahedra, not balls centered at arbitrary points, nor the distribution of distances between two independent random surface points, nor geodesics of all types. No general polyhedral-surface classification is asserted. Originality is assessed against specifically inspected primary literature and relevant searchable records; it is not a proof of global bibliographic uniqueness.

## References
- P. Freitas and D. Krejčiřík, *Alexandrov's isodiametric conjecture and the cut locus of a surface*, arXiv:1406.0811 (initial public version 2014-06-03), https://arxiv.org/html/1406.0811v1.
- D. Davis, V. Dods, C. Traub, and J. Yang, *Geodesic trajectories on regular polyhedra*, arXiv:1508.03546 (initial public version 2015-08-12), https://arxiv.org/abs/1508.03546.
- K. Fontenot et al., *Landscapes of the Tetrahedron and Cube: An Exploration of Shortest Paths on Polyhedra*, arXiv:2201.04253 (2022-01-12), https://arxiv.org/abs/2201.04253.
- D. M. Davis, *Geodesic complexity of a tetrahedron*, arXiv:2306.11059 (2023-06-19), https://arxiv.org/abs/2306.11059.
