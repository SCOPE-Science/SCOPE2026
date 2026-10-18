# A simulation-free resolvent for reflected partial-reset first passage

## Finding
Let \(X_t\) diffuse on the real line with generator \(D\partial_x^2\), where \(D>0\). At independent Poisson times of rate \(r>0\), its position changes instantaneously from \(x\) to \(ax\), where \(-1<a<0\). Let \(L>0\), and let \(\tau_L=\inf\{t\ge0:X_t=L\}\). In particular, a reset jump that passes over \(L\) without landing on it does **not** count as a hit.

Define \(c=D/r\) and, for each integer \(n\ge0\),
\[
F_n(z)=\frac1{2\pi}\int_{\mathbb R}\frac{e^{-ikz}}{\prod_{j=0}^{n}(1+c a^{2j}k^2)}\,dk.
\]
Put
\[
\pi_L=\frac1{2\pi}\int_{\mathbb R}e^{-ikL}\prod_{j=0}^{\infty}(1+c a^{2j}k^2)^{-1}\,dk>0.
\]
The complete mean first-passage function, for **every** starting point \(x\in\mathbb R\), is
\[
\boxed{\mathbb E_x\tau_L=\frac1{r\pi_L}\sum_{n=0}^{\infty}\bigl[F_n(L(1-a^n))-F_n(L-a^n x)\bigr].}
\]
In particular, the boundary constant \(\kappa=\mathbb E_{-L/|a|}\tau_L\), treated as a simulation-supplied input in Biroli et al. (2024), is evaluated by this formula without simulation or unknown parameters. The series converges absolutely. If its terms \(n=0,\ldots,N-1\) are retained, then for every \(N\ge1\),
\[
\left|\mathbb E_x\tau_L-\frac1{r\pi_L}\sum_{n=0}^{N-1}\bigl[F_n(L(1-a^n))-F_n(L-a^n x)\bigr]\right|
\le \frac{|L-x|\log(a^{-2})}{2\pi D(1-a^2)(1-|a|)\pi_L}\,|a|^N.
\]
This is a geometric truncation estimate uniform in \(N\), with explicitly specified parameters. The calculation uses only one-dimensional Fourier integrals and products.

## Assumptions and scope
All lengths are real, \(D,r,L>0\) and \(-1<a<0\); resets are instantaneous and do not themselves detect the target when they cross it. Brownian noise and reset times are independent. The first-passage time is the first exact point visit, which necessarily occurs during a continuous Brownian segment with probability one. No finite-space truncation, simulation-calibrated boundary value, or limitation to starting points on one side of the target is assumed.

The Fourier convention is \(\widehat f(k)=\int_{\mathbb R}e^{ikx}f(x)\,dx\) and \(f(x)=(2\pi)^{-1}\int e^{-ikx}\widehat f(k)\,dk\). Empty products have value one. For \(a=0\), the continuous limiting case recovers the standard fixed-origin reset mean \((e^{L\sqrt{r/D}}-1)/r\) from \(x=0\).

## Proof
**1. Stationary density.** Denote by \(Z_j\) independent centered Laplace random variables with characteristic functions \((1+c k^2)^{-1}\). At equilibrium the age since the last reset is exponential with rate \(r\), and Brownian displacement over that age has precisely the Laplace law of \(Z_0\). Thus the stationary position is distributed as \(\sum_{j\ge0}a^j Z_j\). This series converges in \(L^2\), since its variance is \(2c/(1-a^2)\); its characteristic function is \(\prod_{j\ge0}(1+c a^{2j}k^2)^{-1}\). It has a continuous, strictly positive density everywhere because it is the convolution of a strictly positive Laplace density with an independent probability distribution. Therefore \(\pi_L\) above is well-defined and strictly positive. Contractive coupling under common Poisson resets proves convergence to stationarity, also at the transition-density level by convolution with the nondegenerate Brownian age distribution.

**2. Fourier resolvent.** Let \(p_t(y\mid x)\) be the unrestricted transition density and \(G_s(x,y)=\int_0^\infty e^{-st}p_t(y\mid x)dt\) for \(s>0\). The backward generator is \(\mathcal L f=D f''+r(f(a\cdot)-f)\). The conditional characteristic function obeys
\[
\partial_t\phi_t(k\mid x)=-(Dk^2+r)\phi_t(k\mid x)+r\phi_t(ak\mid x),\qquad \phi_0=e^{ikx}.
\]
Its Laplace transform is obtained by a convergent iteration, because \(r/(s+r)<1\):
\[
\widehat G_s(k\mid x)=\sum_{n\ge0}\frac{r^n e^{ia^n kx}}{\prod_{j=0}^{n}(s+r+D a^{2j}k^2)}.
\]
For \(s>0\), the remainder of the iteration is at most a geometric multiple of \(1/s\), uniformly in \(k\), so this identity is exact.

**3. Resolvent at the target.** Strong Markov decomposition at \(\tau_L\) and the fact that Brownian local time at \(L\) has no pre-hit contribution give
\[
G_s(x,L)=\mathbb E_x[e^{-s\tau_L}]\,G_s(L,L).
\]
This remains valid when reset jumps cross the target: such jumps contribute no point local time, and a continuous Brownian visit is still required. Stationarity implies \(sG_s(L,L)\to\pi_L\) as \(s\downarrow0\). Consequently
\[
\mathbb E_x\tau_L=\lim_{s\downarrow0}\frac{G_s(L,L)-G_s(x,L)}{sG_s(L,L)}.
\]
The existence and finiteness of the limit on the right follow from the domination in the next step, and monotone convergence then identifies it with the mean hitting time without presupposing that the mean is finite.

**4. Exchange of limits and explicit bound.** Fourier inversion of the resolvent difference yields a sum with numerator \(e^{ia^n kL}-e^{ia^n kx}\). The \(n=0\) Fourier integral is absolutely integrable. For \(n\ge1\), use
\[
|e^{ia^n kL}-e^{ia^n kx}|\le |a|^n|k||L-x|
\]
and dominate its denominator by its first two factors. Direct integration gives
\[
\int_{\mathbb R}\frac{|k|}{(1+ck^2)(1+ca^2k^2)}\,dk
=\frac{\log(a^{-2})}{c(1-a^2)}.
\]
Thus dominated convergence allows \(s\downarrow0\), Fourier inversion and summation to be exchanged, producing the boxed exact expression. Summing the geometric majorant for all \(n\ge N\ge1\) gives the boxed truncation estimate. No unproved finite-to-infinite extrapolation is involved.

## Verification
The standalone program `verify.py` evaluates the Fourier integrals through an oscillatory quadrature routine and independently solves a finite-difference discretization of \(-\mathcal LT=1\) with an absorbing interior target. For example, \(D=r=L=1\) and \(a=-1/2\) give \(\mathbb E_0\tau_L\approx1.3472466\) and \(\kappa\approx1.6786311\). Finite-difference estimates approach both values as the grid is refined. The program separately checks the explicit geometric bound and the \(a=0\) standard-reset limit. Numerical agreement supports the algebra but does not replace the all-parameter proof above; numerical quadrature is not claimed to be interval-certified.

## Relationship to prior work
Biroli, Feld, Hartmann, Majumdar and Schehr (arXiv:2406.08387v1, first public 12 June 2024) derive the rescaling-reset process, its steady state, and a mean-first-passage solution for negative multipliers containing an undetermined simulation-calibrated boundary constant (their Sec. III.B, equations (52)–(60)). Their positive-multiplier result and other formulas are not claimed here. The new result closes that expressly remaining negative-multiplier boundary problem with a simulation-free Fourier potential-kernel formula and an all-parameter geometric tail bound. Pierce (arXiv:2204.07215) establishes the proportional-reset diffusion/pantograph framework for positive multipliers and presents, but does not solve in general, a first-passage equation. Harbola (Phys. Rev. E 108, 014135) studies proportional stochastic jumps and displacement statistics rather than this hitting-time resolvent. The generic Markov resolvent and hitting-kernel identity are classical tools, not claimed as new.

## Limitations
This is an exact integral-series representation, not an elementary finite closed form. Evaluating each Fourier integral numerically entails separate quadrature error; the displayed bound controls only truncation in \(n\). It does not establish uniqueness of an optimal resetting rate or solve related noncontractive cases \(|a|\ge1\). Independence and priority have not been externally certified; hidden equivalent resolvent formulas in wider stochastic-process literature remain possible.

## References
1. M. Biroli, Y. Feld, A. K. Hartmann, S. N. Majumdar, G. Schehr, *Resetting by rescaling: exact results for a diffusing particle in one-dimension*, arXiv:2406.08387v1 (12 June 2024), https://arxiv.org/abs/2406.08387; Phys. Rev. E 110, 044142 (2024).
2. J. K. Pierce, *An advection-diffusion process with proportional resetting*, arXiv:2204.07215 (2022), https://arxiv.org/abs/2204.07215.
3. U. Harbola, *Stochastic walker with variable long jumps*, Phys. Rev. E 108, 014135 (2023), https://doi.org/10.1103/PhysRevE.108.014135.
