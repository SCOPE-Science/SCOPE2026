# Review

## Correctness
PASS. The claim is reconstructed from the published martingale formula, the null iid-uniform rank law, and an exact orbit-counting recurrence. The verifier compares the recurrence against brute force on every labeled path through a short horizon, then performs the horizon-\(128\) calculation with exact integers and rational arithmetic. It also exhaustively checks the martingale support gap needed for the minimal-support-threshold statement.

## Originality
PASS. The closest primary source, Henzi and Law, motivates finite-horizon calibration but estimates its Ville-gap thresholds by simulation, and its displayed \(N=128\) value is for a different Sinkhorn variant. Targeted searches using Dirichlet-multinomial, Bayes-factor, uniform-multinomial, boundary-crossing, and finite-horizon formulations found no exact version of the present claim. Residual risk remains that historical sequential multinomial literature may contain an equivalent dynamic program under different notation.

## Value
PASS. The source paper explicitly identifies finite-horizon correction as practically useful when the sample budget is bounded. The exact recurrence removes Monte Carlo calibration error for the canonical \(d=2\) fixed-grid test, yields a certified \(5\%\) threshold at a paper-relevant horizon, and provides a reusable finite-state calculation rather than an isolated numerical simulation.

## Closest literature and limitations
Henzi and Law, *A Rank-Based Sequential Test of Independence* (arXiv:2305.13818; Biometrika 111(4)), supplies the martingale and the finite-horizon motivation. Their Section 4.4 studies a Sinkhorn-corrected variant by simulation; that statistic is not the fixed-grid \(d=2\) process calibrated here. The result does not claim numerical transfer to other martingales, priors, grid depths, or horizons.

Same-model review: passed. Independent audit: not yet performed.
