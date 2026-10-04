# Same-model review

## Correctness
**PASS.** The determinant factorization was reconstructed directly and replayed symbolically. Because distinct columns make the Vandermonde factor nonzero, singularity is equivalent to a weight-six vanishing sum of \(N\)-th roots. The Lam--Leung weight theorem excludes such a sum when \(\gcd(N,6)=1\), while explicit distinct-root constructions cover every \(N\ge5\) divisible by \(2\) or \(3\). The divisor-uniformity statement follows from an exhaustive residue-count argument by divisor size.

## Originality
**PASS.** The closest published full-spark source gives the single order-\(10\) obstruction for these rows and states the broader composite-order problem rather than an all-order classification. A later array-ambiguity paper uses the same symmetric polynomial for a continuous problem, but it does not state the discrete order-\(N\) criterion. Targeted searches for the row pattern, the symmetric-polynomial formulation, and the weight-six formulation found no theorem implying this claim. Residual risk remains for differently phrased or unindexed work.

## Value
**PASS.** The result converts a canonical isolated composite-order counterexample into a complete infinite classification for the same four-row pattern. It also identifies exactly when the standard divisor-uniformity test succeeds yet full spark fails, namely \(N\equiv2\) or \(10\pmod{12}\).

## Closest literature and limitations
The supporting vanishing-sum theorem is Lam--Leung, arXiv:math/9511209. The closest full-spark special case is Alexeev--Cahill--Mixon, arXiv:1110.3548. The closest equivalent polynomial object appears in Matter--Fischer--Pesavento--Pfetsch, arXiv:2110.10756. The finite verifier does not certify the infinite theorem by enumeration; it checks the algebra and substantial finite ranges while the proof supplies the all-order argument.

Same-model review: passed. Independent audit: not yet performed.
