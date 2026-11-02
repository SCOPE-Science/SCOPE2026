# Exact autocorrelation and a one-minimum phase diagram for OU-squared confinement

## Finding
Consider a harmonically confined diffusion whose restoring stiffness itself follows an Ornstein–Uhlenbeck (OU) process. The exact stationary **two-time position covariance** can be expressed through one positive Laplace integral. Its ratio to stationary variance times the averaged impulse response increases strictly with time. In addition, after removal of the dominant exponential relaxation, the covariance has a complete three-regime shape classification: increasing, decreasing, or decreasing to exactly one minimum and then increasing. Two explicit, strictly ordered critical parameters separate these regimes.

Define, for \(A,b,\mu>0\),
\[
I_\mu(A,b)=\int_0^\infty \exp\!\left[-As-b(1-e^{-\mu s})\right]ds,\qquad
M_\mu(A,b)=\frac{\int_0^\infty(1-e^{-\mu s})e^{-As-b(1-e^{-\mu s})}\,ds}{I_\mu(A,b)}.
\]
Set \(d=D_k/\mu^3\), \(A=2\kappa-4D_k/\mu^2\), and \(\lambda=\kappa-D_k/\mu^2\). For every \(t\ge0\), the stationary position covariance satisfies
\[
\boxed{C(t)=2D_x\,e^{-\lambda t-d(1-e^{-\mu t})}\,I_\mu\bigl(A,2d(1+e^{-\mu t})\bigr).}
\]
The averaged linear impulse response is \(G(t)=e^{-\lambda t-d(1-e^{-\mu t})}\). Consequently,
\[
\boxed{\frac{C(t)}{C(0)G(t)}=\frac{I_\mu(A,2d(1+e^{-\mu t}))}{I_\mu(A,4d)}>1\quad (t>0),}
\]
and this ratio increases strictly from \(1\) to \(I_\mu(A,2d)/I_\mu(A,4d)>1\).

For each fixed \(d>0\) define \(a_-(d),a_+(d)\) uniquely by
\[
M_\mu(\mu a_-(d),4d)=\tfrac12,\qquad
M_\mu(\mu a_+(d),2d)=\tfrac12.
\]
These numbers do not depend on the choice of \(\mu\), and \(0<a_-(d)<a_+(d)<\infty\). For \(a=A/\mu\), the **envelope** \(E(t)=e^{\lambda t}C(t)\), at positive lag, is:

- strictly increasing if \(0<a\le a_-(d)\);
- strictly decreasing then strictly increasing, with exactly one finite, strict minimum, if \(a_-(d)<a<a_+(d)\);
- strictly decreasing if \(a\ge a_+(d)\).

There is no regime with a local maximum. The limiting envelope is \(E_\infty=2D_x e^{-d}I_\mu(A,2d)\), and as \(t\to\infty\),
\[
\frac{E(t)}{E_\infty}=1+d[1-2M_\mu(A,2d)]e^{-\mu t}+O(e^{-2\mu t}).
\]
Precisely at \(a=a_+(d)\), this leading term vanishes and the first nonzero correction is
\[
\frac{E(t)}{E_\infty}=1+2d^2\operatorname{Var}_{A,2d}(1-e^{-\mu S})e^{-2\mu t}+O(e^{-3\mu t}),
\]
where \(S\) has density \(e^{-As-2d(1-e^{-\mu s})}/I_\mu(A,2d)\) on \((0,\infty)\). Its variance is strictly positive. In the weak stiffness-noise limit \(d\downarrow0\), the critical values obey
\[
a_-(d)=1-\tfrac43d+O(d^2),\qquad a_+(d)=1-\tfrac23d+O(d^2).
\]

## Assumptions and scope
Let \(B^x\) and \(B^k\) be independent standard Brownian motions on a two-sided stationary construction. Let \(\mu,D_x,D_k>0\), and assume \(\kappa>2D_k/\mu^2\). The model is
\[
dX_t=-(\kappa+K_t)X_t\,dt+\sqrt{2D_x}\,dB^x_t,\qquad
dK_t=-\mu K_t\,dt+\sqrt{2D_k}\,dB^k_t.
\]
The stiffness fluctuation \(K_t\) is stationary, centered Gaussian, with \(\mathbb E[K_uK_v]=(D_k/\mu)e^{-\mu|u-v|}\). The position is the stationary causal stochastic convolution; \(C(t)=\mathbb E[X_0X_t]\), with zero stationary position mean. Positivity of \(A=2\kappa-4D_k/\mu^2\) is exactly the finite-position-variance regime. All statements concern the exact overdamped two-noise model, not a mean-field or discrete-time approximation. An OU stiffness may temporarily be negative; the assumption on \(\kappa\) enforces stationary second-moment integrability, not pointwise positive stiffness.

## Proof
**1. Stationary convolution and Gaussian overlaps.** By variation of constants and independence of the positional driving noise,
\[
X_0=\sqrt{2D_x}\int_{-\infty}^0\exp\!\left[-\kappa(0-u)-\int_u^0K_v\,dv\right]dB^x_u.
\]
Define \(I_s=\int_{-s}^0K_v\,dv\) and \(J_t=\int_0^tK_v\,dv\). The future positional-noise increment contributes zero to \(\mathbb E[X_0X_t]\) conditional on the entire stiffness history; therefore
\[
C(t)=2D_x\int_0^\infty e^{-\kappa(2s+t)}\,\mathbb E[e^{-2I_s-J_t}]\,ds.
\]
With \(d=D_k/\mu^3\), direct integration of the OU covariance gives
\[
\operatorname{Var}(I_s)=\frac{2D_k}{\mu^2}s-2d(1-e^{-\mu s}),\quad
\operatorname{Var}(J_t)=\frac{2D_k}{\mu^2}t-2d(1-e^{-\mu t}),
\]
\[
\operatorname{Cov}(I_s,J_t)=d(1-e^{-\mu s})(1-e^{-\mu t}).
\]
For centered jointly Gaussian \((I_s,J_t)\), the expectation of \(e^{-2I_s-J_t}\) is the exponential of half the variance of \(2I_s+J_t\). Substitution and collection of the \(s\)- and \(t\)-dependent terms give the boxed formula. In particular, \(C(0)=2D_xI_\mu(A,4d)\). Since the integral's large-\(s\) integrand is asymptotic to a positive constant times \(e^{-As}\), stationary variance is finite exactly when \(A>0\). In this regime the defining convolution converges in second moment and gives the stationary solution.

**2. Response and strict correlation excess.** The averaged response to an infinitesimal positional impulse, holding the stiffness process fixed, is \(G(t)=\mathbb E\exp(-\kappa t-J_t)\), yielding the stated expression by the one-dimensional Gaussian moment formula. For fixed \(A>0\), \(I_\mu(A,b)\) decreases strictly with \(b\), since its derivative is minus the integral of the strictly positive function \(1-e^{-\mu s}\) against the integrand. The function \(2d(1+e^{-\mu t})\) decreases strictly from \(4d\) to \(2d\); hence the ratio is strictly increasing and exceeds one for every positive \(t\).

**3. Unique thresholds.** Introduce the probability density
\[
p_{A,b}(s)=I_\mu(A,b)^{-1}\exp[-As-b(1-e^{-\mu s})],\quad s>0,
\]
and set \(h(s)=1-e^{-\mu s}\). Differentiating normalized expectations gives
\[
\partial_A M_\mu(A,b)=-\operatorname{Cov}_{A,b}(S,h(S))<0,
\qquad
\partial_b M_\mu(A,b)=-\operatorname{Var}_{A,b}(h(S))<0.
\]
The strict signs hold because \(h\) is strictly increasing and the density is positive on \((0,\infty)\). As \(A\downarrow0\), \(M_\mu(A,b)\to1\), since \(S\) escapes to infinity under the normalized long-tail distribution; as \(A\uparrow\infty\), \(M_\mu(A,b)\to0\), because \(S\to0\) in probability. Both limits hold at each fixed finite \(b\). Thus the two equations defining the threshold values have unique positive solutions. The strict decrease in \(b\) implies \(a_-<a_+\). Replacing \(u=\mu s\) shows that their definitions depend only on \(a=A/\mu\) and \(d\).

**4. Single-minimum classification.** Differentiate the exact covariance envelope with respect to \(t\), writing \(y=e^{-\mu t}\). Since \(\partial_b\log I_\mu(A,b)=-M_\mu(A,b)\),
\[
\frac{E'(t)}{E(t)}=d\mu y[2M_\mu(A,2d(1+y))-1].
\]
The bracket is **strictly increasing** as \(t\) increases, because its \(b\) argument strictly decreases and \(M\) decreases strictly in \(b\). At \(t=0\) it has the sign of \(M_\mu(A,4d)-1/2\), and as \(t\to\infty\) its sign is determined by \(M_\mu(A,2d)-1/2\). Using the two unique thresholds gives the three cases in the finding and proves uniqueness and strictness of the finite minimum in the intermediate regime. Equality at either critical threshold gives strict monotonicity for every \(t>0\) by strictness of \(\partial_bM\).

**5. Long-lag and weak-noise boundaries.** Divide the envelope by its limit and express it as the exact bounded moment-generating function
\[
\frac{E(t)}{E_\infty}
=\mathbb E_{A,2d}\left[e^{d e^{-\mu t}(1-2h(S))}\right].
\]
Taylor expansion is uniform, since \(|1-2h|\le1\); it gives the stated first-order correction. At \(a=a_+(d)\), \(\mathbb E_{A,2d}h=1/2\), so the linear term vanishes and the positive second-order coefficient is \(2d^2\operatorname{Var}_{A,2d}(h)\). Finally, put \(a=A/\mu\) and \(U=e^{-\mu S}\). At \(d=0\), \(U\) has density \(a u^{a-1}\) on \((0,1)\), and each threshold corresponds to \(\mathbb E U=1/2\) for tilt \(e^{bu}\), with \(b=4d\) and \(b=2d\), respectively. At \(a=1,b=0\), \(\partial_a\mathbb E U=1/4\) and \(\partial_b\mathbb E U=1/12\). The implicit function theorem gives \(a=1-b/3+O(b^2)\), proving the two weak-noise expansions.

## Verification
`VERIFY.py` supplies numerical consistency checks independent of several analytic manipulations. It compares 81 direct positive quadratures of \(I_\mu\) and its tilted mean against confluent hypergeometric evaluations, checks threshold ordering and all three envelope shapes at four noise strengths, tests the weak-noise and large-lag asymptotics, and independently samples stationary OU stiffness paths while analytically integrating out positional Brownian noise. These finite checks corroborate the exact identities but do not replace the preceding proof. Execute with `python VERIFY.py` using NumPy and SciPy.

## Relationship to prior work
Cocconi, Alston, Romano, and Bertrand (2024) introduced and analyzed the \(\mathrm{OU}^2\) confinement model, including the averaged impulse response and stationary moments. Those are prior results. Their zero-lag variance and averaged Green function cannot simply be multiplied to obtain the two-time covariance, because \(X_0^2\) is correlated with the **future** stochastic stiffness. The new Gaussian cross-interval term produces the exact time-dependent integral argument and underlies the excess-correlation inequality and two-threshold envelope phase diagram.

Gupta and Klapp (2025) analyze related stochastic harmonic stiffness, with emphasis on one-time distributions, moments, and energetic properties. Ferraro and collaborators (2024) study a different many-particle annealed-disorder linear model with an effective self-consistent colored-noise structure. Neither is the same exact scalar multiplicative-OU stiffness covariance and envelope classification, in the material inspected. General Feynman–Kac Gaussian-functional identities motivate the calculation and are not claimed as new.

## Limitations
The statements require independent thermal and stiffness noises, stationary OU stiffness, overdamped harmonic confinement, and \(\kappa>2D_k/\mu^2\). They do not cover nonlinear traps, correlated driving noises, all higher-order correlations, or situations without finite stationary variance. The envelope minimum is a property of \(e^{\lambda t}C(t)\), **not** a minimum of the covariance \(C(t)\) itself. The exact mathematical theorem does not establish priority over all possible unpublished or differently formulated results, nor does it constitute an independent scientific audit.

## References
1. L. Cocconi, L. Alston, M. C. Romano, and T. Bertrand, *The OU² process: Characterising dissipative confinement in noisy traps* (first preprint May 15, 2024), arXiv:2405.09460v1, https://arxiv.org/abs/2405.09460.
2. R. Gupta and S. H. L. Klapp, *Nonequilibrium fluctuations in a harmonic trap with annealed stochastic stiffness* (2025), arXiv:2507.20915, https://arxiv.org/abs/2507.20915.
3. F. Ferraro and collaborators, *Exact solution of Dynamical Mean-Field Theory for a linear system with annealed disorder* (2024), arXiv:2405.05183, https://arxiv.org/abs/2405.05183.
4. Biroli and collaborators, work on stochastic two-state harmonic confinement (2023), arXiv:2312.02570, https://arxiv.org/abs/2312.02570 (different telegraph-stiffness model).
