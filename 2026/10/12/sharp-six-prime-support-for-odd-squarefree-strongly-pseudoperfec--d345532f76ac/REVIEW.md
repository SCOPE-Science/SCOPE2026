# Scientific review: sharp odd squarefree prime-support threshold

## Correctness — PASS
Every odd squarefree integer with at most four primes is deficient by the exact \(768/385<2\) bound. For five primes, monotonicity of the abundancy product forces \(3,5,7\) as the first three primes and restricts the last two to 87 candidates. Every candidate has exactly 16 complementary divisor pairs; both exact subset-sum algorithms independently exclude its required deficiency \(\Delta\). The six-prime example has an explicit verified omission set. The computed part is an exhaustive finite certificate following a proof of the finite cutoff, not an inference from partial sampling.

## Originality — PASS, with residual risk
The closest 2026 primary article supplies the six-prime squarefree witness and broad new restrictions, but does not assert or prove its optimality in distinct prime support. The 2023 antecedent introduces the notion and congruence obstructions without this five-prime exclusion. An indexed low-support theorem handles only \(\Omega(N)\le3\), insufficient for five distinct prime factors. Searches for equivalent support thresholds, databases and broader published results found no stated covering result; indexed or unindexed equivalents remain a risk.

## Value — PASS
The exact minimum of distinct prime factors is a natural structural invariant of odd squarefree strongly pseudoperfect numbers. Showing the published six-prime witness is minimal answers the precise first-support threshold, converting an isolated example into a sharp classification barrier. The argument has a motivated finite combinatorial core of 87 cases, not an arbitrary range or a purely numerical discovery. It does not answer whether infinitely many primitive odd examples exist.

Self-review: passed. Independent audit: not yet performed.
