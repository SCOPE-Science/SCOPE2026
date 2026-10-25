# Exact high-circumradius law for random planar cube shadows

## Finding

Let \(Q=[-1,1]^3\), let \(U\) be uniform on the unit sphere, and let \(R\) be the Euclidean radius of the smallest disk containing the orthogonal projection of \(Q\) onto \(U^\perp\). Define the four alternating sign vectors
\[
v_1=(1,1,1),\quad v_2=(1,1,-1),\quad v_3=(1,-1,1),\quad v_4=(-1,1,1).
\]
The radius has exact deterministic form
\[
R^2=3-\min_{1\le j\le4}|\langle U,v_j\rangle|^2,
\qquad \sqrt2\le R\le\sqrt3.
\]
For \(0<t\le1/\sqrt3\), put \(a=t/\sqrt3\), \(c=1/3\), \(s=2\sqrt2/3\), and define the explicit one-dimensional integral
\[
J(t)=\frac1{2\pi}\int_{-a}^{a}
\left[\arcsin\left(\frac{a-cy}{s\sqrt{1-y^2}}\right)
-\arcsin\left(\frac{-a-cy}{s\sqrt{1-y^2}}\right)\right]dy.
\]
Then **the entire upper tail above the sharp three-belt intersection threshold** is exactly
\[
\boxed{\Pr\left(R>\sqrt{3-t^2}\right)=\frac{4t}{\sqrt3}-6J(t),
\qquad 0<t\le\frac1{\sqrt3}.}
\]
Equivalently, the formula holds for all radius thresholds \(\sqrt{8/3}\le r<\sqrt3\), with \(t=\sqrt{3-r^2}\). The upper-tail endpoint expansion is
\[
\boxed{\Pr\left(R>\sqrt{3-t^2}\right)
=\frac{4t}{\sqrt3}-\frac{3\sqrt2}{\pi}t^2
-\frac{3}{4\pi\sqrt2}t^4+O(t^6).}
\]
In terms of an absolute radius deficit \(\varepsilon>0\), this implies
\[
\boxed{\Pr(R>\sqrt3-\varepsilon)
=4\sqrt{\frac2{\sqrt3}}\,\varepsilon^{1/2}
-\frac{6\sqrt6}{\pi}\varepsilon+O(\varepsilon^{3/2}).}
\]
The threshold \(t=1/\sqrt3\) is sharp for the two-term spherical-belt inclusion–exclusion: below it no three of the four belts overlap, whereas just above it triple overlaps have positive spherical area.

## Assumptions and scope

The cube has edge length \(2\) and is centered at the origin. The plane is a uniformly oriented *linear* two-plane; its normal \(U\) has normalized Haar/spherical surface measure. The circumradius is that of the minimal **enclosing** Euclidean disk in the projection plane, not its inradius, area-equivalent radius, intrinsic volume or diameter. For a centrally symmetric planar convex set, one smallest enclosing disk is centered at its symmetry center: if disks of radius \(r\) centered at \(x\) and \(-x\) both contain the set, their midpoint disk centered at zero also contains it. The equality events at fixed radius thresholds have probability zero. The formula claims only the stated upper-tail interval, not a complete distribution on \([\sqrt2,\sqrt3]\).

## Proof

**1. Reduction to four tetrahedral axes.** Projection preserves convex hulls, so the enclosing radius is the largest Euclidean norm of the projected eight cube vertices. Every vertex \(v\) has squared norm \(3\), and orthogonal projection onto \(U^\perp\) has squared norm \(3-(v\cdot U)^2\). Opposite vertices give the same value. Taking the four representatives \(v_j\) proves the deterministic identity. The identity \(\sum_{j=1}^4v_jv_j^\top=4I_3\) gives \(\sum_j(v_j\cdot U)^2=4\), so their least square is at most one; therefore \(R\ge\sqrt2\). Equality holds, for instance, when \(U=(1,0,0)\). A unit normal perpendicular to \(v_1\), such as \(U=(1,-1,0)/\sqrt2\), gives \(R=\sqrt3\). Continuity on the connected sphere gives the full support interval.

**2. Four spherical belts.** For \(t>0\), the event \(R>\sqrt{3-t^2}\) is the union of the four belts \(B_j(t)=\{U:|v_j\cdot U|<t\}\). Because \(v_j/\sqrt3\) is unit length, the spherical coordinate \(v_j\cdot U/\sqrt3\) is uniform on \([-1,1]\). Thus each belt has probability \(t/\sqrt3\). For distinct \(i,j\), the absolute cosine between the two unit axes is \(1/3\); changing the sign of one axis does not change its belt. All six pair intersections therefore have the same probability \(J(t)\).

**3. Evaluation of one belt-pair intersection.** Fix unit axes \(e,f\) with \(e\cdot f=c=1/3\). Write \(Y=e\cdot U\) and \(X=f\cdot U\). Conditioned on \(Y=y\), the point \(U\) lies uniformly on the corresponding latitude circle. Consequently
\[
X=cy+s\sqrt{1-y^2}\cos\Theta,
\qquad s=\sqrt{1-c^2}=\frac{2\sqrt2}{3},
\]
with \(\Theta\) uniform on \([0,2\pi]\). The variable \(Y\) has density \(1/2\) on \([-1,1]\). For \(|y|\le a\le1/3\), the two arguments in the displayed definition of \(J(t)\) lie strictly inside \((-1,1)\). The elementary arcsine law of \(\cos\Theta\) therefore gives exactly \(\Pr(|X|<a,|Y|<a)=J(t)\), establishing the integral with no independence assumption.

**4. The sharp exclusion of triple overlaps.** Choose any three distinct rows of the \(4\times3\) matrix with rows \(v_j\). Coordinate sign changes and cube symmetries reduce the analysis to \(v_1,v_2,v_3\). If \(p=v_1\cdot U\), \(q=v_2\cdot U\), and \(h=v_3\cdot U\), inversion gives
\[
U=\frac12(q+h,\,p-h,\,p-q).
\]
Thus if all three absolute inner products are at most \(t\), then
\[
1=\|U\|^2=\frac14[(q+h)^2+(p-h)^2+(p-q)^2]\le3t^2.
\]
For \(t<1/\sqrt3\) no three belts intersect. At equality only finitely many rays satisfy all required saturated linear constraints, so the intersections still have spherical measure zero. For any \(t>1/\sqrt3\), the unit vector \(U=(-1,1,1)/\sqrt3\) has three absolute inner products equal to \(1/\sqrt3\), and thus belongs to an open triple intersection; rotations give the same for the other triples. This proves sharpness of the cutoff. The fourfold overlap is already excluded on the stated interval. Inclusion–exclusion terminates after six pairs, proving the exact probability formula.

**5. The endpoint coefficients.** The normalized joint density of \((X,Y)\) for the two axes is
\[
\frac{1}{2\pi s}\left(1-\frac{x^2-2cxy+y^2}{s^2}\right)^{-1/2}
\]
in a neighborhood of the origin. Integrating its Taylor expansion over the square \([-a,a]^2\), using the vanishing of the odd cross term and the elementary square moments, yields
\[
J(t)=\frac{t^2}{\pi\sqrt2}+\frac{t^4}{8\pi\sqrt2}+O(t^6).
\]
The integrand is analytic and uniformly bounded near the origin for sufficiently small \(t\), justifying termwise integration and the remainder. Substitution into the six-pair formula yields the first expansion. Since \(t^2=3-(\sqrt3-\varepsilon)^2=2\sqrt3\varepsilon-\varepsilon^2\), expanding the positive square root proves the second expansion. \(\square\)

## Verification

Execute `python3 VERIFY.py` from the directory containing this document, with Python, NumPy and SciPy available. The standalone checker first verifies the exact triple-belt matrix operator norm via all eight sign corners for each of four row triples. It next computes the radii directly from the eight projected cube vertices, rather than using the four-axis shortcut, for 2,048 random orientations. An independent \(2^{20}\)-point scrambled Sobol spherical sample compares the exact one-dimensional integral against six threshold probabilities including the sharp triple-contact threshold. Further checks verify the small-threshold integral coefficient, both radius endpoints and the square-root endpoint expansion. Expected final marker: `ALL_CUBE_SHADOW_CIRCUMRADIUS_CHECKS_OK`. Simulations and finite checks corroborate, but do not establish, the continuous geometric identities.

## Relationship to prior work

Finch, *Planar Projections and Second Intrinsic Volume* (arXiv:1203.2464v1, 12 March 2012), examines exactly these random cube shadows, but his Section 2.2 computes area/perimeter moments and their covariance, not a minimum enclosing-circle radius distribution. The published geometric-probability benchmark thus motivates the distinct natural statistic studied here.

Because the planar cube shadow is centrally symmetric, its diameter is exactly twice its enclosing circumradius; the equivalent *random cube-shadow diameter* formulation was searched directly. The exact published law for the **diameter of a central octahedron section** studies a different extremum: its polar is the reciprocal of the **inradius of the cube projection**, not the enclosing circumradius here. The exact law for the **inradius of an octahedron projection** is polar to the circumradius of a **central cube section**, likewise a different object. Conversely, the circumradius of a cube projection is the reciprocal inradius of a central octahedron section; this equivalent formulation was explicitly included in comparison searches and is not covered by the two previous laws. An exact one-dimensional directional-width distribution for a cube also does not imply the joint four-axis minimum law governing the random *two-dimensional* projected circumradius. All three closest published results were inspected in full. Published projection-area and perimeter moment results are further distinct. A previously overlooked treatment of the equivalent inradius-of-section statistic remains a historical-priority risk.

## Limitations

This is an exact formula only for the upper-tail interval \(\sqrt{8/3}\le r<\sqrt3\) under Haar-uniform linear-plane projections of a centered three-dimensional cube. Triple and quadruple belt intersections must be included to obtain the lower part of the radius distribution. No generalization to rectangular boxes, higher dimensions or nonuniform orientation measures is claimed. Independent mathematical validation and definitive historical-priority verification remain outstanding.

## References

1. Steven R. Finch, *Planar Projections and Second Intrinsic Volume*, arXiv:1203.2464v1, first posted 12 March 2012, especially pp. 1–5, Section 2.2. https://arxiv.org/abs/1203.2464.
2. *Exact Haar diameter law for central sections of the regular octahedron*, published mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-haar-diameter-law-for-central-sections-of-the-regular-octa--4948185eba2f .
3. *Exact inradius law for random planar projections of the regular octahedron*, published mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-inradius-law-for-random-planar-projections-of-the-regular--5fbcddcea5e5 .
4. *Exact directional width law of the cube and its first spherical-cap transition*, published mathematical result (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-directional-width-law-of-the-cube-and-its-first-spherical--c1e6aa54ecb2 .
