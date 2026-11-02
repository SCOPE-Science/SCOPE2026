# Scientific review

## Correctness

**PASS.** The invariant process has a bilateral stationary construction and synchronous contraction. Conditional on the reset history it is Gaussian with bounded random variance. Splitting at a Poisson mark gives a Beta-factorized variance deficit, including an exact small-deficit distribution. The generator gives the exact recurrence for every stationary even moment; the Gamma ratio and an absolutely convergent product give a high-order equivalent. A uniformly dominated Beta integral identifies the same amplitude in the Gaussian density tail. The conditional Gaussian quadratic transform proves the strict and borderline exponential-moment thresholds without finite-sampling inference. Exact rational and independent numerical checks replay from `verify.py` (54 passed).

## Originality

**PASS (qualified).** The motivating 2026 Fokker–Planck article derives the Student-type stationary law of a *diffusion approximation*, not the high-order and far-tail law of the exact contraction-jump model. Earlier work by Olsen and Gupta contains the harmonic-potential second moment, explicitly acknowledged and not submitted as new; its technical §§III.C and IV.B do not present the sharp all-orders asymptotic, the infinite-product Gaussian-edge coefficient, or the critical quadratic tilt. Biroli et al. and Tal-Friedman et al. treat unconfined partial resetting. Olsen's independent resetting-to-a-distribution protocol is not state-dependent proportional resetting. A search of published mathematical results did not locate a statement that implies the combined sharp edge and critical moment theorem. These comparisons establish best-knowledge originality, not uniqueness or a guarantee against broader unpublished/perpetuity-theory results.

## Value

**PASS.** The full density-edge coefficient and universal exponent quantify rare excursions following an anomalously long interval without resets, while the exact quadratic-tilt threshold distinguishes distinct regimes of exponential sensitivity. The same physically motivated linear model has an approximation with the opposite all-order moment behavior, explaining a mathematically precise nonuniformity between weak-reset convergence and extreme-event predictions. The contributions are not simply variance recalculation, a parameter substitution, or a finite numerical example.

## Closest literature and scientific limits

Galla, arXiv:2602.21635, supplemented with the primary full-text §S1.1; Olsen–Gupta, arXiv:2401.11919, §§III.C and IV.B; Biroli et al., arXiv:2406.08387, §§II–IV and conclusion; Tal-Friedman et al., arXiv:2205.03363; Olsen, arXiv:2310.04840. Precise result is confined to linear mean-reverting dynamics and deterministic proportional Poisson contractions. No uniformity is claimed in the near-identity contraction limit or in joint large-excursion/weak-jump scaling. The general theory of Gaussian mixtures and perpetuities could contain an equivalent observation under a different title. No independent audit or publication-priority certification is claimed.

Self-review: passed. Independent audit: not yet performed.
