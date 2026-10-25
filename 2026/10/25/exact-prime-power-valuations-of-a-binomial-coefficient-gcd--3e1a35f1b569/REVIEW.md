# Review of exact binomial-gcd valuations

## Correctness

**PASS.** Kummer's carry criterion gives a lower bound \(a-c\) from disjoint low and high carry positions for every admissible multiplier. The multiplier \(q=1+p^at\), with \(t\) chosen using Lucas's theorem, attains that bound. The pure-prime-power case is checked separately. The two known lemmas from Guo et al. rule out extraneous prime factors and supply zero valuations. Complete finite testing corroborated 139 exact-gcd cases and 4453 valuation cases.

## Originality

**PASS, with residual literature risk.** The 2003 OEIS entry specifies the gcd-one index set; Guo et al. establish the gcd-one characterization and a prime-divisibility criterion but do not give exact positive valuations. Searches for fixed-index multiplier binomial gcds, p-adic exponents, and equivalent formulas produced no matching exact valuation theorem. An equivalent result could exist outside inspected sources.

## Mathematical value

**PASS.** The 2003 problem and subsequent criterion address when the natural gcd vanishes to \(1\). The refinement determines the *complete exact arithmetic invariant* for every index, with constructive coefficient witnesses, and unexpectedly forces the gcd to have at most one prime factor. The exponent information distinguishes indices that the previously published criterion treats alike.

## Scope and limitations

The universal proof uses two published lemmas of Guo et al.; new steps include the nonzero exact valuations and their sharpness. Finite verification is supportive rather than exhaustive, and independent validation remains outstanding.

Self-review: passed. Independent audit: not yet performed.
