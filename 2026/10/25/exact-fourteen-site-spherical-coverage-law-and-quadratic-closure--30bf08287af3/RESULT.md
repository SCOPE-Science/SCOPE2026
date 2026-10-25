# Exact fourteen-site spherical coverage law and quadratic closure of the cube–octahedron gaps

## Finding

Let \(\mathcal S\subset S^2\) consist of the six unit coordinate axes \(\{\pm e_1,\pm e_2,\pm e_3\}\) and the eight unit body diagonals \(\{(\pm1,\pm1,\pm1)/\sqrt3\}\), with all signs independent. Put
\[
C(u)=\max_{s\in\mathcal S}s\cdot u
   =\max\left\{\|u\|_\infty,\frac{\|u\|_1}{\sqrt3}\right\}
\quad(u\in S^2).
\]
For uniformly surface-distributed \(U\in S^2\), write \(F(c)=\Pr\{C(U)\le c\}\). This is also the **uncovered surface fraction** for the fourteen closed spherical caps of angular radius \(\arccos c\) centered at \(\mathcal S\), since boundaries have zero surface area.

Define \(r=\sqrt3-1\), \(q=(1+r^2)^{-1/2}=(5-2\sqrt3)^{-1/2}\), and \(c_0=\sqrt{(1+1/\sqrt3)/2}\). For \(q<c<1\), put \(R(x)=\sqrt{1-x^2}\),
\[
L(x)=\begin{cases}\arccos\bigl(x/R(x)\bigr),&1/\sqrt3\le x<1/\sqrt2,\\0,&x\ge1/\sqrt2,\end{cases}
\]
and, with \(b=(\sqrt3c-x)/R(x)\),
\[
H_c(x)=\begin{cases}0,&b\le1,\\\pi/4-\arccos(b/\sqrt2),&1<b<\sqrt2,\\\pi/4,&b\ge\sqrt2.\end{cases}
\]
Then the **exact full coverage law** is the single integral
\[
F(c)=\begin{cases}
0,&c\le q,\\
\displaystyle\frac{12}{\pi}\int_{1/\sqrt3}^{c}\max\{0,H_c(x)-L(x)\}\,dx,&q<c<1,\\
1,&c\ge1.
\end{cases}
\]
On the entire high-threshold interval \(c_0\le c\le1\), this simplifies exactly to \(F(c)=7c-6\).

The main new local feature is an **exact quadratic gap-closure law**:
\[
\lim_{\varepsilon\downarrow0}\frac{F(q+\varepsilon)}{\varepsilon^2}
=\frac{6}{\pi q^5r^2(1-r)}.
\]
Writing \(\rho_*=\arccos q\), equivalently, if the fourteen caps have radius \(\rho_* -\delta\), the uncovered surface fraction satisfies
\[
F\bigl(\cos(\rho_* -\delta)\bigr)
=\frac{6}{\pi q^3(1-r)}\,\delta^2+o(\delta^2)
\qquad(\delta\downarrow0).
\]
The constants are approximately \(38.8841568518\) for the threshold deficit and \(13.5672757124\) for the angular shortfall in radians. The maximum angular gap \(\rho_*\), the fourteen-site configuration, and its role in antipodal covering were already identified in Fowler–Tarnai–Gáspár (2002), and **are not claimed as new**.

## Assumptions and scope

The sites are exactly the fourteen **equally radialized** axis and body-diagonal directions above. The probability measure is Haar-uniform normalized surface area on \(S^2\). Angular radii and \(\delta\) are in radians unless a degree symbol is explicitly used. The conclusions concern coverage for this fixed configuration, **not** global optimality among all configurations of fourteen spherical caps, nor sphere coverings in arbitrary dimension.

## Proof

**Step 1 — one-chamber reduction.** Signed-coordinate permutations partition \(S^2\), up to measure-zero boundaries, into 48 congruent regions with \(x\ge y\ge z\ge0\). In this chamber, \(C(u)=\max\{x,(x+y+z)/\sqrt3\}\). Set
\[
 u=(x,R(x)\cos\phi,R(x)\sin\phi),\qquad
 1/\sqrt3\le x\le1,\quad 0\le\phi\le\pi/4.
\]
The oriented spherical area Jacobian is \(du=dx\,d\phi\). The condition \(x\ge y\) is \(\phi\ge L(x)\). The condition \(C(u)\le c\) first forces \(x\le c\), and its remaining inequality is
\[
\cos\phi+\sin\phi\le b=(\sqrt3c-x)/R(x).
\]
Since \(\cos\phi+\sin\phi=\sqrt2\cos(\pi/4-\phi)\) increases from \(1\) to \(\sqrt2\) across this angular interval, this gives precisely \(\phi\le H_c(x)\). A chamber occupies 1/48 of the sphere, so multiplying its spherical area by \(48/(4\pi)=12/\pi\) proves the claimed integral. Endpoints \(x=1\), where \(R(x)=0\), are immaterial for integration. The value is zero for \(c\le q\) by Step 2 and is one for \(c\ge1\).

**Step 2 — exact coverage threshold and gap locations.** Let \(c=C(u)\) and \(b_i=|u_i|/c\). Then \(0\le b_i\le1\), \(\sum_i b_i\le\sqrt3\), and \(\sum_i b_i^2=1/c^2\). A convex quadratic function achieves its maximum on the polytope \(\{b\in[0,1]^3:\sum b_i\le\sqrt3\}\) at a vertex; direct vertex classification (or shifting mass to a larger coordinate) gives the sharp maximum \(1+(\sqrt3-1)^2\), attained precisely by signed permutations of \((1,r,0)\) after normalization. Consequently \(c\ge q\); equality occurs at exactly 24 unit directions, namely signed permutations of \(q(1,r,0)\).

**Step 3 — near-threshold local geometry.** Fix \(u_0=q(1,r,0)\). In a sufficiently small neighborhood choose latitude-longitude coordinates
\[
u(t,z)=\left(\sqrt{1-z^2}\cos(\theta_0+t),\sqrt{1-z^2}\sin(\theta_0+t),z\right),\quad\theta_0=\arctan r.
\]
The spherical area element in these coordinates is *exactly* \(dt\,dz\). Only the axis site and the two body-diagonal sites having signs aligned with the first two coordinates can maximize the support; on this neighborhood
\[
 C(u(t,z))-q=\max\{-At,\ Bt+E|z|\}+O(t^2+z^2),
\]
with \(A=rq\), \(B=q(1-r)/\sqrt3\), and \(E=1/\sqrt3\), all positive. This estimate is uniform as \((t,z)\to(0,0)\), including both signs of \(z\). The piecewise-linear function \(H(t,z)=\max(-At,Bt+E|z|)\) is positive away from the origin and coercive. It follows by compact localization around the 24 isolated minimizers, rescaling \((t,z)=\varepsilon(T,Z)\), and dominated convergence of the bounded rescaled sublevel sets that
\[
\lim_{\varepsilon\downarrow0}\varepsilon^{-2}
\operatorname{area}\{u\text{ near }u_0:C(u)\le q+\varepsilon\}
=\operatorname{area}\{(T,Z):H(T,Z)\le1\}.
\]
The last region has \(-1/A\le T\le1/B\) and \(|Z|\le(1-BT)/E\), giving its exact Euclidean area
\[
 \int_{-1/A}^{1/B}\frac{2(1-BT)}E\,dT
 =\frac{(1+B/A)^2}{BE}
 =\frac1{q^5r^2(1-r)}.
\]
Each minimum contributes the same amount. Divide the sum over 24 minima by \(4\pi\) to obtain \(6/(\pi q^5r^2(1-r))\). The angular statement follows from \(\cos(\rho_* -\delta)=q+\sqrt{1-q^2}\,\delta+O(\delta^2)=q+rq\,\delta+O(\delta^2)\), so its coefficient is the threshold coefficient multiplied by \(r^2q^2\).

**Step 4 — disjoint-cap regime.** The smallest geodesic distance between distinct sites is \(\arccos(1/\sqrt3)\), between a coordinate axis and an adjacent body diagonal. Hence fourteen caps of radius at most half this distance have disjoint interiors. Since the normalized area of one radius-\(\arccos c\) cap is \((1-c)/2\), their uncovered fraction is \(1-14(1-c)/2=7c-6\). The disjointness condition is equivalent to \(c\ge c_0\).

## Verification

The standalone `verify_covering.py` evaluates the analytic one-dimensional integral and independently reconstructs the random-direction support function from unit-sphere samples, including a 262144-point low-discrepancy check. It also checks the 24 gap locations, the 2002 numerical benchmark, the cap-disjointness formula, and the quadratic coefficient for four small thresholds. Executed checks report `ALL_FOURTEEN_SITE_COVERAGE_CHECKS_OK`. The code is finite numerical corroboration; the proof above establishes the infinite and exact statements.

## Relationship to prior work

Fowler–Tarnai–Gáspár (2002) studied the antipodal sphere-packing-to-covering transition and already identified the equal-circumradius cube–octahedron compound for seven antipodal pairs, including its approximately \(36.2060^\circ\) covering radius and numerical near-covering data. The new statement here is the exact **full threshold-to-uncovered-area distribution and quadratic coefficient** for their fixed fourteen-site arrangement, not its configuration, covering radius, or conjectured optimum across all site sets. Their numerical coverage about 0.999790 near \(35.9839^\circ\) is consistent with the exact integral, which gives approximately 0.99979036 at that angle.

Bürgisser–Cucker–Lotz (2007) study coverage processes with independent *random* centers and associated probabilistic conditions, unlike this deterministic fourteen-site coverage distribution. General spherical Voronoi algorithms are relevant computational background but, without a verified full-text derivation, are not asserted to rule out all equivalent published formulas. Novelty here is assessed relative to the inspected scientific statements; definitive historical priority is not established.

## Limitations

The exact distribution applies only to the fourteen explicitly normalized sites and Haar-uniform sampling on the two-sphere. No global fourteen-point covering optimality, uniqueness among covering configurations, perturbation stability, or higher-dimensional analogue is proved. The analytic answer is a one-dimensional quadrature, not a completely elementary closed form in the intermediate regime. Independent review and exhaustive historical-priority verification remain unperformed.

## References

1. P. W. Fowler, T. Tarnai, Zs. Gáspár, *From circle packing to covering on a sphere with antipodal constraints*, Proceedings of the Royal Society A **458** (2002), 2275–2287, DOI: `10.1098/rspa.2002.0990`; publicly available online 24 July 2002.
2. P. Bürgisser, F. Cucker, M. Lotz, *Coverage processes on spheres and condition numbers for linear programming*, arXiv:`0712.2816` (2007).
3. H.-S. Na, C.-N. Lee, O. Cheong, *Voronoi diagrams on the sphere*, Computational Geometry **23** (2002), DOI: `10.1016/S0925-7721(02)00077-9` (abstract consulted; full-text novelty comparison not asserted).
