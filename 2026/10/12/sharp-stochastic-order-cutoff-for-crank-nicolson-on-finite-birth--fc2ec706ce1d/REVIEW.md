# Self-review

## Correctness
PASS. The generator-level identity \(DQ=HD\) is obtained by direct subtraction of adjacent birth–death rows. The matrix \(D\) is onto, \(H\) is irreducible Metzler and diagonally symmetrizable, and all its eigenvalues are strictly negative because they are the nonzero generator eigenvalues. Rational functional calculus transfers Crank–Nicolson to the edge space. Strictly positive off-diagonal resolvent entries and strictly decreasing positive spectral combinations on the diagonal give one unique half-crossing per edge and the exact minimum cutoff. Direct inversion proves the stated general three-state formula. Exact rational examples and a four-state indexing test were independently replayed from the packaged checker.

## Originality
PASS, with explicit residual risks. The gradient/Feynman–Kac intertwining is strongly covered by Chafaï and Joulin, and the reversible-Markov Crank–Nicolson **transition-entry positivity** criterion in terms of the original generator resolvent is prior work. The new statement instead uses the resolvent of the killed **edge generator** to characterize *increasing-function order preservation*, gives the exact three-state rate frontier, and exhibits two opposite phase separations. Relevant published works on stochastic monotonicity, absolute monotonicity, and SSP Runge–Kutta methods were compared by mathematical implication, not title alone. No exact birth–death CN order-cutoff statement was located; an alternate formulation in the older dual-process or discretization literature remains a risk.

## Value
PASS. A numerical transition can be probability-positive yet destroy stochastic ordering, and an increasing-cone-preserving rational step can fail to be a legitimate Markov matrix. The theorem makes this distinction quantitative, yields an exact cutoff for every finite nearest-neighbor chain, and provides elementary three-state examples where each cutoff is strictly smaller than the other. These are meaningful order-sensitive numerical boundaries, not just checks of stochastic row sums.

## Closest literature and limitations
Chafaï–Joulin supplies the foundational gradient-semigroup intertwining; Dai Pra–Louis–Minelli supplies the stochastic-order framework; Higueras and Gottlieb–Grant–Higgs treat broader RK strong-stability questions. The result is limited to finite irreducible birth–death generators on totally ordered states, exact arithmetic, and the Crank–Nicolson end-step. It makes no independent-audit claim. Selected portions of the Higueras paper were inspected, so an uninspected theoretical section remains a comparison risk.

Self-review: passed. Independent audit: not yet performed.
