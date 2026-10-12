# Review
## Correctness
PASS. A direct marked-sequence count gives the exact coefficient of every completion time: choose the final new type, choose a distinct multiplicity-\(r\) type, place its \(r\) occurrences, and map the remaining positions onto the other \(m-2\) types. The Stirling-number generating function then gives the transform for all \(m\ge2\) and \(r\ge2\). Differentiation yields the doubleton covariance, and an explicit positive increment proves its strict sign for \(m\ge3\).

The packaged checker exhaustively replays small coupon sequences and independently verifies the harmonic algebra and sign increments using exact rational arithmetic.

## Originality
PASS, with a classical-literature risk. The closest stopping-time source already has the exact singleton/completion-time joint law, so the accepted theorem explicitly excludes \(r=1\). The closest exact-\(r\) spectrum source works at prescribed sampling phases, and the closest modern completion-time spectrum source supplies marginal residual-count identities and asymptotics but not the finite joint transform with \(T_m\).

The principal residual risk is an equivalent Stirling-number identity in older occupancy literature under different notation.

## Value
PASS. The transform links the defining coupon-collector stopping time to every non-singleton multiplicity coordinate and gives all mixed moments by differentiation. The doubleton case reveals a strict finite negative covariance and its \(-m(\log m)^2/2\) scale, providing a concrete measure of how delayed completion redistributes the stopped occupancy spectrum.

## Closest literature and limitations
Singleton/completion-time dependence is prior work, as are marginal multiplicity counts at completion. The new content is the \(r\ge2\) completion-time transform and its mixed-moment consequences. The argument assumes equal coupon probabilities and does not provide the full multivariate transform of all multiplicity coordinates simultaneously.

Self-review: passed. Independent audit: not yet performed.
