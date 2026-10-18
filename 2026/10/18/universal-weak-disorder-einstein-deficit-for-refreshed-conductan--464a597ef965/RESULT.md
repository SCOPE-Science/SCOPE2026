# Universal weak-disorder Einstein deficit for refreshed conductances

## Finding

Fix a refresh rate \(\mu>0\). For the one-dimensional constant-speed walk in independently refreshed, symmetric, weakly disordered positive edge conductances, the unbiased asymptotic variance rate \(\Sigma_\mu(\varepsilon)\) and the derivative of the speed with respect to the field \(\mathcal M_\mu(\varepsilon)\) are analytic even functions of the disorder amplitude near zero. Writing \(\sigma^2=\mathbb E\xi^2>0\), they satisfy

\[
\begin{aligned}
\Sigma_\mu(\varepsilon)&=1-\sigma^2\big[\mu+1-\sqrt{\mu(\mu+2)}\big]\varepsilon^2+O_\mu(\varepsilon^4),\\
\mathcal M_\mu(\varepsilon)&=1-\sigma^2\big[\mu+1-\sqrt{\mu(\mu+2)}+\tfrac12\sqrt{\mu/(\mu+2)}\big]\varepsilon^2+O_\mu(\varepsilon^4).
\end{aligned}
\]

Thus, for every fixed positive refresh rate,

\[
\boxed{\Sigma_\mu(\varepsilon)-\mathcal M_\mu(\varepsilon)=\frac{\sigma^2}{2}\sqrt{\frac{\mu}{\mu+2}}\,\varepsilon^2+O_\mu(\varepsilon^4)>0}
\]

for all sufficiently small nonzero \(\varepsilon\). The universal leading coefficient is strictly increasing in \(\mu\), tends to zero when \(\mu\downarrow0\), and tends to \(\sigma^2/2\) when \(\mu\uparrow\infty\). Limits in \(\mu\) refer to the coefficient only; no joint uniform \(\mu,\varepsilon\) limit is claimed.

## Assumptions and scope

For each unoriented edge \(e=\{j,j+1\}\) of \(\mathbb Z\), independently run a stationary refresh process at rate \(\mu\): whenever its clock rings, its real mark is replaced by a fresh independent sample \(\xi\). Assume \(\xi\) is nondegenerate, supported in \([-1,1]\), has a distribution symmetric about zero, and has variance \(\sigma^2\in(0,1]\). The conductance at time \(t\) is \(c_e(t)=1+\varepsilon\xi_e(t)\), with \(|\varepsilon|<1\). All clocks, marks, and walker randomness are independent. The walker makes jumps at total rate one. At position \(x\), its right-jump probability in external field \(\lambda\in\mathbb R\) is

\[
p_+(x,t;\lambda,\varepsilon)=\frac{e^\lambda c_{\{x,x+1\}}(t)}{e^\lambda c_{\{x,x+1\}}(t)+e^{-\lambda}c_{\{x-1,x\}}(t)}.
\]

Write \(v_\varepsilon(\lambda)=\lim_{t\to\infty}t^{-1}\mathbb E_{\lambda,\varepsilon}X_t\) for the stationary annealed speed, with \(X_0=0\). Define \(\mathcal M_\mu(\varepsilon)=\partial_\lambda v_\varepsilon(\lambda)|_{\lambda=0}\) and \(\Sigma_\mu(\varepsilon)=\lim_{t\to\infty}t^{-1}\operatorname{Var}(X_t)\) at zero field. The bias convention is \(e^{\pm\lambda}\), so both quantities equal one at \(\varepsilon=0\). An alternative convention using half this field would rescale mobility and must not be compared without normalization. The asymptotic result is for every fixed \(\mu>0\), then \(\varepsilon\to0\).

## Proof

**1. Spectral perturbation and stationary response.** Let \(Q\) be the iid product law of the marks viewed relative to the walker, and write \(\eta_j\) for the edge from \(j\) to \(j+1\). Let \(T_\pm\) translate the edge indexing by \(\pm1\), and let \(R_\mu\) be the independent refresh generator. On cylinder functions the environment-viewed-from-the-walker generator is

\[
L_{\varepsilon,\lambda}=R_\mu+p_+(\eta;\lambda,\varepsilon)(T_+-I)+(1-p_+(\eta;\lambda,\varepsilon))(T_--I).
\]

At \(\varepsilon=\lambda=0\), \(L_0=R_\mu+(T_++T_-)/2-I\) is self-adjoint in \(L^2(Q)\). The refresh Dirichlet form controls \(\mu\operatorname{Var}_Q(f)\); the shift Dirichlet form is nonnegative, so \(-L_0\ge\mu\) on mean-zero functions. In particular \(G=(-L_0)^{-1}\) is bounded there. Perturbing the bounded jump part by \(O(|\varepsilon|+|\lambda|)\) and using a Neumann series on the mean-zero subspace gives the local analytic stationary density and resolvents. For small \(\varepsilon\), the density is nonnegative as the invariant law of the perturbed Markov semigroup and is uniquely normalized; the spectral gap also provides the required stationary additive-functional and corrector limits. The law of the marks is symmetric under sign reversal, which conjugates amplitudes \(\varepsilon\) and \(-\varepsilon\); hence the variance rate and mobility are even analytic functions, and odd-order Taylor coefficients vanish.

Let \(g=\eta_0-\eta_{-1}\), and put \(f=Gg/2\). Expanding the right-jump probability at zero field gives \(p_+=1/2+\varepsilon g/4+O(\varepsilon^2)\); the local drift is \(d=2p_+-1=\varepsilon g/2+O(\varepsilon^2)\). If \(h_\varepsilon=d\pi_\varepsilon/dQ\) denotes the stationary density, the adjoint stationarity equation yields

\[
h_\varepsilon=1+\varepsilon h_1+O(\varepsilon^2),\qquad h_1=\tfrac12(T_--T_+)f.
\]

These expansions are in \(L^2(Q)\), with derivatives in the external field controlled by the same resolvent argument. To differentiate the response at nonzero field, set \(p_0(\lambda)=e^\lambda/(e^\lambda+e^{-\lambda})\). Then

\[
-L_{0,\lambda}^*h_1(\lambda)=p_0(\lambda)(1-p_0(\lambda))(T_--T_+)g,\quad L_{0,\lambda}^*=R_\mu+p_0(\lambda)T_-+(1-p_0(\lambda))T_+-I.
\]

At zero field, \(p_0'=1/2\), \((p_0(1-p_0))'=0\). Differentiating the preceding Poisson equation gives

\[
h'_1(0)=\tfrac18G^2(T_--T_+)^2g.
\]

Since \(\partial_\lambda d=1-d^2\) exactly, and \(\mathbb E_Q g^2=2\sigma^2\), differentiating \(v=\int d\,h\,dQ\) yields

\[
\mathcal M_\mu(\varepsilon)=1+\varepsilon^2\left[-\tfrac14\mathbb E_Qg^2+\tfrac12\langle g,h'_1(0)\rangle_Q\right]+O_\mu(\varepsilon^4).
\]

**2. Martingale variance.** Reflection through the starting vertex sends the drift to its negative, so its stationary mean vanishes. The Poisson corrector \(\chi_\varepsilon\) satisfying \(L_{\varepsilon,0}\chi_\varepsilon=-d\) exists in the reflection-odd subspace and has expansion \(\chi_\varepsilon=\varepsilon f+O(\varepsilon^2)\). The process \(X_t+\chi_\varepsilon(\eta_t)-\chi_\varepsilon(\eta_0)\) is a square-integrable martingale. Its bracket includes both walker jumps and mark refreshes. The stationary expectation of its bracket density equals \(\Sigma_\mu(\varepsilon)\); the \(L^2\) corrector boundary terms are negligible divided by \(t\). Expanding the bracket gives

\[
\Sigma_\mu(\varepsilon)=1+\varepsilon^2\Big[\langle (T_+-T_-)f,h_1\rangle_Q+\tfrac12\langle g,(T_++T_--2I)f\rangle_Q+2\langle f,-L_0f\rangle_Q\Big]+O_\mu(\varepsilon^4).
\]

**3. Fourier reduction and evaluation.** All order-two quantities involve only the first-coordinate chaos \(\{\eta_j\}\). In Fourier space set \(a(k)=1-\cos k\), \(G(k)=[\mu+a(k)]^{-1}\) and \(|\widehat g(k)|^2=2\sigma^2a(k)\). Integrals below are normalized by \(dk/(2\pi)\) on \([-\pi,\pi]\). The response formula becomes

\[
\mathcal M_\mu(\varepsilon)=1-\frac{\sigma^2\varepsilon^2}{2}\left[1+\int\frac{a(k)\sin^2 k}{(\mu+a(k))^2}\frac{dk}{2\pi}\right]+O_\mu(\varepsilon^4).
\]

The bracket formula becomes

\[
\Sigma_\mu(\varepsilon)=1+\sigma^2\varepsilon^2\int\left[\frac{a(k)(1-a(k))}{\mu+a(k)}-\frac{a(k)\sin^2 k}{(\mu+a(k))^2}\right]\frac{dk}{2\pi}+O_\mu(\varepsilon^4).
\]

Differentiating \(a(k)\sin k/(\mu+a(k))\) shows that the second integrand is \(-\sin^2 k/(\mu+a(k))\) plus a full periodic derivative, whose integral vanishes. Define

\[
\rho(\mu)=\int\frac{\sin^2 k}{\mu+1-\cos k}\frac{dk}{2\pi}=\mu+1-\sqrt{\mu(\mu+2)}.
\]

The equality follows from \(\int(\mu+1-\cos k)^{-1}dk/(2\pi)=[\mu(\mu+2)]^{-1/2}\), multiplied by \((1-\cos^2k)\) and simplified. Moreover \(\int a\sin^2k/(\mu+a)^2=\rho+\mu\rho'\). Thus \(\Sigma=1-\sigma^2\rho\varepsilon^2+O_\mu(\varepsilon^4)\) and \(\mathcal M=1-(\sigma^2/2)(1+\rho+\mu\rho')\varepsilon^2+O_\mu(\varepsilon^4)\). Finally

\[
1-\rho(\mu)+\mu\rho'(\mu)=\frac{\mu}{\sqrt{\mu(\mu+2)}}.
\]

Subtracting proves the stated deficit, its strict positivity for fixed \(\mu>0\) and sufficiently small nonzero disorder, and the monotonicity and endpoint limits of its order-two coefficient.

## Verification

The standalone script `verify.py` checks the Fourier integrals independently by high-accuracy numerical quadrature; it also constructs finite periodic environments with explicit independent two-state refresh dynamics, solves the finite-state stationary and Poisson equations, and compares numerical mobility and diffusivity against the second-order coefficients. It verifies the normalization \(\Sigma=\mathcal M=1\) at zero disorder. Periodic finite-environment checks are **not** exhaustive proofs for the infinite lattice; the proof above uses the spectral gap, martingale decomposition and Fourier integration.

## Relationship to prior work

Couillard and Scali, *The constant speed random walk on dynamical conductances* (arXiv:2610.04598v1, first posted 2026-10-03), establish the model's invariance principles and exhibit Einstein-relation failure, but do not give this universal fixed-refresh weak-disorder coefficient. The present result quantifies the sign at **every** positive independent refresh rate for a symmetric weak-disorder class; it does not claim the general failure phenomenon.

Avena, Blondel and Faggionato, *Analysis of random walks in dynamic random environments via \(L^2\)-perturbations* (arXiv:1602.06322, 2016; subsequently published 2018), provide general perturbative invariant-density and speed methods under a spectral gap. Those methods are methodological precedents, not new here. The evaluated joint mobility–variance coefficients and resulting fixed-refresh sign in the present edge conductance model were not located in the inspected material. Earlier static random-conductance Einstein relations address a genuinely different temporal environment.

## Limitations

The remainder constants depend on the fixed refresh rate. The result does **not** establish a sign at arbitrary disorder strengths, uniform estimates as \(\mu\downarrow0\), a full joint two-parameter limit, or analogous coefficients in higher dimensions. The coefficient requires nonzero environmental variance. A general perturbative identity or unlocated prior evaluation may subsume the calculation: independent priority verification remains outstanding. No independent audit has been performed.

## References

1. E. Couillard and C. Scali, *The constant speed random walk on dynamical conductances*, arXiv:2610.04598v1 (2026-10-03). https://arxiv.org/abs/2610.04598
2. L. Avena, O. Blondel and A. Faggionato, *Analysis of random walks in dynamic random environments via \(L^2\)-perturbations*, arXiv:1602.06322 (2016); *Stochastic Processes and their Applications* 128 (2018), 3490–3530. https://arxiv.org/abs/1602.06322
3. N. Gantert, X. Guo and J. Nagel, *Einstein relation and steady states for the random conductance model*, arXiv:1512.01884 (2015). https://arxiv.org/abs/1512.01884
4. T. Komorowski and S. Olla, *On mobility and Einstein relation for tracers in time-mixing random environments*, *Journal of Statistical Physics* (2005), DOI 10.1007/s10955-004-8815-3.
