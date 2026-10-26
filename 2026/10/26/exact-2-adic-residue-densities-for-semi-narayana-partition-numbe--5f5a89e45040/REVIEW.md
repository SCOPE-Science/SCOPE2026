# Scientific review: semi-Narayana \(2\)-adic residue densities

## Correctness — PASS
The defining digit-restricted binary-partition product gives \(c(2n)=c(n)\) and \(c(2n+1)=c(n)+c(n-1)\). The corresponding two integer matrices have determinant \(-1\). Direct exact arithmetic establishes the mod-two orbit, the two base lifting identities, and the fourteen explicit conjugation witnesses; an algebraic squaring induction supplies all higher lifting depths. The primitive orbit is complete at every modulus, and the resulting finite Markov chain is irreducible, aperiodic, and doubly stochastic. A binary-prefix cylinder decomposition extends mixing from complete dyadic levels to natural density at arbitrary cutoffs. The one-coordinate marginal and valuation formulas follow from exact counts of primitive triples. The included Python verifier replays the finite witnesses and diagnostics; finite enumeration by itself is not invoked as an infinite proof.

## Originality — PASS (within checked evidence)
Ballantine–Beck (arXiv:2303.11493v1, §7) establishes the semi-Narayana partition representation and mod-two parity classification, but not the complete prime-power joint-residue law. Anders (2016) derives summed growth of nonstandard binary representations rather than congruence-distribution theorems for these triples. The OEIS A120562 sequence entry and the 2023 Sobolewski article concern respectively basic identities and a different partition product. Relevant mathematical-record comparisons and equivalent-formulation searches did not identify prior coverage. Residual risk: general automatic-sequence ergodic results or unindexed work may contain an implicit or equivalent proof; absence from indexed searches is not proof of publication priority.

## Mathematical value — PASS
The existing parity theorem predicts an even-coordinate density of \(3/7\) but leaves local distribution at higher prime powers undetermined. Exact equidistribution over primitive consecutive triples resolves all such local congruence frequencies at once, reveals a nonuniform single-coefficient measure, and gives every finite \(2\)-adic valuation probability. This is a natural structural classification of a named restricted binary-partition sequence, not an arbitrary finite lookup.

## Boundary
No claim about other primes, quantitative mixing uniform in modulus, independent validation, or priority certification. The infinite conclusion requires the matrix-conjugation lifting argument and the ergodic limit; small computational samples alone are insufficient.

Self-review: passed. Independent audit: not yet performed.
