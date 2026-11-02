# Duty-cycle invariance and a sharp zero-order-hold penalty under sampled actuator noise

## Finding

Consider an unstable scalar plant with a noisy actuator and only one state measurement per sampling period. When the actuator may be switched on over any measurable set of a prescribed total duration, the best attainable mean-square contraction is independent of *where* the active periods occur. The optimal hold has a specific exponential shape. Restricting the same system to a conventional constant zero-order hold incurs a strictly positive, exactly quantifiable stabilizability penalty.

**Theorem (arbitrary activation windows).** Let \(\tau>0\), \(\sigma>0\), and let \(a,b\in L^\infty([0,\tau];\mathbb R)\), with \(\operatorname*{ess\,inf}_{s\in[0,\tau]}|b(s)|>0\). Assume
\[
G=\exp\!\left(\int_0^\tau a(s)\,ds\right)>1.
\]
Choose any measurable \(S\subseteq[0,\tau]\) with Lebesgue measure \(\ell=|S|\in(0,\tau]\). On every interval \([k\tau,(k+1)\tau)\), write \(s=t-k\tau\), measure \(X_{k\tau}\), and use the repeated, sample-based actuator waveform
\[
u_t=K(s)X_{k\tau},\qquad K\in L^2([0,\tau]),\quad K=0\ \text{a.e. on }S^c,
\]
in the Itô system
\[
dX_t=(a(s)X_t+b(s)u_t)\,dt+\sigma b(s)u_t\,dW_t.
\]
Here the Brownian increments on distinct sampling intervals are independent; \(X_0\) is deterministic with \(X_0\ne0\). Then the exact optimum of the one-period second-moment multiplier over all admissible \(K\) is
\[
\boxed{R_*(S)=\frac{G^2\sigma^2}{\ell+\sigma^2}},
\]
and it is attained by the **unique** waveform, up to almost-everywhere equality,
\[
\boxed{K_*(s)=-\frac{\exp\left(\int_0^s a(r)\,dr\right)}{b(s)(\ell+\sigma^2)}\,\mathbf1_S(s).}
\]
The sample-and-hold system has \(\mathbb E|X_t|^2\to0\) as \(t\to\infty\) for some such fixed waveform if and only if
\[
\boxed{\ell>\sigma^2(G^2-1).}
\]
At equality, no permitted waveform has mean-square decay, and above that critical noise/duty threshold none can do so. Consequently the optimal contraction and the exact existence boundary depend on the active set only through its total measure, even for nonconstant drift and control-effect profiles. This invariance presumes unconstrained feedback amplitude and a nonvanishing actuator coefficient.

**Corollary (sharp constant-hold penalty).** For constants \(a>0\) and \(b\ne0\), take \(S=[0,\tau]\). When any \(L^2\) waveform is allowed, the maximal admissible noise variance at fixed sampling period is
\[
\sigma^2_{\rm shape}(\tau)=\frac{\tau}{e^{2a\tau}-1}.
\]
If the waveform is restricted further to \(K(s)\equiv k\), the optimal gain, minimum second-moment multiplier, and equivalent effective active duration are
\[
k_*=-\frac{e^{a\tau}(e^{a\tau}-1)/a}{b\left(((e^{a\tau}-1)/a)^2+\sigma^2(e^{2a\tau}-1)/(2a)\right)},
\]
\[
R_{\rm ZOH,*}=\frac{e^{2a\tau}\sigma^2}{\sigma^2+\ell_{\rm ZOH}},\qquad
\ell_{\rm ZOH}=\frac{2}{a}\tanh\!\left(\frac{a\tau}{2}\right)<\tau.
\]
Thus the exact ZOH noise-variance limit is
\[
\sigma^2_{\rm ZOH}(\tau)=\frac{2}{a(e^{a\tau}+1)^2},
\]
and the **sharp shaping advantage** is
\[
\boxed{\frac{\sigma^2_{\rm shape}(\tau)}{\sigma^2_{\rm ZOH}(\tau)}
=\frac{a\tau}{2}\coth\!\left(\frac{a\tau}{2}\right)>1.}
\]
This ratio tends to \(1\) for small \(a\tau\) and grows asymptotically as \(a\tau/2\) for large \(a\tau\). All inequalities defining mean-square stability are strict. For example, at \(a=\tau=b=1\) and \(\sigma^2=0.15\), the optimally shaped hold has \(R_*=0.9637899259\ldots<1\), whereas the best constant hold has \(R_{\rm ZOH,*}=1.0317659749\ldots>1\).

## Assumptions and scope

The coefficient profiles repeat exactly each period. The hold is preprogrammed as a deterministic square-integrable function multiplied by the latest exact sampled state; no within-period observation or adaptation is permitted. The process is a scalar linear Itô SDE with input-linear drift and diffusion driven by one standard Brownian motion, and there is no additive process or observation noise. The activation set is measurable with prescribed positive measure. The actuator coefficient is bounded away from zero, enabling the inverse-actuation shape shown above. The optimization is over all finite-amplitude \(L^2\) functions without a common actuator-gain, peak-power, switching-frequency, or bandwidth constraint. Mean-square stability means decay of the entire continuous-time trajectory's second moment, not merely stability of its sampled skeleton.

## Proof

Set \(A(s)=\int_0^s a(r)\,dr\) and \(\Phi(s,t)=\exp(A(s)-A(t))\). Variation of constants on a sampling interval, using that the sampled state \(X_{k\tau}\) is fixed and measurable at its start, gives
\[
X_{(k+1)\tau}=X_{k\tau}\left[G+\int_S v(s)\,ds+\sigma\int_S v(s)\,dW_{k\tau+s}\right],
\qquad v(s)=e^{A(\tau)-A(s)}b(s)K(s).
\]
The stochastic integral is a zero-mean Gaussian independent of the sampling-start sigma-field, so Itô isometry yields the exact conditional second-moment multiplier
\[
R(K)=\left(G+\int_S v\right)^2+\sigma^2\int_S v^2.
\]
Write \(c=\int_S v\). The exact orthogonal decomposition
\[
\int_S v^2=\frac{c^2}{\ell}+\int_S\left(v-\frac{c}{\ell}\right)^2
\]
therefore gives
\[
R(K)=\frac{G^2\sigma^2}{\ell+\sigma^2}
+\left(1+\frac{\sigma^2}{\ell}\right)
\left(c+\frac{G\ell}{\ell+\sigma^2}\right)^2
+\sigma^2\int_S\left(v-\frac{c}{\ell}\right)^2.
\]
Both nonnegative remainders vanish exactly when \(v(s)=-G/(\ell+\sigma^2)\) almost everywhere on \(S\). Since \(b\) is essentially bounded away from zero, the map between \(v\) and \(K\) is a bounded invertible multiplication operator on \(L^2(S)\), proving the displayed waveform is admissible, unique, and globally optimal. This also proves the active-set placement invariance without discretization or approximations.

For a fixed admissible waveform, Brownian increments on different periods are independent, so repeated conditioning yields
\[
\mathbb E[X_{k\tau}^2]=R(K)^kX_0^2.
\]
For intermediate times \(s\in[0,\tau]\), the analogous one-period conditional multiplier is a finite continuous function of \(s\), bounded uniformly in \(s\) by a constant depending on \(a,b,\sigma,K,\tau\). Consequently \(R(K)<1\) is sufficient for continuous-time mean-square convergence, while \(R(K)\ge1\) precludes it already at the sample times. Comparing the strict inequality \(R_*<1\) proves the if-and-only-if threshold. At the equality boundary \(R_*=1\), the constant optimal waveform has no sample-time decay, and every other waveform performs no better.

For the constant-coefficient ZOH restriction, let \(E=e^{a\tau}\), \(I=\int_0^\tau e^{a(\tau-s)}ds=(E-1)/a\), and \(J=\int_0^\tau e^{2a(\tau-s)}ds=(E^2-1)/(2a)\). The exact multiplier is
\[
R(k)=(E+bIk)^2+\sigma^2b^2Jk^2.
\]
Completing the square uniquely minimizes it at \(k_*=-EI/[b(I^2+\sigma^2J)]\), with minimum \(E^2\sigma^2J/(I^2+\sigma^2J)\). The identity \(I^2/J=(2/a)\tanh(a\tau/2)\) proves the effective-duration formula. The strict inequality \(\tanh z<z\) for \(z>0\) proves the shaped waveform always improves the optimum. Solving each minimum's strict inequality against \(1\) gives the two noise-variance limits. Taking their quotient gives \((a\tau/2)\coth(a\tau/2)\), with the claimed limits from elementary hyperbolic-function asymptotics. This completes all assertions.

## Verification

The accompanying standalone \(\texttt{check.py}\) uses only Python's standard library and a fixed pseudorandom seed. It checks 23,700 numerical identities and inequalities, including discrete exact-optimizer consistency for three qualitatively different activation-set geometries; arbitrary nonconstant scalar coefficient profiles; complete-square nonnegativity under numerous competing holds; independent Gaussian second-moment simulations; and constant-hold effective-duration and relative-noise-margin identities. The analytic complete-square identity and Itô isometry, rather than finite simulations, prove the universal statements.

## Relationship to prior work

Cheng and Chen (2026) establish a general necessary-and-sufficient Riccati-type criterion for sampled linear control systems with control-linear noise, which subsumes the *unconstrained stationary-plant existence question* at an abstract level. Their general criterion is therefore not claimed as new. The present claim instead calculates an explicit sharp frontier under **prescribed measurable actuator-on windows**, for **periodic time-varying scalar drift/actuation coefficients**, and proves window-placement invariance and the exact constant-hold performance penalty. The relevant source does not state these special constrained-windows and shaping-versus-hold results.

Osinenko and Yaremenko (2021) analyze stochastic sample-and-hold stabilization using Lyapunov conditions rather than a sharp optimization of noisy actuator waveforms. Wang and Fridman (2024) compare observer-based ordinary and generalized sampled-data holds for stochastic parabolic PDEs using sufficient LMIs, without this scalar control-linear Brownian actuator model's exact noise/duty threshold. Kabamba (1987) analyzes generalized holds and noise rejection in deterministic linear control; Rojas, Haimovich, and Sbarbaro (2018) examine communication-channel SNR constraints with different noise placement. These are related frameworks but do not, from the inspected material, imply the full present statement. Generalized-hold and stochastic-feedback literature may contain an older equivalent reformulation; priority is not independently certified.

## Limitations

The result is scalar and presumes perfect periodic sampling, repeated deterministic waveform shapes, independent Brownian increments, and no common input-amplitude bound. Placement invariance generally fails under amplitude, switching, or energy constraints or when the control coefficient vanishes. It does not establish optimal feedback for matrix-valued systems, sample jitter, observation noise, adaptive within-period feedback, finite-precision implementations, or other noise models. The ZOH comparison uses constant positive drift and constant nonzero control effectiveness. No claim of independent scholarly validation is made.

## References

- Cynthia Cheng and Xudong Chen, *Feedback Stabilization for Sampled Linear Systems with Control-linear Noise*, first publicly posted 2026-09-24, arXiv:2609.30438, https://arxiv.org/abs/2609.30438 .
- Pavel Osinenko and Grigory Yaremenko, *On stochastic stabilization of sampled systems*, arXiv:2105.07152, https://arxiv.org/abs/2105.07152 .
- Pengfei Wang and Emilia Fridman, *Sampled-Data Finite-Dimensional Observer-Based Control of 1D Stochastic Parabolic PDEs*, SIAM J. Control Optim. 62 (2024), 297–325, https://doi.org/10.1137/22M1538247 .
- Pierre T. Kabamba, *Control of Linear Systems Using Generalized Sampled-Data Hold Functions*, IEEE Trans. Autom. Control 32 (1987), 772–783, https://doi.org/10.1109/TAC.1987.1104711 .
- Alejandro J. Rojas, Hernán Haimovich, and Daniel Sbarbaro, *On the Effect of Sampled-Data Hold and Discretization in Signal-to-Noise Ratio Constrained Control*, American Control Conference (2018), https://doi.org/10.23919/ACC.2018.8431714 .
