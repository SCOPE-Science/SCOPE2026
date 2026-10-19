# An exponential-integral metastability law for two-token normalized self-attention

## Finding
Consider the two-token, single-head, residual, Euclidean-normalized softmax map on the unit sphere, with identity value matrix, positive residual weight and inverse attention temperature. For every fixed residual weight \(\eta>0\), set \(\alpha=2\eta/(1+\eta)\). Let \(c_t\) be the inner product of the two tokens at time \(t\), and let \(T_\beta(c_0,c_*)\) denote their first time reaching correlation at least \(c_*\), where \(-1<c_0<c_*<1\).

Every non-antipodal initial pair converges to consensus, exactly in its initial sum direction. The half-angle variable has an exact multiplicative scalar recursion. As inverse temperature \(\beta\to\infty\), its first-passage time has two sharp regimes:
\[
\lim_{\beta\to\infty}\beta e^{-\beta(1-c_0)}T_\beta(c_0,c_*)=\frac{1}{\alpha(1-c_0^2)}\quad\text{for fixed }-1<c_0<c_*<1,
\]
and, for each fixed \(z>0\) and \(-1<c_*<1\),
\[
\lim_{\beta\to\infty} e^{-2\beta}T_\beta(-1+z/\beta,c_*)=\frac{E_1(z)}{2\alpha},\qquad E_1(z)=\int_z^\infty \frac{e^{-s}}s\,ds.
\]
The second regime exhibits an explicit nontrivial crossover on an initial antipodal angular scale of order \(\beta^{-1/2}\); the limit does not depend on the ambient dimension or on the target correlation (provided the target stays strictly below one).

## Assumptions and scope
Fix any integer \(d\ge2\), scalar \(\eta>0\), and \(\beta>0\). The two tokens \(u_t,v_t\) belong to \(S^{d-1}\). They undergo the exact synchronous updates
\[
 u_{t+1}=\frac{u_t+\eta[(1-p_t)u_t+p_tv_t]}{\|u_t+\eta[(1-p_t)u_t+p_tv_t]\|},\quad
 v_{t+1}=\frac{v_t+\eta[(1-p_t)v_t+p_tu_t]}{\|v_t+\eta[(1-p_t)v_t+p_tu_t]\|},
\]
where \(p_t=[1+\exp(\beta(1-c_t))]^{-1}\) and \(c_t=\langle u_t,v_t\rangle\). Equivalently, this is the complete two-token residual map with query and key \(\sqrt\beta I_d\) and value \(I_d\), with both self and cross attention included. The map and its normalizing denominators are well-defined for all pairs. For \(c_0=-1\) both tokens remain antipodal, and for \(c_0=1\) they remain identical; neither boundary state is included in the first-passage asymptotics.

For the first asymptotic, \(c_0\) and \(c_*\) are fixed independent of \(\beta\). For the second, \(c_0=-1+z/\beta\) and the stated limit is for each fixed \(z>0\), once \(c_0<c_*\). The dimension and residual weight remain fixed as \(\beta\to\infty\).

## Proof
**1. Exact one-dimensional reduction.** Put \(a=(u+v)/2\) and \(b=(u-v)/2\). They are orthogonal, with squared norms \(\|a\|^2=(1+c)/2\) and \(\|b\|^2=(1-c)/2\). The two unnormalized updates equal
\[
(1+\eta)a\pm(1+\eta-2\eta p)b.
\]
Their denominators are equal. Writing \(\alpha=2\eta/(1+\eta)\) and \(\rho=1-\alpha p\), the ratio \(r=\|b\|/\|a\|=\sqrt{(1-c)/(1+c)}\) therefore obeys the **exact** recurrence
\[
r_{t+1}=\rho_\beta(c_t)r_t,\qquad \rho_\beta(c)=1-\frac{\alpha}{1+e^{\beta(1-c)}}.
\]
Here \(0<\rho_\beta(c)<1\) for all \(-1<c<1\). Both updates have the same sum direction because their sum is a positive multiple of \(a\); hence \((u_t+v_t)/\|u_t+v_t\|\) is constant. The exact correlation increment is
\[
\Delta_\beta(c):=c_{t+1}-c_t=
\frac{(1-c^2)(1-\rho_\beta(c)^2)}{1+c+(1-c)\rho_\beta(c)^2}.
\]
It is positive throughout \((-1,1)\). The ratio \(r_t\) decreases, and any limit \(r_\infty>0\) would contradict the exact strict multiplier at its limiting correlation. Hence \(r_t\to0\) and both tokens converge to \((u_0+v_0)/\|u_0+v_0\|\).

**2. Uniform time-integral approximation.** Fix a target \(c_*<1\) and take initial correlations in \((-1,c_*)\), possibly depending on \(\beta\). Define \(p_\beta(c)=[1+e^{\beta(1-c)}]^{-1}\) and \(g_\beta(c)=\alpha(1-c^2)p_\beta(c)\). Algebra in the exact fraction yields
\[
\frac{\Delta_\beta(c)}{g_\beta(c)}=
\frac{2-\alpha p_\beta(c)}{2-(1-c)\alpha p_\beta(c)[2-\alpha p_\beta(c)]}=1+O_\eta(p_\beta(c)),
\]
uniformly for \(-1<c\le c_*\), with denominator bounded away from zero for large \(\beta\). Since \(p_\beta(c)\le e^{-\beta(1-c_*)}\) there, the relative error is uniformly \(o(1)\). Moreover
\[
\frac{d}{dc}\log g_\beta(c)=-\frac{2c}{1-c^2}+\beta[1-p_\beta(c)].
\]
The exact increment is bounded by \(C_\eta(1-c^2)p_\beta(c)\), so the variation of \(\log g_\beta\) across any single step ending below \(c_*\) is at most \(C_{\eta,c_*}(1+\beta)p_\beta(c_*)=o(1)\). This bound remains valid arbitrarily close to \(-1\), since \(1-c^2\) cancels the derivative's endpoint singularity; the same estimate follows by integrating the differential inequality for \(\log(1+c)\) and \(\log(1-c)\) over a step. Thus each full step below the target contributes \(1+o(1)\) to the quadrature of \(1/g_\beta\).

The final crossing step contributes at most a bounded term to the quadrature; its overshoot is \(O_\eta(p_\beta(c_*))\). Since the hitting time diverges exponentially in either regime below, summing the uniform per-step bounds proves
\[
T_\beta(c_0,c_*)\sim \frac1\alpha\int_{c_0}^{c_*}\frac{1+e^{\beta(1-u)}}{1-u^2}\,du.
\]
(The integral comparison can equivalently stop at the last pre-crossing iterate and bound the omitted interval by one further step.)

**3. Fixed-correlation Laplace endpoint.** For fixed \(-1<c_0<c_*<1\), Laplace's endpoint rule applied to the preceding integral gives
\[
\frac1\alpha\int_{c_0}^{c_*}\frac{1+e^{\beta(1-u)}}{1-u^2}\,du\sim
\frac{e^{\beta(1-c_0)}}{\alpha\beta(1-c_0^2)}.
\]
This yields the first asserted limit.

**4. Antipodal boundary layer.** For \(c_0=-1+z/\beta\), substitute \(s=\beta(1+u)\) in the same integral:
\[
e^{-2\beta}\frac1\alpha\int_{c_0}^{c_*}\frac{1+e^{\beta(1-u)}}{1-u^2}\,du
=\frac1\alpha\int_z^{\beta(1+c_*)}\frac{e^{-s}+e^{-2\beta}}{s(2-s/\beta)}\,ds.
\]
For any fixed \(z>0\) this converges by dominated convergence, separating a fixed initial integration range from its exponentially suppressed far tail, to \(\frac1{2\alpha}\int_z^\infty e^{-s}s^{-1}\,ds\). This proves the second limit. Finally, if \(\vartheta=\arccos c_0\), then \(\pi-\vartheta\sim\sqrt{2z/\beta}\); hence the critical angular scale is \(\beta^{-1/2}\).

## Verification
The standalone `checker.py` uses two implementations of one update: a direct pair of unit vectors and the scalar correlation recurrence. It tests 1,440 independent deterministic pseudo-random cases across dimensions \(2,3,5,9\), several temperatures, and several residual weights; it also checks the sum-direction invariant. Finite hitting-time data illustrate convergence to the two proved asymptotic limits, and an independent quadrature evaluates \(E_1(1)\). These numerical checks **do not** establish the infinite-time or large-temperature assertions, which follow from the analytic argument above.

## Relationship to prior work
Altafini's discrete-time normalized self-attention formulation [1] supplies the dynamical model and a general equilibrium/stability framework; the present isotropic two-token slice has no simple distinguished principal eigenvector and admits an exact global scalar reduction. Geshkovski, Koubbi, Polyanskiy and Rigollet [2] study continuous-time spherical self-attention and establish exponential metastability, but do not give the discrete-step, target-specific first-passage prefactor or this \(E_1\) boundary-layer limit. Alcalde, Geshkovski and Ruiz-Balet [3] analyze hardmax and soft attention with a different renormalization and stochastic metastability, not this exact Euclidean-normalized two-token map. Menon and Murray [4] study a related continuous-time bipodal escape mechanism; its linearized exponent is not this finite-step hitting law.

## Limitations
The statement concerns exactly two tokens, symmetric isotropic queries/keys, and identity value matrix with a constant positive residual parameter. It does not assert the same first-passage constants for anisotropic matrices, many tokens, learned layer-varying weights, or genuine transformer layer normalization. The first-passage asymptotics are pointwise in each fixed \(z>0\), and do not cover \(z\to0\) simultaneously. Independent mathematical review is not included in this work.

## References
1. C. Altafini, *Asymptotic Analysis of Discrete-Time Self-Attention Dynamics in Transformers*, arXiv:2610.13518v1 (first posted 2026-10-09), https://arxiv.org/abs/2610.13518.
2. B. Geshkovski, H. Koubbi, Y. Polyanskiy, P. Rigollet, *Dynamic metastability in the self-attention model*, arXiv:2410.06833 (2024), https://arxiv.org/abs/2410.06833.
3. A. Alcalde, B. Geshkovski, D. Ruiz-Balet, *Attention's forward pass and Frank-Wolfe*, arXiv:2508.09628 (2025), https://arxiv.org/abs/2508.09628.
4. V. Menon, R. Murray, *On the Metastability of Bipodal States in Transformer Attention Dynamics*, public manuscript, https://vasumenon.com/projects/metastability-transformer-attention/.
