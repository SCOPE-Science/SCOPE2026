# Scientific review

## Correctness — PASS

The proof fixes the commutator convention, partitions the deterministic permutation into fixed and moved points, and counts the ordered pair of images under a uniformly random permutation. Conditioning on an original-permutation fixed point gives an exhaustive five-branch conditional-probability classification; subtracting the two Bernoulli means yields the six disjoint covariance cases. Exact row sums then give \(fg/[(n-1)(n-2)]\). Pairwise independence for \(f=0\) follows from equality of Bernoulli conditional and unconditional success probabilities, and necessity follows by choosing a fixed index when \(0<f<n\). Aggregate dependence for a derangement follows from conditioning on the identity permutation and the nontriviality of the symmetric group's center for \(n\ge3\).

The standalone program compares exact rational covariances computed from all original permutations against the analytic formula for every deterministic partner through five points and five representative partners on six points, giving 3,773 cross-covariance and aggregate assertions. The finite checks are confirmatory and do not replace the proof.

## Originality — PASS, with a historical-priority risk

Diaconis–Evans–Graham (2013/2014), particularly Section 6, is the closest full-text commutator source. It develops marginal commutator fixed-point statistics and Poisson approximation, not the same-permutation cross-covariance law or all cross-indicator independence. Diaconis–Fulman–Guralnick (2007) treats fixed-point laws for actions of symmetric groups, not the paired commutator/original-permutation diagnostic. Related published fixed-point/descent and linear-succession covariance profiles have different event definitions; the latter do not cover arbitrary deterministic permutation partners or cyclic commutation agreements. Searches by fixed-point commutator covariance, derangement shielding, individual commutation agreements, and alternative formulations found no statement implying the theorem.

An earlier implicit representation-theoretic calculation is possible, so historical novelty must not be read as independently certified.

## Value — PASS

The random commutator fixed-point count is a natural measure of how a shuffled permutation fails to commute with a fixed test permutation, and fixed-point count is a standard permutation statistic. The theorem characterizes their complete cross-indicator dependence and shows the aggregate covariance depends only on the test permutation's fixed-point count, not its other cycles. Particularly striking is the exact independence of every cross-indicator pair for **all** derangement tests, despite dependence of the aggregate counts. This is a structural classification over every finite order, not an arbitrary numerical example or a repackaging of marginal Poisson approximation.

## Closest literature and limitations

Relevant full text: Diaconis–Evans–Graham, *Unseparated pairs and fixed points in random permutations* (arXiv:1308.5459, Sections 1, 5, 6). General fixed-point background: Diaconis–Fulman–Guralnick, *On fixed points of permutations* (arXiv:0708.2643). No full bivariate distribution or convergence-rate bound is asserted. A uniform marginal result cannot settle the same-permutation joint moments. Historical-priority risk remains from possible generalized mixed character identities.

Self-review: passed. Independent audit: not yet performed.
