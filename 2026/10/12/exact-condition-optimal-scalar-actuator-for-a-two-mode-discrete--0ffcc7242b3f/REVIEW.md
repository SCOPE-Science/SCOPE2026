# Self-review

## Correctness
PASS. The infinite-horizon Gramian is obtained by two scalar geometric series and one mixed geometric series. For an interior actuator direction its determinant is positive exactly because the two stable eigenvalues are distinct. In dimension two, minimizing condition number is equivalent to minimizing trace squared divided by determinant. The resulting scalar rational function has one interior critical point and diverges at both endpoints, so that point is the unique global minimizer in squared actuator weight.

Substitution equalizes the modal diagonal Gramian energies and makes the optimal Gramian a scalar multiple of a two-by-two correlation matrix. Its eigenvalue ratio is therefore exactly
\[
\frac{1+\rho}{1-\rho}.
\]
The hyperbolic form follows from writing the stable eigenvalues as hyperbolic tangents. The embedded checker replays an exact example with optimum condition number \(9\).

## Originality
PASS with stated residual risks. Gramian-based actuator placement, use of Gramian condition number as a controllability-quality metric, and Hadamard formulas for diagonalizable systems are prior work.

The closest full paper was inspected through its discrete-time Hadamard construction and all three actuator-selection objectives. It treats determinant, trace inverse, and trace over a finite candidate set, and a full-text search found no condition-number optimization. Earlier network work uses condition number for scaling with network size rather than continuous actuator-direction design. Targeted exact-form and alias searches did not locate the squared-weight optimizer or the hyperbolic-separation formula.

The main residual risk is older modal-control literature using different terminology for the same two-state balancing calculation.

## Value
PASS. The condition number of the controllability Gramian compares the hardest and easiest control-energy directions. The theorem exactly solves the first nontrivial scalar-actuator orientation problem, shows that the condition-optimal direction generally differs from the determinant-optimal direction, and quantifies an unavoidable quadratic loss as the two modes coalesce. This is a motivated control-design boundary rather than an arbitrary two-by-two identity.

## Closest literature and limitations
The closest inspected literature supplies Gramian energy interpretations, condition-number motivation, and the diagonalizable discrete-time Hadamard formula. The result is restricted to an orthonormal two-mode diagonal system, one scalar input, and the infinite horizon. Nonnormal coordinates, multiple inputs, finite horizons, and dimensions above two remain outside the claim.

Self-review: passed. Independent audit: not yet performed.
