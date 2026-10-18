# Scientific review: exact four-step odd greedy threshold

## Correctness — PASS

For every odd denominator at least three the first selected reciprocal gives numerator one or three. In the numerator-three branch, the second selected reciprocal leaves numerator four whenever it fails to finish. The third leaves numerator five. The divisibility of the last fraction reduces, for all starting denominators, to an exhaustive calculation modulo 12 and modulo 5, including the exclusion of the nonsquare discriminant 2 modulo 5. The parity of sums of odd-denominator reciprocals forbids finite odd lengths. The least period follows from three explicit nonperiod witnesses. Exact direct computation for all 10,000 odd q from 3 through 20,001 reproduced the classification; the unrestricted proof does not rely on those samples.

## Originality — PASS relative to inspected sources

Louwsma and Martino (arXiv:2309.07280v1) classify length two with fixed numerator and all length-four fractions conditional on fixing their first three denominators. Their latter parameterization is broader as an *implicit recognition of an individual expansion*, but it does not calculate the modulus-60 global four-step decision, minimal modulus, or natural-density proportions over all odd starting denominators with numerator two. These are the subject of the present result, derived by eliminating the changing first three denominations and proving a quadratic nonresidue obstruction modulo five. Pihko's prescribed-numerator-sequence families and Brown's long-expansion construction do not compute these global counts. The indexed published-results search showed nearby Egyptian fraction problems but no equivalent residue-density claim. Unindexed equivalent work remains a risk.

## Value — PASS

The termination of odd greedy expansions remains open in general, so a complete and exact early-stopping classification for all odd starting denominators in a fixed natural family is a motivated finite-horizon invariant. The exact 4/5 density and sharp period 60 give substantially more information than examples of either short or long expansions. The contribution is a sharp, self-contained arithmetic statistic, not a general resolution of termination or a new generic parameterization.

## Limits and closest work

The computation does not decide whether fractions in six remaining residue classes ever terminate. Generic length-four parameterizations are related prior results, and an undiscovered direct version of the residue criterion is a residual risk. The proof is independent of numerical checks.

Self-review: passed. Independent audit: not yet performed.
