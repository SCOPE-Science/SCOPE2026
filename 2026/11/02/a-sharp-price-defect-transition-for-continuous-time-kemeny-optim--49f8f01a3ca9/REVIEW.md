# Review: price-defect continuous-time Kemeny design

## Correctness (PASS)

The stationary flux relation gives \(\pi_i\propto1/r_i\); exact directed first-passage sums yield the symmetric reciprocal-rate identity (1). Pairwise averaging of any two equal-price rates lowers that identity strictly, by explicit positive derivative (2), with the budget unchanged. Repeated averaging makes the global reduction valid without symmetry assumptions. The scalar objective (3) has derivative sign (4), a strictly increasing quadratic, giving a unique positive optimum below \(n(n-1)/2\) and a strictly increasing objective above it. The high-price boundary is excluded by irreducibility, hence only an infimum is attained in the limit. Algebraic formulas and edge cases checked; 12,516 reproducible finite assertions passed. No finite experiment substitutes for the universal proof.

## Originality (PASS, qualified)

Catral et al. analyze the discrete-time Kemeny constant, perturbations and special cycle-support results. Kirkland treats graph-constrained discrete-time stochastic-matrix design, while Patel et al. optimize weighted Kemeny objectives within reversible chain formulations. An earlier directed-cycle shortcut claim already provides the general reciprocal-holding-time objective at zero shortcut, so the objective identity is not claimed as original. The present claim is an unrestricted positive-rate optimization of the continuous-time Kemeny objective on a nonreversible one-way cycle with one edge price defect; none of the examined primary statements gives the sharp \(n(n-1)/2\) transition or all-rate uniqueness and nonattainment. Searches of published mathematical statements and inspected literature found no covering claim. Absence of a located match is not proof of universal novelty; unindexed specialized literature remains a risk.

## Value (PASS)

The objective is the established stationary-target expected hitting time, useful for stochastic routing and surveillance. The finding solves a natural irreducible directed network rate-allocation problem under a measurable linear price budget, including all parameter regimes, the optimum and a sharp quadratic size-dependent phase boundary. It prevents a misleading 'buy ever less of the costly edge' heuristic from being mistaken for an attained optimum. The distinct rate/price budget structure is not merely a normalization of a known stochastic-matrix optimum.

## Relationship to literature and limitations

Closest primary full texts inspected: Catral–Kirkland–Neumann–Sze (2010), Kirkland's directed-graph fastest expected mixing manuscript, and Patel–Agharkar–Bullo's weighted Kemeny surveillance manuscript. The finding does not extend to arbitrary directed graphs, fixed stationary weights, or multiple exceptional prices. An unlocated equivalent theorem is possible, and no external validation has occurred.

Self-review: passed. Independent audit: not yet performed.
