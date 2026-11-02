# Certified first-passage series for Brownian reflection–rescaling

## Finding

Consider Brownian motion on the real line with diffusion coefficient \(D>0\) and independent Poissonian position updates \(X\mapsto aX\) at rate \(r>0\), where \(-1<a<0\). Let \(L>0\) and let \(\tau_L\) be the *first actual visit* of the trajectory to \(L\), not a crossing by a jump. Put
\[
c=|a|,\qquad b=L\sqrt{r/D},\qquad y=x\sqrt{r/D}.
\]
For each integer \(n\geq0\), let \(H_n(z)\) be the probability density at \(z\) of \(\sum_{j=0}^{n}c^j Z_j\), with independent symmetric unit-scale Laplace variables \(Z_j\) of density \(e^{-|z|}/2\). Let \(H_\infty(z)\) be the density of the almost surely convergent infinite sum. Then **for every finite initial position \(x\in\mathbb R\)**,
\[
\boxed{r\,\mathbb E_x\tau_L=\frac{1}{H_\infty(b)}\sum_{n=0}^\infty\left[H_n\bigl(b-a^n b\bigr)-H_n\bigl(b-a^n y\bigr)\right].}
\]
The numerator converges absolutely at a geometric rate. Every finite summand has an elementary expression:
\[
H_n(z)=\frac12\sum_{j=0}^{n}\frac{e^{-|z|/c^j}}{c^j}
\prod_{\substack{0\leq m\leq n\\m\ne j}}\frac{1}{1-c^{2(m-j)}}.
\]
In particular, the previously numerically supplied boundary value \(\kappa=\mathbb E_{-L/c}\tau_L\) in the negative-rescaling mean-first-passage formulation is obtained by substituting \(y=-b/c\), without Monte Carlo or an unknown integration constant.

The formula has explicit, rigorous error bounds. Define
\[
S_N(y)=\sum_{n=0}^N\left[H_n(b-a^n b)-H_n(b-a^n y)\right],
\quad B_N=H_N(b),
\]
\[
\delta_N=\frac{c^{N+1}}{2(1-c)},\qquad
\epsilon_N(y)=|b-y|\delta_N.
\]
Whenever \(B_N>\delta_N\), the dimensionless mean obeys the certified interval
\[
\boxed{
\max\!\left\{0,\frac{S_N(y)-\epsilon_N(y)}{B_N+\delta_N}\right\}
\leq r\mathbb E_x\tau_L\leq
\frac{S_N(y)+\epsilon_N(y)}{B_N-\delta_N}.}
\]
Thus both the full-line first-passage value and the outstanding boundary constant have computable finite-sum enclosures for any fixed \(-1<a<0\), \(r,D,L>0\) and \(x\in\mathbb R\).

## Assumptions and scope

The Brownian segments have generator \(D\partial_{xx}\), so their variance grows as \(2Dt\). Reset times are an independent homogeneous Poisson process. Each reset multiplies the current pre-reset position by the fixed real number \(a\in(-1,0)\), regardless of position. The particle is killed only upon actually occupying \(L\); a reset that leaps over \(L\) is not itself absorption. The reset origin is fixed at \(0\), the target is fixed at \(L>0\), and any finite initial position \(x\in\mathbb R\) is allowed.

For \(c\in(0,1)\), all finite hypo-Laplace convolution densities \(H_n\) are continuous and positive. Their infinite limit \(H_\infty\) is positive. The expected first hitting time is finite for every fixed initial point: the Lyapunov generator identity
\[
\mathcal L(x^2)=2D-r(1-a^2)x^2
\]
provides finite expected returns to a sufficiently large compact interval; a uniformly positive chance of an uninterrupted Brownian visit to \(L\) during a bounded time interval then gives finite mean hitting time by regeneration at compact returns.

## Proof

**1. Free resolvent.** Let \(u_s(x,z)=\int_0^\infty e^{-st}p_t(x,z)\,dt\) denote the transition-density resolvent before killing, with \(s>0\). Its Fourier transform in the terminal coordinate satisfies the backward resolvent equation
\[
(s+r-D\partial_{xx})\widehat u_s(k;x)=e^{ikx}+r\widehat u_s(k;ax).
\]
Expand the solution as \(\sum_{n\ge0} C_n(k)e^{ia^n kx}\). Matching each exponential yields \(C_0=(s+r+Dk^2)^{-1}\) and \(C_n=rC_{n-1}/(s+r+D a^{2n}k^2)\) for \(n\ge1\). Inverse Fourier transformation then gives, with \(q_s=\sqrt{(s+r)/D}\),
\[
u_s(x,z)=\frac{q_s}{s+r}\sum_{n=0}^\infty
\left(\frac r{s+r}\right)^n
H_n\bigl(q_s(z-a^n x)\bigr).
\]
Indeed, the \(n\)-th Fourier factor is \(e^{ia^n kx}\prod_{j=0}^n(1+c^{2j}k^2/q_s^2)^{-1}\); its inverse transform is the convolution of \(n+1\) symmetric Laplace densities at scales \(1,c,\dots,c^n\). The sum converges absolutely for \(s>0\).

**2. Hitting identity.** By the strong Markov property at the *actual* first visit to \(L\), and because the continuous Brownian component supplies local occupation density whereas jumps landing exactly at \(L\) have probability zero, the standard point-resolvent identity is
\[
\mathbb E_x e^{-s\tau_L}=\frac{u_s(x,L)}{u_s(L,L)}.
\]
The process is positive recurrent under the displayed Lyapunov drift and has unique stationary density \(q_0H_\infty(q_0 z)\), where \(q_0=\sqrt{r/D}\). Consequently
\[
\lim_{s\downarrow0}s\,u_s(L,L)=q_0H_\infty(b)>0.
\]
The formula for \(\mathbb E_x\tau_L\) follows by taking \(s\downarrow0\) in \((1-\mathbb E_xe^{-s\tau_L})/s\), provided the resolvent difference has a finite limit.

**3. Absolute convergence.** Every \(H_n\) is a convolution of the unit Laplace density \(e^{-|z|}/2\) with a probability distribution, so it is globally \(1/2\)-Lipschitz. Hence
\[
\left|H_n(b-a^n b)-H_n(b-a^n y)\right|
\leq\frac12c^n|b-y|.
\]
The same estimate, uniformly for \(s\) near zero in the scaled resolvent above, allows dominated convergence in the difference \(u_s(L,L)-u_s(x,L)\). Its limiting value equals \(\frac{q_0}{r}\sum_{n\ge0}[H_n(b-a^nb)-H_n(b-a^ny)]\), proving the first boxed formula.

**4. Finite elementary densities.** The Fourier transform \(\widehat H_n(k)=\prod_{j=0}^n(1+c^{2j}k^2)^{-1}\) has distinct simple poles at \(k=\pm i/c^j\). Its partial-fraction decomposition is
\[
\widehat H_n(k)=\sum_{j=0}^n\frac{\prod_{m\ne j}(1-c^{2(m-j)})^{-1}}{1+c^{2j}k^2}.
\]
Inverse Fourier transformation gives the displayed finite exponential formula.

**5. Certified error.** The numerator tail is bounded by summing the Lipschitz inequality, giving \(\epsilon_N(y)\). Write the infinite Laplace series as the independent sum through step \(N\) plus the remaining terms. Since \(H_N\) is \(1/2\)-Lipschitz and \(\mathbb E|Z_j|=1\),
\[
|H_\infty(b)-H_N(b)|\leq\frac12\sum_{j=N+1}^\infty c^j=\delta_N.
\]
When \(B_N>\delta_N\), positive-denominator interval arithmetic establishes the two-sided bound. Such \(N\) always exists because \(B_N\to H_\infty(b)>0\) and \(\delta_N\to0\).

## Verification

The standalone `verify.py` checks two independently implemented representations of the finite convolution densities: the finite residue formula and numerical inversion of their Fourier product. It then reconstructs the negative-rescaling boundary constant and checks that substituting it in Eq. (60) of the motivating source reproduces the independent series for the mean from \(x=0\). The positive-rescaling specialization checks Eq. (45) of that source, without claiming its rediscovery. Finally, different truncation depths are compared against the proved two-sided enclosures. Run with `python verify.py` using Python 3 and SciPy. These finite computations are reproducibility checks only; the all-parameter theorem is proved above.

For example, with \(D=L=r=1\), the analytic series gives \(\mathbb E_0\tau_L\approx1.347246602365\) and \(\kappa\approx1.678631096315\) at \(a=-1/2\); at \(a=-1/5\), the corresponding values are \(1.507352991068\) and \(1.428060607780\).

## Relationship to prior work

Biroli, Feld, Hartmann, Majumdar and Schehr (arXiv:2406.08387v1, Sec. II) derived the stationary density, and Secs. III.1–III.2 solved the mean hitting equation for nonnegative rescaling but retained the unknown constant \(\kappa\) for negative rescaling, calibrated numerically (their Eqs. (51)–(60)). Pierce (arXiv:2204.07215v1, Sec. IV.2) considered proportional resetting with a nonnegative multiplier and described difficulties in its first-passage equation. Singh and Pal (arXiv:2202.02715) treated first-passage functionals for resetting to a fixed location. The point-resolvent identity, Fourier inversion, and stationary Laplace-product representation are established methods, not novel claims. The contribution here is their explicit combination into an all-initial-position finite-exponential series **closing the negative-rescaling \(\kappa\) gap**, together with quantitative, purely geometric error bounds. The literature comparison is not a proof of global priority.

## Limitations

The coefficient bounds can be numerically ill-conditioned near \(c=1\), because the finite partial fractions contain cancellation; higher precision may be required even though the analytical bounds remain valid. The result excludes \(|a|\ge1\), non-Poisson reset times, random multipliers and first *crossing* by discontinuous jumps as an absorbing rule. The expression determines a mean first-passage time, not the entire first-passage distribution or an optimal resetting rate. No claim is made of an independently audited proof or an exhaustive literature search.

## References

- M. Biroli, Y. Feld, A. K. Hartmann, S. N. Majumdar, G. Schehr, *Resetting by rescaling: exact results for a diffusing particle in one-dimension*, arXiv:2406.08387v1 (first posted 2024-06-12), https://arxiv.org/html/2406.08387v1.
- J. K. Pierce, *An advection-diffusion process with proportional resetting*, arXiv:2204.07215v1 (first posted 2022-04-14), https://arxiv.org/html/2204.07215v1.
- P. Singh, A. Pal, *First-passage Brownian functionals with stochastic resetting*, arXiv:2202.02715 (first posted 2022-02-06), https://arxiv.org/abs/2202.02715.
