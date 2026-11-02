# A sharp coherence threshold for steady reset-assisted qubit thermometry

## Finding

Consider a two-level thermometer exposed to a bosonic thermal bath, while a Poisson reset continuously replaces its state with a fixed, temperature-independent qubit state. The reset state may contain energy-basis coherence. At any fixed positive normalized reset rate \(s=r/\gamma\), optimizing the steady-state quantum Fisher information (QFI) over *every* reset state exhibits a sharp high-temperature preparation transition at \(s=1/3\): below it the unique optimal target is the ground state; above it the optimal target has nonzero coherence and asymptotic energy-axis Bloch coordinate \(-1/(3s)\). The maximal high-temperature inverse-temperature QFI is

\[
\lim_{\beta\downarrow0}\frac{1}{\omega^2}\max_{\rho_\delta}F_\beta(\rho_{\beta,r}^{\mathrm{ss}})=
\begin{cases}
(1+s)^2/4,&0<s\le1/3,\\
s^2+1/3,&s\ge1/3.
\end{cases}
\]

The maximizer is precisely ground-state resetting for all sufficiently small positive \(\beta\omega\), at each fixed \(0<s\le1/3\). For every fixed \(s>1/3\), at all sufficiently small positive \(\beta\omega\), every maximizing target is pure and coherent; its optimal Bloch latitude converges to \(-1/(3s)\). The optimal phase is arbitrary. In a neighborhood of the transition, the unique smooth critical curve obeys

\[
s_{\mathrm c}(\beta\omega)=\frac13+\frac8{27}\,\beta\omega+O((\beta\omega)^2).
\]

For \(s\) near \(1/3\) and \(\beta\omega>0\) sufficiently small, ground resetting is optimal at or below this curve and coherent pure resetting is optimal above it. The ratio of optimal QFI to the best *incoherent* reset QFI tends, for fixed \(s>1/3\), to \(4(s^2+1/3)/(1+s)^2>1\); its iterated large-\(s\) limit is four. The order of limits matters: the result does **not** claim a fourfold advantage at fixed temperature as \(r\to\infty\).

For a finite, exactly reproducible witness, choose \(\gamma=\omega=1\), \(e^{\beta\omega}=6/5\), \(r=2\), and a pure reset target with Bloch latitude \(a=-1/2\). Then its QFI is \(11574741702400/8063279547193\), strictly larger than the best diagonal-target QFI \(405/338\) at the same reset rate. Thus the coherent advantage is not merely a formal boundary-limit effect.

## Assumptions and scope

Let \(\beta,\omega,\gamma,r>0\) be inverse bath temperature, qubit splitting, base bath rate and reset rate. Set \(n_\beta=(e^{\beta\omega}-1)^{-1}\). The GKSL equation is

\[
\dot\rho=-i[\omega\sigma_z/2,\rho]+\gamma(n_\beta+1)\mathcal D[\sigma_-]\rho+\gamma n_\beta\mathcal D[\sigma_+]\rho+r(\rho_\delta\operatorname{Tr}\rho-\rho),
\]

where \(\mathcal D[A]\rho=A\rho A^\dagger-\{A^\dagger A,\rho\}/2\). The reset density matrix \(\rho_\delta\) is constant with respect to \(\beta\) during estimation; allowing a temperature-dependent preparation would change the estimation problem. The high-temperature limit is \(\beta\downarrow0\) with \(s=r/\gamma>0\), \(\gamma\), and \(\omega\) fixed. QFI is for **inverse temperature** \(\beta\); temperature QFI scales by \(T^{-4}\) and has the same maximizing reset target. No per-reset energy or implementation cost enters the objective.

Write the reset Bloch vector as \((\operatorname{Re}w_\delta,\operatorname{Im}w_\delta,a)\), where \(a\in[-1,1]\) and \(|w_\delta|^2+a^2\le1\). The ground state has \(a=-1\). The stationary Bloch vector is denoted \((\operatorname{Re}w,\operatorname{Im}w,z)\). Define \(x=e^{\beta\omega}-1>0\) and \(\kappa=\omega/\gamma\).

## Proof

**1. Exact stationary solution and metric.** The thermal Davies relaxation rate is \(\Gamma=\gamma\coth(\beta\omega/2)=\gamma(2+x)/x\) and its equilibrium longitudinal Bloch coordinate is \(-\gamma/\Gamma\). The diagonal and off-diagonal master equations give

\[
z=\frac{(sa-1)x}{2+(1+s)x},\qquad
w=\frac{s w_\delta x}{1+(s+1/2+i\kappa)x}.
\]

A change of sign in the harmless imaginary \(i\kappa\) term reflects a convention for \(w\). The thermal upward and downward jump rates are strictly positive at every \(\beta>0\), so the stationary state is full rank. Alternatively, its renewal representation is a positive average of thermalizing Davies trajectories at positive ages, each of which is full rank. For a full-rank qubit with Bloch vector \(v=(\operatorname{Re}w,\operatorname{Im}w,z)\), the exact SLD QFI is

\[
F_\beta=|\partial_\beta v|^2+
\frac{(v\mathbin{\cdot}\partial_\beta v)^2}{1-|v|^2}.
\]

Since \(\partial_\beta x=\omega(1+x)\), its exact derivatives are

\[
\partial_\beta z=\frac{2\omega(1+x)(sa-1)}{[2+(1+s)x]^2},\quad
\partial_\beta w=\frac{\omega(1+x)s w_\delta}{[1+(s+1/2+i\kappa)x]^2}.
\]

These three displayed formulas give an explicit rational real-valued objective for every admissible target (with a complex rational denominator in \(w\)). They also give an independent route for reproducing the result without diagonalizing a Liouvillian.

**2. Uniform boundary expansion.** At fixed \(s>0\), uniformly in the closed Bloch ball, and with uniform derivatives through second order in \(a\) and first order in \(t=|w_\delta|^2\),

\[
\frac{F_\beta}{\omega^2}=
\frac{(sa-1)^2}{4}+s^2t
-x\left[\frac{s}{2}(sa-1)^2+4s^3t\right]+O_s(x^2).
\]

To see uniformity, substitute the exact formulas of Step 1. At \(x=0\) all denominators are bounded away from zero uniformly over the compact Bloch ball; \(|v|=O_s(x)\) makes the QFI metric denominator \(1-|v|^2=1+O_s(x^2)\). Direct differentiation yields the displayed expansion and the stated uniform derivative bounds. In particular, \(\partial_tF_\beta/\omega^2=s^2+O_s(x)>0\). Hence for all sufficiently small \(x>0\) and any fixed \(a\), maximizing over transverse coherence saturates \(t=1-a^2\); *every* global maximizer is a pure reset state.

**3. Sharp phase diagram.** On pure targets, the limiting normalized objective is the strictly concave quadratic

\[
f_s(a)=\frac{(sa-1)^2}{4}+s^2(1-a^2)
=s^2+\frac14-\frac{s a}{2}-\frac{3s^2a^2}{4},\quad -1\le a\le1.
\]

Its derivative is \(f_s'(a)=-s/2-3s^2a/2\). Thus its unique maximizer is \(a=-1\) when \(s\le1/3\) and \(a=-1/(3s)\in(-1,0)\) when \(s>1/3\). The associated maximum is the stated piecewise formula. For each fixed \(s>0\), the second derivative of the *exact* pure-target objective converges uniformly to \(-3s^2\omega^2/2<0\); hence the exact objective is strictly concave for all sufficiently small \(x\). If \(0<s<1/3\), its derivative at \(a=-1\) stays negative, yielding exact ground-state optimality. If \(s>1/3\), the derivative at \(-1\) is positive while that at \(+1\) is negative, so the exact optimizer is uniquely interior in latitude and tends to \(-1/(3s)\). Rotational phase symmetry leaves a circle of physically distinct phase-equivalent optimal pure targets.

**4. Critical-curve slope and the equality case.** Differentiating Step 2 along pure targets at \(a=-1\) gives

\[
\frac1{\omega^2}\left.\partial_a F_\beta\right|_{a=-1,t=1-a^2}=
\frac{s(3s-1)}2+x s^2(1-7s)+O(x^2).
\]

The derivative with respect to \(s\) at \((s,x)=(1/3,0)\) is \(1/2\ne0\). The analytic implicit-function theorem yields the unique nearby critical curve, and solving to first order gives \(s_{\mathrm c}(x)=1/3+8x/27+O(x^2)\). As \(x=\beta\omega+O((\beta\omega)^2)\), this proves the asserted expansion. Strict concavity and \(\partial_aF_\beta(1)<0\) locally yield the classification on either side, including the boundary itself. The positive critical-curve slope also proves that exactly \(s=1/3\) remains ground-optimal at every sufficiently high but finite bath temperature.

**5. Optimal incoherent comparison and finite witness.** Restricting to diagonal reset states sets \(t=0\). At the boundary its QFI is \(\omega^2(sa-1)^2/4\); maximizing \(-1\le a\le1\) selects \(a=-1\), with value \(\omega^2(1+s)^2/4\). Uniform continuity and QFI convexity under mixing temperature-independent reset targets show that ground reset remains the best diagonal target for small \(x\). The coherent-to-diagonal ratio therefore has the displayed limit. Its derivative in \(s>1/3\) is positive, and its limit at infinity equals four.

For the finite witness of the Finding, substitute \((x,s,\kappa,a)=(1/5,2,1,-1/2)\), \(t=3/4\), into the exact QFI. Rational arithmetic gives the displayed \(F_\beta=11574741702400/8063279547193\). For diagonal resetting at the same parameters the endpoint QFIs are \(405/338\) at \(a=-1\) and \(150/1183\) at \(a=1\); their mixtures cannot exceed the larger endpoint by QFI convexity. The exact positive gap is \(3826239519515/16126559094386\).

## Verification

The accompanying `verify.py` checks the exact stationary Bloch formula against the stationary master equations, verifies the analytic state derivatives by centered differences, checks high-temperature limiting coefficients and the critical-line slope, and reproduces the exact finite-parameter witness using rational arithmetic. Run with `python verify.py`; it uses only the Python standard library. Finite tests corroborate algebra and implementation but do not replace the uniform analytic proof or the implicit-function argument.

## Relationship to prior work

Li, Tong and Bao (arXiv:2610.31249v1, submitted 2026-10-22) derive the general reset Lindbladian and optimize *ground-state* steady thermometry; their supplemental Section III confines the stationary Davies-qubit example to a diagonal ground reset. They treat coherent reset targets in a **different frequency-estimation task**, not the present all-target thermal-QFI optimization. The present result reduces to their ground-reset expression on the diagonal boundary, and then determines the coherent-target optimization missing from that benchmark.

Frazão and collaborators (arXiv:2405.14439v1, 2024-05-23) establish that coherence can enhance *transient thermometry through choice of the initial state* under unreset thermalization. Their nonnegative coherence-QFI decomposition is important related prior art, but it does not supply a reset-rate threshold, an optimized stationary reset target, or the boundary slope. The contribution is *not* a claim that coherence first became useful for thermometry here.

Altintas (arXiv:1602.06783v1, 2016-02-19) studies stationary QFI in a different two-qubit dephasing-and-reset model with SU(2) phase estimation, not bath inverse-temperature QFI for a thermal Davies qubit. Neither that model nor its metrological objective implies the present sharp target transition.

## Limitations

The bosonic transition rate \(\Gamma\) diverges as \(\beta\to0\). Consequently the phase law is an exact mathematical boundary result *within the ideal Davies-rate model*, not a device prescription for arbitrarily hot reservoirs. All assertions about an exact optimum at positive temperature are restricted to sufficiently small \(\beta\omega\), with \(s\) fixed or in a specified neighborhood of \(1/3\); a global finite-temperature phase diagram is not claimed. The QFI is for single-copy steady-state inference with unrestricted choice of a temperature-independent reset target and no preparation-cost budget. No claim is made about optimized multi-qubit protocols, finite data Bayesian risk, or an externally independently certified literature priority.

## References

1. Silan Li, Qingjun Tong and Ruicheng Bao, *Reset-Enhanced Dissipative Quantum Metrology*, arXiv:2610.31249v1 (first submitted 2026-10-22). https://arxiv.org/html/2610.31249v1.
2. Gonçalo Frazão, Marco Pezzutto, Yasser Omar, Emmanuel Zambrini Cruzeiro and Stefano Gherardini, *Coherence-enhanced single-qubit thermometry out of equilibrium*, arXiv:2405.14439v1 (first submitted 2024-05-23). https://arxiv.org/abs/2405.14439.
3. Azmi Ali Altintas, *Quantum Fisher Information of an Open and Noisy System in the Steady State*, arXiv:1602.06783v1 (first submitted 2016-02-19). https://arxiv.org/abs/1602.06783.
