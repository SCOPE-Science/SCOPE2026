# Scientific review

## Correctness — PASS

The exact statement applies to two specified stable stationary linear-noise models of the substrate-input Michaelis–Menten reaction. The full drift and diffusion are obtained from the four elementary stoichiometric events, while the heuristic drift and diffusion follow from the reduced saturating propensity. An explicit two-by-two transfer-matrix inversion yields the full power spectrum, and subtracting the heuristic spectrum produces a numerator \(-d\omega^4+B\omega^2+C_0\), where both \(B\) and \(C_0\) are strictly positive for every permitted physical equilibrium. Its unique positive root for \(d>0\) and strict positivity for \(d=0\) establish the result without relying on finite sampling. A separate exact symbolic polynomial check and 5,000 numerical comparisons, including 100 independent Lyapunov covariance cases, substantiate the algebra. The claims concern linear-noise spectra, not the finite-volume chemical master equation.

## Originality — PASS on inspected evidence; historical priority provisional

The strongest exact-model predecessor is Thomas, Straube and Grima (2011), https://arxiv.org/html/1110.6617v1, which proves that the heuristic reduction overstates steady-state substrate *variance*. Because variance is a frequency integral, that finding neither implies nor contradicts the frequency-local reversal; the integral of the signed difference can be positive despite a high-frequency negative tail. The 2012 Thomas–Straube–Grima ssLNA article, https://doi.org/10.1186/1752-0509-6-39, derives general spectral methods but does not give this sharp comparison theorem. The closely relevant 2025 Marmolejo Lozano–Popović–Grima analysis, https://arxiv.org/html/2510.27600v1, studies enzyme **cross-coherence and mutual-information** spectra, not the sign of the *substrate auto-spectrum* difference for this product-untracked model; generic matrix formulas do not by themselves settle the sign or root count. Eilertsen–Srivastava–Schnell (2021), https://arxiv.org/abs/2101.04814, develops geometric model reduction, not this stated comparison. No matching source was found in the examined searches, but absence from a search does not establish priority. The full text of the 2021/2022 geometric treatment was not fully inspected, and broader unlocated spectral comparison results remain a historical risk.

## Mathematical value — PASS

A previously known integrated-variance overestimate can mask *frequency-local underestimation*. The exact single-crossover classification supplies a falsifiable, parameter-sensitive distinction between slow and fast spectral content: the heuristic hQSSA necessarily reverses its error sign when dissociation is nonzero, with an explicit crossover, while absence of dissociation forbids the reversal. The threshold is robust for all permitted binding, catalysis, enzyme and substrate values; no fine tuning, numerical root search, or assumption of arbitrary time-scale separation is needed. The high-frequency scale can be outside the validity of QSSA, and this caveat is part of the interpretation, not a premise hidden from the proof.

## Closest literature and limitations

The 2011 full model and the 2025 full/reduced spectral-matrix setting are the closest inspected research. This is a result for a **specified pair of Gaussian LNA spectra**, not a general theorem about all stochastic reduction methods or physical high-frequency simulation accuracy. Independent evaluation of historical novelty and of the full model beyond LNA has not been carried out.

Self-review: passed. Independent audit: not yet performed.
