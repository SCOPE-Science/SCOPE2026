# The first off-origin sign transition of multidimensional lattice heat flow

## Finding

Let \(d\ge 2\) be an integer, and let \(\Delta_d\) be the standard nearest-neighbor Laplacian on \(\ell^p(\mathbb Z^d)\):
\[
(\Delta_d f)(x)=\sum_{j=1}^d\bigl(f(x+e_j)+f(x-e_j)-2f(x)\bigr).
\]
Write \(W_d(t)=e^{t\Delta_d}\), \(q_{d,t}=\partial_t W_d(t)\delta_0\), and let \(I_m\) denote the modified Bessel function of the first kind. Define \(R(t)=I_1(2t)/I_0(2t)\). For each \(d\ge2\) there is a **unique** \(\tau_d>0\) satisfying
\[
\frac2{R(\tau_d)}-\frac1{\tau_d}+2(d-1)R(\tau_d)-2d=0.
\]
For \(0<t<\tau_d\), the time-derivative kernel is strictly negative at the origin and strictly positive at **every** other lattice site. At \(t=\tau_d\), its only zero entries are the \(2d\) nearest-neighbor sites, while all other off-origin entries remain positive. For every \(t>\tau_d\), the nearest-neighbor entries are strictly negative. Consequently the exact sharp endpoint norm has the maximal single-negative-site interval
\[
\boxed{\ \|\partial_tW_d(t)\|_{\ell^1\to\ell^1}
=\|\partial_tW_d(t)\|_{\ell^\infty\to\ell^\infty}
=4d e^{-2dt}I_0(2t)^{d-1}\bigl(I_0(2t)-I_1(2t)\bigr),\quad 0<t\le\tau_d.\ }
\]
For \(t>\tau_d\) the endpoint norm is **strictly larger** than the displayed single-negative-site expression. The thresholds decrease strictly with dimension, and
\[
\boxed{\ \tau_d=\frac1{2d}+\frac1{4d^2}+\frac1{8d^3}+O(d^{-4})\quad(d\to\infty).\ }
\]
The statement is valid over real or complex sequence spaces. The one-dimensional analogue is classical and is not claimed here as new.

## Assumptions and scope

Here time is normalized so that each of the \(2d\) directed nearest-neighbor jumps occurs at rate one; a time rescaling is required under a probability-normalized graph Laplacian. No finite-volume boundary or periodic quotient is assumed. The infinite convolution kernels belong to \(\ell^1(\mathbb Z^d)\), and their convolution operator norms on \(\ell^1\) and \(\ell^\infty\) equal the absolute sums of their coefficients. The asymptotic is for positive integers \(d\to\infty\). This does not give an exact norm expression for arbitrary times beyond the first sign transition, nor does it assert any optimal \(\sup_t t\|\partial_tW_d(t)\|\).

## Proof

**Product kernel.** For \(t>0\), write \(p_t(m)=e^{-2t}I_{|m|}(2t)>0\). The heat kernel on \(\mathbb Z^d\) is
\[
P_{d,t}(x)=\prod_{j=1}^d p_t(x_j).
\]
Define the real logarithmic score \(s_m(t)=\partial_t\log p_t(m)\) for \(m\ge0\). Then
\[
q_{d,t}(x)=P_{d,t}(x)\sum_{j=1}^d s_{|x_j|}(t).
\]
In particular, \(s_0(t)=2(R(t)-1)<0\), as \(I_0(2t)>I_1(2t)\) follows by integrating \((1-\cos\theta)e^{2t\cos\theta}\) over \([0,\pi]\).

**Strict ordering of spatial scores.** Set \(r_m(z)=I_{m+1}(z)/I_m(z)\), for each integer \(m\ge0\). The standard Bessel recurrences yield the Riccati equation
\[
r_m'(z)=1-r_m(z)^2-\frac{2m+1}{z}r_m(z).
\]
The power series gives \(r_m'(z)>0\) for all sufficiently small positive \(z\). At any hypothetical zero of \(r_m'\), differentiating the Riccati equation gives \(r_m''=(2m+1)r_m/z^2>0\). The first zero of an initially positive derivative could not have positive derivative of that derivative. Thus \(r_m'(z)>0\) for every \(z>0\). It follows that
\[
s_{m+1}(t)-s_m(t)=2\,\partial_z\log r_m(z)\big|_{z=2t}>0.
\]
Therefore every off-origin site has score at least \(s_1+(d-1)s_0\), with equality *only* at the \(2d\) nearest-neighbor sites; the origin has strictly negative score \(ds_0\).

**Exactly one crossing.** Let \(E=e_1\). The neighboring heat probability satisfies \(P_{d,t}(E)=P_{d,t}(0)R(t)\), and its derivative has the sign of
\[
\Phi_d(t)=s_1(t)+(d-1)s_0(t)
=\frac2{R(t)}-\frac1t+2(d-1)R(t)-2d.
\]
To prove unique crossing without assuming monotonicity of \(\Phi_d\), use the Fourier spectral parameter
\[
\lambda(\theta)=2d-2\sum_{j=1}^d\cos\theta_j,
\qquad \theta\in[-\pi,\pi]^d.
\]
If \(\rho_d\) is the pushforward of normalized torus measure under \(\lambda\), coordinate symmetry gives
\[
\partial_t P_{d,t}(E)
=\int_{[0,4d]}\lambda\left(\frac{\lambda}{2d}-1\right)e^{-\lambda t}\,d\rho_d(\lambda)
=A_d(t)-B_d(t),
\]
where \(A_d\) integrates the positive integrand over \((2d,4d]\), and \(B_d\) integrates its negative over \((0,2d)\) with its sign reversed. Both are strictly positive. The logarithmic derivative of \(A_d/B_d\) is the difference of the respective weighted mean spectral parameters with a minus sign; it is strictly negative since every parameter contributing to \(A_d\) exceeds every parameter contributing to \(B_d\). At \(t=0\), \(\partial_t P_{d,t}(E)=1>0\), so \(A_d(0)>B_d(0)\). As \(t\to\infty\), \(A_d(t)/B_d(t)\to0\): the former is bounded by a constant times \(e^{-2dt}\), whereas the latter receives positive mass from an interval strictly inside \((0,2d)\). Thus exactly one crossing occurs, from positive to negative. This is \(\tau_d\), and \(\Phi_d\) has the corresponding sign because \(P_{d,t}(E)>0\).

**Sharp norm and maximality.** Up to and including \(\tau_d\), the derivative kernel has one negative site, namely the origin. Its total mass vanishes by differentiation of the Markov mass-one identity. Hence its total variation is twice the negative mass at the origin:
\[
\sum_{x\in\mathbb Z^d}|q_{d,t}(x)|
=-2q_{d,t}(0)=4d P_{d,t}(0)(1-R(t)).
\]
This is the boxed Bessel expression. Beyond \(\tau_d\), at least the nearest-neighbor coefficients are negative as well as the origin coefficient, so total variation is strictly greater than \(-2q_{d,t}(0)\). For an \(\ell^1\) convolution kernel the \(\ell^1\) norm is attained by input \(\delta_0\), and the \(\ell^\infty\) norm equals the same total variation by choosing the coordinatewise signs of a reflected kernel. Thus these are sharp operator norms.

**Dimension and asymptotics.** Since \(s_0(t)<0\), \(\Phi_{d+1}(t)=\Phi_d(t)+s_0(t)<\Phi_d(t)\). The unique positive-to-negative crossing therefore moves strictly earlier with increasing \(d\). The Bessel power series yields
\[
R(t)=t-\frac{t^3}{2}+\frac{t^5}{3}+O(t^7).
\]
Since \(\Phi_d(t)=0\) is equivalent to \(t\asymp1/d\) (obtainable by comparing fixed small multiples of \(1/d\)), substitution and coefficient matching with a remainder controlled by \(\partial_t\Phi_d=-4d^2+O(d)\) near the root gives
\[
\tau_d=\frac1{2d}+\frac1{4d^2}+\frac1{8d^3}+O(d^{-4}).
\]
The derivative estimate is local on a bounded multiple of \(1/d\), not a claim that \(\Phi_d\) is globally decreasing.

## Verification

The separately supplied `verify.py` checks Bessel recurrences, spatial score ordering, threshold signs, and the threshold asymptotic on finite grids and dimensions. It is a finite consistency diagnostic, not an exhaustive proof; the infinite sign assertion and unique crossing are established by the Riccati and spectral arguments above. The formulas use the same unit-rate normalization throughout.

## Relationship to prior work

Dowker's 2012 full-text treatment gives the one-dimensional Bessel heat kernel and the passage to Cartesian products, but not the first off-origin time-derivative sign threshold or its dimension law. Baricz's 2012 treatment supplies classical Bessel ratio and Turán inequalities, without deriving this semigroup norm cutoff. Abadias and de León-Contreras's 2021 full-text study gives discrete heat-kernel derivative bounds and Hölder-space characterizations on \(\mathbb Z\); the relevant estimates do not imply the dimension-dependent exact sign cutoff on \(\mathbb Z^d\). Existing one-dimensional exact derivative-norm studies are not claimed as new. The present result is the all-dimensional first-sign classification, the associated maximal exact endpoint-norm interval, strict dimensional ordering, and its three-term high-dimensional scale.

## Limitations

The theorem concerns only the first sign transition and not all later sign changes. It does not classify the kernel's complete later-time sign geometry, its all-time exact norm, the maximal analytic constant over time, weighted or anisotropic lattices, or finite quotients. Bibliographic searches cannot establish global priority; a historical treatment under heat-kernel unimodality or total-variation-speed language remains a possible overlap risk. Independent external review has not been performed.

## References

1. J. S. Dowker, *Heat-kernels on the discrete circle and interval*, arXiv:1207.2096 (first posted 2012-07-09), especially §§1–3 and discussion of Cartesian products.
2. Á. Baricz, *Bounds for Turánians of modified Bessel functions*, arXiv:1202.4853 (first posted 2012-02-22), especially §§1–3 on Bessel ratios and recurrences.
3. L. Abadias and M. de León-Contreras, *Discrete Hölder spaces, their characterization via semigroups associated to the discrete Laplacian and kernels estimates*, arXiv:2107.06778 (first posted 2021-07-14), especially §§1–2.
