# Same-model review

## Correctness
PASS. The exact lower bound is the expected distance of a product-distributed word to the target type-class support. The constructed minimal repair kernel is coordinate-permutation equivariant, so exchangeability forces its target law to be uniform on the transitive type-class orbit; hence the lower bound is attained. The finite bound follows from multinomial variances, and the sharp fixed-type constant follows from the multinomial central limit theorem plus uniform integrability. The quantum corollary uses the single-system classical-to-quantum \(W_1\) data-processing step explicitly used in arXiv:2609.17309v1. Orthogonal prepared states recover classical Hamming-Wasserstein distance.

## Originality
PASS. The closest direct source, arXiv:2605.15114v2, gives Proposition 23 with a \(\sqrt{\log(n+1)}\) loss and only a heuristic earth-mover explanation in Remark 26. The September 2026 GQSL paper repeats that estimate as Proposition 22 and uses it in equations (3.56)--(3.59), without a sharper quantitative statement. The inspected constant-composition distribution-matching paper studies informational divergence rather than Hamming-Wasserstein cost. Public literature and database searches over exact-claim, slice/type-class, multinomial-deviation, and fixed-composition aliases did not surface a covering statement. Residual risk remains that an equivalent classical identity appears in older literature under remote terminology.

## Value
PASS. This is the exact transport computation behind a recent almost-i.i.d. construction: it removes an artificial logarithmic loss, supplies the sharp fixed-type asymptotic coefficient, and proves that the normalized \(n^{-1/2}\) order cannot be improved uniformly over quantum signal families. The improvement is directly reusable in quantitative versions of the cited type-class and arbitrarily-varying-null arguments.

## Closest literature and limitations
The closest papers are Girardi--De Palma--Lami, arXiv:2605.15114v2, and Girardi--Lee--Hayashi--Lami, arXiv:2609.17309v1. The quantum inequality may be strict for nonorthogonal signal states, no second-order asymptotic is claimed, and the improved rate does not by itself alter the already-established asymptotic Stein exponent.

Same-model review: passed. Independent audit: not yet performed.
