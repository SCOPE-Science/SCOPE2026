# Sharp two-orientation maximum central sections of circular double cones

## Finding
For every equatorial radius \(r>0\) and half-height \(h>0\), consider the solid circular double cone
\[
K_{r,h}=\left\{(x,y,z)\in\mathbb R^3:\frac{\sqrt{x^2+y^2}}r+\frac{|z|}h\le1\right\}.
\]
For every two-dimensional linear plane \(H\subset\mathbb R^3\), let \(A(H)=\operatorname{area}_2(K_{r,h}\cap H)\) denote intrinsic Euclidean section area. Then
\[
\boxed{\max_{\dim H=2}A(H)=\max\{\pi r^2,\,2rh\}.}
\]
The complete equality classification has exactly one sharp aspect-ratio threshold:

* If \(h/r<\pi/2\), the unique maximizing plane is \(z=0\).
* If \(h/r>\pi/2\), precisely the planes containing the \(z\)-axis maximize.
* If \(h/r=\pi/2\), both of those classes, and **no other plane**, maximize.

In particular, no genuinely oblique central section ever maximizes. A strengthened, sharp auxiliary inequality for all \(a>0\) is
\[
\boxed{\;I(a):=2\int_0^{\pi/2}\frac{d\theta}{(1+a\cos\theta)^2}
<\frac{\pi}{\sqrt{1+\pi^2a^2/4}}.\;}
\]
The comparison is sharp in the limiting senses \(a\downarrow0\) and \(a\to\infty\), and its strictness supplies every non-endpoint equality exclusion.

## Assumptions and scope
The set \(K_{r,h}\) is **solid**, compact, centrally symmetric and convex: the convex hull of the radius-\(r\) disk in the plane \(z=0\) and the two opposite axial vertices \((0,0,\pm h)\). Its equatorial diameter is \(2r\), and the full axial height is \(2h\). Sections are **linear planes through the center**, with intrinsic (not projected) area. Rotational symmetry permits each nonvertical section to be expressed as the graph \(z=kx\) after rotating the \(x,y\) coordinates. A plane containing the axis is the limiting vertical meridional case. The theorem does not concern noncentral affine planes, single cones, unequal half-heights or higher-dimensional section maxima.

## Proof
**Exact area profile.** Rotate about the axis and, for a nonvertical plane, write \(z=kx\) with \(k\ge0\). Its induced Euclidean area element is \(\sqrt{1+k^2}\,dx\,dy\). Polar coordinates in the \(x,y\)-domain give the radial cutoff
\[
\rho(\theta)=\frac r{1+(kr/h)|\cos\theta|}.
\]
Set \(a=kr/h\). Integrating the area element, using fourfold symmetry, yields the exact full one-variable central-section profile
\[
\boxed{A(k)=r^2\sqrt{1+(ha/r)^2}\,I(a),\qquad
I(a)=2\int_0^{\pi/2}(1+a\cos\theta)^{-2}\,d\theta.}
\]
At \(a=0\), the equatorial disk area is \(\pi r^2\). For a vertical meridional plane the inequalities reduce to a planar diamond \(\frac{|y|}r+\frac{|z|}h\le1\), whose area is \(2rh\). Equivalently \(aI(a)\to2\) as \(a\to\infty\), as follows from the integral transformation below and dominated convergence. Thus the two candidate extremes have precisely the areas claimed.

**First strict comparison.** Put \(s=\tan\theta\). A change of variables gives, for every \(a>0\),
\[
I(a)=2\int_0^\infty\frac{ds}{(a+\sqrt{1+s^2})^2}.
\]
Since \(a>0\) and \(\sqrt{1+s^2}>s\), we have
\(\big(a+\sqrt{1+s^2}\big)^2>1+(a+s)^2\), hence
\[
\boxed{I(a)<2\int_0^\infty\frac{ds}{1+(a+s)^2}
=2\arctan(1/a).}
\]
Every inequality is strict for finite \(a>0\).

**Second strict comparison.** We prove for \(0<\phi<\pi/2\)
\[
2\phi<\frac\pi{\sqrt{1+(\frac\pi2\cot\phi)^2}}.
\]
Write \(u=2\phi/\pi\in(0,1)\). This is equivalent to
\(\tan(\pi u/2)/(\pi u/2)>(1-u^2)^{-1/2}\). The classical cosine-product partial fraction identity, obtained by logarithmic differentiation of the uniformly convergent Euler product, is
\[
\frac{\tan(\pi u/2)}{\pi u/2}
=\frac8{\pi^2}\sum_{m=0}^\infty\frac1{(2m+1)^2-u^2}
=1+\sum_{j=1}^\infty c_j u^{2j},
\quad c_j=\frac8{\pi^2}\sum_{m=0}^\infty (2m+1)^{-2j-2}.
\]
For every \(j\ge1\), \(c_j\ge8/\pi^2>1/2\) (since \(\pi^2<16\)). The binomial expansion
\[
(1-u^2)^{-1/2}=1+\sum_{j=1}^\infty b_j u^{2j},
\qquad b_j=\binom{2j}{j}4^{-j}\le\frac12
\]
has \(b_1=1/2\) and \(b_j\) strictly decreasing. Positivity and termwise comparison of the absolutely convergent expansions prove strictness on \(0<u<1\). Substitute \(\phi=\arctan(1/a)\), so \(\cot\phi=a\), and combine with the first comparison to obtain
\[
\boxed{I(a)<2\arctan(1/a)<\frac\pi{\sqrt{1+\pi^2a^2/4}},\quad a>0.}
\]

**Global bound and rigidity.** For \(0<a<\infty\), the area therefore satisfies the strict estimate
\[
A(k)<\pi r^2
\sqrt{\frac{1+(h/r)^2a^2}{1+\pi^2a^2/4}}.
\]
If \(h/r\le\pi/2\), the square-root ratio is at most one, so \(A(k)<\pi r^2\). If \(h/r\ge\pi/2\), the same expression is at most \(2rh\), because
\[
\pi^2\big(1+(h/r)^2a^2\big)
\le 4(h/r)^2\big(1+\pi^2a^2/4\big)
\quad\Longleftrightarrow\quad \pi^2\le4(h/r)^2.
\]
Thus every genuinely oblique plane is strictly worse than the larger of the two explicit endpoint areas. Comparing \(\pi r^2\) with \(2rh\) gives the exact crossover \(h/r=\pi/2\) and all equality cases. This exhausts all central planes by rotational symmetry.

For completeness, an elementary closed form for the directional integral is
\[
I(a)=\begin{cases}
2\left(\dfrac{\arccos a}{(1-a^2)^{3/2}}-\dfrac{a}{1-a^2}\right),&0\le a<1,\\[3pt]
\frac43,&a=1,\\[3pt]
2\left(\dfrac{a}{a^2-1}-\dfrac{\operatorname{arccosh}a}{(a^2-1)^{3/2}}\right),&a>1.
\end{cases}
\]
These expressions follow by elementary integration of the displayed \(I(a)\); the proof of the maximum does not depend on their numerically unstable near-\(1\) subtraction forms.

## Verification
The bundled standard-library program `check_bicone.py` independently evaluates the full integral by polar and planar-chord quadrature, cross-checks the elementary forms on representative parameters, probes \(6500\) combinations of aspect ratios and genuinely oblique orientations, and checks both endpoint areas. Execute `python3 check_bicone.py` with Python 3. It prints `BICONE_ALL_CHECKS_OK` on success. The partial-fraction comparison and resulting global assertion are symbolic continuum arguments above; no finite sampling is presented as a proof of infinitely many directions or parameter values.

## Relationship to prior work
Alfonseca and Kim [1, Sections 1 and 3] identify circular double cones as model symmetric bodies of revolution, write their intersection-body transform and analyze local equatorial convexity. Their formulas concern intersection-body regularity rather than a complete global maximum central-section area/equality classification. Saroglou [2, Theorem 1.4] identifies circular double cones as equality bodies for a **different**, second-projection-body inequality, and [2, Section 5] studies an integrated section-root functional; neither statement forces the sharp maximum intrinsic area for all central planes. The closely related published analysis *Bisector sections of affine double cones and a strict section-root gap* [3] calculates a tilted fixed-direction beta-function profile for a section-root integral and explicitly does not determine the maximizing direction of that other functional; the present theorem instead optimizes raw planar area over every central direction for every Euclidean aspect ratio. Neither assertion follows from the other merely by changing parameters. Basic formulas for volume and lateral surface area of a bicone also do not imply a central-section optimizer classification.

## Limitations
The result is restricted to centrally symmetric **circular** three-dimensional double cones, central affine-free plane sections, and Euclidean section area. It does not establish an analogous law for ellipsoidal double cones in the *same* Euclidean metric, unequal upper/lower cone heights, general off-center sections or higher dimensions. Exact publication priority is provisional: an older equivalent cone-section calculation outside the inspected primary materials could exist. The published bisector analysis optimizes a different functional and should not be conflated with the assertion here. No independent mathematical audit has yet been performed.

## References
[1] M. A. Alfonseca and J. Kim, *On the local convexity of intersection bodies of revolution*, arXiv:1304.3359, first submitted 2013-04-11, Sections 1–3. https://arxiv.org/html/1304.3359v1

[2] C. Saroglou, *On the shape of a convex body with respect to its second projection body*, arXiv:1409.4347, first submitted 2014-09-15, Theorems 1.4–1.5 and Section 5. https://arxiv.org/html/1409.4347v2

[3] *Bisector sections of affine double cones and a strict section-root gap*, public research record, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-bisector-sections-of-affine-double-cones-and-a-strict-section-ro--f83ae948e0d8
