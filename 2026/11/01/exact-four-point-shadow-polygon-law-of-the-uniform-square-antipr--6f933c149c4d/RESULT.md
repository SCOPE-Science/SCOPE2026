# Exact four-point shadow-polygon law of the uniform square antiprism

## Finding

Let \(P\) be the convex uniform square antiprism (two congruent squares joined by eight equilateral triangles). Orthogonally project \(P\) onto a plane with uniformly random unoriented unit normal, and let \(N\) denote the number of vertices of the projected convex polygon. Then, almost surely, \(N\) takes precisely the values \(5,6,7,8\). Put
\[
\beta=\frac{\sqrt2-1}{2^{1/4}},\qquad
\rho=\sqrt{\frac{2}{2+\beta^2}},\qquad
G(t)=\arcsin(\rho\sin t),
\]
where \(G\) takes its principal-branch values. With \(X=G(\pi/8)\), \(Y=G(\pi/4)\), \(Z=G(3\pi/8)\), and \(W=G(\pi/2)\), the complete probability law is
\[
\begin{aligned}
\Pr(N=5)&=\frac8\pi(2Z-Y-W),\\
\Pr(N=6)&=\frac8\pi(W+2Y-2Z-X),\\
\Pr(N=7)&=\frac8\pi(2X-Y),\\
\Pr(N=8)&=1-\frac8\pi X.
\end{aligned}
\]
The respective values are approximately \(0.356758138764322\), \(0.600915394900956\), \(0.011795388796146\), and \(0.030531077538576\). In particular, heptagonal shadows occur with strictly positive probability but are rare.

## Assumptions and scope

Fix circumradius one for each square. The upper vertices are
\[
T_j=(\cos(j\pi/2),\sin(j\pi/2),h),\quad j=0,1,2,3,
\]
and the lower vertices are
\[
B_j=(\cos((j+1/2)\pi/2),\sin((j+1/2)\pi/2),-h),\quad
h=2^{1/4}/2.
\]
These coordinates give equal edge lengths \(\sqrt2\): upper and lower square edges have that length, and the inclined edges satisfy \((1-1/\sqrt2)^2+1/2+(2h)^2=2\). All eight triangles are equilateral. The direction of orthogonal projection is Haar-uniform on the sphere, identifying antipodal normals; directions parallel to facet planes or generating degenerate silhouettes form a set of spherical measure zero. Vertices and sides of a generic convex planar polygon are equinumerous.

## Proof

**1. Facets and visibility.** Write \(A_j\) for the four upper triangular facet normals and \(D_j\) for the four lower triangular facet normals. Outward normals may be chosen as
\[
\begin{array}{llll}
A_0=(1,1,\beta),&A_1=(-1,1,\beta),&A_2=(-1,-1,\beta),&A_3=(1,-1,\beta),\\
D_0=(\sqrt2,0,-\beta),&D_1=(0,\sqrt2,-\beta),&D_2=(-\sqrt2,0,-\beta),&D_3=(0,-\sqrt2,-\beta).
\end{array}
\]
The other two outward facet normals are \(\pm e_3\). The incident faces at the upper vertex \(T_j\) are the upper cap, \(A_{j-1}\), \(A_j\), and \(D_j\), with indices mod four. At the lower vertex \(B_j\) they are the lower cap, \(A_j\), \(D_j\), and \(D_{j+1}\). For a generic viewing direction \(u\), a convex polyhedron vertex projects to a silhouette vertex exactly when the incident outward facet normals have both positive and negative dot products with \(u\). Indeed, the boundary between front and back incident facets passes through such a vertex exactly in the mixed-sign case, and the projected polygon is strictly convex at that vertex away from finitely many exceptional great circles.

**2. All sign intervals.** Because of antipodal identification, fourfold rotation, and vertical mirror symmetry, it suffices to take the direction proportional to \((\cos\phi,\sin\phi,w)\) with \(0<\phi<\pi/4\) and \(w>0\). Put \(c=\cos\phi\), \(s=\sin\phi\), and
\[
a=\frac{c-s}{\beta},\quad b=\frac{\sqrt2s}{\beta},\quad
q=\frac{c+s}{\beta},\quad t=\frac{\sqrt2c}{\beta}.
\]
The only relevant changing signs are \(A_1\cdot u\) at \(w=a\), \(D_1\cdot u\) at \(w=b\), \(A_2\cdot u\) at \(w=q\), and \(D_0\cdot u\) at \(w=t\). The strict inequalities
\[
0<\min(a,b)<\max(a,b)<\min(q,t)<\max(q,t)
\]
hold except at the harmless sector crossover \(\phi=\pi/8\). The vertex incidence list shows that \(T_0\) is absent exactly when \(w<t\), and \(B_2\) is absent exactly when \(w<q\). One additional vertex is absent exactly when \(w\) lies strictly between \(a\) and \(b\): it is \(B_1\) if \(\phi<\pi/8\) and \(T_1\) if \(\phi>\pi/8\). All other vertices are always present. Hence the complete side-count partition is
\[
\begin{array}{c|c}
\text{range of }w&N\\\hline
(0,\min(a,b))&6\\
(\min(a,b),\max(a,b))&5\\
(\max(a,b),\min(q,t))&6\\
(\min(q,t),\max(q,t))&7\\
(\max(q,t),\infty)&8.
\end{array}
\]
This sign analysis is exhaustive because every silhouette change is caused by a facet-normal dot product passing through zero. Each of the four outcomes occupies an open set of viewing directions, so the support of the law is exactly the displayed four-point set.

**3. Spherical integration.** With \(F(v)=v/\sqrt{1+v^2}\), the spherical area element in \((\phi,w)\) coordinates is \(d\phi\,dw/(1+w^2)^{3/2}\). Eight azimuth sectors and antipodal identification give the factor \(4/\pi\) for integrating over \(0\le\phi\le\pi/4\). Consequently
\[
\begin{aligned}
\Pr(N=5)&=\frac4\pi\int_0^{\pi/4}|F(a)-F(b)|\,d\phi,\\
\Pr(N=7)&=\frac4\pi\int_0^{\pi/4}|F(q)-F(t)|\,d\phi,\\
\Pr(N=8)&=\frac4\pi\int_0^{\pi/4}[1-F(\max(q,t))]\,d\phi.
\end{aligned}
\]
Both orderings switch at \(\phi=\pi/8\). Set \(k=\sqrt2/\beta\). Since
\[
F(k\cos v)=\frac{d}{dv}G(v),
\]
all integrals have elementary antiderivatives, giving
\[
\int_0^{\pi/4}|F(a)-F(b)|\,d\phi=4Z-2Y-2W,
\]
\[
\int_0^{\pi/4}|F(q)-F(t)|\,d\phi=4X-2Y,
\qquad
\int_0^{\pi/4}[1-F(\max(q,t))]\,d\phi=\pi/4-2X.
\]
The expressions for the first, third, and fourth probabilities follow; the second follows by subtracting their sum from one.

**4. Independent mean identity.** For any convex polyhedron the probability that one edge belongs to a random silhouette is the exterior dihedral angle divided by \(\pi\). Here eight square–triangle edges have angle \(\theta_1=\arccos(\beta/\sqrt{2+\beta^2})\), and eight triangle–triangle edges have angle \(\theta_2=\arccos((\sqrt2-\beta^2)/(2+\beta^2))\). Hence
\[
\mathbb E N=\frac8\pi(\theta_1+\theta_2)=5.716099405108975\ldots,
\]
which agrees independently with the four-point law.

## Verification

Running `python3 verify.py` prints the four probabilities; verifies their normalization and numerical spherical quadrature; independently constructs all ten supporting facets from the eight vertices; and tests 20,000 deterministic sphere directions. At each direction, the predicted regime, the incident-facet sign count, and the vertex count of a separately computed planar convex hull agree. The mean also agrees with a direct sum of all sixteen exterior dihedral angles. These finite tests are diagnostic; the proof of the full probability law is the exhaustive facet-sign partition followed by exact spherical integration.

## Relationship to prior work

Glisse and Lazard's 2007 analysis of silhouettes develops general asymptotic bounds and gives the classical edge-probability/exterior-dihedral-angle identity. That identity implies the mean above, but not the joint event probabilities needed for the distribution. Glisse, Lazard, Michel, and Pouget (2016) study silhouette complexity for Poisson random polytopes, rather than the orientation law of this fixed square antiprism. The present result is specifically the full four-outcome exact Haar law for one canonical Archimedean solid. Related results on shadows of different polytopes do not determine these antiprism probabilities merely from combinatorial equivalence: the metric facet-normal angles matter.

## Limitations

The law assumes a *uniform* square antiprism: arbitrary height changes the normal angles and therefore the probabilities. Exceptional viewing directions, with measure zero, are excluded from the almost-sure support statement. The article establishes no priority claim beyond the explicitly compared literature; an equivalent computation in older silhouette tables or geometric-visualization literature cannot be ruled out without further independent historical review. No independent audit has been performed.

## References

1. Marc Glisse and Sylvain Lazard, *An Upper Bound on the Average Size of Silhouettes*, arXiv:cs/0702087 (public preprint posted 2007-02-14), https://arxiv.org/abs/cs/0702087.
2. Marc Glisse, Sylvain Lazard, Julien Michel, and Marc Pouget, *Silhouette of a Random Polytope*, *Journal of Computational Geometry* 7 (2016), 86–99, DOI:10.20382/jocg.v7i1a5, https://jocg.org/index.php/jocg/article/view/3009.
3. Lutz Kettner and Emo Welzl, *Contour Edge Analysis for Polyhedron Projections*, *Geometric Modeling* (1997), 379–394; a public institutional bibliographic record and restricted PDF endpoint were found, but the full text was not inspected.
