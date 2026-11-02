# Logarithmically corrected stable limits at isolated minima of periodic jump indices

## Finding

Consider a spatially periodic, symmetric, regime-switching stable-like process in dimension \(d\), with local jump-index function \(\alpha(z,i)\) attaining its global minimum \(\alpha_0\in(0,2)\) only at finitely many nondegenerate quadratic minima on the periodic state space. Under the explicit mixing and stationary-density assumptions below, define for every integer \(n\ge3\)
\[
 b_n=\left(\frac{n}{(\log n)^{d/2}}\right)^{1/\alpha_0}.
\]
For each fixed starting state \((x,i)\), the rescaled spatial process \(\bigl(X(nt)/b_n\bigr)_{t\ge0}\) converges in distribution in the Skorokhod \(J_1\) topology to a nondegenerate rotationally invariant \(\alpha_0\)-stable Lévy process \(L\) starting at zero. Its Lévy measure is
\[
 \nu_L(dy)=C_*|y|^{-d-\alpha_0}\,dy,\qquad
 C_*=(2\pi\alpha_0)^{d/2}
 \sum_{\ell=1}^{r}
 \frac{\rho_{i_\ell}(z_\ell)\gamma(z_\ell,i_\ell)}
 {\sqrt{\det H_\ell}}\in(0,\infty).
\]
Here \((z_\ell,i_\ell)\), \(1\le\ell\le r\), are exactly the minimum points on the torus; \(H_\ell\) are the spatial Hessians of \(\alpha(\cdot,i_\ell)\) at those points; and \(\rho_i\) are invariant probability densities with respect to Lebesgue measure on one period cell.

The normalization is sharp up to a fixed multiplicative constant: if \(c_n/b_n\to\infty\) then \(X(nt)/c_n\) converges to the zero process, whereas if \(c_n/b_n\to0\), then \(|X(nt)|/c_n\to\infty\) in probability for every fixed \(t>0\). The latter conclusion is about one-time marginals, not an asserted path-space limit.

## Assumptions and scope

Fix integers \(d,m\ge1\) and a period vector \(\tau\in(0,\infty)^d\). Let \((X_t,I_t)\) be the nonexplosive strong Markov process with generator
\[
 \begin{aligned}
 \mathcal A f(x,i)&=\int_{\mathbb R^d}\left[f(x+y,i)-f(x,i)
 -\mathbf1_{\{|y|<1\}}\langle y,\nabla_x f(x,i)\rangle\right]
 \frac{\gamma(x,i)}{|y|^{d+\alpha(x,i)}}\,dy\\
 &\quad+\sum_{j=1}^{m}q_{ij}(x)f(x,j).
 \end{aligned}
\]
The index \(\alpha\), intensity \(\gamma\), and generator rates \(q_{ij}\) are periodic and spatially Lipschitz, with \(0<\inf\alpha\le\sup\alpha<2\), \(0<\inf\gamma\le\sup\gamma<\infty\), and irreducible switching in the sense of assumptions (A1)–(A3) of Sandrić (2026). In the one-regime case the switching generator vanishes. We use the source's established uniform exponential total-variation mixing of the projected process \(Z_t=(X_t\bmod\tau,I_t)\): there are \(A,\lambda>0\) and a unique invariant law \(\pi\) with
\[
 \sup_z\|\mathbb P_z(Z_t\in\cdot)-\pi\|_{\mathrm{TV}}
 \le A e^{-\lambda t}\qquad(t\ge0).
\]
We further assume that \(\pi(dx,i)=\rho_i(x)dx\), and the density \(\rho_{i_\ell}\) is continuous and strictly positive at every global minimizer of \(\alpha\). These local density hypotheses are additional to the cited mixing theorem, not asserted as automatic consequences of its assumptions.

Specifically, the set \(\{(z,i):\alpha(z,i)=\alpha_0\}\) on \(\mathbb T_\tau^d\times[m]\) consists of exactly \(r\ge1\) points \((z_\ell,i_\ell)\). The spatial function \(\alpha(\cdot,i_\ell)\) is twice continuously differentiable on a neighborhood of \(z_\ell\), with zero gradient and strictly positive-definite Hessian \(H_\ell\). There are no additional minimum points. The coefficients \(\gamma\) are continuous at each of these points (already ensured by the Lipschitz assumption). All limits take \(n\to\infty\) through positive integers, starting from any single fixed \((x,i)\).

## Proof

**Step 1: predictable jump characteristics and symmetry.** For the rescaled process \(Y_n(t)=X(nt)/b_n\), the predictable compensator of its jumps is
\[
 N_n(ds,dy)=n\,b_n^{-\alpha(Z_{ns-})}
 \gamma(Z_{ns-})|y|^{-d-\alpha(Z_{ns-})}\,dy\,ds,
\]
where \(\alpha(Z_{ns-})\) and \(\gamma(Z_{ns-})\) abbreviate evaluation in the torus position and regime. This follows from the deterministic change of variables in the symmetric jump kernel; regime switches do not move the spatial coordinate. Relative to the symmetric truncation \(h(y)=y\mathbf1_{\{|y|<1\}}\), the drift characteristic is zero, and there is no continuous martingale component. The modified second characteristic comes entirely from integrating \(h(y)h(y)^T\) against \(N_n\).

**Step 2: a uniform triangular-array mixing lemma.** If \(F_n\) is a bounded observable on the compact projected state space, \(\|F_n\|_\infty\le M_n\), then uniform exponential mixing and the Markov property give, for \(U_n=F_n-\pi(F_n)\),
\[
 \mathbb E\left|\int_0^t U_n(Z_{ns})\,ds\right|^2
 \le \frac{C t M_n^2}{n},
\]
with \(C\) depending only on the uniform mixing constants, not on \(n\), the initial state, or \(t\). Indeed, for \(s\ge u\), the conditional expectation of \(U_n(Z_{ns})\) given the history through \(nu\) is \(P_{n(s-u)}U_n(Z_{nu})\); its supremum is at most \(C M_n e^{-\lambda n(s-u)}\). Integrating the resulting covariance bound over \(0\le u\le s\le t\) proves the inequality. Consequently any \(M_n=O((\log n)^{d/2})\) yields a vanishing \(O((\log n)^d/n)\) mean-square error. The estimate holds from arbitrary initial states, not merely at stationarity.

**Step 3: nondegenerate Laplace saddlepoint.** Put \(\ell_n=\log b_n\). We have the exact identity
\[
 n b_n^{-\alpha_0}=(\log n)^{d/2},
 \qquad\frac{\log n}{\ell_n}\longrightarrow\alpha_0.
\]
For any continuous \(v\) on the torus-by-regime space, Laplace's method at the finitely many nondegenerate minima gives
\[
 \begin{aligned}
 &(\log n)^{d/2}\sum_i\int_{\mathbb T_\tau^d}
 e^{-\ell_n(\alpha(z,i)-\alpha_0)}v(z,i)\rho_i(z)\,dz\\
 &\quad\longrightarrow (2\pi\alpha_0)^{d/2}
 \sum_{\ell=1}^r\frac{v(z_\ell,i_\ell)\rho_{i_\ell}(z_\ell)}{\sqrt{\det H_\ell}}.
 \end{aligned}
\]
To see this, remove fixed small neighborhoods of the minimum set, where the exponent has a strictly positive lower bound. In each remaining neighborhood use the Taylor expansion \(\alpha(z,i_\ell)-\alpha_0=\frac12(z-z_\ell)^T H_\ell(z-z_\ell)+o(|z-z_\ell|^2)\), rescale \(z-z_\ell\) by \(\ell_n^{-1/2}\), dominate by a fixed integrable Gaussian, and let the radius tend to infinity. The fixed period-cell normalization is contained in the invariant densities \(\rho_i\); no extra torus-volume factor is inserted.

**Step 4: averaged predictable characteristics.** Let \(\psi:\mathbb R^d\to\mathbb R\) be either a bounded continuous function vanishing on a neighborhood of zero, a coordinate product \(y_k y_l\mathbf1_{\{|y|<1\}}\), or the nonnegative integrability test \(\min\{1,|y|^2\}\). Define
\[
 \Phi_\psi(a)=\int_{\mathbb R^d}\psi(y)|y|^{-d-a}\,dy,
 \quad F_{n,\psi}(z,i)=n b_n^{-\alpha(z,i)}\gamma(z,i)\Phi_\psi(\alpha(z,i)).
\]
On the compact index interval inside \((0,2)\), each \(\Phi_\psi\) is finite, continuous, and uniformly bounded (the coordinate product may be signed). Thus \(\|F_{n,\psi}\|_\infty=O((\log n)^{d/2})\). Applying Step 3 to \(v(z,i)=\gamma(z,i)\Phi_\psi(\alpha(z,i))\) shows
\[
 \pi(F_{n,\psi})\longrightarrow C_*\Phi_\psi(\alpha_0).
\]
Step 2 therefore proves for each \(t\ge0\), in mean square,
\[
 \int_0^t\!\int\psi(y)\,N_n(ds,dy)
 \longrightarrow t C_*\Phi_\psi(\alpha_0).
\]
For tests of either sign, convergence is promoted to uniform-on-compact in probability using a fixed time grid and the bound on variation of the integral over short intervals; the expected variation is controlled by applying the same stationary-average and mixing bounds to \(|F_{n,\psi}|\). These conclusions cover the jump compensators away from zero, their modified second characteristics, and the small-jump-tightness control.

**Step 5: the path-space limit.** The drift is identically zero by symmetry, there is no continuous-martingale characteristic, and Step 4 identifies all limiting modified second and jump characteristics with those of the Lévy process whose measure is \(C_*|y|^{-d-\alpha_0}dy\). Uniform mixing bounds control integrated jump intensity and truncated quadratic variation on short intervals, so the corresponding tightness conditions hold. The standard semimartingale convergence theorem for deterministic Lévy characteristics (Jacod–Shiryaev, Theorem VIII.2.17, as invoked in Sandrić's proof) gives \(Y_n\Rightarrow L\) in the \(J_1\) topology. Its starting point is \(x/b_n\to0\). All assumptions of the test-function argument have been stated explicitly; the numerical checks below are not used to establish infinite-process convergence.

**Step 6: scale sharpness.** If \(c_n/b_n\to\infty\), then \(X(n\cdot)/c_n=(b_n/c_n)Y_n\Rightarrow0\) by tightness of the convergent sequence. If \(c_n/b_n\to0\), then for every fixed \(t>0\), \(Y_n(t)\Rightarrow L_t\), whose nondegenerate stable law has no atom at zero. For each \(R>0\), \(\mathbb P(|X(nt)|/c_n\le R)\to0\) by the portmanteau theorem after trapping the shrinking ball inside an arbitrarily small fixed ball. This proves the stated divergence in probability and completes the proof.

## Verification

The enclosed `verify_scaling.py` checks the deterministic saddlepoint normalization on exactly integrable periodic index models, using
\[
 \alpha(x)=\alpha_0+\sum_{j=1}^d\varepsilon_j(1-\cos(2\pi x_j)),
 \qquad H=\operatorname{diag}(4\pi^2\varepsilon_j).
\]
The torus integral factors into exponentially rescaled modified Bessel functions. Tests cover dimensions one, two, and three, two weighted regime components, and the exact logarithmic normalization identity, for 95 passing checks. These illustrative weighted integrals do **not** assert that a constant density is the stationary density of a spatially varying-index process. The infinite-dimensional convergence follows from Steps 1–6, not from those tests. Execute with `python verify_scaling.py` (Python 3 and SciPy).

## Relationship to prior work

Sandrić (arXiv:2610.30342v1, first public October 21, 2026) proves a periodic regime-switching stable-like functional limit at the conventional \(n^{1/\alpha_0}\) normalization. If the minimizer set has zero Lebesgue measure, that limit is the zero process under the source's stated additional conditions; the paper explicitly poses nondegenerate alternative normalization as an open problem. The present result treats the isolated Morse-minimum case and establishes the distinct nonzero scale and stationary-density/Hessian coefficient. It reuses, and credits, Sandrić's exponential-mixing and semimartingale-characteristic machinery.

Franke's 2006 periodic stable-like result also addresses conventional scaling according to the measure of the minimum-index set. Only its abstract and bibliographic metadata could be inspected during this comparison; a full-document priority comparison remains unresolved. Kuhwald and Pavlyukevich (2016) already derive logarithmic saddlepoint factors for a **time-periodic additive process with independent increments** in a metastable exit problem. Thus neither the Laplace method nor logarithmic factors alone are claimed new. The difference here is the **spatially state-dependent, potentially regime-switching process**, its ergodic occupation weighting, and its full-process nondegenerate \(J_1\) limit at a zero-measure minimum set.

## Limitations

The theorem requires finitely many nondegenerate quadratic minimizers, continuity and strict positivity of the relevant invariant densities, symmetric jump kernels, a fixed starting state, and uniform exponential mixing of the torus projection. It does not treat flat/degenerate minima, fractal minimizer sets, asymmetric jumps, or a universally valid normalization without these assumptions. Historical priority is qualified by incomplete access to Franke's original full paper and by possible stronger general results not located in the accessible literature. No independent mathematical audit has been performed.

## References

1. N. Sandrić (2026), *A note on functional non-central limit theorem for periodic regime-switching stable-like processes*, arXiv:2610.30342v1, posted October 21, 2026, https://arxiv.org/html/2610.30342v1; Sections 2–3 and the final open problem.
2. B. Franke (2006), *The scaling limit behaviour of periodic stable-like processes*, Bernoulli 12(3), 551–570, https://doi.org/10.3150/bj/1151525136 (full text not accessed in this comparison).
3. B. Franke (2007), *Correction to: The scaling limit behaviour of periodic stable-like processes*, arXiv:0708.4283, https://arxiv.org/abs/0708.4283.
4. I. Kuhwald and I. Pavlyukevich (2016), *Bistable behaviour of a jump-diffusion driven by a periodic stable-like additive process*, Discrete and Continuous Dynamical Systems B 21(9), 3175–3190, https://doi.org/10.3934/dcdsb.2016092; especially its Laplace-method scaling argument.
5. J. Jacod and A. N. Shiryaev (2003), *Limit Theorems for Stochastic Processes*, second edition, Springer; Theorem VIII.2.17 (the source's cited semimartingale-convergence criterion).
