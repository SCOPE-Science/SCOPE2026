# Unique correlation-induced mean-square frontier for Gaussian-probe multiscale Langevin stepping

## Finding

A scalar derivative-free multiscale Langevin step can have bounded mean-square position with fresh Gaussian probes and unbounded mean-square position when the probes retain enough Ornstein–Uhlenbeck correlation, even when each probe has exactly the same standard Gaussian marginal at every time. There is a **unique** sharp critical correlation for every fixed finite probe budget in the fresh-probe stable regime.

Let \(J\ge1\), \(h>0\), \(a>0\), \(c=ah\) and \(0\le\rho<1\). Define \(\gamma_J=\mathcal N(0,I_J)\), the stationary OU transition \(P_\rho\) on \(L^2(\gamma_J)\), and
\[
g(z)=\left|1-\frac cJ\|z\|^2\right|,\qquad
(K_\rho u)(z)=\int g(z)p_\rho(z,y)g(y)u(y)\,\gamma_J(dy),
\]
where \(p_\rho\) is the density of \(Z'=\rho z+\sqrt{1-\rho^2}\,\zeta\) relative to \(\gamma_J\). Let \(\Lambda_J(c,\rho)=\|K_\rho\|_{L^2(\gamma_J)\to L^2(\gamma_J)}\). Then
\[
\Lambda_J(c,0)=1-2c+\left(1+\frac2J\right)c^2,
\quad \Lambda_J(c,\rho)\text{ is strictly increasing in }\rho,
\quad \lim_{\rho\uparrow1}\Lambda_J(c,\rho)=\infty.
\]
Therefore, when \(0<c<2J/(J+2)\), a unique \(\rho_*(c,J)\in(0,1)\) satisfies \(\Lambda_J(c,\rho_*)=1\), and the chain below has bounded position second moments **if and only if** \(\rho<\rho_*\). At \(\rho=\rho_*\) they grow linearly; above it they grow exponentially. When \(c\ge2J/(J+2)\), they are unbounded for every \(\rho\in[0,1)\).

An exact witness occurs at \(J=1\), \(c=1/2\): the independent-probe multiplier is \(\Lambda_1(1/2,0)=3/4\), whereas \(\Lambda_1(1/2,1/2)\ge25/24>1\). Thus probe persistence alone crosses the mean-square stability frontier.

## Assumptions and scope

Take the real-valued potential \(\Phi(x)=a x^2/2\), affine forward model \(G(x)=x\), and loss \(\ell(y)=a y^2/2\). Initialize \(X_0=0\). Let \(Z_{0,j}\), \(\eta_n\), and \(\zeta_{n,j}\) be independent standard Gaussians, with independent \(j\) and \(n\) indices. The unadjusted slow Euler and exactly updated fast OU method becomes
\[
X_{n+1}=\left(1-\frac cJ\sum_{j=1}^J Z_{n,j}^2\right)X_n+\sqrt{2h}\,\eta_n,\qquad
Z_{n+1,j}=\rho Z_{n,j}+\sqrt{1-\rho^2}\,\zeta_{n,j}.
\]
For an OU time scale \(\varepsilon>0\), the exact fast update has \(\rho=e^{-h/\varepsilon}\); \(\rho=0\) denotes the independent-probe limit. Because \(G\) is affine, this recurrence does not depend on the finite-difference perturbation scale. The definition uses the Gaussian state space \(\mathbb R\), not a periodic identification. All assertions are over finite \(J\), positive finite \(h,a\), stationary probes and the stated Gaussian independence assumptions.

## Proof

**Step 1: Exact moment transfer.** Put \(f=g^2\). Expand \(X_n\) into independent additive Gaussian innovations and condition on the full probe path. Cross terms vanish, giving for every integer \(n\ge1\)
\[
\frac{\mathbb E X_n^2}{2h}
 =1+\sum_{k=0}^{n-2}\langle g,K_\rho^k g\rangle_{L^2(\gamma_J)}.
\]
Indeed, the summand is the expectation of a product of \(k+1\) consecutive \(f(Z_n)\) factors under the stationary Markov law. This identity does not assume independence across time.

**Step 2: Compactness, sign and the spectral criterion.** For \(0<\rho<1\), the Mehler density \(p_\rho(z,y)\) is positive. The kernel \(g(z)p_\rho(z,y)g(y)\) is square-integrable against \(\gamma_J\otimes\gamma_J\): squaring the Mehler density relative to the Gaussian product law leaves a positive-definite quadratic Gaussian precision for every \(\rho<1\), and polynomial weights have finite moments. Thus \(K_\rho\) is compact and self-adjoint. On compactly supported test functions its quadratic form is \(\langle gu,P_\rho gu\rangle\ge0\), since the Hermite eigenvalues of \(P_\rho\) are \(\rho^{|\alpha|}\ge0\). Density extends nonnegativity to all of \(L^2\). As \(g>0\) Gaussian-almost everywhere and \(p_\rho>0\), \(K_\rho\) is positivity improving. Its top eigenvalue \(\Lambda_J(c,\rho)>0\) is simple and has a strictly positive normalized eigenfunction \(u_\rho\); in particular \(\langle g,u_\rho\rangle>0\). At \(\rho=0\), the operator is the rank-one projection multiple \(K_0u=g\langle g,u\rangle\), with the same properties.

The spectral theorem applied to the exact moment formula gives
\[
\sup_n\mathbb E X_n^2<\infty \quad\Longleftrightarrow\quad \Lambda_J(c,\rho)<1.
\]
For \(\Lambda=1\) the simple top eigenspace contributes \(\mathbb E X_n^2\sim2h\,|\langle g,u_\rho\rangle|^2 n\). For \(\Lambda>1\), its contribution gives \(\mathbb E X_n^2\sim 2h\,|\langle g,u_\rho\rangle|^2\Lambda^{n-1}/(\Lambda-1)\). The remaining eigenvalues are strictly smaller than \(\Lambda\).

**Step 3: Strict increase with probe correlation.** Let \(\{H_\alpha\}\) be the normalized multivariate Hermite basis for \(\gamma_J\). The OU operator satisfies \(P_\rho H_\alpha=\rho^{|\alpha|}H_\alpha\). For \(0\le\rho_1<\rho_2<1\), evaluate the difference of quadratic forms on the top eigenfunction \(u_{\rho_1}\). The additional weighted-Hilbert–Schmidt estimate with output weight \(g\) shows \(gu_{\rho_1}\in L^2\), so
\[
\begin{aligned}
\Lambda_J(c,\rho_2)-\Lambda_J(c,\rho_1)
&\ge\langle u_{\rho_1},(K_{\rho_2}-K_{\rho_1})u_{\rho_1}\rangle\\
&=\sum_{|\alpha|\ge1}\bigl(\rho_2^{|\alpha|}-\rho_1^{|\alpha|}\bigr)
\left|\langle gu_{\rho_1},H_\alpha\rangle\right|^2.
\end{aligned}
\]
This sum is strictly positive. Otherwise \(gu_{\rho_1}\) would be a nonzero constant almost everywhere. But \(g\) vanishes linearly on the sphere \(\|z\|=\sqrt{J/c}\), and \(1/g\notin L^2(\gamma_J)\) by the inverse-square divergence across that sphere, so \(u_{\rho_1}\) cannot be a constant multiple of \(1/g\). The zero constant is equally impossible. Thus \(\Lambda_J\) is strictly increasing. Hilbert–Schmidt kernel continuity on compact subintervals of \([0,1)\) proves its continuity.

**Step 4: Endpoints and sharp threshold.** At independence, \(P_0u=\int u\,d\gamma_J\), hence
\[
\Lambda_J(c,0)=\int g^2\,d\gamma_J=1-2c+\frac{J+2}{J}c^2.
\]
It is below one exactly when \(0<c<2J/(J+2)\). As \(\rho\uparrow1\), \(P_\rho\to I\) strongly on \(L^2(\gamma_J)\). For any compactly supported normalized \(u\), \(\langle u,K_\rho u\rangle\to\int g^2u^2\,d\gamma_J\). Selecting supports at arbitrarily large radius makes the latter arbitrarily large because \(g(z)\to\infty\). Hence \(\Lambda_J(c,\rho)\to\infty\), which, together with strict continuity, gives the unique threshold and all claimed cases.

**Step 5: Exact rational instability witness.** For \(J=1\), \(c=1/2\), write \(f(z)=(1-z^2/2)^2\). In probabilists' Hermite polynomials,
\[
f(z)=\frac34+\frac12\operatorname{He}_2(z)+\frac14\operatorname{He}_4(z).
\]
For standard Gaussians \((Z_0,Z_1)\) with correlation \(\rho\), Hermite orthogonality gives
\[
\mathbb E[f(Z_0)f(Z_1)]=\frac9{16}+\frac12\rho^2+\frac32\rho^4.
\]
At \(\rho=1/2\) the expectation is \(25/32\). A Rayleigh quotient using \(g\) therefore yields
\[
\Lambda_1(1/2,1/2)\ge
\frac{\langle g,K_{1/2}g\rangle}{\langle g,g\rangle}
=\frac{25/32}{3/4}=\frac{25}{24}>1.
\]
By contrast the independent-probe eigenvalue is \(3/4<1\).

## Verification

Run `python3 verify.py` with the Python standard library. The script checks \(95\) exact-rational identities, including independent Wick-pairing and OU-polynomial transfer computations of correlated Gaussian moments; the independent-probe moment factorization; the \(J\)-probe fresh-probe threshold formula; and the rational \(25/24\) Rayleigh witness. These finite tests are supplementary and do not certify infinite-dimensional spectral or asymptotic claims, which follow from the preceding proof.

## Relationship to prior work

Della Noce and Vaes (2026) define the same slow-Euler/fast-exact OU discretization and prove strong, weak and ergodic approximation estimates on a torus. They explicitly identify the noncompact real-space setting as an extension beyond their theorems; their estimates do not state this exact Gaussian second-moment correlation frontier. Pavliotis, Stuart and Vaes (2021) introduced related multiscale derivative-free samplers and discussed numerical stiffness, without the uniqueness and spectral monotonicity proved here. Mulayoff and Michaeli (2024) establish exact mean-square stability for linearized SGD with independently sampled batches, whereas the essential effect here is persistence of Gaussian probes over consecutive steps. Douglas (1993) studied exact expectations for LMS with time-correlated Gaussian input and reports step-size bounds; that work is a serious historical-priority comparator, but the accessible abstract does not establish the specific strict monotonicity and unique OU-correlation transition for the present finite-\(J\) sampler. General Markov multiplicative-functional spectral techniques are classical ingredients, not claimed as new.

## Limitations

The threshold is characterized by the principal eigenvalue of a compact integral operator rather than an elementary closed form. This establishes a second-moment stability transition for a specified unadjusted real-space, scalar, linear-forward, quadratic-target sampler with stationary Gaussian probes; it makes no claim about almost-sure Lyapunov stability, existence or uniqueness of invariant probability distributions with infinite moments, nonquadratic objectives, nonstationary probe initialization, general dimensions, torus samplers or acceptance-corrected methods. The relation to older exact colored-input LMS literature requires additional specialist historical review; no independent mathematical audit is claimed.

## References

- A. Della Noce and U. Vaes, *Analysis of a zeroth-order multiscale sampler: strong convergence, convergence of ergodic averages and weak convergence*, arXiv:2610.17037v1, first public 2026-10-12, https://arxiv.org/html/2610.17037v1.
- G. A. Pavliotis, A. M. Stuart and U. Vaes, *Derivative-free Bayesian Inversion Using Multiscale Dynamics*, arXiv:2102.00540, https://arxiv.org/abs/2102.00540.
- R. Mulayoff and T. Michaeli, *Exact Mean Square Linear Stability Analysis for SGD*, COLT/PMLR 247 (2024), https://proceedings.mlr.press/v247/mulayoff24a.html.
- S. C. Douglas, *Exact expectation analysis of the LMS adaptive filter for correlated Gaussian input data*, ICASSP (1993), DOI:10.1109/ICASSP.1993.319549.
- J. Pitman, *Kac's moment formula for additive functionals of a Markov process*, Ann. Probab. 25 (1997), 855–900, https://statistics.berkeley.edu/tech-reports/427.
