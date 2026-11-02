# Self-review

## Correctness (C): PASS
The valuation description \(d_i=\nu_2(i+1)\bmod2\) follows from the substitution, and it forbids both `11` and `0000`. The prefix inheritance lemma is proved for arbitrary infinite binary words with a one in every length-\(L\) factor; a collision beyond \(L\) would induce a collision at \(L\). The residue-modulo-16 argument proves exhaustiveness of the length-ten windows in an actual 42-symbol prefix; the 16-image table proves injectivity. Every shorter factor extends to ten, so the nine initial counts and the sharp collision pair are exact. The independent arithmetic implementation agrees with the complete certificate. No claim rests on an unsupported finite-to-infinite extrapolation.

## Originality (O): PASS, subject to ordinary priority risk
The April 28, 2026 source develops tortoise complexity but treats paperfolding and Thue–Morse; its general theorem controls the bounded deficit without settling exact injectivity for period-doubling. The 2020 foundational paper defines tortoise sorting; OEIS A275202 gives the familiar unsorted factor counts. Checked period-doubling published research records concern attractors, symbolic lifts, or periodic complexity, not tortoise classes. Search comparisons include aliases, injectivity and equivalence classes, and stronger theorem implications, as detailed in `AUDIT.json`. The original source's paperfolding analogue is explicitly not claimed as new. Residual risk: an unindexed equivalent period-doubling calculation could have been missed.

## Value (V): PASS
The factor-tortoise function is a newly studied invariant connecting partial stack sorting with automatic-word complexity. A complete infinite-length classification for the canonical period-doubling fixed point is a natural test case, and the precise cutoff is not implied by the source's bounded-deficit theorem. The valuation residue certificate explains why an infinite equality is reducible to a finite 16-factor calculation and establishes a transferable prefix-inheritance principle. This is a small structural classification, not an assertion of a general solution across substitutions.

## Limits
The result concerns only the specified fixed point and one tortoise application. The finite checker is exhaustive only through the rigorously proved finite reduction; independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
