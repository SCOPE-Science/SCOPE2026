# Exact circumradius distribution and a curvature transition for random planar cube shadows

## Finding
Let \(Q=[-1,1]^3\) and let \(E\) be a Haar-uniform unoriented plane in \(\mathbb R^3\). The planar orthogonal projection \(P_EQ\) has Euclidean circumradius \(R(E)\), measured about the origin (which is a circumcenter by central symmetry). The **complete exact CDF** of \(R\) is given below by one-dimensional quadratures of elementary functions.

For \(0\le t\le1\), \(0\le\phi\le\pi/4\), set
\[
 s(\phi)=\cos\phi+\sin\phi,\qquad q(\phi)=1+s(\phi)^2,\qquad
 b_-(t,\phi)=\frac{t+s(\phi)\sqrt{q(\phi)-t^2}}{q(\phi)}.
\]
Define
\[
 B(t)=\frac{12}{\pi}\int_0^{\pi/4}\bigl[1-b_-(t,\phi)\bigr]d\phi.
\]
For \(0\le t<1/\sqrt3\), define
\[
 \phi_t=\arccos\sqrt{\frac{1-t^2}{1+t^2}},\qquad
 b_+(t,\phi)=\frac{-t+s(\phi)\sqrt{q(\phi)-t^2}}{q(\phi)},
\]
\[
 J(t)=\frac{12}{\pi}\int_{\phi_t}^{\pi/4}\left[b_+(t,\phi)-\frac{\cos\phi}{\sqrt{1+\cos^2\phi}}\right]d\phi.
\]
Set \(J(t)=0\) when \(1/\sqrt3\le t\le1\). Then
\[
 \boxed{\Pr\{R\le r\}=B\bigl(\sqrt{3-r^2}\bigr)+J\bigl(\sqrt{3-r^2}\bigr),\quad \sqrt2\le r\le\sqrt3.}
\]
The CDF is zero for \(r<\sqrt2\) and one for \(r>\sqrt3\); there are no atoms. These are **evaluated one-dimensional elementary integrals**, not asserted elementary antiderivatives.

There is exactly one interior change in the quadrature geometry, at \(r_*=\sqrt{8/3}\), corresponding to \(t_*=1/\sqrt3\). The new branch turns on as
\[
 J(t)=\frac{9\sqrt3}{4\pi}(t_*-t)^2+O((t_*-t)^3)
 \quad(t\uparrow t_*),
\]
so that the complete CDF is continuously differentiable at \(r_*\) but its second derivative has the **positive jump**
\[
 \boxed{F_R''(r_*+)-F_R''(r_*-)=\frac{36\sqrt3}{\pi}.}
\]
The sharp endpoint laws are
\[
 \boxed{F_R(\sqrt2+\varepsilon)=\frac6\pi\varepsilon^2+O(\varepsilon^3),\qquad
 1-F_R(r)=\frac4{\sqrt3}\sqrt{3-r^2}+O(3-r^2)\quad(r\uparrow\sqrt3).}
\]
In particular the upper-tail exponent is \(1/2\) as a function of \(\sqrt3-r\), while the lower-endpoint CDF vanishes quadratically.

## Assumptions and scope
The cube has side length two and is centered at the origin. All distances and projections are Euclidean; Haar-uniformity is that of the Grassmannian \(\operatorname{Gr}(2,3)\). The polygon \(P_EQ\) is centrally symmetric, so its minimum enclosing circle can be centered at the origin. The randomness is solely the orientation of \(E\); the cube is deterministic. The claimed distribution concerns the two-dimensional **shadow circumradius**, not the inradius, the area, the perimeter, the one-dimensional width, or the circumradius of a cube *section*.

## Proof
**1. Exact deterministic reduction.** Represent \(E=U^\perp\), where \(U\in S^2\) is uniform. For every cube vertex \(v\in\{-1,1\}^3\),
\[
 \|P_Ev\|_2^2=\|v\|_2^2-(v\cdot U)^2=3-(v\cdot U)^2.
\]
Every point of the projected cube is a convex combination of its eight projected vertices, and the norm is convex; therefore its maximum occurs at a projected vertex. By the symmetry of the projected cube its origin-centered disk of radius equal to this maximum is a smallest enclosing disk. Set the ordered absolute coordinates of \(U\) to \(0\le a\le b\le c\). Among all signed sums of these three numbers, the smallest absolute value is \(|c-a-b|\): the only competing nonnegative representatives are \(c+a-b\), \(c+b-a\), and \(a+b+c\), all no smaller, using \(a\le b\le c\). Thus
\[
 \boxed{R(U)=\sqrt{3-(c-a-b)^2}.}
\]
In particular \(0\le|c-a-b|\le1\). The value \(1\) is approached near coordinate-axis normals; the value \(0\) occurs along nonempty curves. This proves the sharp support \([\sqrt2,\sqrt3]\).

**2. Exact Haar integration.** Coordinate permutations and independent sign changes split the unit sphere into \(48\) congruent sorted sign chambers. In the positive chamber \(0\le x\le y\le z\), parameterize
\[
 (x,y,z)=(\sin\theta\sin\phi,\sin\theta\cos\phi,\cos\theta),
 \quad 0\le\phi\le\pi/4,\quad0\le\theta\le\theta_{\max}(\phi),
\]
where \(\theta_{\max}(\phi)=\arctan(1/\cos\phi)\). The spherical area element is \(\sin\theta\,d\theta\,d\phi\). Multiplication by \(48/(4\pi)=12/\pi\) converts area in this chamber into full-sphere probability. Put \(s=\cos\phi+\sin\phi\), so \(z-x-y=\cos\theta-s\sin\theta\). For \(0\le t\le1\), the event \(R\le\sqrt{3-t^2}\) is \(|\cos\theta-s\sin\theta|\ge t\).

The function \(\theta\mapsto\cos\theta-s\sin\theta\) is strictly decreasing on this chamber. Its positive part exceeds \(t\) precisely when \(0\le\theta\le\theta_-(t,\phi)\), where the elementary trigonometric solution satisfies
\[
 \cos\theta_-(t,\phi)=b_-(t,\phi)=\frac{t+s\sqrt{1+s^2-t^2}}{1+s^2}.
\]
This range is always present (possibly of zero width at an endpoint) and integrates to \(B(t)\), because \(\int_0^{\theta_-}\sin\theta\,d\theta=1-\cos\theta_-\).

The negative part can have magnitude at least \(t\) only when its endpoint value reaches \(-t\). At \(\theta_{\max}(\phi)\),
\[
 -\bigl(\cos\theta_{\max}-s\sin\theta_{\max}\bigr)
 =\frac{\sin\phi}{\sqrt{1+\cos^2\phi}}
 =:h(\phi).
\]
This increases strictly from zero at \(\phi=0\) to \(1/\sqrt3\) at \(\phi=\pi/4\). Hence no negative branch appears for \(t\ge t_*=1/\sqrt3\). For \(t<t_*\), solving \(h(\phi_t)=t\) gives exactly the displayed \(\phi_t\), and the negative branch is \(\theta_+(t,\phi)\le\theta\le\theta_{\max}\) for \(\phi_t\le\phi\le\pi/4\). The lower endpoint has \(\cos\theta_+=b_+(t,\phi)\), while \(\cos\theta_{\max}=\cos\phi/\sqrt{1+\cos^2\phi}\). Its integrated contribution is \(J(t)\). Adding both disjoint portions and the sign/order chamber factor proves the exact CDF for every orientation except the measure-zero chamber boundaries; continuity handles those as well. The event boundaries are finite arcs of smooth spherical curves, proving the absence of atoms.

**3. Sharp interior transition.** Write \(\delta=t_*-t>0\) and \(\eta=\pi/4-\phi\). Direct differentiation at the corner gives
\[
 h'(\pi/4)=\frac4{3\sqrt3},\qquad
 \partial_t\left[b_+(t,\phi)-\cos\theta_{\max}(\phi)\right]_{(t_*,\pi/4)}=-\frac12.
\]
Thus the shrinking integration interval has width \(\delta\cdot3\sqrt3/4+O(\delta^2)\), and its integrand is a smooth triangular ramp with leading profile \(\tfrac12(\delta-\tfrac4{3\sqrt3}\eta)_+\). Integration gives
\[
 J(t)=\frac{12}{\pi}\frac{\delta^2}{4(4/(3\sqrt3))}+O(\delta^3)
 =\frac{9\sqrt3}{4\pi}\delta^2+O(\delta^3).
\]
The first branch \(B\) is smooth around \(t_*\). Since \(t=\sqrt{3-r^2}\) has derivative \(-r_*/t_*=-2\sqrt2\) at \(r_*\), the new branch equals \((18\sqrt3/\pi)(r-r_*)_+^2+O(|r-r_*|^3)\). Its second derivative jump is \(36\sqrt3/\pi\), as claimed.

**4. Sharp endpoint probabilities.** Near a coordinate-axis normal, the two small transverse absolute coordinates satisfy \(a+b\le\delta+O(\delta^2)\) for \(|c-a-b|\ge1-\delta\). Each of the six axis poles contributes spherical area \(2\delta^2+O(\delta^3)\), from the two-dimensional diamond \(\{|x|+|y|\le\delta\}\). Dividing the total \(12\delta^2+O(\delta^3)\) by \(4\pi\) gives \(\Pr\{|c-a-b|\ge1-\delta\}=3\delta^2/\pi+O(\delta^3)\). For \(r=\sqrt2+\varepsilon\), \(1-\sqrt{3-r^2}=\sqrt2\varepsilon+O(\varepsilon^2)\). This proves the lower-endpoint expansion.

For the upper endpoint, \(|c-a-b|\le t\) is precisely the union of four spherical strips \(\{|v\cdot U|\le t\}\), where \(v\) ranges over the four antipodal classes of cube vertices \(\{-1,1\}^3\). Since \(\|v\|_2=\sqrt3\), the dot product with a uniform direction is uniform on \([-\sqrt3,\sqrt3]\), and each strip has probability \(t/\sqrt3\). Distinct strip great circles meet transversely, so their pairwise overlaps have probability \(O(t^2)\). Inclusion-exclusion yields \(\Pr\{|c-a-b|\le t\}=4t/\sqrt3+O(t^2)\). Substitute \(t=\sqrt{3-r^2}\) to obtain the upper-endpoint expansion. \(\square\)

## Verification
The accompanying standalone `verify.py` uses the Python standard library. Run `python3 verify.py` from the directory containing this file. It checks the exact CDF support, monotonicity on 200 grid points, and normalizes the zero-threshold case; reconstructs 800 independent random projected-cube vertices in an orthonormal basis of each random plane and matches the deterministic ordered-coordinate formula; compares the one-dimensional quadrature against an independently parameterized two-dimensional spherical grid; checks both endpoint coefficients and the interior transition coefficient numerically; and compares 120,000 independently sampled random orientations with predicted CDF events at four thresholds. Successful execution prints `ALL_CUBE_SHADOW_CIRCUMRADIUS_CHECKS_PASSED`. These finite and numerical checks corroborate but do not prove the continuum theorem; the proof is given above.

## Relationship to prior work
Kabluchko, Prochno, and Thäle (2019) study asymptotic random projections of high-dimensional cubes and general product measures. Their inspected results concern the large-dimensional regime and do not evaluate the fixed three-dimensional Euclidean shadow circumradius. Kabluchko and Seidel (2020) compute combinatorial face-count information for random projections of regular polytopes, including cubes; facet counts do not determine a metric circumradius distribution. Finch's earlier width calculations treat one-dimensional directional projections rather than this random **planar** max-vertex-radius invariant.

The published result *Exact Haar diameter law for central sections of the regular octahedron* determines the reciprocal of the cube **projection inradius**, by polarity; it does not determine the cube **projection circumradius**. Conversely, *Exact inradius law for random planar projections of the regular octahedron* concerns the reciprocal of the cube **section circumradius**, a different section/projection interchange. The published *Exact directional width law of the cube and its first spherical-cap transition* treats the one-dimensional random width \(\sum_i|U_i|\), not the minimum signed diagonal sum arising here. The published *Exact planar shadow-area moments for all orthotopes* does not determine radius distributions. These distinctions were checked at the level of mathematical statements, not merely titles. The new contribution is the complete fixed-dimensional planar cube-shadow circumradius law and its nontrivial phase and endpoint geometry; standard spherical integration and cube projection identities themselves are not claimed as new.

## Limitations
The formula concerns exactly the centered Euclidean cube of side length two, Haar-random planes through the origin, and its planar orthogonal shadow. The CDF is expressed by evaluated one-dimensional quadratures, not asserted as a closed elementary antiderivative. The proof does not cover oblique or affine projections, arbitrary orthotopes, or higher dimensions. Full historical priority remains provisional: a differently indexed special-case result in older projection geometry could exist, despite the inspected exact-metric and random-projection literature. No independent mathematical audit has been performed.

## References
1. Z. Kabluchko, J. Prochno, C. Thäle, *A new look at random projections of the cube and general product measures*, arXiv:1910.02676v1, first posted 2019-10-07, https://arxiv.org/pdf/1910.02676.
2. Z. Kabluchko and Z. Seidel, *Convex cones spanned by regular polytopes*, arXiv:2006.09492v1, first posted 2020-06-16, https://arxiv.org/pdf/2006.09492.
3. S. R. Finch, *Width Distributions for Convex Regular Polyhedra*, arXiv:1110.0671, first posted 2011-10-04, https://arxiv.org/pdf/1110.0671.
4. *Exact Haar diameter law for central sections of the regular octahedron*, public mathematical research note, October 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-haar-diameter-law-for-central-sections-of-the-regular-octa--4948185eba2f.
5. *Exact inradius law for random planar projections of the regular octahedron*, public mathematical research note, October 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-inradius-law-for-random-planar-projections-of-the-regular--5fbcddcea5e5.
6. *Exact directional width law of the cube and its first spherical-cap transition*, public mathematical research note, October 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-directional-width-law-of-the-cube-and-its-first-spherical--c1e6aa54ecb2.
7. *Exact planar shadow-area moments for all orthotopes*, public mathematical research note, October 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-planar-shadow-area-moments-for-all-orthotopes--0d2368f94d4d.
