# Self-review

## Correctness
PASS. For orders at most three, every genuinely incomplete natural-order case reduces to one dropped fill before the final pivot; the resulting IC(0) final pivot is a \(2\times2\) principal-minor Schur quantity and is positive for every SPD matrix. For the signed four-cycle, the signed adjacency satisfies
\[
B^2=2I,
\]
so the SPD interval is exact. The IC(0) recurrence gives
\[
q_4=
\frac{(1-t^2)(1-3t^2)}
{1-2t^2},
\]
and the first three pivots stay positive throughout the SPD interval. This proves the sharp boundary
\[
t=\frac1{\sqrt3}.
\]
The condition-number identity is algebraic, and the packaged checker replays the rational special cases exactly.

## Originality
PASS. The fixed \(4\times4\) Kershaw breakdown matrix is prior work and is not claimed as new. Eijkhout's full 1999 survey explicitly reproduces it and states that its fourth ILU(0) pivot is negative.

The new claim is narrower and different: every SPD matrix of order at most three is IC(0)-safe; the Kershaw witness lies in a canonical signed-cycle family with a complete exact phase diagram; and within that family breakdown starts at
\[
t=\frac1{\sqrt3},
\qquad
\kappa_2=5+2\sqrt6.
\]
Targeted database and literature searches found no implication-equivalent statement of those three additions.

Residual risk remains because the complete body of Kershaw's 1978 journal article was not accessible through the inspected route, and older incomplete-factorization literature may encode the same family calculation under different notation.

## Value
PASS. Nonpositive incomplete-Cholesky pivots remain a practical robustness problem, motivating shifts, pivot repair, and alternative preconditioners. The result turns a classical isolated counterexample into a sharp local robustness law and establishes the first possible dimension for exact-arithmetic failure. The condition-number threshold is not presented as a global bound, only as the exact onset in the historical Jacobi-scaled signed-cycle family.

## Closest literature and limitations
The closest source is Eijkhout's full survey, which attributes the fixed \(4\times4\) negative-pivot example to Kershaw. Modern robust-IC work gives larger SPD breakdown examples and practical safeguards. The theorem is restricted to unshifted IC(0), natural ordering, and exact arithmetic; the sharp condition-number constant is family-specific.

Self-review: passed. Independent audit: not yet performed.
