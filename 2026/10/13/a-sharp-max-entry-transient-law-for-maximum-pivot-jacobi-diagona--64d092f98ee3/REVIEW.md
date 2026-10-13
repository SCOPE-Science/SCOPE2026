# Self-review

## Correctness
PASS. A Jacobi rotation acts orthogonally on every two-entry vector
\[
(a_{pk},a_{qk})^{\mathsf T},
\]
so if every nonpivot entry is bounded by \(s\), each transformed component is bounded by
\[
\sqrt2\,s.
\]
Untouched entries stay at most \(s\), and the pivot becomes zero. This proves the universal upper bound.

The sharp family has a unique pivot of magnitude \(1\), two nonpivot entries of magnitude \(\tau\), and equal pivot diagonals. Its \(45^\circ\) Jacobi rotation combines the two entries into one of magnitude \(\sqrt2\,\tau\). The explicit scalar shift makes the matrix SPD with any prescribed condition number \(\kappa>1\) without changing the rotation. Only one off-diagonal pair survives, so the following rotation diagonalizes exactly. The packaged checker replays these identities at high precision.

## Originality
PASS with stated residual risks. The maximum-element Jacobi strategy, orthogonal pair update, aggregate off-diagonal energy decrease, and global convergence are classical.

The closest inspected sources establish Jacobi convergence, single-step eigenvalue perturbation theory, and the largest-element strategy, but no located statement gives the sharp second-largest-to-pivot threshold
\[
1/\sqrt2,
\]
the equality factor
\[
\sqrt2\,\tau,
\]
or the arbitrary-condition-number three-dimensional equality family. Targeted published-record and literature searches found no implication-equivalent result.

The main residual risk is older Jacobi literature using max-norm or elementwise language that was not exposed in the inspected sources.

## Value
PASS. Maximum-element Jacobi explicitly searches the largest off-diagonal entry to choose its next pivot, while standard theory monitors an aggregate off-diagonal norm. The theorem precisely quantifies the mismatch between those two diagnostics and proves that even excellent SPD conditioning does not prevent a one-step max-entry spike. The sharp minimal-dimensional family and next-step exact termination make the boundary transparent.

## Closest literature and limitations
Hari supplies archive-era global-convergence and MSC context. Matejaš is a particularly relevant single-step perturbation source, though full access was restricted through the inspected route. A modern open treatment confirms the largest-element strategy. The theorem is exact-arithmetic and one-step; full-sweep max-entry dynamics, block variants, pivot-search costs, and finite precision are outside scope.

Self-review: passed. Independent audit: not yet performed.
