# A universal integrated fluctuation–response anomaly in an intermittently switched harmonic trap

## Finding

Let a Brownian particle experience a harmonic trap that alternates between completely off and on. In the stationary state its (unperturbed) autocovariance \(C(t)\) and its additive-force impulse response \(R(t)\) have an explicit, strictly positive nonequilibrium fluctuation–response gap for every \(t>0\):

\[
G(t):=-\frac{C'(t)}{D}-R(t)
=\frac{k}{2\Omega}\left(e^{-\lambda_-t}-e^{-\lambda_+t}\right)>0,
\qquad \Omega=\sqrt{k^2+4s^2},\quad
\lambda_\pm=\frac{k+2s\pm\Omega}{2}.
\]

For all \(k,s,D>0\), the gap has a **universal integrated sum rule**,
\[
\int_0^\infty G(t)\,dt=\frac{1}{2s},\qquad G'(0^+)=\frac{k}{2}.
\]
Consequently, the entire switching rate and the on-state relaxation strength can be reconstructed from the discrepancy between position correlations and force response:
\[
s=\left(2\int_0^\infty G(t)\,dt\right)^{-1},
\qquad k=2G'(0^+).
\]
The gap has precisely one maximum, at
\[
t_*=\frac{1}{\Omega}\log\frac{\lambda_+}{\lambda_-}>0,
\qquad
G(t_*)=\frac{k}{2\lambda_+}\left(\frac{\lambda_-}{\lambda_+}\right)^{\lambda_-/\Omega}.
\]
The gap and its maximizing lag are independent of the thermal noise amplitude \(D\). In particular, no finite positive switching rate restores the equilibrium formula at all positive lags.

## Assumptions and scope

Fix \(k,s,D>0\). Let \(J_t\in\{1,0\}\) be a stationary, symmetric two-state continuous-time Markov chain with jump rate \(s\) in each direction. The independent standard Brownian motion \(W_t\) drives
\[
dX_t=-kJ_tX_t\,dt+\sqrt{2D}\,dW_t.
\]
The trap is present at \(J_t=1\) and absent at \(J_t=0\). Time is continuous and \(t\ge0\). The mobility multiplying a small applied additive force is normalized to one, so \(D\) is the corresponding equilibrium thermal scale. Define \(C(t)=\mathbb E[X_tX_0]\) with the joint process in its unique stationary distribution. The stationary mean is zero.

To define the causal impulse response, perturb position by an infinitesimal \(h\) at time zero without changing \(J\), equivalently apply an additive force impulse of area \(h\):
\[
R(t)=\lim_{h\to0}\frac{\mathbb E[X_t^{(h)}]-\mathbb E[X_t]}{h},\qquad t\ge0.
\]
This is an *unconditioned* response averaged over the stationary trap state; it is not a response to perturbing the switching clock. The equilibrium comparison identity would be \(R(t)=-C'(t)/D\); the theorem quantifies its violation for the nonequilibrium switching model.

## Proof

**Existence and stationary second moments.** With the telegraph environment defined for all real times, the stationary solution is the past stochastic convolution
\[
X_t=\sqrt{2D}\int_{-\infty}^t
\exp\!\left[-k\int_u^t J_v\,dv\right]dW_u.
\]
The ergodic telegraph process spends half its time in the on state. More quantitatively, the Feynman–Kac generator below has two strictly negative eigenvalues, so the expected squared kernel decays exponentially with backward duration, ensuring \(L^2\) convergence. Coupling a solution with any square-integrable initial condition to the same driving noises makes the difference decay by that kernel, giving uniqueness of the stationary law and vanishing stationary mean.

Put \(q_i=\mathbb E[X_0^2\mathbf 1_{\{J_0=i\}}]\). Stationarity of the generator applied to \(x^2\mathbf 1_{\{j=i\}}\) gives
\[
0=-2kq_1+D+s(q_0-q_1),\qquad 0=D+s(q_1-q_0).
\]
(The \(D\) in each equation equals \(2D\mathbb P(J=i)\), and each state has probability \(1/2\).) Hence
\[
q_1=\frac{D}{k},\qquad q_0=\frac{D}{k}+\frac{D}{s},\qquad C(0)=\frac{2D}{k}+\frac{D}{s}.
\]

**Conditional propagation.** For \(i=1,0\), define \(\phi_i(t)=\mathbb E[\exp(-k\int_0^tJ_v\,dv)\mid J_0=i]\). The finite-state Feynman–Kac equations read
\[
\begin{pmatrix}\phi_1'\\\phi_0'\end{pmatrix}
=A\begin{pmatrix}\phi_1\\\phi_0\end{pmatrix},\qquad
A=\begin{pmatrix}-(k+s)&s\\s&-s\end{pmatrix},\qquad
\phi_1(0)=\phi_0(0)=1.
\]
The eigenvalues are \(-\lambda_-\) and \(-\lambda_+\), since the trace is \(-(k+2s)\), the determinant is \(ks>0\), and the discriminant is \(\Omega^2=k^2+4s^2\). In particular, \(0<\lambda_-<\lambda_+\).

The additive impulse evolves by exactly the homogeneous propagator; therefore
\[
R(t)=\frac{\phi_1(t)+\phi_0(t)}{2}.
\]
Independence of future Brownian increments from the past, conditional on \(J_0\), similarly gives
\[
C(t)=q_1\phi_1(t)+q_0\phi_0(t).
\]
The row vector of stationary partial moments has the exact cancellation
\[
-\frac1D\begin{pmatrix}q_1&q_0\end{pmatrix}A
=\begin{pmatrix}0&1\end{pmatrix}.
\]
Consequently, for all \(t\ge0\),
\[
-\frac{C'(t)}D=\phi_0(t),\qquad
G(t)=\frac{\phi_0(t)-\phi_1(t)}2.
\]
This identifies the normalized correlation derivative with the *off-conditioned* impulse response, while the physical response averages equally over on and off initial states.

**Strict sign and explicit gap.** Put \(\delta(t)=\phi_0(t)-\phi_1(t)\). The two backward equations imply
\[
\delta''+(k+2s)\delta'+ks\delta=0,
\qquad \delta(0)=0,\quad\delta'(0)=k.
\]
Its unique solution is
\[
\delta(t)=\frac{k}{\Omega}\left(e^{-\lambda_-t}-e^{-\lambda_+t}\right).
\]
Because \(k>0\) and \(0<\lambda_-<\lambda_+\), it is strictly positive for every \(t>0\). Dividing by two proves the stated formula. Differentiation at zero yields \(G'(0^+)=k/2\).

**Sum rule, identification, and unique maximum.** Direct integration and \(\lambda_-\lambda_+=ks\) give
\[
\int_0^\infty G(t)\,dt
=\frac{k}{2\Omega}\left(\frac1{\lambda_-}-\frac1{\lambda_+}\right)
=\frac1{2s}.
\]
This proves both reconstruction formulas. For the peak, \(G'(t)\) has the sign of \(\lambda_+e^{-\lambda_+t}-\lambda_-e^{-\lambda_-t}\). The ratio of these two terms is \((\lambda_+/\lambda_-)e^{-\Omega t}\), which decreases strictly from a number greater than one to zero. There is therefore exactly one critical point, the given \(t_*\), and it is the global maximum because \(G(0)=\lim_{t\to\infty}G(t)=0\). Inserting \(e^{-\Omega t_*}=\lambda_-/\lambda_+\) gives the stated maximum.

**Regime checks.** With \(k\) fixed, slow switching \(s\downarrow0\) yields \(t_*\sim k^{-1}\log(k/s)\) and \(G(t_*)\to1/2\). Fast switching \(s\to\infty\) yields \(t_*\sim(2s)^{-1}\log(4s/k)\) and \(G(t_*)\sim k/(4s)\). These follow by expanding the two exact positive roots; neither endpoint is included in the theorem's parameter domain.

## Verification

The accompanying `verification/check_fdt.py` evaluates the generator and stationary-moment cancellation by exact symbolic algebra, confirms the response/correlation derivative identity through sixteen Taylor orders, and compares the closed form with 168 high-precision matrix-exponential evaluations for seven positive parameter triples and eight time lags. Fourteen onset/integral identities and 42 strict-maximum comparisons are also checked. The universal proof above does not rely on finite testing.

For a simple exact check, choose \(k=3\), \(s=2\), \(D=5\), for which \(\Omega=5\), \(\lambda_-=1\), \(\lambda_+=6\). The formulas reduce to
\[
C(t)=6e^{-t}-\tfrac16e^{-6t},\quad
R(t)=\tfrac1{10}(9e^{-t}+e^{-6t}),\quad
G(t)=\tfrac3{10}(e^{-t}-e^{-6t}).
\]
The gap integrates to \(1/4\) and is maximized at \(t_*=(\log6)/5\).

## Relationship to prior work

Santra, Das and Nath (2021, arXiv:2104.00609) introduce the same switching-on/off harmonic Brownian dynamics, derive the time-dependent one-time variance and stationary distribution limits, and analyze first-passage properties. The current proof uses their model and does not claim those results as new. Alston, Cocconi and Bertrand (2022, arXiv:2202.02630) treat the same intermittent potential and establish stationary entropy-production laws; their key fully intermittent result is an entropy-production rate, not a two-time force-response law. Frydel (2024, arXiv:2407.12213) provides a stationary Gaussian-mixture representation and stationary moments, again not an explicit comparison of stationary position correlations and impulse response.

Di Terlizzi, Baiesi and Ritort (2024, arXiv:2403.10442) develop general nonequilibrium fluctuation/variance sum rules, but their example called a 'stochastic switching trap' switches the *trap center at fixed stiffness* rather than switching stiffness between zero and \(k\). These general fluctuation–response identities may provide an alternative derivation in principle; the specific off-conditioned identity, positive gap, universal integral and unique peak are the contribution here. An application of general response theory could implicitly cover the theorem without using the same formulation; priority is not independently certified.

## Limitations

The theorem is specific to symmetric exponential on/off times, a one-dimensional linear trap, constant additive thermal noise, and an impulse that leaves the trap-state process unchanged. It does not establish a comparable sign or sum rule for asymmetric switching, nonexponential dwell times, spatially varying mobilities, or arbitrary nonlinear confinement. Only self-review has been conducted; no independent audit or experimental validation has been performed. The measured gap is a two-observable comparison and its reconstruction assumes continuous-lag access and an accurately calibrated diffusivity.

## References

1. I. Santra, S. Das and S. K. Nath, *Brownian motion under intermittent harmonic potentials*, arXiv:2104.00609, first public 2021-04-01, https://arxiv.org/abs/2104.00609.
2. H. Alston, L. Cocconi and T. Bertrand, *Non-equilibrium thermodynamics of diffusion in fluctuating potentials*, arXiv:2202.02630, first public 2022-02-05, https://arxiv.org/abs/2202.02630.
3. I. Di Terlizzi, M. Baiesi and F. Ritort, *Variance sum rule: proofs and solvable models*, arXiv:2403.10442, first public 2024-03-15, https://arxiv.org/abs/2403.10442.
4. D. Frydel, *Statistical mechanics of passive Brownian particles in a fluctuating harmonic trap*, arXiv:2407.12213, first public 2024-07-16, https://arxiv.org/abs/2407.12213.
