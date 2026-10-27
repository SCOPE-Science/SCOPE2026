# Self-review

## Correctness

PASS. The source's capped proximal step is reconstructed for the specified loss and regularizer. The resulting map has two explicit affine branches and an invariant interval. Its global Lipschitz constant is strictly below one exactly below the stated threshold; at equality the invariant reflection interval supplies nonconvergent orbits. Above threshold exact algebra locates one point on each branch and confirms the two-step map and its local derivative. The neutral case is classified only at the linear level. Independent exact-fraction checks corroborate sample formulas.

## Originality

PASS (best-knowledge, residual risk retained). The 2023 source gives sufficient generic stepsize bounds, not a sharp necessary-and-sufficient interval-wide convergence frontier, a continuum of critical cycles, or the particular locally attracting nonoptimal cycle. The broader earlier model-based proximal work does not give these conclusions for the capped update. Search comparisons with related algorithmic cycles concern distinct update laws and so do not imply the result; unindexed equivalent scalar results remain possible.

## Value

PASS. The phase transition is a qualitative limitation of a motivated algorithmic safeguard: a regularizer creates a discontinuous-onset limit cycle absent in the unregularized scalar model. The exact threshold separates globally convergent caps from explicit counterexamples, and the return multiplier resolves whether the nonoptimal orbit attracts nearby initializations. It is not merely an isolated experimental counterexample.

## Sources and limitations

Primary: Schaipp, Gower, Ulbrich, arXiv:2301.04935, Algorithm 3 and convergence analysis. Baseline: Asi and Duchi, arXiv:1810.05633. Later comparison: arXiv:2602.09842. Strongly related periodicity results for other algorithms were compared at the implication level, not assumed equivalent. Only the deterministic scalar family and initial interval stated in the theorem are established; other regularizers, data noise, nonlinear behavior at neutral stability, and all-orbit postcritical dynamics are outside scope. Independent verification remains pending.

Self-review: passed. Independent audit: not yet performed.
