# Scientific review: index-eleven permutation-binomial characteristics

## Correctness
**PASS.** The theorem quantifies over every prime characteristic, every finite extension degree, all positive exponents, and every nonzero coefficient. The quotient-map criterion follows from fibers of the power map. The product of nonzero permutation values forces the Wendt obstruction. The exact resultant has four prime divisors. For the three primes beyond \(23\), every eleventh root of unity lies in the prime field, so the two reciprocal-moment equations are necessary independent of the extension degree. The finite certificate enumerates every possible value of their parameters and finds no joint root. A direct permutation over \(\mathbb F_{23}\) proves sufficiency. The finite enumerations are certificates of the reduction, not arbitrary-degree experiments.

## Originality
**PASS, provisionally.** The September 2026 characterization of \(X^r(X^{q-1}+a)\) concerns gcd index \(q-1\), not the fixed index \(11\) studied here. The October 2026 Wendt-determinant article proves characteristic finiteness for all fixed indices and the index-eleven classification over prime fields, but only obtains the candidate-prime set over arbitrary extensions. Its prime-field argument does not imply the extension-field exclusion of \(199\), nor the unrestricted exclusion of \(67\) and \(89\). The new joint reciprocal-moment certificate closes exactly that distinction. Exact-statement, equivalence, and stronger-coverage searches did not identify an already-published covering theorem. Residual risk: an older general criterion or unpublished computation might imply the same spectrum. This has not been independently audited.

## Mathematical value
**PASS.** The least fixed index beyond the previously tabulated first ten is a natural test of whether prime-field obstructions persist over all extensions. The unrestricted spectrum is a complete classification of a meaningful characteristic invariant, not a special parameter calculation or mere recomputation of Wendt factors. It eliminates three prima facie allowed characteristics that survive the principal known necessary obstruction, providing a reusable two-moment elimination template.

## Evidence and limits
The included `verify.py` performs fraction-free integer resultant evaluation, prime-factor verification, and all twenty-four finite joint-moment exclusions, as well as the characteristic-23 witness. The exact theorem concerns the *set of characteristics*, not the permutation behavior of every binomial in characteristic \(23\). The 2026-09-23 paper is the earlier relevant source; the subsequent 2026-10-13 publication was examined as a close coverage comparison. Literature searches cannot establish priority or uniqueness. The review is not independent.

Self-review: passed. Independent audit: not yet performed.
