# Exact intrinsic vertex-distance law of the regular tetrahedral surface

## Finding

Let \(T\) be the boundary surface of a regular Euclidean tetrahedron of edge length \(1\), with its intrinsic shortest-path metric \(d_T\), and fix any vertex \(v\). If \(X\) is uniformly distributed by surface area on \(T\), the random distance \(R=d_T(v,X)\) has support \([0,2/\sqrt3]\) and cumulative distribution function

\[
F(r)=\Pr\{R\le r\}=\begin{cases}
0,&r<0,\\[2pt]
\dfrac{\pi r^2}{2\sqrt3},&0\le r\le1,\\[6pt]
\sqrt3\left[r^2\left(\dfrac\pi6-\arccos\dfrac1r\right)+\sqrt{r^2-1}\right],&1<r<\dfrac2{\sqrt3},\\[6pt]
1,&r\ge\dfrac2{\sqrt3}.
\end{cases}
\]

In particular its density, apart from the irrelevant endpoints, is

\[
f(r)=\begin{cases}
\dfrac{\pi r}{\sqrt3},&0<r<1,\\[6pt]
2\sqrt3\,r\left(\dfrac\pi6-\arccos\dfrac1r\right),&1<r<2/\sqrt3.
\end{cases}
\]

Every real moment of order \(k>-2\) is given by the convergent elementary integral

\[
\mathbb E[R^k]=\frac{2\sqrt3}{k+2}\int_0^{\pi/6}\sec^{k+2}(u)\,du.
\]

Consequently,

\[
\mathbb E[R]=\frac{2\sqrt3}{9}+\frac{\sqrt3\log3}{6},
\qquad \mathbb E[R^2]=\frac59.
\]

The transition at \(r=1\) is a sharp nonanalyticity:

\[
F(r)-\frac{\pi r^2}{2\sqrt3}
=-\frac{4\sqrt6}{3}(r-1)^{3/2}+O((r-1)^{5/2})
\quad(r\downarrow1).
\]

At the intrinsic radius \(r_*=2/\sqrt3\), the upper tail satisfies

\[
1-F(r)=3(r_*-r)^2+O((r_*-r)^3)\quad(r\uparrow r_*).
\]

Thus the intrinsic ball area follows the flat-cone quadratic law all the way to the distance of the other three vertices, then develops a \(3/2\)-power deficit and a quadratic final tail.

## Assumptions and scope

The tetrahedron is the usual convex three-dimensional Euclidean regular tetrahedron; its surface carries the length metric, not the ambient chord metric, graph distance, or a spherical metric. Its four equilateral faces have area \(\sqrt3/4\) apiece, so the full area is \(\sqrt3\). Uniformity means normalized two-dimensional surface area. Scaling the edge length to any \(a>0\) multiplies all distances and moments of order \(k\) by \(a\) and \(a^k\), respectively. The conclusions are exact for every surface point except that the choice of a shortest path may be nonunique on the cut locus, which has zero area and does not affect the law.

## Proof

**1. A direct shortest-path reduction.** Write the tetrahedral vertices as \(v,b,c,d\). If \(p\) lies on one of the three faces incident with \(v\), the straight segment in that face achieves the ambient Euclidean lower bound, hence
\(d_T(v,p)=|v-p|\).

Suppose \(p\) lies in the opposite face \(\triangle bcd\). Any surface path from \(v\) to \(p\) has a last entry into that face, at a point \(q\) of one of its edges, say \(bc\). The length before \(q\) is at least \(|v-q|\), achievable in face \(vbc\); the length after \(q\) is at least \(|q-p|\), achievable within face \(bcd\). Therefore the global minimum is exactly

\[
d_T(v,p)=\min_{e\in\{bc,cd,db\}}\ \min_{q\in e}
\bigl(|v-q|+|q-p|\bigr).
\]

Develop each incident face across its shared edge into the plane of \(\triangle bcd\). Its opposite vertex becomes the outward apex \(v_e\) of a unit equilateral triangle on edge \(e\). For every edge, the two-segment path has length at least \(|v_e-p|\); equality holds if the joining planar segment intersects \(e\). The three planar outward apexes form another equilateral triangle centered at the centroid \(g\) of \(bcd\). The nearest-apex Voronoi region in \(\triangle bcd\) for apex \(v_{bc}\) is exactly \(\triangle bcg\). On this region, segment \(v_{bc}p\) crosses edge \(bc\) within that edge, so equality is achieved. By symmetry the same is true for the other two regions. Thus \(d_T(v,p)=\min_e|v_e-p|\) everywhere on the opposite face.

**2. Three congruent radial kites.** Pair incident face \(vbc\) with the one-third opposite-face sector \(bcg\) and unfold both into the plane of \(vbc\). Their union is a convex kite with vertices \(v,b,g,c\). The three kites are disjoint up to shared boundaries on the tetrahedral surface, cover it all, and preserve both area and the distance from \(v\) to each point. The preceding shortest-path reduction proves the last statement, rather than merely assuming that a locally straight unfolding minimizes distance.

Put \(v\) at the planar origin; choose its kite's symmetry axis as polar angle \(0\), with \(-\pi/6\le\theta\le\pi/6\). The two near corners \(b,c\) lie at radius \(1\), at angles \(\pm\pi/6\). The far corner \(g\) lies at radius \(2/\sqrt3\) and angle \(0\). The line from \(g\) to \(c\) has polar equation \(r\cos(\pi/6-\theta)=1\) for \(0\le\theta\le\pi/6\), and the other side follows by reflection. Thus every radial slice is precisely

\[
0\le r\le\rho(\theta),\qquad
\rho(\theta)=\sec\bigl(\pi/6-|\theta|\bigr),
\quad |\theta|\le\pi/6.
\]

This gives the maximal intrinsic distance \(2/\sqrt3\) uniquely at the centroid of the opposite face.

**3. Area integration.** Let \(A(r)\) denote the area inside one kite with distance at most \(r\). Its exact polar integral is

\[
A(r)=\frac12\int_{-\pi/6}^{\pi/6}
\min\{r^2,\rho(\theta)^2\}\,d\theta.
\]

For \(0\le r\le1\) no radial boundary is met and \(A(r)=\pi r^2/6\). For \(1<r<2/\sqrt3\), set \(\alpha=\arccos(1/r)\in(0,\pi/6)\). The middle angular sector \(|\theta|<\pi/6-\alpha\) reaches radius \(r\), while the remaining angular intervals terminate at the kite boundary, giving

\[
A(r)=r^2\left(\frac\pi6-\alpha\right)
+\int_0^\alpha\sec^2u\,du
=r^2\left(\frac\pi6-\alpha\right)+\sqrt{r^2-1}.
\]

Each kite has area \(\sqrt3/3\); the total surface has area \(\sqrt3\). Therefore \(F(r)=3A(r)/\sqrt3=\sqrt3 A(r)\), yielding the asserted CDF. Direct differentiation gives the density, whose two branches agree at \(r=1\), and whose upper branch vanishes at \(r=2/\sqrt3\).

**4. Moments and critical behavior.** Polar integration of \(r^k\) over the three kites yields, for every real \(k>-2\),

\[
\mathbb E[R^k]=\frac{3}{\sqrt3(k+2)}
\int_{-\pi/6}^{\pi/6}\rho(\theta)^{k+2}\,d\theta
=\frac{2\sqrt3}{k+2}\int_0^{\pi/6}\sec^{k+2}u\,du.
\]

The standard antiderivatives of \(\sec^3u\) and \(\sec^4u\) evaluate the first and second moments as stated. For the first singularity, put \(\alpha=\arccos(1/r)\). Then
\(\sqrt{r^2-1}=\tan\alpha\), \(r^2=\sec^2\alpha\), and

\[
F(r)-\frac{\pi r^2}{2\sqrt3}
=\sqrt3\bigl(\tan\alpha-\alpha\sec^2\alpha\bigr)
=-\frac{2\sqrt3}{3}\alpha^3+O(\alpha^5).
\]

Since \(\alpha=\sqrt{2(r-1)}+O((r-1)^{3/2})\), the \(3/2\)-power coefficient follows. At the upper endpoint, write \(r=r_*-\delta\). With \(\alpha'(r_*)=3/2\) and
\(f(r)=2\sqrt3\,r(\pi/6-\alpha(r))\), one has
\(f(r)=6\delta+O(\delta^2)\); integrating from \(r\) to \(r_*\) gives the quadratic terminal tail. This completes the proof.

## Verification

An additional facewise exact check of the second moment avoids the polar formula: the three source-incident triangles have mean squared vertex distance \(5/12\) each, while the opposite face has mean squared intrinsic distance \(35/36\). The latter is computed over one triangle bounded by an opposite-face edge and the opposite centroid, using the unfolded source and uniform triangular barycentric second moments. Thus the overall second moment independently equals \(\frac34\cdot\frac5{12}+\frac14\cdot\frac{35}{36}=\frac59\).

The standalone `verify.py` independently samples each of the four equilateral physical faces using barycentric coordinates, obtains the opposite-face intrinsic distance from the nearest of three planar unfolded apex images, and compares empirical CDF values at twelve radii with the closed formula. With 500,000 sampled surface points, the maximum discrepancy in that reproducible run was approximately \(0.000657\). The sample mean was \(0.702459\) against the formula \(0.702042\); the sampled second moment was \(0.556058\) against \(5/9\). Separate numerical quadrature checks the moment integrals. Arbitrary-precision endpoint calculations check the coefficients of both singular asymptotics. All assertions passed. Random samples and numeric quadrature are corroboration; the all-points and all-moments statements are established by the preceding geometric proof.

Run using `python verify.py` with Python, NumPy, SciPy, and mpmath installed. The checker is self-contained apart from these conventional numerical libraries; it does not require unpublished data.

## Relationship to prior work

Miller and Pak (first posted December 12, 2003) establish general polyhedral cut-locus and nonoverlapping source-unfolding machinery. That framework motivates a radial-area calculation, but their relevant theorems do not give the explicit vertex-to-uniform-surface-point tetrahedral CDF or its moments and endpoint powers. Davis, Dods, Traub and Yang (first posted August 12, 2015) classify tetrahedral geodesic trajectories and directions, not the surface-area law of shortest distances. D. M. Davis (first posted June 19, 2023) analyzes minimal geodesics and cut loci on tetrahedra for geodesic motion-planning complexity, but its stated theorems concern that topological invariant rather than the CDF or moment formula. Li and Qiu (published December 8, 2016) provide distance laws within ordinary planar triangles; such formulas alone do not identify which planar unfolding gives the intrinsic shortest path on a closed polyhedral surface. The result here specializes and integrates the tetrahedron's exact distance field into an elementary probability law and extracts both sharp boundary singularities.

## Limitations

The metric is intrinsic, and the random endpoint is uniform on the *surface*, with one endpoint fixed at a tetrahedral vertex. The result does not give the two-independent-surface-points distance distribution, geodesic laws from a generic interior-face source, or a comparable law for an irregular tetrahedron. The closed CDF follows from a relatively small source-unfolding computation; broad geodesic-algorithm literature makes it possible that the same specialized formula appeared in unindexed educational or historical sources. The originality assessment is provisional and not independently audited.

## References

1. Ezra Miller and Igor Pak, *Metric combinatorics of convex polyhedra: cut loci and nonoverlapping unfoldings*, arXiv:math/0312253, first posted 2003-12-12, especially §§II–III, https://arxiv.org/abs/math/0312253.
2. Diana Davis, Victor Dods, Cynthia Traub, Jed Yang, *Geodesic trajectories on regular polyhedra*, arXiv:1508.03546, first posted 2015-08-12, especially §3, https://arxiv.org/abs/1508.03546.
3. Donald M. Davis, *Geodesic complexity of a tetrahedron*, arXiv:2306.11059, first posted 2023-06-19, especially §2, https://arxiv.org/abs/2306.11059.
4. Hongjun Li and Xing Qiu, *Moments of Distance from a Vertex to a Uniformly Distributed Random Point within Arbitrary Triangles*, *Mathematical Problems in Engineering* (2016), DOI:10.1155/2016/8371750, https://doi.org/10.1155/2016/8371750.
