# Self-review

## Correctness
PASS. The proof reduces the first two Heavy-Ball updates to exact scalar modal polynomials. In two dimensions, exact condition number forces the spectrum to the two endpoints, making the objective ratio a weighted average of two explicit modal ratios; the larger one is the \(L\)-mode and yields the exact frontier
\[
\kappa=9+4\sqrt5.
\]
In three dimensions, \(1/\alpha\) is strictly interior for every \(\kappa>1\). That mode makes the first-step polynomial vanish while the second remains \(-\beta\), and an interior perturbation yields an unbounded adjacent objective ratio. The packaged exact-rational checker replays the algebra and witnesses.

## Originality
PASS. The closest full-text paper on Heavy-Ball non-monotonicity already establishes peak effects and analyzes endpoint modes under standard initialization. It does not state the interior reset, the infinite supremum of \(f(x_2)/f(x_1)\) for every \(\kappa>1\), the minimal dimension-three classification at fixed exact condition number, or the sharp two-dimensional formula and \(9+4\sqrt5\) frontier.

Targeted searches for those formulations and exact constants found no implication-equivalent Heavy-Ball statement. Related published comparison results concern Nesterov acceleration, interval root geometry, or one-step Polyak-type steps rather than this recurrence and adjacent objective ratio.

Residual risk remains that the 2018 peak-effect recurrence makes the theorem a short unstated corollary, or that older second-order difference-equation literature contains the interior-zero mechanism under different terminology.

## Value
PASS. The result quantifies a practically relevant failure mode behind restart heuristics. It shows that no condition-number-only bound on the first local objective rebound exists once a third curvature is present, while also giving the exact protection that survives in two dimensions. The contrast is structural and sharp, not a numerical artifact.

## Closest literature and limitations
The closest literature is the 2014 Heavy-Ball convergence paper and the 2018 dedicated peak-effect paper. The theorem is limited to the first two completed updates, classical spectral-endpoint parameters, exact SPD quadratics, and zero-velocity initialization. The infinite ratio is relative to a vanishing first-step objective and does not imply global divergence or large amplification relative to the initial objective.

Self-review: passed. Independent audit: not yet performed.
