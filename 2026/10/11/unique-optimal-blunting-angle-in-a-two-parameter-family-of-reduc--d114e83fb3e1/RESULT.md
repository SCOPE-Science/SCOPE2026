# Unique optimal blunting angle in a two-parameter family of reduced planar bodies

## Finding
Consider the thickness-one reduced planar bodies defined by Kominers' two-arc, two-segment support-function construction. On the natural convexity-constrained quadrant
\[
\frac{\pi}{4}\le m<\frac{\pi}{2},\qquad 0\le\varepsilon\le\varepsilon_*(m),
\]
where
\[
 k(m)=\frac12\cot^2m,\qquad q(m)=\frac{2\sin m}{m+\sin m\cos m},\qquad
 \varepsilon_*(m)=\frac{\frac12-k(m)}{1-q(m)\cos m},
\]
the **area has a unique global maximizer**. It occurs at the curvature boundary \(\varepsilon=\varepsilon_*(m)\) and the unique point \(m=m_*\in(1.02,1.17)\) satisfying \(F'(m_*)=0\), with \(F\) explicitly defined below. Certified bounds locate the maximum as
\[
1.0783169<m_*<1.0783171,\qquad
0.78884378<\operatorname{area}(R_{m_*,\varepsilon_*(m_*)})<0.78884380,
\]
with \(\varepsilon_*(m_*)\approx0.8043961172\). Every body in this family has minimum width exactly one and is reduced, including at the optimizer where one curvature radius vanishes only at the active-arc endpoints. In particular the construction yields an area lower bound \(0.78884378\) for the general planar reduced-body extremal problem.

## Assumptions and scope
For \(\theta\in[0,2m]\), set \(u_\theta=(\cos\theta,\sin\theta)\), \(v_\theta=(-\sin\theta,\cos\theta)\), and
\[
 r_{m,\varepsilon}(\theta)=k(m)+\varepsilon[1-q(m)\cos(\theta-m)],\quad
 c_{m,\varepsilon}(\theta)=\int_0^\theta r_{m,\varepsilon}(t)v_t\,dt.
\]
The boundary consists of \(a(\theta)=c_{m,\varepsilon}(\theta)+\frac12u_\theta\), \(b(\theta)=c_{m,\varepsilon}(\theta)-\frac12u_\theta\) for \(0\le\theta\le2m\), and the two connecting segments \([a(2m),b(0)]\) and \([b(2m),a(0)]\), oriented as in Kominers' original construction. At \(m=\pi/4,\varepsilon=0\) the lower arc degenerates to a single point (the reduced quarter-disk); that endpoint is included. The upper endpoint \(m=\pi/2\) is excluded.

The theorem optimizes this **specified quadrant only**: the nonnegative amplitude, \(m\ge\pi/4\), and the boundary imposed by requiring the upper curvature radius split to satisfy \(r_{m,\varepsilon}\le1/2\). It does not optimize negative amplitudes, other parameters of the construction, or all reduced planar bodies.

## Proof
**1. Convexity and reducedness throughout the claimed parameter set.** The choice of \(q\) makes \(\int_0^{2m}(r_{m,\varepsilon}-k)v_\theta\,d\theta=0\), so the endpoint closure and two straight edges are independent of \(\varepsilon\). The support-function curvature densities on the active arcs are \(\frac12+r\) and \(\frac12-r\), and each connecting edge has positive length \(\cot m\). For \(m\in[\pi/4,\pi/2)\), the functions satisfy \(1\le q(m)<4/3\) and \(1-q(m)\cos m>0\). The exact interval certificate described below proves \(0\le\varepsilon_*(m)<0.81<1\). As \(\cos(\theta-m)\in[\cos m,1]\), for \(0\le\varepsilon\le\varepsilon_*(m)\),
\[
 r\le k+\varepsilon(1-q\cos m)\le\frac12,\qquad
 r\ge k+\varepsilon(1-q)>-\frac13.
\]
Thus both densities are nonnegative; in the open active arcs they are strictly positive except at the isolated degenerate quarter-disk endpoint, and the gap edge atoms are positive. The support function is convex. Opposite active supports have total width one; the gap width is \(\cos z+\cot m\sin z>1\) for \(0<z<\pi-2m\), as in the original width calculation. Hence thickness is one. Any convex subset of thickness at least one has both opposite active support values unchanged. The unique active support points then belong to that subset; taking closure and convex hull recovers the entire body. The limiting quarter-disk satisfies this argument by its circular arc and its single opposite support point. Every member is therefore reduced.

For completeness, \(m/\sin m+\cos m\) decreases to \(\pi/2\), giving \(q\le4/\pi<4/3\); and \(2\sin m-m-\sin m\cos m\) is increasing and positive from \(m=\pi/4\), giving \(q\ge1\).

**2. Area polynomial and curvature-boundary profile.** Write \(s=\sin m,c=\cos m\) and
\[
 I_0=2m-2sc,\quad I_1=2mc-2s-2s^3,\quad
 I_2=m(s^2-\tfrac14)+\tfrac14sc(1+2s^2).
\]
Kominers' boundary integral, alternatively obtained by integrating \(r(\theta)\int_0^\theta r(t)\sin(\theta-t)dt\), gives
\[
 A(m,\varepsilon)=(k+\varepsilon)^2I_0+(k+\varepsilon)q\varepsilon I_1+q^2\varepsilon^2I_2+\frac m2+\frac{sc}{2}.
\]
In particular
\[
 A=C_0+B\varepsilon+C\varepsilon^2,\qquad
 C_0=k^2I_0+\frac m2+\frac{sc}{2},\quad
 B=k(2I_0+qI_1),\quad C=I_0+qI_1+q^2I_2.
\]
At \(\varepsilon=\varepsilon_*(m)\), define
\[
 \beta(m)=\frac{s^2-c^2}{s(m-sc)},\quad
 J_1(m)=3mc-3s+s^3,\quad
 J_2(m)=m(\tfrac{15}{4}-3s^2)+\tfrac14sc(2s^2-15).
\]
Using \(q\varepsilon_*=\beta\) and \(k+\varepsilon_*=\frac12+c\beta\), expansion and cancellation yield
\[
 F(m):=A(m,\varepsilon_*(m))=m+\beta(m)J_1(m)+\beta(m)^2J_2(m).
\]
This identity also provides a separate numerical consistency check against the unsimplified area integral.

**3. A global, rational interval certificate.** The attached standard-library verifier uses fixed-point rational intervals of scale \(10^{40}\), outward rounding after each operation, and Taylor enclosures for \(\sin\) and \(\cos\) through term \(17\), with the next alternating term bounding the remainder on \([0,2]\). Automatic first and second derivatives are propagated algebraically, and the mean-value theorem bounds each rational subinterval using its midpoint and an enclosing derivative interval. For intervals crossing \(\pi/2\), the enclosure explicitly includes the maximum \(\sin=1\). The cover slightly exceeds the required angular domain: \([0.785398,1.570797]\).

On the first \(1000\) intervals of \([0.785398,1.02]\), it proves
\[
 B>0.01485,\quad B+2C\varepsilon_*>0.01473,\quad F<0.788510.
\]
On the next \(3000\) intervals of \([1.02,1.17]\), it proves
\[
 B>0.02198,\quad B+2C\varepsilon_*>0.00441,\quad F''<-0.13030.
\]
On the last \(10000\) intervals of \([1.17,1.570797]\), it proves
\[
 C<-0.01135,\qquad C_0-\frac{B^2}{4C}<0.788329.
\]
In all three intervals \(0\le\varepsilon_*<0.81\). Thus the derivative \(B+2C\varepsilon\) is positive throughout the feasible \(\varepsilon\)-interval in the first two angular ranges (positivity at both ends suffices because it is affine), so the maximum there lies uniquely at \(\varepsilon=\varepsilon_*\). In the last range, strict negativity of \(C\) bounds the area of **every** amplitude, including feasible amplitudes, by its unconstrained quadratic maximum \(C_0-B^2/(4C)<0.788329\).

The same exact calculation gives \(F'(1.02)>0\), \(F'(1.17)<0\). The strict negativity of \(F''\) on the middle interval therefore gives a unique zero \(m_*\), necessarily its unique maximum. The direct rational enclosure \(F(1.07831698)>0.78884378\) strictly exceeds the upper bounds in both other angular ranges, proving global optimality and uniqueness. Finally the verifier establishes \(F'(1.0783169)>0\), \(F'(1.0783171)<0\) and \(F(1.07831698)<0.78884380\). Since \(F\) is strictly concave in the middle interval, its maximal value differs from this nearby sample by far less than \(10^{-8}\), as additionally certified using the derivative enclosures and the root bracket. Hence the stated strict area interval follows.

## Verification
Extract `verify.py` and execute `python verify.py` with Python 3. The output is `VERIFY_OK`, after 14000 rigorous interval checks, sign tests, and an auxiliary independent numerical evaluation of the source's area integral. The exhaustive interval proof is over the **continuous two-parameter domain** via interval enclosures, not over sampled bodies. The code has no third-party dependencies. For reference, high-precision noncertifying evaluation gives \(m_*\approx1.0783169768421266176\), \(\varepsilon_*(m_*)\approx0.8043961172477684864\), and \(A_*\approx0.7888437886265518067\). The interval and analytic arguments, not the decimals, establish the theorem.

## Relationship to prior work
Kominers (arXiv:2606.28612v1, June 26, 2026) defines this support-function family, establishes the source construction at \(m=15/16,\varepsilon=13/20\) and its area \(0.7862156027\ldots\), and observes that its choice of parameters need not optimize area. The published result **"Exact area optimizer on the fixed-angle blunted quarter-disk slice"** subsequently establishes the best area \(0.7871835267\ldots\) at fixed \(m=15/16\), explicitly leaving varying \(m\) outside its scope. The present theorem optimizes both \(m\) and the admissible nonnegative \(\varepsilon\) over the stated domain, gives the unique maximizing angle, and improves both previously displayed concrete lower bounds. It does not derive the unrestricted sharp area of a reduced planar body.

## Limitations
No claim is made about the full two-parameter construction with negative perturbations, the excluded angular range, other support-function deformations, or the global supremum over all reduced bodies. The area optimizer sits at a boundary where a curvature radius vanishes at two isolated arc endpoints; the contact-point argument establishes reducedness there. Originality is subject to possible unindexed earlier optimizations or equivalent parameterizations.

## References
1. S. D. Kominers, *A reduced planar body with area greater than \(\pi\Delta^2/4\)*, arXiv:2606.28612v1 (2026), https://arxiv.org/html/2606.28612v1.
2. *Exact area optimizer on the fixed-angle blunted quarter-disk slice* (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-area-optimizer-on-the-fixed-angle-blunted-quarter-disk-sli--369c8e768fcb.
3. M. Lassak and H. Martini, *Reduced convex bodies in Euclidean space—a survey*, Expositiones Mathematicae 29 (2011), 204–219.
