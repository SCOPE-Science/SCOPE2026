# Exact two-disk covering radius of every regular odd polygon
## Finding
Let \(P_n\subset\mathbb R^2\) be a regular convex \(n\)-gon with odd \(n\ge3\) and circumradius \(R>0\). Two congruent closed Euclidean disks are allowed arbitrary centers, and their union must contain **every point** of the polygon. Write
\[
\rho_2(P_n)=\inf\big\{r\ge0: P_n\subseteq \overline B(c_1,r)\cup\overline B(c_2,r),\; c_1,c_2\in\mathbb R^2\big\}.
\]
Then
\[
\boxed{\rho_2(P_n)=R\cos\left(\frac{\pi}{2n}\right)}.
\tag{1}
\]

A concrete optimal pair is obtained by orienting the polygon so that one vertex is \((R,0)\), putting
\[
t=\frac{\pi}{2n},\qquad r=R\cos t,\qquad c_\pm=(\pm R\sin t,0),
\tag{2}
\]
and taking disks \(\overline B(c_\pm,r)\).

There is rigidity in the lower-bound mechanism: in **every** optimal pair, at least one disk contains at least \((n+1)/2\) vertices. Any optimal disk containing that many vertices has center equal to the midpoint of the two endpoints of a run of exactly \((n+1)/2\) cyclically consecutive polygon vertices. Thus such a center belongs to a forced \(n\)-point orbit on the circle of radius \(R\sin t\) around the circumcenter. We do not claim that this condition alone classifies the other disk of every optimal pair.

The discrete vertex two-center value therefore equals the full-body two-center value for all odd regular polygons. The distinction matters: finite vertex coverage alone does not generally imply coverage of every polygonal edge or interior point.

## Assumptions and scope
The disks are closed, equal in radius, and unconstrained in position. The target is the compact convex polygon including its boundary. The theorem covers exactly odd integers \(n\ge3\); it concerns neither unequal disks nor arbitrary nonregular polygons. Normalizing \(R=1\) loses no information because covering radii scale linearly.

## Proof
Normalize \(R=1\), and set \(t=\pi/(2n)\).

**1. How many circumcircle vertices fit in one small disk?** For a Euclidean disk of radius \(0\le r<1\), with center at distance \(d>0\) from the origin, a point \((\cos\theta,\sin\theta)\) of the unit circle belongs to the disk exactly when
\[
\cos(\theta-\theta_c)\ge \frac{1+d^2-r^2}{2d}
\ge\sqrt{1-r^2}.
\tag{3}
\]
The final inequality is the arithmetic–geometric mean inequality applied to \(d+(1-r^2)/d\). If the center is the origin, a disk of radius \(r<1\) meets the circumcircle nowhere. Equation (3) implies that the covered portion of the circumcircle is either empty or one angular arc of length at most \(2\arcsin r\).

A circular arc containing \(m\) of the \(n\) equally spaced vertices has angular length at least \(2\pi(m-1)/n\) for \(1\le m\le n-1\); this follows by counting the \(m-1\) successive angular gaps between those selected vertices. For \(m=(n+1)/2\), the required arc length is
\[
\frac{n-1}{n}\pi=\pi-2t.
\tag{4}
\]
If \(r<\cos t\), then \(2\arcsin r<\pi-2t\), so each disk can contain at most \((n-1)/2\) polygon vertices. Two such disks cover at most \(n-1\) of the \(n\) vertices, a contradiction. This proves the lower bound
\[
\rho_2(P_n)\ge\cos t.
\tag{5}
\]

**2. Explicit upper bound for the whole polygon.** Orient the vertices at angles \(2\pi k/n\), \(0\le k<n\), and define the centers (2) with \(R=1\). As \(n\) is odd, there is no vertex on the vertical axis. Indeed each vertex \(v=(x,y)\) has \(|x|\ge\sin t\). If \(x\ge0\), then
\[
\|v-c_+\|^2=1+\sin^2t-2x\sin t
\le1-\sin^2t=\cos^2t.
\tag{6}
\]
The analogous inequality holds for \(x<0\) with \(c_-\).

The vertical line \(x=0\) cuts the upper and lower boundary of \(P_n\) at
\[
q_\pm=\left(0,\pm\frac{\cos(2t)}{\cos t}\right).
\tag{7}
\]
To see this, the upper polygon edge crossing the line has outward normal making angle \(t\) with the vertical axis, and its support distance is the polygonal inradius \(\cos(2t)\). The exact cut points obey
\[
\cos^2t-\|q_\pm-c_\pm\|^2
=\cos(2t)\tan^2t>0.
\tag{8}
\]
In fact both cut points lie in both disks, since changing the sign of the center does not change the squared distance to points with zero horizontal coordinate.

Every vertex of the convex polygon \(P_n\cap\{x\ge0\}\) is either an original vertex with nonnegative horizontal coordinate or one of \(q_\pm\). Equations (6) and (8) place all its vertices in \(\overline B(c_+,\cos t)\). Convexity of a disk then places the **entire** right half-polygon in that disk. The left half-polygon is similarly contained in \(\overline B(c_-,\cos t)\). These halves cover \(P_n\), proving the upper bound and (1).

**3. Forced majority-disk centers.** For any optimal cover, pigeonhole ensures at least one disk contains at least \((n+1)/2\) original vertices. By (3)–(4), its covered circumcircle arc has length at most \(\pi-2t\), so its \((n+1)/2\) contained vertices are exactly a cyclically consecutive run, with endpoint angular separation \(\pi-2t\). Their Euclidean chord length is
\[
2\sin\left(\frac{\pi-2t}{2}\right)=2\cos t=2r.
\tag{9}
\]
A radius-\(r\) disk containing two points exactly \(2r\) apart is necessarily centered at their midpoint. That midpoint lies at distance \(\sin t\) from the origin. There are exactly \(n\) possible consecutive runs of the required length, and their midpoints are distinct and dihedrally permuted. This proves the rigidity statement. Restoring arbitrary \(R\) completes the proof.

## Verification
The standalone `verify.py` checks the algebra of the chord length, axis-cut intersection and disk-distance identity using exact symbolic trigonometry. It then explicitly constructs every odd regular polygon for \(3\le n\le201\), checks all vertices and cutpoints against the proposed disks, and samples interiors of polygonal boundary edges independently. These finite checks are regressions; they do not replace the all-order analytic proof above.

The lower bound depends only on a circumcircle-arc argument and a counting pigeonhole principle; no hypothesis about splitting a polygon into connected chains is needed. The upper bound explicitly verifies the cutpoints, which is essential because vertex-only disk covering would otherwise be insufficient for the continuous two-center problem.

## Relationship to prior work
I. Vigan's geodesic polygon-covering paper gives a general exact algorithm for two geodesic disks, and in convex polygons a contained segment is geodesically shortest; hence his setting includes Euclidean covering as a special case. Choi, Jeong, and Ahn later develop a faster algorithm directly for Euclidean congruent two-disk covering of arbitrary convex polygons. These algorithmic results solve the input-optimization problem but do not state the odd-regular closed form or the forced-majority-center geometry.

Published work on regular **even** polygons gives a different closed form and a complete optimizer classification, relying on their central symmetry. Its hypothesis excludes the odd family, and the numerical expression does not imply (1). The present proof instead uses the odd cardinality and the fact that two disks cannot each capture fewer than half the vertices.

Birgin, Gardenghi, and Laurain investigate bounds and shape-optimization algorithms for covering domains with multiple equal disks, including numerical experiments on regular polygons. The accessible author full text covers asymptotics for the number of disks tending to infinity and illustrative regular-polygon experiments for substantially more disks; it gives no exact two-disk odd-family formula in the materially inspected sections.

A complete equivalence and dominance check also considered vertex two-center problems, shortest enclosing two-disk covers, radius-diameter covering aliases, and regular pentagon/heptagon specializations. No statement implying (1) was located. Absence in these searches is not a proof of universal historical novelty.

## Limitations
The theorem does not classify *every* optimal pair of centers: it determines the exact optimal radius, exhibits explicit optimal pairs, and forces the center of any disk containing a majority of vertices. The other center of an arbitrary optimal pair need not be unique under this argument.

The work does not address even polygons, arbitrary convex polygons, unequal radii, or the case of more than two disks. An equivalent elementary special-case fact may exist in unindexed geometry literature; that is the main remaining originality risk.

## References
1. I. Vigan, *Packing and Covering a Polygon with Geodesic Disks*, arXiv:1311.6033v1 (23 November 2013).
2. J. Choi, D. Jeong, H.-K. Ahn, *Covering Convex Polygons by Two Congruent Disks*, arXiv:2105.02483v1 (6 May 2021).
3. E. G. Birgin, J. L. Gardenghi, A. Laurain, *Bounds on the Optimal Radius When Covering a Set with Minimum Radius Identical Disks*, Mathematics of Operations Research (2023 online), DOI:10.1287/moor.2022.0104; author preprint titled *Asymptotic bounds on the optimal radius when covering a set with minimum radius identical balls*, 18 April 2022.
4. H. Kaplan, M. Katz, N. Morgenstern, M. Sharir, *Optimal Cover of Points by Disks in a Simple Polygon*, SIAM Journal on Computing, DOI:10.1137/100808459 (2011).
