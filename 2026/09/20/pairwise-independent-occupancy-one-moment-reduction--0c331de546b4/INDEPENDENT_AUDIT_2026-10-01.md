# Independent scientific audit — SCOPE-20260920-0c331de546b4

Audited at: 2026-10-01T20:13:40.771389Z

Disposition: **passed**

## Correctness — PASS

Averaging any feasible law over coordinate permutations and common label permutations preserves pairwise-uniform marginals and every occupancy-invariant objective. The group orbits are exactly occupancy types. For a fixed orbit, coordinate symmetry fixes the equality probability at \(c(\lambda)/\binom n2\), while label symmetry makes all diagonal ordered pairs equal and all off-diagonal ordered pairs equal. Therefore the symmetrized law is pairwise uniform exactly when the mixture's mean collision count is \(\binom n2/q\), proving both necessity and sufficiency of the single moment constraint. The feasible weights form a simplex cut by two equalities, so a linear extremum has support on at most two occupancy types. The collision-free endpoint mixtures have the required mean and give exactly the stated interval; the exact verifier checks every two-coordinate marginal for small \(q\).

### Correctness sources

- assigned RESULT.md
- assigned artifacts/verify_bounds.py
- Luby-Wigderson pairwise independence notes
- Ramachandra-Natarajan 2023

### Correctness risks

- The reduction is for objectives invariant under coordinate permutations and common alphabet relabeling; it does not classify nonsymmetric objectives or all nonsymmetric feasible laws.

## Originality — PASS

Universal-hashing sources use pairwise independence to fix expected collision count, and orthogonal-array sources encode the same strength-two marginals, but no inspected source states that after occupancy symmetrization this single moment is also sufficient for every pairwise marginal and hence solves every symmetric linear extremum. Ramachandra-Natarajan solve tight union/intersection bounds for genuinely pairwise-independent Bernoulli events; the collision indicators here are not pairwise independent in general, so their theorem does not cover the occupancy problem.

### Equivalent formulations

No equivalent finite-exchangeability, orthogonal-array, or hashing formulation was located.

### Broader coverage

These frameworks supply ingredients or neighboring extremal problems but not the audited one-moment sufficiency theorem.

### Exact database or table

The endpoint formulas arise from the structural reduction rather than from a known birthday-probability table.

### Claim versus prior implication

The final theorem is not mechanically implied by a union bound or a pairwise-Bernoulli extremal theorem; the orbit calculation is the essential new structural step.

### Sources inspected

- Tight Probability Bounds with Pairwise Independence — https://doi.org/10.1137/21M1408294. NOT_COVERING: Its hypotheses concern the event indicators themselves; collision indicators of overlapping coordinate pairs do not satisfy those hypotheses.
- Pairwise Independence and Derandomization — https://doi.org/10.1561/0400000009. COVERING_INGREDIENT: It motivates \(\mathbb E C=\binom n2/q\) but does not give the occupancy-orbit sufficiency or exact two-sided collision-free interval.

### Checked sources

- https://doi.org/10.1561/0400000009
- https://doi.org/10.1137/21M1408294
- https://arxiv.org/abs/2306.04583
- https://arxiv.org/abs/2405.08787
- https://doi.org/10.1002/wics.70029

### Residual risks

- An equivalent convex-geometric statement may exist in weighted orthogonal-array or finite-exchangeability literature under different terminology; targeted searches did not locate it.

## Value — PASS

The theorem collapses an entire family of symmetric high-dimensional limited-independence optimization problems to a one-dimensional moment polytope, gives two-orbit extremizers, and makes both sides of the pairwise-independent birthday problem exact. That is a reusable structural reduction rather than an isolated collision estimate.

### Value sources

- Luby-Wigderson
- Ramachandra-Natarajan 2023
- orthogonal-array literature

### Value risks

- The reduction does not extend automatically to nonuniform marginals or higher-wise independence.

## Limitations

- The objective must be invariant under coordinate permutations and common relabeling of the finite uniform alphabet.
- No characterization is claimed for nonsymmetric objectives, nonuniform marginals, or higher \(k\)-wise independence.
- The collision-free corollary is stated for \(2\le n\le q\).
