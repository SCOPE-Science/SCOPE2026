# Sharp covariance anisotropy law for symmetric Euclidean ball lenses

## Finding
Fix an integer \(n\ge2\). For \(0\le a<1\), let
\[
L_{n,a}=\{x\in\mathbb R^n:\|x-ae_1\|_2\le1,\ \|x+ae_1\|_2\le1\}
\]
and let \(X\) be distributed uniformly by \(n\)-dimensional Lebesgue measure on \(L_{n,a}\). Symmetry gives \(\mathbb EX=0\) and
\[
\operatorname{Cov}(X)=\operatorname{diag}(\sigma_\parallel^2,\sigma_\perp^2,\ldots,\sigma_\perp^2).
\]
The eigenvalue \(\sigma_\parallel^2\) is in the line joining the ball centers, and \(\sigma_\perp^2\) is in every perpendicular direction. Define \(k=(n-1)/2\), \(\delta=1-a\), and
\[
B_j(a)=\int_0^1s^j(1-s)^k(1+a+\delta s)^k\,ds\quad(j=0,1,2).
\]
Then the exact eigenvalues are
\[
\boxed{\sigma_\parallel^2=\delta^2\frac{B_2}{B_0},\qquad
\sigma_\perp^2=\delta^2\frac{B_2}{B_0}+a\delta\frac{B_1}{B_0}.}
\]
In particular, the exact moment identity
\[
\boxed{\sigma_\perp^2-\sigma_\parallel^2=a\,\mathbb E|X_1|}
\]
holds (unit generating-ball radius). For \(0<a<1\), this gap is strictly positive.

The **covariance anisotropy ratio**
\[
\mathcal A_n(a)=\frac{\sigma_\perp^2}{\sigma_\parallel^2}
=1+\frac a{1-a}\frac{B_1(a)}{B_2(a)}
\]
is a continuous, strictly increasing bijection from \([0,1)\) onto \([1,\infty)\). The rescaled excess \((1-a)(\mathcal A_n(a)-1)/a=B_1/B_2\) is itself strictly increasing on \((0,1)\), with **sharp endpoint constants**
\[
\boxed{c_n=\frac{\Gamma((n+4)/2)}{\Gamma(3/2)\Gamma((n+3)/2)},\qquad
C_n=\frac{n+5}{4}.}
\]
Consequently, every \(0<a<1\) satisfies the strict sharp two-sided envelopes
\[
\boxed{1+c_n\frac a{1-a}<\mathcal A_n(a)<1+C_n\frac a{1-a}.}
\]
The constants cannot respectively be increased or decreased because the rescaled ratio tends to \(c_n\) as \(a\downarrow0\) and to \(C_n\) as \(a\uparrow1\).

At the thin-lens endpoint \(\delta=1-a\downarrow0\), the two eigenvalues have different exact leading scales:
\[
\boxed{\sigma_\parallel^2\sim\frac{8\delta^2}{(n+3)(n+5)},\qquad
\sigma_\perp^2\sim\frac{2\delta}{n+3},\qquad
\mathcal A_n(a)\sim\frac{n+5}{4\delta}.}
\]
In dimension \(n=3\), all eigenvalues are rational:
\[
\boxed{\sigma_\parallel^2=\frac{(1-a)^2(4+a)}{10(2+a)},\quad
\sigma_\perp^2=\frac{(1-a)(8+9a+3a^2)}{20(2+a)},\quad
\mathcal A_3(a)=1+\frac{5a(3+a)}{2(1-a)(4+a)}.}
\]

## Assumptions and scope
All balls are closed Euclidean unit balls in \(\mathbb R^n\), and uniform measure means normalized full-dimensional volume. The parameter range \(0\le a<1\) ensures nonempty interior; \(a=1\) is the collapsed-point limit, not a probability measure with full-dimensional density. For radius \(R>0\), dilating the displayed lens by \(R\) multiplies both covariance eigenvalues by \(R^2\) and leaves \(\mathcal A_n\) unchanged. The center separation equals \(2aR\); the theorem is not about physical optical refraction or the unnormalized mechanical inertia tensor.

The anisotropy ratio \(\mathcal A_n(a)\) is a natural dimensionless measure of the eccentricity of the uniform-volume covariance ellipsoid. Its bijectivity implies that, for known dimension and generating-ball radius, a measured anisotropy uniquely identifies center separation within this family.

## Proof
**1. Geometric slices and normalization.** Write \(x=(t,z)\in\mathbb R\times\mathbb R^{n-1}\). Membership in the two unit balls is equivalent to
\[
|t|\le\delta,\qquad \|z\|_2^2\le1-(a+|t|)^2.
\]
For \(0\le t\le\delta\), set \(w(t)=[1-(a+t)^2]^k\). The cross-section is an \((n-1)\)-ball, so its volume is a fixed dimensional constant times \(w(t)\). Its uniform coordinate variance along any perpendicular axis is \([1-(a+t)^2]/(n+1)\). Reflection and rotational symmetry prove that off-diagonal covariances vanish and that
\[
\sigma_\parallel^2=\frac{\int_0^\delta t^2w(t)\,dt}{\int_0^\delta w(t)\,dt},\qquad
\sigma_\perp^2=\frac1{n+1}\frac{\int_0^\delta[1-(a+t)^2]w(t)\,dt}{\int_0^\delta w(t)\,dt}.
\]
These formulas include \(a=0\), which is the unit ball and has both eigenvalues \(1/(n+2)\).

**2. Exact cancellation.** Since \(2(k+1)=n+1\), differentiation yields
\[
\frac{d}{dt}[1-(a+t)^2]^{k+1}
=-(n+1)(a+t)w(t).
\]
Integrate by parts against \(t\) on \([0,\delta]\). Both boundary terms vanish: \(t=0\) at the left endpoint, and \(1-(a+t)^2=0\) at the right. Therefore
\[
\frac1{n+1}\int_0^\delta[1-(a+t)^2]^{k+1}\,dt
=\int_0^\delta t(a+t)w(t)\,dt.
\]
Subtracting the axial second moment gives
\[
\sigma_\perp^2-\sigma_\parallel^2
=a\frac{\int_0^\delta t w(t)\,dt}{\int_0^\delta w(t)\,dt}
=a\mathbb E|X_1|.
\]
Now set \(t=\delta s\); the identity
\[
1-(a+\delta s)^2=\delta(1-s)(1+a+\delta s)
\]
gives the formulas in the Finding section and \(\mathcal A_n=1+aB_1/(\delta B_2)\).

**3. Strict rescaled monotonicity.** For \(0\le a<1\) define
\[
f_a(s)=(1-s)^k(1+a+(1-a)s)^k\quad(0<s<1).
\]
The probability measure \(d\nu_a(s)=s f_a(s)ds/B_1(a)\) has mean \(B_2(a)/B_1(a)\). Differentiation of the density in \(a\) gives
\[
g_a(s)=\partial_a\log f_a(s)
=\frac{k(1-s)}{1+a+(1-a)s},\qquad
\partial_sg_a(s)=-\frac{2k}{[1+a+(1-a)s]^2}<0.
\]
Differentiation under the integral is justified on every compact subinterval of \([0,1)\) because all weights are bounded and continuously dependent on \(a\). Hence
\[
\frac{d}{da}\frac{B_2}{B_1}
=\operatorname{Cov}_{\nu_a}(s,g_a(s))<0.
\]
Strictness follows from the identity
\[
2\operatorname{Cov}_{\nu_a}(s,g_a(s))=
\int\!\!\int(s-t)[g_a(s)-g_a(t)]\,d\nu_a(s)d\nu_a(t)<0,
\]
because \(\nu_a\) has a positive density on \((0,1)\) and \(g_a\) strictly decreases. Thus \(B_1/B_2\) strictly increases, and multiplication by the strictly increasing positive factor \(a/(1-a)\) makes \(\mathcal A_n\) strictly increasing on \((0,1)\).

**4. Sharp endpoints.** At \(a=0\), \(f_0(s)=(1-s^2)^k\). Substitution \(u=s^2\) gives
\[
B_1(0)=\frac1{2(k+1)},\qquad
B_2(0)=\frac12\mathrm B(3/2,k+1),
\]
so \(B_1(0)/B_2(0)=c_n\). At \(a=1\), understood only as a limit of the integrals \(B_j\), the weight tends uniformly to \(2^k(1-s)^k\); beta integration yields \(B_1(1)/B_2(1)=(k+3)/2=C_n\). All moments are positive, so dominated convergence and the preceding strict monotonicity yield \(c_n<B_1(a)/B_2(a)<C_n\) for \(0<a<1\). The ratio \(\mathcal A_n(a)\) is continuous, equals \(1\) at \(a=0\), and diverges to infinity as \(a\uparrow1\), proving the bijection and optimality of both envelopes.

**5. Thin-lens limits and dimension three.** The same beta integrals give, as \(a\uparrow1\),
\[
\frac{B_1}{B_0}\longrightarrow\frac1{k+2},\qquad
\frac{B_2}{B_0}\longrightarrow\frac2{(k+2)(k+3)}.
\]
Substitute these in the eigenvalue formulas to obtain the three displayed asymptotic equivalents. If \(n=3\), then \(k=1\) and
\[
f_a(s)=(1+a)-2as-(1-a)s^2.
\]
Direct integration gives \(B_0=(2+a)/3\), \(B_1=(3+a)/12\), and \(B_2=(4+a)/30\), proving the exact rational specialization. No numerics or finite enumeration are needed for any dimension.

## Verification
Run `python verify.py` after installing `mpmath>=1.3.0`. The included checker independently integrates the perpendicular cross-sectional second moment, checks the exact integration-by-parts identity and the strict-size-bias covariance sign across dimensions and separations, verifies the sharp endpoints, derives the dimension-three polynomial moments using exact rational arithmetic, and checks thin-lens asymptotic normalizations. In the supplied execution, **412 checks passed**. The proof is the analytic argument above; the finite checks are not a substitute for its universally quantified conclusions.

## Relationship to prior work
Drach, Solanes, and Tatarko (2026) study reverse isoperimetric extremality of \(\lambda\)-convex lenses in three-dimensional space forms, with the corresponding Euclidean result as background. Drach and Tatarko (2025) study all-dimensional extremality of lens mean width and intrinsic volumes. The works motivate lens geometry, but their inspected results do not supply the uniform-volume covariance eigenvalue identity or its all-dimensional strict monotonicity.

Finch (2013, Section 1) gives volume, area, and mean-width formulas for intersections of two congruent spheres and discusses arbitrary-dimensional volume and area. Explicit lens moment-of-inertia calculations in three dimensions may also be extracted from classical spherical-cap identities; the rational dimension-three eigenvalues alone are **not** asserted to be historically novel. An earlier public mathematical calculation of symmetric-lens mean width in every dimension provides a different valuation and does not logically imply the covariance anisotropy law. The proposed contribution is the unified *all-dimensional* exact covariance gap, strict monotonicity, sharp two-sided envelopes and thin-lens rates.

## Limitations
The findings apply only to *two congruent* Euclidean balls, their equal-density intersection, and ordinary Lebesgue covariance. They do not establish extremality of covariance among all \(\lambda\)-convex bodies, anisotropy laws for unequal balls or nonuniform densities, or analogous statements in curved model spaces. The sharp inequalities control a dimensionless ratio, not the individual eigenvalues at fixed volume. The exact historical priority of the all-dimensional monotonicity law remains provisional; classical physical-inertia and cap-integral literature may contain an equivalent result under different notation. Independent validation has not been performed.

## References
1. K. Drach, G. Solanes, and K. Tatarko, *A reverse isoperimetric inequality in three-dimensional space forms*, arXiv:2603.08132v1, first publicly posted 2026-03-09, Sections 1–2.
2. K. Drach and K. Tatarko, *A solution to Bezdek's conjecture*, arXiv:2511.11901v1, first publicly posted 2025-11-14, Sections 1–2.
3. S. R. Finch, *Mutually Equidistant Spheres that Intersect*, arXiv:1301.5515v1, 2013, Section 1.
4. *Mean width of a symmetric lens in every dimension*, public mathematical record dated 2026-10-04, identifier `80ec085cfff6` (comparison of the distinct mean-width invariant).
