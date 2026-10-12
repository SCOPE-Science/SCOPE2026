# Review of Sharp finite-grid positivity threshold for Peaceman–Rachford heat stepping

## Correctness
PASS. The one-step operator factorizes exactly into one-dimensional Crank–Nicolson factors. The tridiagonal inverse formula makes all off-diagonal signs explicit, while the diagonal-ratio argument proves that endpoint diagonals are the only possible obstruction. Strict resolvent monotonicity gives a unique threshold. The limit follows from the exact scalar fixed point, not from numerical extrapolation. The exact \(2\times2\) witness is independently replayed by the bundled checker.

## Originality
PASS. The original Peaceman–Rachford paper and the Hundsdorfer–Verwer analysis establish stability/convergence, not the finite-grid entrywise positivity law. Nearby positivity literature treats other Padé or exponential-splitting maps. Focused statement-level searches found a one-dimensional backward-Euler-filtered Crank–Nicolson positivity result as the closest published database match, but that map and geometry are different. No inspected source implied the determinant threshold, the rectangular if-and-only-if conditions, or the limit \(4-2\sqrt2\). The remaining risk is older discrete-maximum-principle literature using different terminology; abstract-only access to two nearby papers is also recorded in the structured audit.

## Value
PASS. Peaceman–Rachford is classically unconditionally stable, so an exact positivity frontier answers a mathematically and numerically natural question that stability alone leaves open. The result supplies a complete finite-grid classification for the standard rectangular Dirichlet heat operator, an asymptotic constant, and a minimal exact counterexample illustrating the distinction.

Self-review: passed. Independent audit: not yet performed.
