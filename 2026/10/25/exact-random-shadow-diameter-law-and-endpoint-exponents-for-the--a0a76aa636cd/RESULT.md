# Exact random-shadow diameter law and endpoint exponents for the regular tetrahedron

## Finding
Let \(T\subset\mathbb R^3\) be any regular tetrahedron of edge length \(\ell>0\), and let \(U\) be uniformly distributed over the unit sphere. The random variable
\[
D=\operatorname{diam}(\Pi_{U^\perp}T)
\]
measures the Euclidean diameter of its planar orthogonal shadow, not the directional caliper width of the three-dimensional tetrahedron.

Its support is exactly \([3\ell/\sqrt{10},\ell]\). Write \(t=d/\ell\), \(r=\sqrt{2(1-t^2)}\), and \(z_*(r)=\sqrt{(1-2r^2)/3}-r\). The complete distribution is
\[
\Pr(D\le d)=\begin{cases}
0,&d\le 3\ell/\sqrt{10},\\
\displaystyle\frac{12}{\pi}\int_0^{z_*(r)}\left[\arccos\frac{r}{\sqrt{2(1-z^2)}}-\frac\pi4-\arcsin\frac{z+r}{\sqrt{1-z^2}}\right]dz,&3\ell/\sqrt{10}<d<\ell,\\
1,&d\ge\ell.
\end{cases}
\]
This elementary one-dimensional quadrature is exact for every admissible diameter threshold; no elementary antiderivative is asserted. The law has no atoms and has strictly increasing CDF in its open support. The minimum is achieved exactly for the viewing normals which, in the standard tetrahedron coordinates defined below, are signed permutations of \((2,1,0)/\sqrt5\) (24 oriented normals or 12 unoriented planes). The maximum is achieved precisely when at least two normal coordinates have equal absolute value.

There are distinct sharp endpoint orders:
\[
\lim_{\varepsilon\downarrow0}\frac{\Pr\{D>\ell(1-\varepsilon)\}}{\varepsilon^{1/2}}=6\sqrt2,
\qquad
\lim_{\delta\downarrow0}\frac{\Pr\{D\le\ell(3/\sqrt{10}+\delta)\}}{\delta^2}=\frac{150\sqrt5}{\pi}.
\]

## Assumptions and scope
The tetrahedron is a three-dimensional, nondegenerate regular tetrahedron of arbitrary positive edge length. Plane normals are distributed according to normalized surface area on \(S^2\); antipodal normals define the same plane. The projected diameter is the maximum planar distance between any two points of the entire projected convex body. Its convexity ensures a pair of projected original vertices attains this maximum.

## Proof
**Six-edge reduction.** By rigid motion, scale so \(\ell=1\) and take vertices
\[
(1,1,1)/(2\sqrt2),\quad(1,-1,-1)/(2\sqrt2),\quad(-1,1,-1)/(2\sqrt2),\quad(-1,-1,1)/(2\sqrt2).
\]
Every pair of vertices is an edge. Their six unoriented unit difference vectors are the normalized signed two-coordinate vectors \((0,1,\pm1)/\sqrt2\) and cyclic permutations. For every unit plane normal \(U=(u_1,u_2,u_3)\), orthogonal projection changes an edge of unit length, parallel to \(e\), into length \(\sqrt{1-(U\cdot e)^2}\). Hence
\[
D/\ell=\sqrt{1-\tfrac12\min_{i<j}\min\{|u_i-u_j|^2,|u_i+u_j|^2\}}
=\sqrt{1-\tfrac12\,\min_{i<j}(|u_i|-|u_j|)^2}.
\]
If \(x\ge y\ge z\ge0\) are the decreasing rearrangement of the three absolute normal coordinates, this becomes
\[
D/\ell=\sqrt{1-\tfrac12\min\{(x-y)^2,(y-z)^2\}}.
\]
**Exact support and equality.** Put \(m=\min(x-y,y-z)\). The inequalities \(x\ge z+2m\), \(y\ge z+m\) give
\[
1=x^2+y^2+z^2\ge(z+2m)^2+(z+m)^2+z^2\ge5m^2.
\]
Thus \(0\le m\le1/\sqrt5\). Equality at the upper end holds only for \((x,y,z)=(2,1,0)/\sqrt5\). Equality at the lower end holds exactly when two absolute coordinates coincide. Continuity on the connected sphere gives all intermediate values.

**Spherical chamber measure.** A generic unit vector belongs to one of 48 congruent signed-permutation chambers. In one chamber set \(x=\sqrt{1-z^2}\cos\phi\), \(y=\sqrt{1-z^2}\sin\phi\), \(z\ge0\), with \(0\le\phi\le\pi/4\) and \(0\le z\le1/\sqrt3\). The sphere surface element is exactly \(d\phi\,dz\), so the normalized whole-sphere measure of a measurable region in this chamber is \(12/\pi\) times its planar \((z,\phi)\)-area.

For a threshold \(t\in(3/\sqrt{10},1)\), let \(r=\sqrt{2(1-t^2)}\in(0,1/\sqrt5)\). The event \(D/\ell\le t\) is \(x-y\ge r\) and \(y-z\ge r\). The first inequality is \(\phi\le \arccos(r/\sqrt{2(1-z^2)})-\pi/4\); the second is \(\phi\ge\arcsin((z+r)/\sqrt{1-z^2})\). Both can hold exactly for \(0\le z\le z_*(r)\). Indeed the necessary condition from \(x\ge z+2r\), \(y\ge z+r\) is \(3z^2+6rz+5r^2\le1\), and for such \(z\) the angular interval is nonempty. Integrating its length and multiplying by \(12/\pi\) proves the CDF. The boundary level sets have zero spherical area; every interior threshold admits an open interval of positive area, proving continuity, absence of atoms, and strict increase.

**Full-diameter endpoint.** At \(m=0\), one of the six distinct great circles \(u_i=u_j\) or \(u_i=-u_j\) is met. Each band \(|u_i\pm u_j|\le r\) has spherical probability \(r/\sqrt2\) for \(0<r<\sqrt2\), because the dot product with a fixed unit vector is uniform on \([-1,1]\). Different great-circle bands overlap in probability \(O(r^2)\). Inclusion-exclusion therefore gives \(\Pr(m\le r)=3\sqrt2\,r+O(r^2)\). Substituting \(r=\sqrt{2(1-(1-\varepsilon)^2)}=2\varepsilon^{1/2}+O(\varepsilon^{3/2})\) proves the first sharp limit.

**Minimum-diameter endpoint.** Let \(r_0=1/\sqrt5\), \(s=r_0-r\downarrow0\), and denote the angular interval length in the CDF integrand by \(G(z,r)\). Taylor expansion at \((0,r_0)\) gives, uniformly for \(0\le z\le z_*(r)\),
\[
z_*(r)=\frac53s+O(s^2),\qquad G(z,r)=\frac{5\sqrt5}{6}s-\frac{\sqrt5}{2}z+O(s^2+sz+z^2).
\]
Consequently
\[
\Pr(D\le d)=\frac{12}{\pi}\left(\frac{25\sqrt5}{36}s^2+O(s^3)\right)
=\frac{25\sqrt5}{3\pi}s^2+O(s^3).
\]
For \(d=\ell(3/\sqrt{10}+\delta)\), differentiation of \(r=\sqrt{2(1-t^2)}\) at \(t=3/\sqrt{10}\) shows \(s=3\sqrt2\,\delta+O(\delta^2)\). The coefficient becomes \(150\sqrt5/\pi\), as claimed.

## Verification
The included Python 3 standard-library program `verify_tetra_projection_diameter.py` reconstructs the four original vertices, projects all six independent edge pairs into 30,000 randomly oriented planes, and checks agreement with the coordinate-gap reduction. It independently approximates the exact spherical-chamber CDF by composite midpoint integration and checks five thresholds and both endpoint coefficients numerically. Run `python3 verify_tetra_projection_diameter.py`. Its output should conclude `ALL_RANDOM_TETRAHEDRON_SHADOW_DIAMETER_CHECKS_OK`. These finite checks corroborate but cannot prove the analytical distribution or its asymptotics.

## Relationship to prior work
Finch (2011), *Width Distributions for Convex Regular Polyhedra*, analyzes the distributional moments of **three-dimensional directional caliper width** of the tetrahedron; that functional is the length of its projection onto a line, not the diameter of its projection onto a plane. Finch (2012), *Planar Projections and Second Intrinsic Volume*, directly studies random tetrahedral planar shadows, but its Section 2.1 reports area and perimeter moments and the probabilities of three versus four silhouette vertices, not the diameter statistic. Related geometric-probability studies of central sections of the octahedron concern different operations and bodies. These statements do not imply the diameter CDF or the two endpoint coefficients without additional analysis.

## Limitations
The claim is specific to regular tetrahedra, Haar-uniform central plane directions, and Euclidean orthogonal projections. It makes no assertion about random nonregular tetrahedra, perspective projection, offset planar sections, shadow area or perimeter distributions, or independent mathematical certification. A literature comparison cannot establish exhaustive historical priority; less visible equivalent treatments remain possible. The CDF is specified by an exact definite integral rather than a closed antiderivative.

## References
1. Steven R. Finch, *Width Distributions for Convex Regular Polyhedra*, 4 October 2011, arXiv:1110.0671, https://arxiv.org/abs/1110.0671.
2. Steven R. Finch, *Planar Projections and Second Intrinsic Volume*, 12 March 2012, arXiv:1203.2464, https://arxiv.org/html/1203.2464v1.
3. *Exact Haar diameter law for central sections of the regular octahedron*, published published-finding corpus research record, 2026 (comparison of sectional and projected diameters only).
4. *Area-weighted silhouette probabilities of arbitrary tetrahedra*, published published-finding corpus research record, 2026 (comparison of shadow area and combinatorial observables only).
