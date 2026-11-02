# Exact intrinsic vertex-distance law on the surface of a unit cube

## Finding
Let \(C=\partial[0,1]^3\) have its intrinsic length metric, fix the vertex \(o=(0,0,0)\), and let \(X\) be uniformly sampled with respect to surface area. Write \(D=d_C(o,X)\). For \(c>0\) and \(r\ge c\), define
\[
\Phi_c(r)=\frac12\left[r^2\arcsin\frac{c}{r}+c\sqrt{r^2-c^2}\right].
\]
Then the complete distribution of \(D\) is
\[
\boxed{F_D(r)=\begin{cases}
0,&r<0,\\
\pi r^2/8,&0\le r\le1,\\
\Phi_{1/\sqrt2}(r)-1/4,&1<r\le\sqrt2,\\
\Phi_1(r)+\Phi_{1/\sqrt2}(r)-\pi r^2/8-3/4,&\sqrt2<r\le\sqrt5,\\
1,&r>\sqrt5.
\end{cases}}
\]
In particular, \(\max_{x\in C}d_C(o,x)=\sqrt5\), achieved at the opposite cube vertex, and
\[
\boxed{\mathbb E[D^2]=\frac32.}
\]
The density exists and is continuous, and is exactly
\[
\boxed{f_D(r)=\begin{cases}
\pi r/4,&0<r\le1,\\
r\arcsin\!\left(1/(\sqrt2r)\right),&1<r\le\sqrt2,\\
r\left[\arcsin(1/r)+\arcsin\!\left(1/(\sqrt2r)\right)-\pi/4\right],&\sqrt2<r<\sqrt5,\\
0,&\text{otherwise}.
\end{cases}}
\]
The CDF is \(C^1\) on \(\mathbb R\). Its second derivative jumps by \(-1\) at each of the two interior geometric transition radii \(1\) and \(\sqrt2\), and by \(+5/6\) at the upper endpoint \(\sqrt5\). The terminal tail is sharp:
\[
\boxed{1-F_D(\sqrt5-\varepsilon)\sim\frac5{12}\varepsilon^2\quad(\varepsilon\downarrow0).}
\]

## Assumptions and scope
All lengths are in units of the cube edge, which is exactly one. Only the two-dimensional boundary surface is sampled; the solid interior is excluded. The intrinsic distance is the infimum of lengths of surface-confined curves, rather than ambient Euclidean distance or graph-edge distance. Boundary edges and vertices have zero sampling area; the distance identities hold on these sets as well. For an edge length \(a>0\), the distribution rescales as \(D_a\overset{\mathrm{law}}=aD\), with \(\mathbb E[D_a^2]=3a^2/2\).

## Proof
**1. Exact distance on each face.** On each face containing \(o\), parametrized by \((0,u,v)\), the straight line in that face and the Euclidean chord bound imply \(d_C(o,(0,u,v))=\sqrt{u^2+v^2}\). On an opposite face, say \(x=1\), write \(p=(1,u,v)\) with \(0\le u,v\le1\), and set
\[
g(p)=\min\left\{\sqrt{(1+u)^2+v^2},\ \sqrt{(1+v)^2+u^2}\right\}.
\]
The two expressions are lengths of feasible straight paths unfolded across the edges of the incident source faces \(y=0\) and \(z=0\). They supply the upper bound \(d_C(o,p)\le g(p)\): the crossing of the common edge occurs within the unit segment because the other coordinate is at most one. Define \(g\) on all six faces by these formulas and by symmetry. They agree on every shared edge (including edges between two opposite faces). Every expression is the Euclidean distance from a fixed point in a face chart, so each restriction of \(g\) is \(1\)-Lipschitz; so is their pointwise minimum. A continuous facewise \(1\)-Lipschitz function on the cubical length surface is globally \(1\)-Lipschitz, by subdividing any rectifiable path at its face crossings (or by approximation). Hence \(g(p)-g(o)\le d_C(o,p)\), and \(g(o)=0\). Both inequalities establish \(g=d_C(o,\cdot)\). On \(x=1\) this gives
\[
\boxed{d_C(o,(1,u,v))^2=1+u^2+v^2+2\min(u,v).}
\]

**2. A planar square and triangle.** Let \(S=[0,1]^2\), and let \(T\) be the right triangle with vertices \((1,0),(1,1),(2,1)\). Each of the three incident faces contributes the disk-intersection area \(|S\cap B_r|\). Splitting one opposite face into \(u\le v\) and \(v\le u\), and translating the smaller coordinate by one, proves that its contribution is \(2|T\cap B_r|\). Dividing the sum over all six faces by total area six gives the exact identity
\[
F_D(r)=\frac12|S\cap B_r|+|T\cap B_r|.
\]
In polar coordinates \((s\cos\theta,s\sin\theta)\), the triangle is described by \(s\cos\theta\ge1\), \(s(\cos\theta-\sin\theta)\le1\), \(s\sin\theta\le1\), with \(0\le\theta\le\pi/4\). Its angular intersection with a circle of radius \(r\), for \(1<r<\sqrt5\), runs from
\[
\theta_-(r)=\arccos\!\left(1/(\sqrt2r)\right)-\pi/4
\]
to \(\arccos(1/r)\) if \(r<\sqrt2\), and to \(\arcsin(1/r)\) if \(r>\sqrt2\). This follows by comparing the constraints on the two straight sides and the left side of the triangle. The square contributes angular measure \(\pi/2\) for \(r<1\), \(\pi/2-2\arccos(1/r)\) for \(1<r<\sqrt2\), and zero thereafter. Multiplying these angular measures by \(r\) and using the preceding area identity yields exactly the three density branches in the Finding. Integrating, using \(\Phi'_c(r)=r\arcsin(c/r)\), gives the stated CDF, including all constants. The branches match at \(1\), \(\sqrt2\), and \(\sqrt5\), where the CDF reaches one.

**3. Moments and differentiability.** On an incident face, \(\mathbb E[D^2\mid\text{incident face}]=2/3\). On an opposite face, independence of the uniform coordinates and \(\mathbb E[\min(U,V)]=1/3\) give \(\mathbb E[D^2\mid\text{opposite face}]=1+2/3+2/3=7/3\). The two classes comprise three faces each; hence \(\mathbb E[D^2]=(2/3+7/3)/2=3/2\). For the density derivative, on the three open positive support intervals one gets respectively
\[
 f_D'(r)=\frac\pi4,\qquad
 f_D'(r)=\arcsin(c/r)-\frac{c}{\sqrt{r^2-c^2}},\qquad
 f_D'(r)=\arcsin(1/r)+\arcsin(c/r)-\frac\pi4-\frac1{\sqrt{r^2-1}}-\frac{c}{\sqrt{r^2-c^2}},
\]
where \(c=1/\sqrt2\). The second minus first one-sided value at \(r=1\) is \(-1\); the third minus second at \(r=\sqrt2\) is also \(-1\). At the terminal radius \(r=\sqrt5\), the interior value is \(-5/6\), and the exterior value is zero, hence the jump is \(+5/6\). The first derivative is continuous, including at the endpoints of the support.

**4. Upper-tail coefficient.** Only the three opposite faces contribute at radii near \(\sqrt5\), equivalently the single triangle in the area identity. Near its farthest vertex \((2,1)\), write \((x,y)=(2-s,1-t)\). The triangle has \(s\ge t\ge0\), and
\[
\sqrt5-\sqrt{(2-s)^2+(1-t)^2}=(2s+t)/\sqrt5+O(s^2+t^2).
\]
The first-order region \(2s+t\le\sqrt5\varepsilon\), \(0\le t\le s\), is a triangle of area \(5\varepsilon^2/12\). Uniform quadratic remainders imply the required equivalent for the true intersection region. Thus the tail coefficient is \(5/12\), and in particular the density has slope \(-5/6\) as the endpoint is approached from below.

## Verification
The standalone Python standard-library checker `verify_cube.py` reproduces the piecewise CDF and density, compares the analytic CDF to independent planar square/triangle quadrature and deterministic pseudo-random sampling, tests the exact second moment, and checks the sharp endpoint coefficient. Every probabilistic or numerical check is finite evidence; the universal equality and smoothness statements follow from the preceding facewise Lipschitz argument and exact area integration. Reproduce with `python3 verify_cube.py` from the directory containing that file.

## Relationship to prior work
Miller and Pak's source-unfolding theory treats geodesic wavefronts on convex polyhedral surfaces and illustrates cube unfoldings, but does not evaluate this vertex-source area distribution. Goldstone, Roca, and Valli study shortest paths with source and target in the interiors of opposite cube faces and estimate the frequency of four-face minimizers, a different endpoint and probability problem. Mathai, Moschopoulos, and Pederzoli treat *ambient Euclidean* distances between points sampled in and on cubes; that metric differs on this surface (e.g. the opposite vertex has ambient distance \(\sqrt3\) but intrinsic distance \(\sqrt5\)). Thus neither those general methods nor those ambient-distance formulas contain the present three-branch intrinsic law without additional case-specific analysis.

## Limitations
This theorem is for a fixed cube vertex and a single surface-uniform point. It does not determine the distance law between two independent surface points, nor generalize automatically to rectangular cuboids. The priority search cannot exclude older unindexed mathematical recreations of the vertex-source calculation. No independent mathematical or historical-priority audit has been performed.

## References
- E. Miller and I. Pak, *Metric combinatorics of convex polyhedra: Cut loci and nonoverlapping unfoldings*, arXiv:math/0312253 (first posted 2003-12-12), https://arxiv.org/abs/math/0312253.
- R. Goldstone, R. Roca, and R. Suzzi Valli, *Shortest Paths on Cubes*, arXiv:2003.06096 (first posted 2020-03-13), https://arxiv.org/html/2003.06096v1.
- A. M. Mathai, P. Moschopoulos, and G. Pederzoli, *Distance between random points in a cube*, Statistica **59** (1999), 61–81, https://doi.org/10.6092/issn.1973-2201/1104.
