# Soft-thresholded Gaussian last-iterate law for anytime stochastic subgradient descent

## Finding
Fix \(b,\gamma,\theta>0\). For each integer \(n\ge2\), put
\[
H_n=\sum_{t=1}^{n-1}t^{-1},\qquad S_n=\sum_{t=1}^{n-1}t^{-1/2},\qquad
\varepsilon_n=\frac{\theta b\sqrt{H_n}}{S_n}.
\]
For all sufficiently large \(n\), apply scalar stochastic subgradient descent to the uniquely minimized convex objective \(f_n(x)=\varepsilon_n|x|\), starting from \(X_1=0\), with subgradient \(g_n(x)=\varepsilon_n\operatorname{sgn}(x)\), \(\operatorname{sgn}(0)=0\), step \(\eta_t=\gamma/\sqrt t\), and independent centered noise \(W_t=(b-\varepsilon_n)\xi_t\), where \(\xi_t\) are equiprobable signs. Then
\[
\frac{X_n}{\gamma b\sqrt{H_n}}\ \Longrightarrow\ -\operatorname{soft}_{\theta}(Z),\quad
\operatorname{soft}_{\theta}(z)=\operatorname{sgn}(z)(|z|-\theta)_+,\quad Z\sim N(0,1).
\]
The limit has an atom of mass \(2\Phi(\theta)-1\) at zero. The normalized last-iterate objective obeys
\[
\frac{\sqrt n}{\log n}\,f_n(X_n)\Longrightarrow
\frac{\gamma b^2\theta}{2}(|Z|-\theta)_+,
\qquad
\lim_{n\to\infty}\frac{\sqrt n}{\log n}\,\mathbb E f_n(X_n)
=\gamma b^2\theta\bigl[\phi(\theta)-\theta\overline\Phi(\theta)\bigr],
\]
where \(\phi\), \(\Phi\), and \(\overline\Phi=1-\Phi\) are the standard normal density, CDF, and survival function. For \(u\ge0\), its limiting normalized objective has exceedance probability
\[
\Pr\!\left(\frac{\gamma b^2\theta}{2}(|Z|-\theta)_+>u\right)
=2\overline\Phi\!\left(\theta+\frac{2u}{\gamma b^2\theta}\right).
\]
Within this explicitly specified horizon-tuned family, the limiting expected-error coefficient has a unique maximizer \(\theta_*\) determined by
\[
\phi(\theta_*)=2\theta_*\overline\Phi(\theta_*),\qquad
\theta_*=0.612003180962481\ldots,
\]
and its value is \(0.101228245094012\ldots\,\gamma b^2\). This is a within-family optimization, not a minimax bound over all stochastic oracles.

## Assumptions and scope
All iterates and parameters are real. Each horizon specifies its own objective and bounded independent identically distributed symmetric noise; the stochastic first-order oracle is conditionally unbiased. For sufficiently large \(n\), \(0<\varepsilon_n<b/2\), so \(f_n\) is globally \(b/2\)-Lipschitz, the stochastic gradients have magnitude at most \(b\), and the minimizer is exactly zero. There are no constraints (projection onto \(\mathbb R\) is the identity). The statements concern exact arithmetic and \(n\to\infty\) with fixed positive \(b,\gamma,\theta\).

## Proof
**1. Deterministic soft-threshold tracking.** For any finite sequence of nonnegative increments \(d_j\), cumulative disturbance \(U_0=0,U_j\), and recurrence
\[
z_{j+1}=z_j-d_j\operatorname{sgn}(z_j)+(U_{j+1}-U_j),
\]
write \(D=\sum_jd_j\), \(\delta=\max_j|U_j|\), and \(h=\max_jd_j\) (set \(h=0\) for an empty sequence). Then
\[
\left|z_{\rm end}-\operatorname{soft}_{D}(z_{\rm start})\right|\le3\delta+h.
\]
Indeed, \(y_j=z_j-U_j\) moves inward by exactly \(d_j\) whenever \(y_j>\delta\) or \(y_j<-\delta\). The interval \([-\delta-h,\delta+h]\) is forward-invariant: an inward step cannot cross its opposite endpoint, and a step from its central band has size at most \(h\). If the total drift does not reach the band, the sign stays fixed and \(y_{\rm end}=y_{\rm start}-\operatorname{sgn}(y_{\rm start})D\). Otherwise the final \(y\) lies in that invariant band, while the soft-thresholded initial value has magnitude at most \(\delta\). Adding the final disturbance of magnitude at most \(\delta\) proves the bound. The argument is symmetric under sign reversal, including the convention \(\operatorname{sgn}(0)=0\).

**2. Concentration of the late noise and late drift.** Choose \(m_n=\max\{2,\lfloor n/(\log n)^4\rfloor\}\), and divide the recursion at \(m_n\). Put \(Z_{n,t}=X_t/(\gamma b\sqrt{H_n})\). The drift accumulated up to \(m_n\) is bounded by \(\theta S_{m_n}/S_n=o(1)\), while its centered-noise component is
\[
-\frac{b-\varepsilon_n}{b\sqrt{H_n}}\sum_{t=1}^{m_n-1}\frac{\xi_t}{\sqrt t}.
\]
The triangular-array Lindeberg theorem applies: the largest coefficient is \(O(H_n^{-1/2})=o(1)\), and \(H_{m_n}/H_n\to1\). Therefore \(Z_{n,m_n}\Longrightarrow -Z\) for \(Z\sim N(0,1)\).

For the remaining indices, the normalized drift increments are \(d_t=\theta/(S_n\sqrt t)\). They have \(\max d_t\to0\) and total mass \(D_n=\theta(S_n-S_{m_n})/S_n\to\theta\). The normalized late noise is a partial-sum martingale. Doob's maximal inequality gives
\[
\mathbb E\!\left[\max_{m_n\le j\le n}\left|\frac{b-\varepsilon_n}{b\sqrt{H_n}}\sum_{t=m_n}^{j-1}\frac{\xi_t}{\sqrt t}\right|^2\right]
\le4\frac{H_n-H_{m_n}}{H_n}\longrightarrow0.
\]
Applying the deterministic tracking estimate, then the continuous-mapping theorem and Slutsky's theorem, yields the asserted Gaussian soft-threshold limit. Importantly, the *late* noise vanishes on this scale even though the *early* noise accumulates a full Gaussian fluctuation.

**3. Loss distribution and mean.** Since \(\sqrt n/S_n\to1/2\) and \(H_n/\log n\to1\), the distributional objective limit follows. Unrolling the exact recursion also gives
\[
\left|\frac{X_n}{\gamma b\sqrt{H_n}}\right|
\le\theta+\left|\frac{\sum_{t=1}^{n-1}\xi_t/\sqrt t}{\sqrt{H_n}}\right|.
\]
The right-hand side has uniformly bounded second moment, so the scaled objectives are uniformly integrable. Consequently their expectations converge, and Gaussian integration gives
\[
\mathbb E(|Z|-\theta)_+=2\bigl[\phi(\theta)-\theta\overline\Phi(\theta)\bigr].
\]
The atom, exceedance curve, and expectation formula follow.

**4. Unique optimal tuning within the family.** Let \(F(\theta)=\theta[\phi(\theta)-\theta\overline\Phi(\theta)]\). Then \(F'(\theta)=\phi(\theta)-2\theta\overline\Phi(\theta)\). The function
\[
\frac{\theta\overline\Phi(\theta)}{\phi(\theta)}
=\int_0^\infty e^{-v-v^2/(2\theta^2)}\,\mathrm dv
\]
is strictly increasing from zero to one as \(\theta\) grows from zero to infinity. Thus \(F'\) has precisely one positive zero, at which \(F\) attains its global maximum. Numerical root values are reproducible by the standalone verifier; uniqueness is analytical.

## Verification
Run `python3 verify.py` with the Python 3 standard library. The script tests the deterministic perturbation inequality across 13,760 deterministic and seeded random configurations, reconstructs the optimum and numerical coefficient, and computes finite-horizon trajectories using the *actual stated recurrence* for four horizons. These are finite corroborations only; the universal asymptotic claim is proved analytically in the preceding section.

## Relationship to prior work
Beretta, Cesari, and Colomboni (arXiv:2610.30143v1, Section 2, Theorem 2 and its complete proof) established the matching worst-case **rate** for anytime scalar stochastic subgradient descent, using the same natural absolute-value and bounded-Rademacher mechanism. They deduced a finite-horizon expected-error lower bound using triangle and Khintchine inequalities; the inspected paper does not state a weak law, Gaussian soft-threshold atom, exact expected leading constant, or unique optimal within-family curvature tuning. These further properties are the claimed addition, not a rediscovery of the logarithmic lower bound. Beretta et al. (arXiv:2606.24879v1) analyze fixed-horizon constant-step stochastic subgradient descent, so its stated conclusions do not imply an anytime-harmonic-noise limit. General scalar stochastic-approximation central-limit ideas motivate the early-noise decomposition but do not, without the vanishing-drift analysis, produce the stated nonlinear Gaussian soft-threshold law.

## Limitations
The problem is one-dimensional and nonsmooth; the objective and oracle distribution change with the horizon. The result is a weak-limit and mean-leading-constant theorem, not a finite-horizon error bound or an exact finite-horizon atom. The limit law has an atom at zero, but no claim is made that the finite-horizon iterate itself has a positive atom at zero. The \(\theta\)-optimum applies only to the specified one-parameter family, not to all admissible lower-bound instances. Specialized prior literature on stochastic-approximation weak limits remains a possible source of equivalent formulations.

## References
1. G. Beretta, T. Cesari, and R. Colomboni, *The Last Iterate of the Projected Stochastic Subgradient Method Pays a Logarithm, Even in Dimension One*, arXiv:2610.30143v1 (first publicly posted July 31, 2026), especially Section 2 and Theorem 2. https://arxiv.org/html/2610.30143v1
2. G. Beretta, T. Cesari, R. Colomboni, and A. Paudice, *New Bounds for the Last Iterate of the Stochastic subGradient Method*, arXiv:2606.24879v1 (June 23, 2026). https://arxiv.org/abs/2606.24879
3. G. Beretta, T. Cesari, R. Colomboni, and A. Paudice, *Sharp Dimension Dependence for the Last Iterate of the SubGradient Method*, arXiv:2607.15980 (July 2026). https://arxiv.org/abs/2607.15980
4. S. J. Szarek, *On the best constants in the Khinchin inequality*, Studia Mathematica 58 (1976), 197–208; used as background in Reference 1, not needed for the new proof.
