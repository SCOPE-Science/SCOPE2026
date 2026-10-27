# A sharp tangential boundary-layer law for zeros of stationary Gaussian analytic functions

## Finding
For a smooth stationary spectral density with an isolated zero of even order \(2m\), the normalized mean zero intensity has a nontrivial transition on the **sharp angular scale** \((1-r)^{1/(2m)}\). The transition profile is explicitly
\[
\mathcal P_m(x)=1-\left(\frac{b}{b+a x^{2m}}\right)^2,
\]
where \(a\) is the first nonzero Taylor coefficient of the spectral density and \(b\) its positive nonlocal Poisson boundary slope. This scaling also determines the exact leading expected zero count of boundary sectors of matching angular width.

## Assumptions and scope
Let \((\xi_n)_{n\in\mathbb Z}\) be a centered, circular complex stationary Gaussian sequence whose spectral measure is \(w(\theta)d\theta/(2\pi)\), with \(w\ge0\), \(w\not\equiv0\), and \(w\in C^{2m+2}(\mathbb R/2\pi\mathbb Z)\). Define \(f(z)=\sum_{n=0}^\infty\xi_n z^n\), analytic on \(|z|<1\) almost surely. Its zeros have mean planar density \(\rho(z)\) (normalized against the ordinary area element \(dA\)).

Suppose \(w(\theta_0+s)=a s^{2m}+O(s^{2m+1})\) as \(s\to0\), with integer \(m\ge1\) and \(a>0\). The density is permitted to have other zeros elsewhere. Define
\[
b=\frac1{2\pi}\int_{-\pi}^{\pi}\frac{w(\theta_0+s)}{1-\cos s}\,ds.
\]
The integrand is integrable at the origin, so \(0<b<\infty\) because \(w\) is nonnegative, nonzero, and continuous.

For every compact \(E\subset\mathbb R\), as \(r\uparrow1\) we have uniformly for \(x\in E\)
\[
\pi(1-r^2)^2\rho\bigl(r e^{i(\theta_0+(1-r)^{1/(2m)}x)}\bigr)
\longrightarrow1-\left(\frac{b}{b+a x^{2m}}\right)^2.\tag{1}
\]
At fixed nonzero \(x\), replacing the angular displacement by \((1-r)^\alpha x\) gives limiting normalized intensity \(1\) for \(0<\alpha<1/(2m)\), and \(0\) for \(\alpha>1/(2m)\). At the transition exponent the limit is (1); these three regimes are sharp.

For any fixed \(C>0\), write \(N_\epsilon(C)\) for the number of zeros with \(1-2\epsilon<|z|<1-\epsilon\) and angular displacement \(|\arg z-\theta_0|<C\epsilon^{1/(2m)}\). Then
\[
\lim_{\epsilon\downarrow0}\epsilon^{1-1/(2m)}\mathbb E N_\epsilon(C)
=\frac1{4\pi}\int_{1}^{2}\int_{-C}^{C}
\frac{1}{t^2}\left[1-\left(\frac{bt}{bt+a x^{2m}}\right)^2\right]dx\,dt\;>0.\tag{2}
\]
All limits refer to the mean one-point intensity; no point-process limit is claimed.

## Proof
**1. Exact intensity identity and normalization.** Let \(u(r,\theta)=(P_r*w)(\theta)\) be the Poisson extension with \(P_r(t)=(1-r^2)/(1-2r\cos t+r^2)\) and normalized integration \(dt/(2\pi)\). Stationarity implies
\[
K(z,z)=\mathbb E|f(z)|^2=\frac{u(r,\theta)}{1-r^2},\qquad z=re^{i\theta}.
\]
Because \(u\) is positive and harmonic, \(\Delta\log u=-|\nabla u|^2/u^2\). The Gaussian zero-intensity identity \(\rho=(4\pi)^{-1}\Delta\log K(z,z)\) therefore gives the **exact** identity
\[
\pi(1-r^2)^2\rho(re^{i\theta})
=1-\frac{(1-r^2)^2}{4u(r,\theta)^2}
\left(u_r(r,\theta)^2+\frac{u_\theta(r,\theta)^2}{r^2}\right).\tag{3}
\]
No finite numerical approximation is used here.

**2. First boundary jet and the nonlocal coefficient.** Since \(w\in C^{2m+2}\), its Poisson extension is continuously differentiable up to the closed unit circle. At \(\theta_0\), dominated convergence in \(u(r,\theta_0)/(1-r)\), using \(w(\theta_0)=0\) and \(w(\theta_0+s)=O(s^{2m})\), gives
\[
-u_r(1,\theta_0)=\lim_{r\uparrow1}\frac{u(r,\theta_0)}{1-r}
=\frac1{2\pi}\int_{-\pi}^{\pi}\frac{w(\theta_0+s)}{1-\cos s}\,ds=b.\tag{4}
\]
The limit follows also from the radial Hopf boundary lemma; (4) fixes its exact factor. Writing \(\delta=1-r\) and \(s=\delta^{1/(2m)}x\), uniform boundary differentiability and the Taylor expansion of \(w\) give, uniformly for \(x\) in any fixed compact interval,
\[
u(1-\delta,\theta_0+s)=w(\theta_0+s)-\delta u_r(1,\theta_0+s)+o(\delta)
=\delta(a x^{2m}+b)+o(\delta).\tag{5}
\]
Furthermore \(u_r\to-b\) and \(u_\theta\to w'(\theta_0)=0\), uniformly on those moving compact sectors. Substituting into (3) and using \((1-r^2)^2/(4\delta^2)\to1\) proves (1), including the boundary value \(\mathcal P_m(0)=0\).

**3. Sharpness of the angular scale.** If \(s=\delta^\alpha x\) with \(x\ne0\) and \(0<\alpha<1/(2m)\), then \(u\sim a x^{2m}\delta^{2m\alpha}\gg\delta\), and \(u_r\) and \(u_\theta\) are bounded; since \(\delta/u\to0\), (3) tends to \(1\). If \(\alpha>1/(2m)\), then \(u\sim b\delta\), \(u_r\to-b\), \(u_\theta\to0\), giving limit \(0\). Only \(\alpha=1/(2m)\) balances the spectral zero and the Poisson leakage and gives a nonconstant profile.

**4. Sector counts.** Put \(r=1-\epsilon t\), \(\theta=\theta_0+\epsilon^{1/(2m)}x\) with \(1\le t\le2\), \(|x|\le C\). The proof of (5) works uniformly on this rectangle and gives \(u/\epsilon\to bt+a x^{2m}\), \(u_r\to-b\), and \(u_\theta\to0\). Consequently
\[
\epsilon^2\rho((1-\epsilon t)e^{i(\theta_0+\epsilon^{1/(2m)}x)})
\longrightarrow\frac{1}{4\pi t^2}\left[1-\left(\frac{bt}{bt+a x^{2m}}\right)^2\right]
\]
uniformly there. The polar area Jacobian is \((1-\epsilon t)\epsilon^{1+1/(2m)}\,dt\,dx\); integration of the one-point intensity gives (2). The integral is strictly positive for \(C>0\) because the integrand is positive for \(x\ne0\).

## Verification
An independent finite-degree spectral-density family \(w_m(\theta)=(2-2\cos\theta)^m\), with \(m=1,2,3\), has exact Fourier coefficients \((-1)^k\binom{2m}{m+k}\). Formula (4) gives \(a=1\) and \(b=2\binom{2m-2}{m-1}\). The accompanying checker computes \(u,u_r,u_\theta\) as finite sums, evaluates the exact left side of (3) for shrinking \(\delta\), and checks numerical convergence to (1) for multiple offsets. It also checks the scalar spectral normalizations and the three-scale predictions. These finite tests corroborate the proof and are not an infinite proof.

## Relationship to prior work
Noda and Shirai (2021) study expected zero counts of Gaussian analytic power series with finitely dependent stationary coefficients, including effects of vanishing spectral densities; they identify primary MSC 30B20. Shirai (2025), especially Theorem 2.1 and its proof, derives **fixed-direction** one-point density asymptotics: universal quadratic divergence away from zeros, reduced divergence at quadratic spectral zeros, and a finite limit for higher-order zeros. Those fixed-angle results do not supply the joint tangential/radial limit (1), the unique angular crossover exponent, or the joint-sector counting law (2). The latter must control the boundary derivative uniformly while the angle approaches a spectral zero. Shirai (2025b) supplies the general spectral representation of one-point and higher correlations; this exact kernel description does not itself establish the moving-angle boundary-layer asymptotic. The exact Poisson kernel and one-point intensity identity are classical inputs, not claimed as new.

## Limitations
The result requires a smooth absolutely continuous spectral density and a zero of specified finite even order. It is a first-moment result only; it neither determines fluctuations nor provides a limiting random point process. It does not cover singular spectral measures, densities vanishing to infinite order, or general correlated non-Gaussian coefficients. The 2025 fixed-direction formulas are prior work rather than independent new components of this result. Originality remains subject to any uncatalogued equivalent angular crossover theorem.

## References
1. Kohei Noda and Tomoyuki Shirai, *Expected number of zeros of random power series with finitely dependent Gaussian coefficients*, arXiv:2106.02860v1, first posted 5 June 2021, https://arxiv.org/abs/2106.02860 .
2. Tomoyuki Shirai, *The density of zeros of random power series with stationary complex Gaussian coefficients*, arXiv:2501.02586, first posted 5 January 2025, https://arxiv.org/abs/2501.02586 . In particular Theorem 2.1 and Sections 3–5.
3. Tomoyuki Shirai, *Spectral representation of correlation functions for zeros of Gaussian power series with stationary coefficients*, arXiv:2501.03704v1, first posted 7 January 2025, https://arxiv.org/abs/2501.03704 .
4. Edelman–Kostlan Gaussian analytic zero-intensity formula, used in the form \(\rho=(4\pi)^{-1}\Delta\log K(z,z)\).
