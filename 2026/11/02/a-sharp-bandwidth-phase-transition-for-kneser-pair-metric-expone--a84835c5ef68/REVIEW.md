# Scientific review — Kneser exponential pair-metric kernels

## Correctness
**PASS.** The elementary incidence identity \(BB^{\mathsf T}=(n-2)I+J\) produces the full orthogonal eigenspace decomposition, and direct multiplication gives the three kernel eigenvalues, with the unique potentially nonpositive eigenvalue \(1-(n-3)e^{-t}+(n-4)e^{-2^p t}\). Its derivative changes sign at most once, proving strict negativity precisely before the unique positive root when the exponent exceeds the stated threshold. Positive-root differentiation and a uniform Taylor argument establish monotonicity and the fixed-\(c\) critical-window correction. Exact incidence and rational checks, independent full-matrix tests, and selected root tests passed; the proof, not sampling, supports all quantifiers. No separate formal verification was performed.

## Originality
**PASS, qualified.** Aalipour et al. (arxiv:1509.01196, Section 3.2) already determine the broader Kneser distance spectrum; Meckes (arxiv:1012.5863, Theorem 3.3) establishes the all-scales negative-type equivalence; Sánchez (arxiv:1108.0451) supplies general finite-metric negative-type criteria; and Feragen–Lauze–Hauberg (arxiv:1411.0296) address general geodesic exponential kernels. None of the directly inspected materials states the scale-resolved one-root phase diagram, exact inertia, increasing dimension-dependent critical window or first-order correction. The spectral ingredients and the unpowered negative-type corollary are **not** presented as new. An equivalent derivation in other association-scheme literature remains possible.

## Mathematical value
**PASS.** One finite matrix family has a sharp three-phase Gram signature at individual bandwidths, an exact boundary in admissible powers, and a nonzero universal crossover timescale when the power and graph size vary together. These outcomes address a natural kernel-validity distinction not decided by the all-bandwidth Schoenberg criterion, without asserting a general Kneser-graph theorem.

## Closest sources and scientific limits
The nearest coverage risk is the general Kneser distance-spectrum theorem of Aalipour et al.; applying its eigenspaces to transformed two-distance data leads to the scalar reduction here. The new claim rests on following that reduction through the full parameter domain and critical asymptotics. It applies only to unweighted \(KG(n,2)\), all positive real powers and bandwidths, and fixed \(c>1\) in the asymptotic regime. It does not assert novelty for raw eigenspace formulas or establish uniformity at the boundary \(c=1\).

Self-review: passed. Independent audit: not yet performed.
