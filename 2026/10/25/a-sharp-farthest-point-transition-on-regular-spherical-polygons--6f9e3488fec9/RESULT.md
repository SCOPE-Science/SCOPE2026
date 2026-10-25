# A sharp farthest-point transition on regular spherical polygons

## Finding

Let \(n\ge3\) and \(0<\rho<\pi/2\). For the geodesically convex regular \(n\)-gon on the unit sphere with its vertices at colatitude \(\rho\), the complete farthest-point set from one specified vertex is determined as follows. If \(n\) is even, the unique farthest point is the opposite vertex, at spherical distance \(2\rho\). If \(n\) is odd, set
\[
a=\pi/n,\qquad m=\cos^2\rho-\sin^2\rho\cos a,\qquad c=\sqrt{1-\sin^2\rho\sin^2 a},\qquad \rho_*=\arctan\!\bigl(1/\sqrt{\cos a}\bigr).
\]
Writing \(E_{n,\rho}\) for the maximum spherical distance from the chosen vertex to the closed polygon, the exact answer is
\[
E_{n,\rho}=\begin{cases}
\arccos(m),&0<\rho\le\rho_*,\\
\arccos(m/c),&\rho_*\le\rho<\pi/2.
\end{cases}
\]
For \(\rho<\rho_*\), precisely the two vertices adjacent to the opposite edge maximize the distance. For \(\rho=\rho_*\), **every point of that entire geodesic edge**, and no other point, maximizes the distance \(\pi/2\). For \(\rho>\rho_*\), the **unique** maximizer is the geodesic midpoint of that edge. The two branches agree at the threshold.

## Assumptions and scope

The ambient metric is the standard unit-sphere geodesic distance \(d(p,q)=\arccos(p\cdot q)\) with values in \([0,\pi]\), not intrinsic distance on a flat-faced polyhedral surface. Let
\[
v_j=(\sin\rho\cos(2\pi j/n),\ \sin\rho\sin(2\pi j/n),\ \cos\rho),\qquad 0\le j<n.
\]
The domain \(K_{n,\rho}\) is the closed, shorter-geodesic convex hull of the \(v_j\); its edges are the shorter great-circle arcs joining consecutive vertices. Set \(E_{n,\rho}=\max_{x\in K_{n,\rho}}d(v_0,x)\). The northern open-hemisphere hypothesis \(\rho<\pi/2\) guarantees uniqueness of the geodesic convex hull and excludes antipodal ambiguities. All equalities below concern the full **continuum** \(K_{n,\rho}\), not merely its vertex set.

## Proof

**Boundary reduction.** Every point of \(K_{n,\rho}\) has a representation \(x=z/\|z\|_2\) for a nonzero convex combination \(z=\sum_j\lambda_jv_j\) with nonnegative \(\lambda_j\) summing to one. Its third coordinate satisfies \(x_3=\cos\rho/\|z\|_2\ge\cos\rho>0\). Hence the entire polygon lies in the northern hemisphere. Minimizing \(v_0\cdot x\) is equivalent to maximizing \(d(v_0,x)\). The only critical points of the linear function \(x\mapsto v_0\cdot x\) on the smooth sphere are \(\pm v_0\). The first is a global maximum, and the second lies outside \(K_{n,\rho}\). Thus the minimum over the compact polygon occurs on its geodesic boundary. (For any possible interior constant derivative, the same critical-point condition applies.)

**Even case.** A point \(x\in K_{n,\rho}\) has spherical colatitude \(r\le\rho\) by the coordinate bound above. Its longitude difference \(\theta\) from \(v_0\) obeys
\[
v_0\cdot x=\cos\rho\cos r+\sin\rho\sin r\cos\theta\ge\cos(\rho+r)\ge\cos(2\rho).
\]
Since \(\rho+r<\pi\), the last inequality follows from decreasing cosine. Equality holds precisely when \(r=\rho\) and \(\theta=\pi\), a point present exactly as \(v_{n/2}\) when \(n\) is even. Its distance is \(2\rho\).

**Odd case.** The smallest vertex dot product with \(v_0\) is
\[
\min_j (v_0\cdot v_j)=\cos^2\rho-\sin^2\rho\cos(\pi/n)=m.
\]
The minimum occurs exactly at \(v_{(n-1)/2}\) and \(v_{(n+1)/2}\), the endpoints of the opposite edge. Any boundary point of an edge from consecutive vertices \(u,w\) is uniquely expressible as
\[
x=\frac{z}{L},\qquad z=\lambda u+(1-\lambda)w,\qquad L=\|z\|_2,\qquad 0\le\lambda\le1.
\]
The common consecutive-vertex dot product is \(u\cdot w=1-2\sin^2\rho\sin^2(\pi/n)\). Therefore
\[
L^2=1-4\lambda(1-\lambda)\sin^2\rho\sin^2(\pi/n),\qquad c\le L\le1,
\]
with \(L=c\) only at \(\lambda=1/2\). Moreover \(t=v_0\cdot z=\lambda(v_0\cdot u)+(1-\lambda)(v_0\cdot w)\ge m\); equality \(t=m\) can hold only along the opposite edge.

If \(m>0\), then \(v_0\cdot x=t/L\ge t\ge m\). Equality requires \(L=1\), hence \(\lambda=0\) or \(1\), and \(t=m\); only the two opposite vertices qualify. If \(m=0\), \(t/L\ge0\), and equality is attained precisely where \(t=0\), meaning the entire opposite edge. If \(m<0\), then \(t/L\ge m/L\ge m/c\) because \(L\ge c\) and \(m<0\). Equality forces simultaneously \(t=m\) and \(L=c\), which characterizes the unique normalized midpoint of the opposite edge,
\[
x_* =\frac{v_{(n-1)/2}+v_{(n+1)/2}}{\|v_{(n-1)/2}+v_{(n+1)/2}\|_2}.
\]
Finally \(m=0\iff\tan^2\rho=1/\cos(\pi/n)\), yielding the stated sharp threshold \(\rho_*\). Since \(\arccos\) is decreasing, the equality loci above and lower bounds for dot products give every stated maximum distance. \(\square\)

## Verification

The analytic proof covers every integer \(n\ge3\) and every real \(\rho\in(0,\pi/2)\), with no finite-enumeration dependence. The included `spherical_vertex_check.py` independently samples 1,001 normalized chord interpolation points on every boundary edge for 32 test pairs (\(n\in\{3,4,5,6,7,8,9,11\}\) and \(\rho\in\{0.18,0.70,1.05,1.35\}\)) and compares the predicted extremal distance to within \(2\times10^{-6}\) radians. It is a numerical sanity check, **not** proof of the continuum assertion. The sharp equality classification follows from strict equality conditions for the two edge bounds.

## Relationship to prior work

Zachos, *An analytical solution of the weighted Fermat–Torricelli problem on the unit sphere* (arXiv:1408.6495v1, first public 27 August 2014), examines minimization of weighted sums of spherical vertex-distances, principally in spherical triangles. Its objective differs: it does not present this maximum-of-one-distance, all-\(n\), varying-colatitude classification. The computational-geometry account of spherical polygon boundaries in O'Rourke, *Computational Geometry Column 51*, supplies context for the distinction between spherical and Euclidean convex polygons. Existing Euclidean farthest-point profiles for regular polygons do not imply the spherical midpoint transition: their metric and convex arcs differ. Available indexed comparisons did not identify an equivalent sharp threshold; this does not certify uniqueness in unindexed literature.

## Limitations

The theorem assumes a regular geodesically convex polygon with all vertices at a common northern colatitude strictly less than \(\pi/2\). It does not classify arbitrary spherical polygons, nonhemispherical or degenerate great-circle polygons, other base points, global two-point diameter, or farthest-point maps on polyhedral surfaces. Publication novelty may be affected by undetected specialized spherical-geometry literature. Independent mathematical validation is not performed.

## References

1. A. N. Zachos, *An analytical solution of the weighted Fermat-Torricelli problem on the unit sphere*, arXiv:1408.6495v1 (public 27 August 2014), https://arxiv.org/abs/1408.6495.
2. J. O'Rourke, *Computational Geometry Column 51*, available at https://www.science.smith.edu/~jorourke/Papers/51.pdf (spherical polygon geometry background; no precise first-public date used here).
3. E. W. Weisstein, *Spherical Distance*, MathWorld, https://mathworld.wolfram.com/SphericalDistance.html (metric normalization).
