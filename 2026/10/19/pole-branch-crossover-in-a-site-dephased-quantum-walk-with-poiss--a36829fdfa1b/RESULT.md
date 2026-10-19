# Pole–branch crossover in a site-dephased quantum walk with Poisson resetting

## Finding
Fix real hopping \(h\ne0\), reset rate \(r>0\), and site-dephasing rate \(\gamma\ge0\). For the infinite nearest-neighbor quantum walk specified below, write \(p_m\) for the probability of site \(m\in\mathbb Z\) in its unique reset-stationary state. Define
\[
\kappa_b=2\operatorname{arsinh}\frac{r+\gamma}{4|h|},\qquad
\kappa=2\operatorname{arsinh}\frac{\sqrt{r(r+2\gamma)}}{4|h|},\qquad
C_\gamma=8h^2\sinh\kappa_b,
\]
and \(V_\gamma(t)=8h^2[\cosh(\kappa_b+t)-\cosh\kappa_b]\). All \(p_m\) are positive and symmetric in \(m\); their characteristic function is
\[
F_\gamma(k)=\sum_{m\in\mathbb Z}p_m e^{ikm}
=\frac{r}{\sqrt{(r+\gamma)^2+16h^2\sin^2(k/2)}-\gamma}.
\]
For every integer \(m\ge0\) the **exact** decomposition into a pole and a nonnegative branch integral is
\[
\boxed{p_m=\frac{r\gamma}{4h^2\sinh\kappa}e^{-\kappa m}
+\frac{r e^{-\kappa_b m}}{\pi}\int_0^\infty e^{-mt}
\frac{\sqrt{V_\gamma(t)}}{\gamma^2+V_\gamma(t)}\,dt.}\tag{1}
\]
At \(\gamma=0\) the first term vanishes and the integrand means \(1/\sqrt{V_0(t)}\). For fixed \(\gamma>0\), \(\kappa<\kappa_b\), so
\[
p_m=\frac{r\gamma}{4h^2\sinh\kappa}e^{-\kappa m}
+\frac{r\sqrt{C_\gamma}}{2\sqrt\pi\gamma^2}
 m^{-3/2}e^{-\kappa_bm}(1+O(m^{-1})).\tag{2}
\]
For \(\gamma=0\) instead,
\[
p_m=\frac{r}{\sqrt{\pi C_0m}}e^{-\kappa_bm}(1+O(m^{-1})).\tag{3}
\]
Thus arbitrarily weak positive site dephasing changes the ultimate spatial-tail prefactor from \(m^{-1/2}\) to a pure exponential. The singular change has the following **universal crossover**: for any positive sequence \(\gamma_m\to0\) such that \(u_m=\gamma_m\sqrt{m/C_{\gamma_m}}\to u\in[0,\infty)\),
\[
\boxed{\lim_{m\to\infty}\frac{\sqrt{C_{\gamma_m}m}}{r}
 e^{\kappa_b(\gamma_m)m}p_m(\gamma_m)
=\frac1{\sqrt\pi}+u e^{u^2}\operatorname{erfc}(-u).}\tag{4}
\]
The crossover spatial scale is \(m\asymp C_0/\gamma^2\). At fixed rates the exact stationary variance is \(4h^2/[r(r+\gamma)]\).

## Assumptions and scope
Work on \(\ell^2(\mathbb Z)\). Define \(H=h\sum_j(|j+1\rangle\langle j|+|j\rangle\langle j+1|)\) and the bounded trace-class generator
\[
\mathcal L_0(\rho)=-i[H,\rho]+\gamma\left(\sum_{j\in\mathbb Z}|j\rangle\langle j|\rho|j\rangle\langle j|-\rho\right).
\]
The reset generator on normalized states is \(\mathcal L(\rho)=\mathcal L_0(\rho)+r(|0\rangle\langle0|\operatorname{Tr}\rho-\rho)\). The total dephasing rate of off-diagonal entries is exactly \(\gamma\), not twice that value. Results concern site-diagonal probabilities in the unique infinite-time stationary state; no claim about off-diagonal stationary coherences or finite observation times is needed. All parameters are physical constants independent of the site index.

## Proof
**1. Reset renewal and uniqueness.** The trace-preserving completely positive semigroup \(e^{t\mathcal L_0}\) contracts trace norm. Two normalized solutions of the reset equation differ by \(e^{-rt}e^{t\mathcal L_0}\) applied to the initial difference, hence approach one another exponentially. In trace norm the unique stationary state equals
\[
\rho_*=r\int_0^\infty e^{-rt}e^{t\mathcal L_0}(|0\rangle\langle0|)\,dt.
\]
**2. Exact Fourier transform.** Site monitoring at rate \(\gamma\) yields a renewal equation for the position probabilities: between monitoring events the free amplitude from the origin to \(m\) is \((-i)^mJ_m(2ht)\), so the free kernel is \(J_m(2ht)^2\). The addition formula for Bessel functions gives its spatial Fourier transform \(J_0(4ht\sin(k/2))\). The Laplace transform for \(s>0\) is
\[
K(k,s)=\int_0^\infty e^{-(s+\gamma)t}J_0(4ht\sin(k/2))dt
=[(s+\gamma)^2+16h^2\sin^2(k/2)]^{-1/2}.
\]
After a monitoring event the walker is localized at its measured site. Translation covariance makes the renewal convolution exact; summing all event counts gives \(\widehat P(k,s)=K(k,s)/(1-\gamma K(k,s))\). Set \(s=r\) and multiply by \(r\) to obtain \(F_\gamma\). This is not an assumption of classical diffusive hopping; the coherent Bessel kernel is retained between all monitoring events. Normalization follows from \(F_\gamma(0)=1\).

**3. Exact Fourier-coefficient decomposition.** Let \(W(k)=(r+\gamma)^2+8h^2(1-\cos k)\). Algebraically,
\[
\frac r{\sqrt W-\gamma}=\frac r{\sqrt W+\gamma}+\frac{2r\gamma}{W-\gamma^2}.
\]
The second term is the Fourier transform of \(r\gamma e^{-\kappa|m|}/(4h^2\sinh\kappa)\), since \(W-\gamma^2=8h^2(\cosh\kappa-\cos k)\). The first term is analytic in the annulus bounded by the branch points at \(e^{\pm\kappa_b}\). Its Fourier coefficients can be obtained by contour deformation for \(z=e^{ik}\), with the external square-root cut \(z=e^{\kappa_b+t}\), \(t\ge0\). Across the cut \(W=-V_\gamma(t)\) and the jump of \(r/(\sqrt W+\gamma)\) is \(-2ir\sqrt V/(\gamma^2+V)\); the inversion contour contributes the positive integral in (1). For \(m=0\), convergence at infinity follows from the extra exponentially decreasing jump; at \(t=0\), the singularity is integrable even when \(\gamma=0\). This proves (1) for all \(m\ge0\). Spatial reflection handles negative \(m\).

**4. Fixed-rate tails.** Since \(\cosh\kappa_b-\cosh\kappa=\gamma^2/(8h^2)\), \(\kappa<\kappa_b\) for \(\gamma>0\). At the branch edge \(V_\gamma(t)=C_\gamma t+O(t^2)\), with \(C_\gamma>0\). For \(\gamma>0\), Watson's lemma gives
\[
\int_0^\infty e^{-mt}\frac{\sqrt{V_\gamma(t)}}{\gamma^2+V_\gamma(t)}dt
=\frac{\sqrt{\pi C_\gamma}}{2\gamma^2m^{3/2}}(1+O(m^{-1})).
\]
For \(\gamma=0\), the integrand is \((C_0t)^{-1/2}(1+O(t))\), yielding \(\sqrt{\pi/(C_0m)}(1+O(m^{-1}))\). Substitution proves (2)–(3); for positive \(\gamma\), the branch correction is exponentially smaller than the pole.

**5. Uniform weak-dephasing window.** Put \(\gamma=\gamma_m\), \(u_m=\gamma_m\sqrt{m/C_{\gamma_m}}\). Rescaling \(t=s/m\) in the nonnegative branch integral and using \(V_{\gamma_m}(s/m)=(C_{\gamma_m}s/m)(1+o(1))\) locally uniformly shows
\[
\lim_{m\to\infty}\frac{\sqrt{C_{\gamma_m}m}}{\pi}
\int_0^\infty e^{-mt}\frac{\sqrt{V_{\gamma_m}(t)}}{\gamma_m^2+V_{\gamma_m}(t)}dt
=\frac1\pi\int_0^\infty e^{-s}\frac{\sqrt s}{u^2+s}\,ds.
\]
Uniform domination follows by splitting the integral at a fixed small \(t\): on the first interval \(V_\gamma(t)\) is uniformly bounded between positive multiples of \(t\) for all sufficiently small \(\gamma\), and \(\sqrt V/(\gamma^2+V)\le1/\sqrt V\); the rest is killed by \(e^{-mt}\), with \(V\) increasing. The integral evaluates to \(1/\sqrt\pi-u e^{u^2}\operatorname{erfc}(u)\), continuously at \(u=0\). The pole factor satisfies
\[
\kappa_b-\kappa=\gamma^2/C_\gamma+O(\gamma^4),\qquad
\frac{\sqrt{C_\gamma m}\,\gamma}{4h^2\sinh\kappa}\longrightarrow 2u.
\]
Therefore its scaled limit is \(2ue^{u^2}\). Adding the branch limit and using \(\operatorname{erfc}(-u)=2-\operatorname{erfc}(u)\) proves (4), including \(u=0\).

**6. Variance and positivity.** Expansion at \(k=0\) yields \(F_\gamma(k)=1-2h^2k^2/[r(r+\gamma)]+O(k^4)\), proving the variance. The Bessel process has strictly positive probability to visit every lattice displacement before a reset (for \(h\ne0\)), giving \(p_m>0\); normalization and symmetry are already proved.

## Verification
Run `python artifacts/verify.py` with `numpy>=1.24` and `scipy>=1.10` (versions are minimum tested APIs; no exact upper version asserted). The verifier independently forms finite-ring Liouvillian linear systems with site-dephasing Lindblad terms and reset, compares local stationary populations against the infinite-lattice Fourier expression, evaluates independent Bessel-reset integrals in the coherent case, checks moments and prefactor asymptotics. Reported execution: `VERIFY_OK finite_lindbladian=28 bessel_integrals=5 stationary_moments=4 tail_checks=7 branch_cut=15 crossover=3 max_error=1.4e-09`. Ring computations test finite-size approximations, **not** an infinite-volume proof; the latter is analytical above. The integral contour and uniform asymptotic proofs do not rest on floating-point calculations.

## Relationship to prior work
Solenov and Fedichkin (2005) studied site decoherence and finite-cycle continuous-time quantum walks; Bessen (2006) analyzed exact coherent lattice-walk distributions. Wald and Böttcher (2020 preprint, 2021 journal) established general stochastic-reset stationary-state methods on networks for their quantum stochastic walk family; this gives a general reset-resolvent framework but not the spatial pole–branch coalescence proved here for infinite-lattice **projector site dephasing**. Bressanini, Benedetti and Paris (2022) explicitly considered Haken–Strobl position dephasing on finite graphs without resetting. These standard model ingredients and the general resolvent are not novelty claims. The specific exact split (1), fixed-rate tail-type distinction (2)–(3), and singular universal transition law (4) are the assessed contribution. Equivalence under Fourier/Laplace rewriting, specialization of network resetting, and generic singularity analysis were evaluated; broader unknown literature might still cover these calculations.

## Limitations
The asymptotic crossover assumes \(r,h\) fixed while \(\gamma\to0\) and \(m\to\infty\); it does not describe finite-time approach to stationarity, position-dependent dephasing, finite rings in their ultimate large-distance regime, coherent resets to mixed states, or other graph families. A general reset-resolvent formula is known, and a more general unpublished or unlocated special-function treatment could contain the same explicit asymptotics. No independent publication-priority audit has been performed.

## References
1. D. Solenov and L. Fedichkin, *Continuous-time Quantum Walks on a Cycle Graph*, arXiv:quant-ph/0506096 (first public version 2005-06-13), https://arxiv.org/abs/quant-ph/0506096.
2. A. Bessen, *Distributions of continuous-time quantum walks*, arXiv:quant-ph/0609128 (2006), https://arxiv.org/abs/quant-ph/0609128.
3. S. Wald and L. Böttcher, *From classical to quantum walks with stochastic resetting on networks*, arXiv:2008.00510 (2020), Phys. Rev. E 103, 012122 (2021), https://arxiv.org/abs/2008.00510.
4. G. Bressanini, C. Benedetti and M. G. A. Paris, *Decoherence and classicalization of continuous-time quantum walks on graphs*, Quantum Information Processing 21, 317 (2022), https://doi.org/10.1007/s11128-022-03647-x.
