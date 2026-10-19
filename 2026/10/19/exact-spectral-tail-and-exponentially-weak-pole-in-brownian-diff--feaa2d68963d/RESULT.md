# Exact spectral tail and exponentially weak pole in Brownian diffusion with refreshed reset rates

## Finding

Consider one-dimensional Brownian diffusion of generator \(D\partial_{xx}\), with \(D>0\). Independently of the Brownian motion, a stationary positive resetting intensity \(\Lambda_t\) is held constant between rate-\(\mu>0\) Poisson refresh times and redrawn at each refresh from the exponential distribution of mean \(a>0\). Conditional on this intensity, resets of the position to zero have hazard \(\Lambda_t\); resetting does not change the intensity. Let \(p_\mu(x)\) be the unique stationary position density.

Put
\[
\phi_a(u)=\int_0^\infty\frac{e^{-\lambda/a}}{a(\lambda+u)}\,d\lambda
=\frac{e^{u/a}}a E_1(u/a),\qquad u>0,
\]
where \(E_1(z)=\int_z^\infty e^{-v}dv/v\). There is exactly one \(u_\mu\in(0,\mu)\) satisfying \(\mu\phi_a(u_\mu)=1\). Define
\[
\theta_\mu=\mu-u_\mu,\qquad
w_\mu=\frac{a u_\mu}{\mu\theta_\mu},\qquad
\kappa_\mu=\sqrt{\theta_\mu/D}.
\]
For every \(\mu,a,D>0\), \(0<\theta_\mu<\min\{a,\mu\}\) and \(0<w_\mu<1\). The exact far-field asymptotic, including its positive leading coefficient, is
\[
\boxed{\displaystyle
p_\mu(x)\sim \frac{w_\mu\kappa_\mu}{2}
\exp(-\kappa_\mu |x|)\quad(|x|\to\infty).}
\]
The function \(\theta_\mu\) is continuously differentiable and strictly increasing, and satisfies the exact spectral-response identity
\[
\boxed{\displaystyle \frac{d\theta_\mu}{d\mu}=1-w_\mu\in(0,1).}
\]
With \(\gamma_E\) denoting the Euler--Mascheroni constant, the slow-refresh regime \(\mu/a\to0\) obeys
\[
\boxed{\displaystyle
u_\mu=\mu-\theta_\mu
=a\exp(-a/\mu-\gamma_E)(1+o(1)),\qquad
w_\mu=\frac{a^2}{\mu^2}\exp(-a/\mu-\gamma_E)(1+o(1)).}
\]
In particular \(\theta_\mu\sim\mu\), although the exact isolated-mode coefficient becomes exponentially small. In the opposite, fast-refresh limit \(\mu/a\to\infty\),
\[
\theta_\mu=a-\frac{a^2}{\mu}+O(a^3/\mu^2),\qquad
w_\mu=1-\frac{a^2}{\mu^2}+O(a^3/\mu^3).
\]

This exact extreme-tail rate differs parametrically from the decay rate suggested by matching the stationary variance. If \(V_\mu=\mathbb E[X^2]\) and \(\lambda_{\mathrm{var}}=2D/V_\mu\), then
\[
\lambda_{\mathrm{var}}\sim\frac{a}{\log(a/\mu)},\qquad
\frac{\theta_\mu}{\lambda_{\mathrm{var}}}\to0
\quad(\mu/a\to0).
\]
Thus a variance-matched exponential profile does not predict the ultimate spatial tail in the slow-refresh regime. The order of limits matters: for any fixed positive refresh rate, the far tail is exponential, whereas at zero refresh rate the stationary environment-averaged mixture has an algebraic tail.

## Assumptions and scope

All statements concern the explicitly specified continuous-state Markov-modulated resetting model. Independent Brownian increments have conditional variance \(2D\,dt\). The environmental refresh clock has rate \(\mu\), each newly drawn intensity has density \(a^{-1}e^{-\lambda/a}\) on \(\lambda>0\), and resets occur according to a conditionally Poisson process with time-dependent intensity \(\Lambda_t\). Neither a positional reset nor Brownian motion changes the environmental intensity. The result concerns the stationary *one-point marginal* of the position, not first-passage times, currents, or a nonstationary initial environment.

The stationary construction is well-defined because the stationary refresh process is ergodic with positive mean intensity, so the integrated reset hazard diverges almost surely into the past. The results quantify the strict \(|x|\to\infty\) tail for each fixed \(\mu>0\); they are not a uniform approximation at spatial distances of order \(\sqrt{D/\mu}\) as \(\mu\downarrow0\).

## Proof

**1. Past no-reset probability and the exact transform.** Let \(f_a(\lambda)=a^{-1}e^{-\lambda/a}\), and equip \(L^2(f_a\,d\lambda)\) with its usual real inner product. Let \(P h=\int h(\lambda)f_a(\lambda)d\lambda\) be the projection onto constants, and put
\[
T_\mu h(\lambda)=\lambda h(\lambda)+\mu(h(\lambda)-P h).
\]
This is a nonnegative self-adjoint operator, a bounded rank-one perturbation of multiplication by \(\lambda+\mu\). The stationary probability of *no* positional reset in an interval of length \(t\) equals, by Feynman--Kac for the reversible refresh process,
\[
S_\mu(t)=\mathbb E\exp\left(-\int_0^t\Lambda_s\,ds\right)
=\langle1,e^{-tT_\mu}1\rangle.
\]
The spectral theorem supplies a probability measure \(\nu_\mu\) on \([0,\infty)\) with
\(S_\mu(t)=\int e^{-st}\nu_\mu(ds)\). Its Stieltjes transform is, by the rank-one resolvent identity,
\[
H_\mu(z):=\int\frac{\nu_\mu(ds)}{s+z}
=\frac{\phi_a(\mu+z)}{1-\mu\phi_a(\mu+z)},\qquad z>0.
\]
Consequently the stationary characteristic function, either by the stationary backward reset age or by direct renewal conditioning, is
\[
\widehat p_\mu(k)
=1-Dk^2 H_\mu(Dk^2)
=\frac{1-(\mu+Dk^2)\phi_a(\mu+Dk^2)}
{1-\mu\phi_a(\mu+Dk^2)}.
\]
This transform is the known finite-parameter expression; no novelty is asserted for it.

**2. Unique isolated rate and its mass.** The strictly decreasing map \(u\mapsto\phi_a(u)\) diverges at zero and satisfies \(\mu\phi_a(\mu)<1\), giving a unique root \(u_\mu\in(0,\mu)\). The function \(h_\mu(\lambda)=(\lambda+u_\mu)^{-1}\) is an eigenfunction of \(T_\mu\) with eigenvalue \(\theta_\mu=\mu-u_\mu\). The essential spectrum of \(T_\mu\) is \([\mu,\infty)\); this is the unique isolated eigenvalue because the rank-one secular equation has exactly one root below \(\mu\). The constant function has squared normalized overlap
\[
w_\mu
=\frac{\phi_a(u_\mu)^2}{\int (\lambda+u_\mu)^{-2}f_a(\lambda)d\lambda}
=-\frac1{\mu^2\phi_a'(u_\mu)}.
\]
Differentiating \(\phi_a(u)=a^{-1}e^{u/a}E_1(u/a)\) gives
\(\phi_a'(u)=\phi_a(u)/a-1/(au)\). Inserting \(\phi_a(u_\mu)=1/\mu\) yields the exact formula \(w_\mu=a u_\mu/(\mu\theta_\mu)\). The overlap is strictly between zero and one because \(h_\mu\) is strictly nonconstant. Jensen's strict inequality \(\phi_a(u)>1/(u+a)\) shows \(\theta_\mu<a\). Differentiating the secular equation yields \(\theta_\mu'=1-w_\mu\), establishing monotonicity and the response identity.

**3. Complete spectral-mixture density and the far tail.** For \(y>0\), define
\[
A_a(y)=-\frac{e^{-y/a}}{a}\operatorname{Ei}(y/a),\qquad
b_a(y)=\frac{e^{-y/a}}{a}.
\]
The boundary value \(\phi_a(-y+i0)=A_a(y)-i\pi b_a(y)\), followed by Stieltjes inversion, gives the absolutely continuous part of the spectral measure at \(s=\mu+y\):
\[
\frac{d\nu_\mu(\mu+y)}{dy}
=\frac{b_a(y)}{[1-\mu A_a(y)]^2+[\pi\mu b_a(y)]^2}.
\]
The remaining mass is precisely the isolated atom \(w_\mu\delta_{\theta_\mu}\). No other atom is possible, and the total spectral mass is one because \(S_\mu(0)=1\). Given a spectral rate \(s>0\), the stationary Brownian position contribution is a centered Laplace density \(\frac12\sqrt{s/D}e^{-|x|\sqrt{s/D}}\). Therefore the *exact* stationary density is
\[
\begin{aligned}
p_\mu(x)={}&\frac{w_\mu\kappa_\mu}{2}e^{-\kappa_\mu|x|}\\
&+\frac12\int_0^\infty\sqrt{\frac{\mu+y}{D}}
\exp\left(-|x|\sqrt{\frac{\mu+y}{D}}\right)
\frac{b_a(y)\,dy}{[1-\mu A_a(y)]^2+[\pi\mu b_a(y)]^2}.
\end{aligned}
\]
Since \(\theta_\mu<\mu\), the continuum has a strictly faster spatial exponential rate. Indeed, for \(|x|\ge\sqrt{D/\mu}\), the function \(s\mapsto\sqrt{s/D}\exp(-|x|\sqrt{s/D})\) decreases on \([\mu,\infty)\), so the second term is bounded above by \(\frac12(1-w_\mu)\sqrt{\mu/D}\exp(-|x|\sqrt{\mu/D})\). Dividing this by the positive isolated term proves the displayed sharp far-field asymptotic.

**4. Singular slow-refresh and regular fast-refresh limits.** The standard small-argument expansion
\(e^tE_1(t)=-\gamma_E-\log t+O(t|\log t|)\) applied to \(\mu\phi_a(u_\mu)=1\) yields
\(u_\mu/a=\exp(-a/\mu-\gamma_E)(1+o(1))\). Substitution in the exact weight formula gives the slow-refresh asymptotics. For large \(u\),
\(\phi_a(u)=u^{-1}-au^{-2}+2a^2u^{-3}-6a^3u^{-4}+O(a^4u^{-5})\). Inverting the secular equation through this order yields
\(u_\mu=\mu-a+a^2/\mu-2a^3/\mu^2+O(a^4/\mu^3)\); substituting this into the exact expressions for both \(\theta_\mu\) and \(w_\mu\) gives the displayed fast-refresh laws. Finally, the stationary variance is
\[
V_\mu=2D H_\mu(0)
=\frac{2D\phi_a(\mu)}{1-\mu\phi_a(\mu)}
\sim\frac{2D}{a}\log(a/\mu)
\quad(\mu/a\to0).
\]
This proves the separation between its inverse-variance proxy and the true tail rate.

## Verification

The supplementary standalone program `verify.py` runs deterministic high-precision tests against the explicit exponential-integral secular equation. It checks root existence intervals, eigenweight bounds and residues, Fourier-transform identities, the spectral measure normalization and reconstruction of the resolvent by numerical quadrature, the response identity by independent symmetric differences, and both asymptotic regimes. On the stated execution environment it passed **125 checks**. These finite computations corroborate but do not replace the analytic argument.

## Relationship to prior work

Arutkin and Reuveni (2025), *Diffusion with doubly stochastic resetting*, introduce precisely the exponential-rate-refresh model and derive its complete stationary Fourier transform (their Eqs. (23) and (24)). They describe qualitative spatial crossovers and infer an effective exponential scale from low-wave-number expansions. The transform, stationarity framework, and the existence of an eventual exponential region are therefore prior work. What is isolated here is the exact *ultimate* spatial decay pole, its residue and positive continuous spectral remainder, an exact sensitivity law, and the exponentially small slow-refresh eigenmode. These show why a low-wave-number or second-moment scale need not identify the strict far-field exponent.

Rose, Touchette, Lesanovsky, and Garrahan (2018) establish spectral formulas for resetting with a constant, state-independent reset rate; their generator shift does not directly supply the Markov-modulated, intensity-dependent killing eigenvalue or its singular refresh-rate scaling. The classical constant-rate model of Evans and Majumdar (2011) is an additional baseline. The exact transform of the 2025 source implicitly determines all stationary observables, so implicit coverage by a suitably general spectral singularity analysis remains an originality risk; no claim is made that the underlying model or transform is new.

## Limitations

The law assumes an exponential distribution of environmental intensities, an independent Poisson rate-refresh clock, a conditionally Poisson positional resetting clock, and a one-dimensional Brownian displacement with constant diffusivity. The leading asymptotic is for fixed positive \(\mu\) followed by \(|x|\to\infty\). Because \(w_\mu\) is exponentially small at slow refresh, the theorem does not identify a uniform finite-distance crossover threshold or claim that the ultimate mode is experimentally visible at moderate positions. No first-passage or higher-dimensional theorem is established. Independent scientific validation has not been performed.

## References

1. M. Arutkin and S. Reuveni, *Diffusion with doubly stochastic resetting* (2025), arXiv:2509.25365v1, https://arxiv.org/abs/2509.25365 (initial public posting: 2025-09-29).
2. D. C. Rose, H. Touchette, I. Lesanovsky, and J. P. Garrahan, *Spectral properties of simple classical and quantum reset processes*, Physical Review E **98**, 022129 (2018), arXiv:1806.01298, https://arxiv.org/html/1806.01298v2.
3. M. R. Evans and S. N. Majumdar, *Diffusion with Stochastic Resetting*, Physical Review Letters **106**, 160601 (2011), https://doi.org/10.1103/PhysRevLett.106.160601.
