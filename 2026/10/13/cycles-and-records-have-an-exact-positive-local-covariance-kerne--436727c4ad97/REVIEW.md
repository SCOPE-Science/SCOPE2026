# Review

## Correctness

PASS. The largest-label cycle insertion is a bijection between \(S_{n-1}\times[n]\) and \(S_n\), so both the insertion site and the smaller permutation are exactly uniform and independent. The upper-record event at a fixed earlier position has a complete three-case description according to whether the new maximum is inserted before, at, or after that position.

Conditioning on the insertion site gives the mixed-moment recurrence exactly. Subtracting the product of the known means collapses it to a multiplicative covariance recurrence with an explicit boundary value at \(n=j\). The displayed kernel follows by a finite product. The total covariance, variance, and asymptotic correlation then follow by exact summation and elementary bounds.

The packaged checker independently enumerates all permutations through \(n=9\) and recomputes cycles and records from their definitions.

## Originality

PASS, with a specific residual risk from older joint-enumeration literature. Gnedin--Gorin is the closest full primary source inspected: it defines the same upper records, gives the independent initial-rank coordinates under the uniform law, and explains the fundamental-bijection relation from records to cycles. That relation establishes equidistribution through a transformation of permutations, not the same-permutation covariance in the accepted claim.

Bakšajeva--Manstavičius develops cycle statistics in the Ewens framework and verifies the probability classification. Its stated results concern additive cycle statistics and do not contain record coordinates.

Targeted database searches combining cycle count with record indicators, left-to-right maxima, total records, covariance, and joint distribution did not locate the displayed kernel. Search absence is not treated as proof: the residual risk explicitly includes classical bivariate generating functions that may imply it.

## Value

PASS. Cycle count and record count are two of the most classical equidistributed permutation statistics, and their equality in distribution can obscure their dependence when evaluated on the same object. The local kernel resolves that distinction at every record coordinate, showing a uniform positive sign with an unexpectedly sparse binomial profile.

The aggregate result also quantifies the scale of the dependence: covariance is of order \(1/n\), while the correlation is only \(1/(n\log n)\). This provides an exact finite bridge between two canonical coordinate systems for random permutations rather than a routine marginal identity.

Self-review: passed. Independent audit: not yet performed.


Exact replay: `VERIFY_OK permutations_checked=409112 probability_checks=44 local_covariance_checks=44 positivity_checks=36 total_covariance_checks=8 variance_checks=16`.
