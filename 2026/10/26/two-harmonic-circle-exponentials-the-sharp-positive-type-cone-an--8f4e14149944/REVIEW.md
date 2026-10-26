# Scientific review

## Correctness — PASS
The Fourier criterion on \(\mathbb T\) is correctly normalized: multiplication by the strictly positive constant \(e^{-a-b}\) does not affect coefficient signs. Positive Bessel convolution proves every admissible coefficient's sign and the exact gcd support. For necessity, the proof does not mistake experiments for a universal theorem: if only finitely many coefficients were negative, correcting them by a finite Laurent polynomial would enforce the complex-circle inequality \(|\Phi(re^{i\theta})|\le\Phi(r)+2P(r)\). Explicit angles force incompatible exponential growth for each forbidden sign combination. The quotient-circle Vandermonde step proves the sharp strictness statement. The checker reproduces supplementary finite calculations, but the proof handles arbitrary harmonic integers, parameters, and finite configurations.

## Originality — PASS under bounded comparison
The closest inspected primary source, Janke–Kleinert (arXiv:hep-lat/9504010v1, 1995), treats generalized Bessel coefficients of the two-harmonic exponential when the frequencies are one and two; its analysis concerns a few low-order weights and lattice phase-transition mechanisms, not the entire coefficient sign sequence or the sharp quadrant across arbitrary harmonic pairs. Gatto–Jammalamadaka (2007) studies positive probability densities, not stationary positive-type kernels. Gneiting (arXiv:1111.7077) gives the spectral criterion rather than the signed-coefficient classification. Indexed comparisons with sparse trigonometric-polynomial extremal theorems concern different objects and do not subsume the present exponential-kernel assertion. General or unindexed results might still contain an equivalent consequence; novelty is not certified beyond these inspected comparisons.

## Mathematical value — PASS
The object is a natural two-harmonic exponential covariance profile related to generalized von Mises and compact-model Bessel coefficients. The theorem gives a full, non-obvious admissibility classification across every pair of integer harmonics, strengthens failure to infinitely many negative frequencies, identifies the precise strictness quotient, and explains why a finite sampling grid can miss a small illegal signed perturbation. This is structural information about a motivated family rather than a single arbitrary computation.

## Boundaries and reproducibility
All nontrivial sign combinations and \(a=0\) or \(b=0\) boundaries are covered. No claim is made about three or more harmonics, arbitrary phases, or a quantitative universal witness size. `checker.py` needs Python 3 only; experiments support, but do not certify, the analytic proof. Literature comparison and model-level review are bounded, and independent audit is pending.

Self-review: passed. Independent audit: not yet performed.
