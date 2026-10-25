# A universal vertex-count fingerprint in short chords of rounded convex polygons

## Finding

Let \(P\) be a convex Euclidean polygon with \(m\geq3\) vertices, strictly positive exterior angles \(\omega_v\in(0,\pi)\) and perimeter \(L\). Let \(B\) be the unit disk. For \(r>0\) set \(K_r=P+rB\), and let \(X_r\) be the length of the intersection with an invariant-random unoriented line, conditioned on the line meeting \(K_r\). The line is sampled with density proportional to \(dp\,d\theta\) in normal coordinates \(\theta\in[0,\pi)\) and signed offset \(p\).

Define the dimensionless threshold \(s_*:=\min_v 2\sin(\omega_v/2)>0\). For every fixed \(s\in(0,s_*)\) there exists \(r_0(P,s)>0\) such that **for every** \(0<r<r_0(P,s)\),

\[
\boxed{\Pr\{X_r\leq rs\}=\frac{r}{L+2\pi r}\left[2\pi H(s)+m\Psi(s)\right],}
\]
where
\[
H(s)=1-\sqrt{1-s^2/4},\quad a_s=\arcsin(s/2),
\]
\[
\Psi(s)=2\int_0^{a_s}\!\left[1-\cos\left(\arccos(1-s\sin a)-a\right)-H(s)\right]da.
\]
The integral is elementary and unambiguous for \(0<s<2\). It is strictly negative there. In particular, sufficiently short chord probabilities for any two polygons of the **same perimeter and the same number of vertices** are identical after the same rounding, even when their interior-angle lists differ. The formula makes no assertion that the entire chord distributions coincide.

There is also a sharp vertex-count expansion, uniform for \(s\downarrow0\) at each fixed admissible rounding radius sufficiently small for the indicated \(s\):
\[
\boxed{\frac{L+2\pi r}{r}\Pr\{X_r\le rs\}
=\frac{\pi}{4}s^2-\frac{m}{30}s^3+\frac{\pi}{64}s^4+O_P(s^5).}
\]
Consequently the coefficient of the cubic term in this normalized short-chord law recovers exactly the number of corners \(m\). This is distinct from the known short-chord asymptotics for *unrounded* polygons.

## Assumptions and scope

The polygon is fixed, bounded, convex, full-dimensional, with no consecutive collinear edges, and has a finite positive minimum edge length. Its exterior angles satisfy \(\sum_v\omega_v=2\pi\). The radius \(r\) tends to zero relative to the fixed polygon; the inequality \(s<s_*\) excludes transitions in which both endpoints enter tangent rays at the same corner. The normalization is Crofton/invariant-line measure conditioned on intersection; it is not the distribution obtained by sampling two boundary points or by conditioning all lines through a fixed center. No independence of polygon sides is assumed.

## Proof

**1. Invariant-line normalization.** For normal angle \(\theta\in[0,\pi)\), all hit-line offsets form an interval of length equal to the width of \(K_r\). Cauchy's projection identity yields total invariant hit-line measure \(\int_0^\pi w_{K_r}(\theta)d\theta=\operatorname{Per}(K_r)=L+2\pi r\). For short chords, measure the offset distance from the support line on the unique nearer side; integration over **outward** normals in \([0,2\pi)\) counts each such line exactly once (except a null boundary set).

**2. Localization at one corner.** Fix \(s<s_*\) and let \(r\downarrow0\). A line through a nonvertex support point of \(P\) has a positive full edge chord (away from finitely many edge-normal changes); more quantitatively, any chord of \(P+rB\) of length at most \(rs\) has endpoints within \(O_P(r)\) of one vertex. Indeed, compactness of the polygonal boundary minus disjoint vertex neighborhoods and the minimum positive distances between nonincident edges rule out any such small chord elsewhere; lines nearly parallel to a side still span essentially its positive length. After shrinking \(r_0(P,s)\), the entire short chord agrees exactly with the corresponding chord of the infinite wedge obtained by extending the two incident edges and adding the disk of radius \(r\). Distinct vertex neighborhoods are disjoint, so their contributions add. Each vertex corresponds to an exterior normal interval of angular length \(\omega\).

**3. Unit-rounded wedge.** Translate the vertex to the origin, divide lengths by \(r\), and let \(a\in(0,\omega)\) be the angle of the outward unit normal from the first adjacent edge normal; write \(b=\omega-a\). The rounded wedge has a unit circular fillet spanning that interval of normals, connected to two tangent rays. If the cutting line is at distance \(h\) inward from the support line, set \(p=1-h\). Its intersections with the unit circle are separated by \(2\sqrt{1-p^2}\) if both fall on the fillet; this is the case at threshold length \(s\) whenever \(a\ge a_s\) and \(b\ge a_s\). Then \(h=H(s)\).

For \(0<a<a_s\), the nearer endpoint is on one tangent ray and the other on the circular fillet. Write \(p=\cos t\), where \(t\in(0,a)\). Elementary normal/tangent projection gives the chord length
\[
s=\sin t+\frac{1-\cos t\cos a}{\sin a},\qquad
\cos(t+a)=1-s\sin a.
\]
Thus
\[
t=\arccos(1-s\sin a)-a,\quad h_m(s,a)=1-\cos t.
\]
The same contribution occurs for \(\omega-a_s<a<\omega\) with the two sides exchanged. Because \(s<2\sin(\omega/2)\), these two boundary strips are disjoint, and all middle normals have both endpoints on the fillet. Chord length is strictly increasing in inward depth until the prescribed threshold, so the eligible offset interval is exactly the stated depth. Integrating over one exterior normal cone gives
\[
\begin{aligned}
J_\omega(s)&=(\omega-2a_s)H(s)+2\int_0^{a_s}h_m(s,a)\,da\\
&=\omega H(s)+\Psi(s).
\end{aligned}
\]
Scaling the support offsets multiplies this measure by \(r\).

**4. Summation and strict inequality.** Sum \(rJ_{\omega_v}(s)\) over vertices and use \(\sum_v\omega_v=2\pi\), then divide by \(L+2\pi r\) to obtain the exact probability formula. On \(0<a<a_s\), the tangent-ray endpoint lies farther from the support line than would the second intersection with the full circle at the same chord length. Hence \(0<h_m(s,a)<H(s)\) for a set of positive measure, so \(\Psi(s)<0\).

**5. Sharp cubic coefficient.** Set \(a=su\) with \(0\le u\le\frac12+O(s^2)\). Taylor expansions, uniform on this interval, give
\[
H(s)=s^2/8+s^4/128+O(s^6),\quad
h_m(s,su)=s^2\left(u+\frac{u^2}{2}-u\sqrt{2u}\right)+O(s^4).
\]
The boundary-layer integrand is bounded by a fixed multiple of \(s^2\), allowing termwise integration. Its leading coefficient is
\[
2\int_0^{1/2}\left(u+\frac{u^2}{2}-u\sqrt{2u}-\frac18\right)du
= -\frac1{30}.
\]
Taylor parity and the \(a=su\) change of variables give \(\Psi(s)=-s^3/30+O(s^5)\). Substitute into the exact expression to obtain the displayed expansion. Its leading \(s^4\) coefficient comes solely from \(2\pi H(s)\), and equals \(\pi/64\). All expansions concern the dimensionless short-chord range, not a claim about fixed positive chord lengths as \(r\downarrow0\).

## Verification

The included program `verify_rounded_chords.py` independently approximates rounded polygon boundaries by high-resolution circular arcs, intersects supporting normal lines with those boundaries, and solves for chord-length offsets by bisection. It compares the direct line-integrated probability against the theoretical expression for squares, rectangles, and an equilateral triangle with matching perimeter, including differing corner counts; it checks the cubic asymptotic numerically. Mesh and quadrature errors persist: these tests corroborate but do not replace the geometric proof. Run `python verify_rounded_chords.py` with Python, NumPy, SciPy, and Shapely installed.

## Relationship to prior work

García-Pelayo (2015, arXiv:1501.00292) derives chord-length calculations for polygonal domains from edge-pair contributions, rather than the rounded parallel-body short-chord germ; relevant sections on polygon chords were inspected. Dobrohotoff and collaborators (2012) describe rounded polygons/spheropolygons as Minkowski sums with disks but study shape modeling rather than invariant chord probabilities. Classical polygon chord-length literature (including Gates 1987 and Bäsel 2014) concerns unrounded polygon laws or qualitative shape distinctions. The latter two sources were not verified throughout their full texts; consequently historical priority, including possible equivalent formulas in the older stochastic-geometry literature, remains a residual risk. A search of accessible published mathematical finding records identified point-distance and center-chord laws but not this exact rounded-body vertex-count fingerprint. A negative search alone cannot certify novelty.

## Limitations

The polygon must be fixed while the rounding radius is sufficiently small, with a threshold satisfying \(s<s_*\). The smallness bound on \(r\) depends on polygon geometry and on \(s\). The formula does not cover arbitrary smooth convex bodies, nonuniform line sampling, moderate/long chords, or all chord thresholds. The asymptotic series is a small-\(s\) expansion of the exact short-chord expression. No independent mathematical review or definitive exhaustive historical-priority check has been performed.

## References

- R. García-Pelayo, *Computation of the multi-chord distribution of convex and concave polygons* (2015), arXiv:1501.00292, https://arxiv.org/abs/1501.00292.
- L. Dobrohotoff et al., *Optimal description of two-dimensional complex-shaped objects using spheropolygons*, Granular Matter 14 (2012), 651–658, https://doi.org/10.1007/s10035-012-0357-9.
- J. Gates, *Some properties of chord length distributions*, Journal of Applied Probability 24 (1987), 863–874.
- U. Bäsel, *Random chords and point distances in regular polygons* (2014).
