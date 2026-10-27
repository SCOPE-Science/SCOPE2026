# Scientific review

## Correctness — PASS

For a fixed primitive-root component, Theorem 4.13 of Clader–Damiolini–Li–Ramadas gives the additive Chow decomposition with ordered jumps of size at least two. Its exponential generating series is computed explicitly, yielding a three-term differential recurrence. At a zero of the degree-\(n\) polynomial, the derivative and interlacing degree-\(n-1\) polynomial have identical signs. Because \(r-2\ge0\), the recurrence forces alternating evaluations and one simple negative zero in every interlacing gap, including the two exterior gaps. All quantifiers \(r\ge2\), \(n\ge0\) and base cases are covered. The standalone checker independently matches the published additive formula and recurrence in 54 exact small cases; finite checks are auxiliary to the general proof.

## Originality — PASS, with documented residual risk

The primary 2023 paper (revised v3, Section 4.4) explicitly labels all-parameter log-concavity Conjecture 4.15, whereas its Theorem 4.13 and tables give ranks without asserting real-rootedness. Its recognized \(r=2\) type-B case is subsumed but does not imply the result for \(r\ge3\). The original 2021 paper concerns boundary geometry. Semantic-result searches for negative roots, cyclic moduli Betti polynomials, the conjecture, and generalized Eulerian recurrences did not identify an equivalent or stronger coverage statement; the closest similarly named real-rootedness result concerns the different space \(\overline{\mathcal M}_{1,n}\). Generalized Eulerian literature presents overlapping formal generating-function techniques; the possibility of an implicit stronger theorem or unindexed subsequent proof is a residual risk.

## Value — PASS

This resolves a precisely stated open algebraic-geometric Betti-number conjecture for every cyclic order and dimension, while proving the stronger stable interlacing property. The proof explains *why* the uniform log-concavity holds by an explicit recurrence and a sign invariant, rather than by a finite enumeration or a reinterpretation of the existing low-dimensional tables. The new root-location property also yields ultra-log-concavity by Newton inequalities.

Self-review: passed. Independent audit: not yet performed.
