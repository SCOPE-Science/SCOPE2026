# Anisotropic boundary localization and equatorial tomography of spherical hyperplane cells

## Finding

Let \(p=(0,0,1)\in S^2\). Independently sample \(n\ge1\) great circles with unit normals having probability density \(f\) with respect to normalized area \(d\sigma/(4\pi)\). Assume \(f\in C^2(S^2)\), \(f(u)=f(-u)\), \(\min f>0\), and \(\int f\,d\sigma/(4\pi)=1\). Let \(C_n\) be the closed spherical cell containing \(p\), and \(P_n=\mathcal H^1(\partial C_n)\) its intrinsic boundary length. Write a boundary point in geodesic polar coordinates
\[
x(\theta,\alpha)=(\sin\theta\cos\alpha,\sin\theta\sin\alpha,\cos\theta),\quad0<\theta<\pi,\ 0\le\alpha<2\pi.
\]
The polar angle \(\alpha\) records the **position of a boundary point**, not the normal of the great circle supporting its edge.

Define the equatorial trace \(g(\psi)=f(\cos\psi,\sin\psi,0)\), its mass \(h_0=(4\pi)^{-1}\int_0^{2\pi}g(\psi)d\psi>0\), and the positive, \(\pi\)-periodic angular rate
\[
a(\alpha)=\frac1{4\pi}\int_0^{2\pi}|\cos(\psi-\alpha)|g(\psi)\,d\psi.
\]
For the **annealed arclength boundary measure** \(\mu_n(B)=\mathbb E[\mathcal H^1\{x\in\partial C_n:(n\theta(x),\alpha(x))\in B\}]\), the finite measures \(n\mu_n\) converge in total variation to the measure with density
\[
\boxed{h_0 s\,e^{-s a(\alpha)}}\qquad(s>0,\ 0\le\alpha<2\pi).
\]
Consequently, writing \(R=\lim_{n\to\infty}n\mathbb EP_n\), one has
\[
\boxed{R=h_0\int_0^{2\pi}\frac{d\alpha}{a(\alpha)^2}}.
\]
If a boundary point is drawn from the **normalized expected boundary-length measure** (not by first normalizing the length of each realized cell), its limiting angular density and conditional radial law are
\[
\boxed{w(\alpha)=\frac{a(\alpha)^{-2}}{\int_0^{2\pi}a(\beta)^{-2}d\beta},\qquad s\mid\alpha\sim\operatorname{Gamma}(2,\text{rate }a(\alpha))}.
\]
The joint law converges in total variation.

The boundary angular law \(w\) determines the trace \(g\) up to a positive common factor. **Together \((w,R)\) determine the complete, absolutely normalized equatorial trace \(g\)**. Explicitly, put \(J=\int_0^{2\pi}w(\alpha)^{-1/2}\,d\alpha\). Then
\[
\boxed{a(\alpha)=\frac{J}{4R}w(\alpha)^{-1/2},\qquad h_0=\frac{J^2}{16R}.}
\]
For \(\widehat b(j)=(2\pi)^{-1}\int_0^{2\pi}b(t)e^{-ijt}dt\), reconstruct \(g\) by
\[
\boxed{\widehat g(0)=\pi\widehat a(0),\quad\widehat g(2k)=\pi(-1)^{k-1}(4k^2-1)\widehat a(2k)\ (k\ge1),}
\]
with negative modes given by complex conjugation and odd modes zero. These coefficients uniquely determine the continuous equatorial trace.

There is also a **sharp anisotropic perimeter inequality**, for fixed equatorial mass \(h_0\):
\[
\boxed{R\ge\frac{\pi^3}{2h_0},}
\]
with equality if and only if \(g\) is constant along the equator. Other latitudes may remain anisotropic.

## Assumptions and scope

Each normal \(U_i\) is sampled independently with density \(f\); the corresponding great circle is \(G_i=\{x\in S^2:U_i\cdot x=0\}\). Since \(f\) is continuous, almost surely \(U_i\cdot p\neq0\) for every \(i\). Then
\[
C_n=\bigcap_{i=1}^n\{x\in S^2:(U_i\cdot x)(U_i\cdot p)\ge0\}.
\]
The boundary consists of geodesic arcs; intersections of distinct supporting great circles have zero arclength, so every edge is counted exactly once. All limits take \(n\to\infty\) with \(f\) fixed. The arclength is geodesic length on the **unit** sphere. The polar coordinates are measured relative to the fixed pole \(p\).

The density \(w\) is a probability density in radians on \([0,2\pi)\). The rate \(a\) has reciprocal-angle units matching \(s=n\theta\). Total-variation convergence is understood after identifying \(n\mu_n\) with a finite density on \((0,\infty)\times[0,2\pi)\), extended by zero when \(s>n\pi\).

## Proof

**1. Exact boundary first intensity.** For a general \(x\in S^2\), let
\[
q_f(p,x)=\frac1{4\pi}\int_{S^2}\mathbf1\{(u\cdot p)(u\cdot x)<0\}f(u)\,d\sigma(u),
\qquad h_f(x)=\frac1{4\pi}\int_{u\cdot x=0}f(u)\,d\mathcal H^1(u).
\]
The spherical coarea identity for \(u\cdot x\) (whose spherical gradient has norm one on its zero set) yields, for bounded nonnegative Borel \(F\),
\[
\mathbb E\left[\int_{\partial C_n}F(x)\,d\mathcal H^1(x)\right]
=\boxed{n\int_{S^2}F(x)h_f(x)[1-q_f(p,x)]^{n-1}\,d\sigma(x).}\tag{1}
\]
To prove (1), sum over the \(n\) proposed supporting circles. Conditional on the first circle containing the boundary point \(x\), each other independent circle must not separate \(p\) from \(x\), a probability of \(1-q_f(p,x)\). Intersections of two circles contribute zero arclength. Fubini and coarea average the remaining circle. The formula also holds at \(n=1\) with the empty product equal to one.

**2. Uniform local separation law.** Let \(v_\alpha=(\cos\alpha,\sin\alpha,0)\) and \(v_\alpha^\perp=(-\sin\alpha,\cos\alpha,0)\). Parameterize a normal by
\[
u=\sqrt{1-t^2}(\sin\phi\,v_\alpha+\cos\phi\,p)+t v_\alpha^\perp,
\quad -1<t<1,\ 0\le\phi<2\pi.
\]
The spherical area element is \(dt\,d\phi\). For \(x=x(\theta,\alpha)\), the signs of \(u\cdot p\) and \(u\cdot x\) differ exactly when
\(\phi\in(\pi/2,\pi/2+\theta)\cup(3\pi/2,3\pi/2+\theta)\), interpreted modulo \(2\pi\). Integrating \(f\) over these two angular strips and expanding at \(\theta=0\), uniformly in \(\alpha\), gives
\[
q_f(p,x(\theta,\alpha))=\theta a(\alpha)+O_f(\theta^2).
\tag{2}
\]
The factor \(|\cos(\psi-\alpha)|\) arises from the substitution \(t=\sin(\psi-\alpha)\) on the equator; evenness of \(f\) identifies the two strip contributions. Also \(h_f(x(\theta,\alpha))=h_0+O_f(\theta)\) uniformly. Positivity implies \(q_f(p,x)\ge(\min f)\theta/\pi\), since an isotropic normal separates two points at geodesic distance \(\theta\) with probability \(\theta/\pi\).

**3. Total-variation boundary limit.** In spherical polar coordinates \(d\sigma(x)=\sin\theta\,d\theta\,d\alpha\). Substitute \(s=n\theta\) in (1) to find the density of \(n\mu_n\):
\[
F_n(s,\alpha)=n h_f(x(s/n,\alpha))\sin(s/n)[1-q_f(p,x(s/n,\alpha))]^{n-1}\mathbf1_{0<s<n\pi}.
\]
By (2), \(F_n(s,\alpha)\to h_0s\exp(-s a(\alpha))\) pointwise. Uniformly for \(n\ge2\),
\[
0\le F_n(s,\alpha)\le \frac{\max f}{2}s\exp\left(-\frac{\min f}{2\pi}s\right),
\]
using \(\sin(s/n)\le s/n\), \(h_f\le(\max f)/2\), and the lower bound for \(q_f\). Dominated convergence therefore gives \(L^1\), hence total-variation, convergence of the unnormalized finite measures. Integration in \(s\) gives the formula for \(R\). Dividing by their positive masses gives the asserted joint probability law, its angular marginal and conditional gamma density.

**4. Exact equatorial tomography.** Write \(K(t)=|\cos t|\), so \(a=(4\pi)^{-1}(K*g)\) for circular convolution without extra normalization. Its Fourier multipliers are
\[
\widehat K(0)=\frac2\pi,\quad\widehat K(2k)=\frac{2(-1)^{k-1}}{\pi(4k^2-1)}\ (k\ge1),\quad\widehat K(2k+1)=0.
\]
Because \(g(\psi+\pi)=g(\psi)\), no odd Fourier mode is needed; every relevant multiplier is nonzero. Thus \(\widehat a(j)=\frac12\widehat K(j)\widehat g(j)\) and the displayed inversion follows. For absolute normalization let \(Z=\int a^{-2}\), so \(w=a^{-2}/Z\) and \(a=Z^{-1/2}w^{-1/2}\). Integrating the cosine kernel yields \(\int_0^{2\pi}a=4h_0\), whence \(J=4h_0\sqrt Z\). Combining with \(R=h_0Z\) gives \(h_0=J^2/(16R)\) and \(a=Jw^{-1/2}/(4R)\). The trace is determined as a continuous function by its Fourier coefficients. This does **not** reconstruct \(f\) away from the equator and does **not** assert stable inversion from noisy observations.

**5. Sharp perimeter inequality.** The mean of \(a\) over the circle is \(2h_0/\pi\). Strict Jensen convexity for \(t\mapsto t^{-2}\) therefore gives
\[
\int_0^{2\pi}a(\alpha)^{-2}d\alpha\ge 2\pi\left(\frac{2h_0}{\pi}\right)^{-2},
\]
proving \(R\ge\pi^3/(2h_0)\). Equality means \(a\) constant. Fourier invertibility on even trace functions gives exactly constant \(g\), proving both necessity and sufficiency.

**6. An explicit anisotropic benchmark.** For the even smooth density
\[
f_\varepsilon(u)=1+\varepsilon(u_1^2-u_2^2),\qquad |\varepsilon|<1,
\]
which integrates to one against normalized area, direct integration yields, for \(x=x(\theta,\alpha)\),
\[
h_{f_\varepsilon}(x)=\frac12-\frac\varepsilon4\sin^2\theta\cos2\alpha,\qquad
q_{f_\varepsilon}(p,x)=\frac\theta\pi+\frac\varepsilon{6\pi}\sin2\theta\cos2\alpha.
\]
Consequently, \(a_\varepsilon(\alpha)=\pi^{-1}(1+\varepsilon\cos2\alpha/3)\), \(h_0=1/2\), and evaluation of a standard trigonometric integral gives
\[
\boxed{R_\varepsilon=\frac{\pi^3}{(1-\varepsilon^2/9)^{3/2}}.}
\]
The formula is strictly larger than the isotropic constant \(\pi^3\) for every nonzero \(\varepsilon\). Equation (1), with the displayed \(h\) and \(q\), is an explicit two-variable finite-\(n\) quadrature for the mean perimeter in this family.

## Verification

The standalone file `verify_anisotropic.py` evaluates the exact benchmark separation probability by independent spherical midpoint quadrature, integrates the finite-\(n\) first-intensity formula by Gauss–Legendre quadrature, and reconstructs the boundary of independently sampled spherical cells through planar halfspace intersections followed by inverse gnomonic projection. It also inverts the angular cosine transform in a nontrivial quadratic density example. Its successful terminal line is `ALL_ANALYTICAL_AND_GEOMETRIC_TESTS_PASSED`.

The computations use `numpy` and `scipy`; invoke `python verify_anisotropic.py`. Numerical results check formula normalization and special cases. They do not replace the proof of (1) or the limiting theorem for all positive even \(C^2\) densities.

## Relationship to prior work

Kabluchko and Thäle, *Faces in random great hypersphere tessellations* (arXiv:2005.01055, first posted May 3, 2020), develop this general anisotropic binomial tessellation and determine **global typical-face directional distributions**, including directions of their supporting subspheres. Their Theorem 4.1 measures the direction of a sampled face, not the geodesic polar position of boundary arclength in a *fixed-pole cell*. It does not give the present joint rescaled radial-angle density, sharp equatorial extremal law, or tomography from the fixed-pole boundary statistic.

Hug and Schneider, *Random conical tessellations* (arXiv:1508.07768, first posted August 31, 2015), Section 5, compute isotropic fixed-ray-cell geometric expectations. Thus the isotropic scalar perimeter asymptotic is **already implicit in that work** and is not claimed new. Their argument uses rotational invariance, unlike the angularly resolved anisotropic law and inversion here.

Lybrand, Ma and Saab, *On the Number of Faces and Radii of Cells Induced by Gaussian Spherical Tessellations* (arXiv:2108.13523, first posted August 30, 2021), analyze Gaussian/isotropic spherical cells and radius/facet bounds. Bonnet, *Small cells in a Poisson hyperplane tessellation* (arXiv:1702.01964, first posted February 7, 2017), treats stationary Euclidean Poisson **typical cells conditioned to be small**, a different geometric probability law. The cosine-transform Fourier inversion is classical harmonic analysis; the contribution claimed here is its occurrence and sharp quantitative consequences in a fixed-pole boundary observation problem.

## Limitations

The result requires an even, strictly positive \(C^2\) density on \(S^2\) and studies **annealed** arclength on the boundary of the cell containing a predetermined pole. It is not the almost-sure law of a randomly chosen boundary point after normalizing each realized cell. It recovers only the equatorial trace, not the three-dimensional sampling density. Indeed \(f_\delta(u)=1+\delta u_1u_3\), for \(|\delta|<2\), is positive, even, normalized and anisotropic away from the equator, yet has the same constant equatorial trace as the uniform density. Its exact separation probability is \(q_{f_\delta}(p,x(\theta,\alpha))=\theta/\pi-\delta\sin^2\theta\cos\alpha/(3\pi)\), so its finite-sample law differs despite an identical asymptotic boundary law. The Fourier inversion amplifies high-frequency noise quadratically, so statistical recovery rates are not asserted. Higher-dimensional versions, nonsmooth or vanishing directional densities, and second-order perimeter fluctuations are outside the claim. Historical priority of the specific joint angular formula remains subject to further external review.

## References

1. Z. Kabluchko and C. Thäle, *Faces in random great hypersphere tessellations*, arXiv:2005.01055 (first public version 2020-05-03), particularly Sections 2–5.
2. D. Hug and R. Schneider, *Random conical tessellations*, arXiv:1508.07768 (first public version 2015-08-31), especially Section 5 and equation (36).
3. E. Lybrand, A. Ma and R. Saab, *On the Number of Faces and Radii of Cells Induced by Gaussian Spherical Tessellations*, arXiv:2108.13523 (first public version 2021-08-30), Introduction and Results.
4. G. Bonnet, *Small cells in a Poisson hyperplane tessellation*, arXiv:1702.01964 (first public version 2017-02-07), Sections 1–4.
