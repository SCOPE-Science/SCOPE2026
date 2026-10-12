# Self-review

## Correctness
PASS. Every active Schur complement of an SPD matrix stays between the original spectral endpoints:
\[
\mu I\preceq S\preceq LI.
\]
A current elimination multiplier is therefore an off-diagonal-to-diagonal ratio in a \(2\times2\) SPD principal block whose condition number is at most \(\kappa\). Direct optimization over the eigenbasis angle gives the exact block maximum
\[
\frac{q-1}{2\sqrt q},
\]
attained at
\[
\tan\theta=\frac1{\sqrt q}.
\]
Monotonicity in \(q\) yields the universal bound, and the explicit \(2\times2\) family attains it. Solving when the bound equals one gives
\[
\kappa_*=3+2\sqrt2.
\]
The rational condition-\(9\) matrix verifies a genuine forced row swap.

## Originality
PASS with stated residual risks. Classical theory already says that SPD Gaussian elimination needs no pivoting, that partial pivoting selects a maximal-magnitude entry in the active column, and that its multipliers are bounded by one.

The complete Broyden paper was inspected because it is the closest older condition-number/pivoting source. It explicitly defines the no-row-interchange class and derives factor-conditioning bounds, but no SPD spectral threshold or sharp multiplier formula was located. Full-text inspection of Higham's Gaussian-elimination overview and Higham–Higham's pivot-growth paper likewise found the classical premises but not the displayed frontier.

Targeted semantic, alias, exact-constant, and implication searches did not locate an equivalent theorem. The main residual risk is an older Kantorovich-inequality or Cholesky-multiplier formulation using different terminology.

## Value
PASS. The result resolves a natural distinction left open by the standard statement that pivoting is “not necessary” for SPD matrices. A generic GEPP code can still decide to swap rows on an SPD input; the theorem identifies exactly when a condition-number bound rules this out for every input and every stage. The same argument supplies a sharp dimension-free multiplier bound and a minimal two-dimensional obstruction.

## Closest literature and limitations
Broyden is the closest condition-number/pivoting source; Higham gives the modern standard statements about partial pivoting and SPD elimination; Higham–Higham supplies primary pivoting context and primary MSC \(65F05\). The theorem is exact-arithmetic, scale-sensitive through \(\kappa_2\), and specific to scalar partial pivoting. At the boundary a tie is possible, so the actual permutation depends on tie policy. Recognized SPD problems are normally better served by Cholesky factorization.

Self-review: passed. Independent audit: not yet performed.
