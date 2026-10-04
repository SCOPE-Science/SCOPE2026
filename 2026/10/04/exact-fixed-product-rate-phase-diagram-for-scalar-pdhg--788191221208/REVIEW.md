# Same-model review

## Correctness
PASS. The recurrence was reconstructed directly from the published basic-PDHG update. Its trace, determinant, and discriminant reduce to functions of \(p=\tau\sigma\) and \(s=\tau+\sigma\). The complex-root modulus is strictly decreasing in \(s\); the dominant real root is strictly increasing in \(s\); this yields the complete fixed-product minimizer classification. The remaining one-variable derivative identity proves the unique global optimum. The reciprocal adaptive updates preserve the product by direct multiplication. The packaged checker independently re-evaluates the algebraic identities and representative numerical cases.

## Originality
PASS. Targeted searches covered the exact scalar claim, fixed-product aliases, critical damping, reciprocal step updates, and spectral-radius tuning. Goldstein et al. provide the adaptive rule and residual-balancing motivation but no spectral-radius solution. Fercoq provides the closest broader treatment: a general quadratic iteration matrix and a spectral-radius adaptation strategy, while explicitly arguing that residual balancing can be nonoptimal. The inspected relevant sections do not state the closed-form scalar phase transition, the two asymmetric minimizers, or the unique global pair claimed here. Previously recorded findings were checked by claim and method; the closest scalar primal-dual record concerns a different PDAL/least-squares recurrence and does not imply this strongly convex-concave PDHG classification.

## Value
PASS. The source paper presents residual balancing as a practical way to tune the primal/dual ratio while keeping the product fixed. The exact scalar classification identifies what that invariant leaves untuned and shows a non-obvious symmetry breaking below a natural product threshold. This gives a clean benchmark for designing or testing product-adaptive PDHG rules and a closed-form target against which spectral heuristics can be checked.

## Closest literature and limitations
The closest broader source is Fercoq (2024), which motivates direct spectral-radius tuning for quadratic PDHG and reports that it can improve on residual balancing. The present claim is intentionally narrower and exact. It does not assert multidimensional optimality or a rate theorem for the nonstationary adaptive sequence. An unindexed thesis, note, or implementation analysis could contain the same scalar calculation.

Same-model review: passed. Independent audit: not yet performed.
