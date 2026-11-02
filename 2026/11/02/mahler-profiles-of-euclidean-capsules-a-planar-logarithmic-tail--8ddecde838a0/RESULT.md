# Mahler profiles of Euclidean capsules: a planar logarithmic tail and a Gaussian dimension crossover

## Finding

For an integer \(d\ge 2\) and a real parameter \(s\ge0\), define the Euclidean capsule
\[
K_{d,s}=B_2^d+[-s,s]e_1\subset\mathbb R^d,
\]
where \(B_2^d\) is the closed unit Euclidean ball and \(e_1\) is a unit coordinate vector. Let \(K^\circ=\{y:\langle x,y\rangle\le1\text{ for every }x\in K\}\), and set \(P_d(s)=\operatorname{vol}_d(K_{d,s})\operatorname{vol}_d(K_{d,s}^\circ)\). Write
\[
\kappa_d=\frac{\pi^{d/2}}{\Gamma(1+d/2)},\qquad
m_d=\frac{2\kappa_{d-1}}{d\kappa_d},\qquad
c_d=(d-1)m_d.
\]
The following **combined quantitative profile** holds in every dimension. Its strict-monotonicity component is compatible with, and may also follow from, classical general shadow-system inequalities; no general monotonicity principle is asserted to be new.

**Exact profile and inversion.** For all \(s\ge0\),
\[
\boxed{P_d(s)=\kappa_d^2(1+d m_d s)c_d
\int_0^1\frac{(1-u^2)^{(d-3)/2}}{(1+s u)^d}\,du.}
\]
The function \(P_d\) is strictly decreasing on \((0,\infty)\), from \(P_d(0)=\kappa_d^2\) to the unattained limit
\[
\boxed{L_d=\frac{4\kappa_{d-1}^2}{d}=\kappa_d^2d m_d^2.}
\]
It therefore gives a unique inverse aspect ratio \(s\) for every product in \((L_d,\kappa_d^2]\).

**Sharp small-aspect behavior.** As \(s\downarrow0\),
\[
\frac{P_d(s)}{\kappa_d^2}=1-\alpha_d s^2+\frac{d(d-1)m_d}{6}s^3+O_d(s^4),
\qquad \boxed{\alpha_d=d^2m_d^2-\frac{d+1}{2}>0.}
\]
Consequently the inverse at the ball endpoint has exactly square-root rather than Lipschitz stability.

**Dimension-dependent long-capsule tail.** In dimension two, for \(s>1\),
\[
\boxed{P_2(s)=(2\pi+8s)
\left(\frac{s}{s^2-1}-\frac{\operatorname{arcosh}s}{(s^2-1)^{3/2}}\right),}
\]
and as \(s\to\infty\),
\[
\boxed{P_2(s)=8+\frac{2\pi}{s}+\frac{8[1-\log(2s)]}{s^2}
+O\!\left(\frac{\log s}{s^3}\right).}
\]
For every fixed integer \(d\ge3\), by contrast,
\[
\boxed{P_d(s)=L_d+\frac{\kappa_d^2m_d}{s}
-\frac{L_d}{(d-2)s^2}+o_d(s^{-2}).}
\]
Thus the second-order logarithmic term is confined to planar capsules.

**Gaussian dimension crossover.** Put \(\mu=\sqrt{2/\pi}\). For every fixed \(\tau\ge0\),
\[
\boxed{\lim_{d\to\infty}\frac{P_d(\tau/\sqrt d)}{\kappa_d^2}
=(1+\mu\tau)e^{\tau^2/2}\operatorname{erfc}(\tau/\sqrt2)=:H(\tau).}
\]
The continuous function \(H\) decreases strictly from \(H(0)=1\) to \(\lim_{\tau\to\infty}H(\tau)=2/\pi\). For every **fixed** \(s>0\), however,
\[
\lim_{d\to\infty}P_d(s)/\kappa_d^2=2/\pi,
\]
while \(P_d(0)/\kappa_d^2=1\). The high-dimensional and zero-aspect limits therefore do not commute; the distinguished transition scale is \(s=\tau/\sqrt d\).

## Assumptions and scope

All volumes are ordinary \(d\)-dimensional Lebesgue measures, not Gaussian-weighted volumes. The capsule is an origin-symmetric convex body, so the origin is its Santaló point. The dimension is an integer at least two. Its ball radius is normalized to one; replacing it by any positive radius simply makes \(s\) the segment half-length divided by the radius. The polar uses the standard Euclidean inner product. All stated limits in \(s\) hold with \(d\) fixed unless the high-dimensional parameter is explicitly specified; high-dimensional convergence is pointwise in the indicated fixed parameter. The inverse assertion uses exact population volume products, not noisy empirical estimates.

## Proof

**(1) Exact volumes.** The capsule consists of a circular cylinder of axial length \(2s\), whose transverse section is \(B_2^{d-1}\), capped by two hemispheres of total volume \(\kappa_d\). Therefore
\[
\operatorname{vol}_d(K_{d,s})=\kappa_d+2s\kappa_{d-1}=\kappa_d(1+d m_ds).
\]
The support function of the Minkowski sum is \(h_{K_{d,s}}(\theta)=1+s|\theta_1|\) for every unit vector \(\theta\). Its polar has radial function \(1/(1+s|\theta_1|)\). By polar integration,
\[
\operatorname{vol}_d(K_{d,s}^\circ)=\kappa_d\,\mathbb E(1+sU)^{-d},
\]
where \(U=|\Theta_1|\) and \(\Theta\) is uniform on the unit sphere. The density of \(U\), for \(0<u<1\), is
\[
f_d(u)=c_d(1-u^2)^{(d-3)/2},\qquad
c_d=\frac{2\Gamma(d/2)}{\sqrt\pi\Gamma((d-1)/2)}=(d-1)m_d.
\]
In particular \(\mathbb E U=m_d\), \(\mathbb E U^2=1/d\), and \(\mathbb E U^3=2m_d/(d+1)\). The exact integral follows.

**(2) Strict decrease.** For each \(s\ge0\), abbreviate
\[
A_s=\mathbb E(1+sU)^{-d-1},\quad
B_s=\mathbb E[U(1+sU)^{-d-1}],\quad
C_s=\mathbb E[U^2(1+sU)^{-d-1}].
\]
Integrating the derivative of \(u(1-u^2)^{(d-1)/2}(1+su)^{-d}\) from zero to one, whose endpoint terms vanish even for \(d=2\), yields
\[
A_s-(d-1)s B_s=d C_s.
\]
Because \(\mathbb E(1+sU)^{-d}=A_s+s B_s\), differentiation gives
\[
\frac{P_d'(s)}{d\kappa_d^2}=d m_d C_s-B_s.
\]
The ratio \(C_s/B_s\) is the mean of \(u\) under the probability law with density proportional to \(u f_d(u)(1+s u)^{-d-1}\). This mean is strictly decreasing in \(s\): its derivative is
\[
-(d+1)\operatorname{Cov}_{\nu_s}
\left(U,\frac{U}{1+sU}\right)<0,
\]
since both arguments are strictly increasing and the law is nondegenerate. At \(s=0\), \(C_0/B_0=1/(d m_d)\), so \(P_d'(s)<0\) whenever \(s>0\). The limits at both ends are computed below, proving the range and uniqueness of the inverse.

**(3) Ball-end expansion and sharpness.** Taylor-expand the absolutely convergent expectation at \(s=0\), using the three displayed moments of \(U\), and multiply by \(1+d m_ds\). This gives the asserted quadratic and cubic coefficients. More quantitatively, let \(\nu_0\) be the size-biased distribution with density \(u f_d(u)/m_d\). Then
\[
2\alpha_d=d^2(d+1)m_d^2\operatorname{Var}_{\nu_0}(U)>0,
\]
which proves strict positivity without relying on a numerical estimate. Therefore \(\kappa_d^2-P_d(s)\sim\kappa_d^2\alpha_d s^2\) and the inverse has optimal Hölder exponent \(1/2\) at the ball; no larger exponent is possible there.

**(4) Long-capsule expansions.** Let \(F_d(s)=\mathbb E(1+sU)^{-d}\). For \(d\ge4\), the substitution \(v=su\), the expansion
\[
(1-u^2)^{(d-3)/2}=1-\frac{d-3}{2}u^2+o(u^2)
\]
and the integrability of \(v^2(1+v)^{-d}\) give, by dominated convergence with the stated second-order subtraction,
\[
F_d(s)=\frac{m_d}{s}-\frac{m_d}{(d-2)s^3}+o_d(s^{-3}).
\]
Here the beta integrals are \(\int_0^\infty(1+v)^{-d}dv=1/(d-1)\) and \(\int_0^\infty v^2(1+v)^{-d}dv=2/[(d-1)(d-2)(d-3)]\). For \(d=3\), the density is identically one and direct integration instead gives \(F_3(s)=(s+2)/[2(1+s)^2]\), with the same expansion. Multiplication by \(\kappa_d^2(1+d m_ds)\) proves the \(d\ge3\) expression and the limit \(L_d\).

When \(d=2\), angular integration yields
\[
P_2(s)=(2\pi+8s)\int_0^{\pi/2}(1+s\cos\theta)^{-2}\,d\theta.
\]
For \(s>1\), first evaluate the elementary auxiliary integral \(\int_0^{\pi/2}(1+s\cos\theta)^{-1}d\theta=\operatorname{arcosh}(s)/\sqrt{s^2-1}\); differentiating its product with \(s\) yields the stated exact expression for the squared denominator. The expansions \(\operatorname{arcosh}(s)=\log(2s)+O(s^{-2})\) and \((1-s^{-2})^{-q}=1+q s^{-2}+O(s^{-4})\) prove the planar logarithmic tail. In particular, the displayed second-order term cannot be replaced by a finite constant times \(s^{-2}\).

**(5) High-dimensional crossover.** By the standard spherical-coordinate density above and the gamma-ratio asymptotic, \(\sqrt d\,m_d\to\mu\), while \(\sqrt d\,U\) converges in distribution to \(|Z|\), for \(Z\sim N(0,1)\). For fixed \(\tau\ge0\), the bounded functions \((1+\tau\sqrt d\,U/d)^{-d}\) converge, jointly in distribution and by bounded expectation convergence, to \(e^{-\tau |Z|}\). It follows that
\[
\lim_{d\to\infty}F_d(\tau/\sqrt d)
=\mathbb E e^{-\tau|Z|}
=e^{\tau^2/2}\operatorname{erfc}(\tau/\sqrt2).
\]
Multiplication by \(1+\tau\sqrt d\,m_d\) proves the crossover. It is nonincreasing as a pointwise limit of the strictly decreasing finite-dimensional profiles. It is real analytic and nonconstant on \((0,\infty)\), so it cannot be constant on any subinterval; hence it is strictly decreasing. Its endpoint values follow from the half-normal Laplace integral, whose leading tail is \(\mu/\tau\).

Finally, for fixed \(s>0\), put \(v=du\) in the expectation:
\[
F_d(s)=\frac{c_d}{d}\int_0^d
\left(1-\frac{v^2}{d^2}\right)^{(d-3)/2}
\left(1+\frac{s v}{d}\right)^{-d}dv.
\]
For \(d\ge3\), the integrand is bounded by the integrable envelope \(e^{-sv/(1+s)}\), extended as zero for \(v>d\), and tends pointwise to \(e^{-sv}\). Dominated convergence gives \(F_d(s)\sim c_d/(ds)\). Consequently \((1+d m_ds)F_d(s)\to\mu^2=2/\pi\), as claimed. The distinct value at \(s=0\) proves the noncommuting limits.

## Verification

The companion program `verification/check_capsules.py` implements independent symbolic identities in dimension three and numerical quadrature of the exact angular formula in dimensions two through fourteen. It also checks the planar inverse-hyperbolic identity and logarithmic tail, the higher-dimensional second-order tails, the Gaussian crossover at dimension four hundred, and the fixed-aspect limit at dimension one thousand. It reports `ALL_CHECKS_PASSED` when the consistency tests succeed. Python packages are stated in `verification/requirements.txt`. The finite tests are neither an exhaustive verification of all dimensions nor substitutes for the analytic arguments in this proof.

## Relationship to prior work

The volume product, its Santaló normalization, the Blaschke–Santaló upper bound, and general shadow-system convexity are classical. In particular, Campi–Gronchi (2006) and Meyer–Reisner (2006) prove broad convexity properties of inverse polar volumes along shadow systems, and Fradelizi–Meyer–Zvavitch (2023) survey those results. Nothing here claims a new general monotonicity principle. The present result is a **particular exact all-dimensional capsule profile**, with quantified second-order large-aspect behavior (including the special planar logarithm), sharp ball-end inverse conditioning, and the explicit half-normal crossover/noncommuting high-dimensional limits. The inspected sources did not state or imply these exact quantitative terms as written. Earlier specialized calculations of spherocylinders under alternative names may exist; historical priority of the combined profile is therefore provisional.

## Limitations

The theorem concerns Minkowski sums of a Euclidean ball and a single centered segment, in integral dimensions at least two. It does not cover general convex cylinders, ellipsoidal caps with arbitrary orientations, multiple segments, or Gaussian-weighted polar products. The strict monotonicity and first-order asymptotics alone should not be interpreted as newly discovered facts independent of classical inequalities. The crossover is pointwise, not a uniform error bound over diverging aspect parameters. No finite-sample estimation guarantee is proved, and independent historical-priority review has not occurred.

## References

1. M. Fradelizi, M. Meyer and A. Zvavitch, *Volume Product* (first public arXiv submission 2023-01-15), arXiv:2301.06131, https://arxiv.org/abs/2301.06131.
2. M. Meyer and S. Reisner, *Shadow systems and volume of polar convex bodies* (arXiv first submitted 2006-06-13), arXiv:math/0606305, https://arxiv.org/abs/math/0606305, and *Mathematika* **53** (2006), 129–148.
3. S. Campi and P. Gronchi, *On volume product inequalities for convex sets*, *Proceedings of the American Mathematical Society* **134** (2006), 2393–2402. DOI:10.1090/S0002-9939-06-08241-4.
4. M. Meyer and S. Reisner, *Ellipsoids are the only local maximizers of the volume product* (2018-12-30), arXiv:1812.11607, https://arxiv.org/abs/1812.11607.
5. H. Yan, work on a special case of the Mahler volume in \(\mathbb R^3\), *Journal of Inequalities and Applications* **2012**, article 3, DOI:10.1186/1029-242X-2012-3 (generalized cylinders and bodies of revolution).
