# Self-review

## Correctness — PASS
The finite random-graph component construction gives the exact factorial-cumulant factor, with the diagonal factorial correction explicitly retained. A positive Laplace representation converts the logarithmic threshold to a product of normalized geometric sums. Their logarithms are strictly convex in component size, yielding the claimed strict fixed-sum ordering for every integer parameter. Global endpoints follow from strict increase of the telescoping log kernel. The accompanying exact checker tests every graph state through six vertices; it is not used to assert infinite correctness.

## Originality — PASS on inspected material, historical priority remains uncertain
Sun (arXiv:2608.04799), Proposition 3.2, already proves the general exact factorial moments; this is acknowledged rather than claimed as a discovery. The additional strict Schur-convex *threshold ordering* and coexistence of opposite covariances do not appear in the inspected statements. De Ambroggio and Roberts (arXiv:2101.05358) establish near-critical largest-component tail estimates. Andreis, König and Patterson (arXiv:1901.01876) study asymptotic large deviations of the cluster-size spectrum. A previously published isolate-versus-component result covers an extremal boundary subfamily but not the all-pair balance inequality. Residual risk: equivalent results may exist in classical convex-order or falling-factorial inequality literature.

## Value — PASS
At fixed total component mass, the theorem completely orders the edges of the sign-transition diagram and explains why different pairs of ordinary component counts can have opposite covariance signs at the same probability. This is a natural structural question about the cluster-size point process, with exact finite-order classifications, rather than a restatement of the known moment formula.

## Limitations
The original contribution is the ordering, not the factorial-moment enumeration. The diagonal concerns factorial cumulants; inhomogeneous graphs and fixed-edge models are not covered. No outside validation or proof of historical priority is claimed.

Self-review: passed. Independent audit: not yet performed.
