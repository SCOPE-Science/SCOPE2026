# Scientific review: sharp spectral-onset bifurcation

## Correctness
PASS. The stated spectrum is independently reconstructed from a four-state cyclic generator and a symmetric binary switch; its stationary covariance is a damped cosine plus a decaying exponential. Exact common-denominator algebra reduces positive oscillation efficiency to the strict positivity of a concave quadratic. The quadratic maximizer stays below the finite cut-off required for its monotonicity in switching rate. The critical directionality follows from an explicitly increasing scalar function, and the local maximum expansions prove all three onset laws. `VERIFY.py` passed 321 deterministic tests, including direct eight-state resolvent checks. Numerical tests are not treated as proof.

## Originality
PASS under same mathematical model literature comparison. Jia (arXiv:2610.23310v1) defines the same model and prints the complete spectrum, but states only a sufficient local-curvature condition, not the sharp global criterion, directionality threshold, or finite-frequency jump. Dechant (arXiv:2306.00417) establishes broader spectral-dissipation bounds; its accessible abstract and the originating article's full discussion do not settle this model-specific optimization. General spectral methods might contain related extrema results; full prior coverage cannot be ruled out.

## Value
PASS. A positive-frequency peak can become globally dominant before the zero-frequency curvature changes sign, which is a practical distinction when detecting stochastic molecular oscillations from a measured spectrum. The exact bias boundary and crossover exponents provide a meaningful finite-state classification, including a distinct jump regime. The result is a global spectral analysis rather than merely a numeric fit.

## Scope and limitations
The result is specific to the finite independent Markov model, its total-phosphorylation observable, the stationary spectral normalization, and strictly positive rates. The transition is a change of global spectral maximizer, not a singular change in the invariant distribution. The full text of the 2023 general spectral-bounds predecessor was not accessible, and independent correctness and priority validation remain outstanding.

Self-review: passed. Independent audit: not yet performed.
