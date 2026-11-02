# Review of the labeled-two-cycle inversion profile

## Correctness
PASS. For a fixed two-cycle the remaining labels form a uniform permutation of size \(n-2\). Separating inversion pairs into the fixed pair, two free positions, and mixed pairs yields the exact formula without asymptotic assumptions. Factoring and taking limits establishes the sign diagram; a polynomial summation establishes the aggregate check. The embedded verifier independently exhausts conditional completions through size eight and uses separate pairwise expectations. Finite tests are supplemental, not the proof of the general identity.

## Originality
PASS on the searched evidence, with acknowledged historical-priority risk. Hultman (arXiv:1301.0430v1, Lemma 6.1 and Theorem 6.2) gives conjugacy-class averaged inversion probabilities and expected inversion counts. The present question instead fixes the *specific labels* in one two-cycle. Hultman's class average is not sufficient to recover a label-by-label conditional profile. In particular, the known aggregate covariance is explicitly treated as prior work, not new. Pinsky (arXiv:2505.02058) conditions on fixed-point counts, a different event. Maples–Nikeghbali–Zeindler (arXiv:1203.4132) studies probabilistic cycle counts and contains no such inversion profile in the inspected introduction and main theorems. Research-record summaries for cycle-count/inversion covariances and inversion-indicator precision also have different joint observables. Unexamined historical work on labeled partial cycles remains a residual risk.

## Mathematical value
PASS. A labeled two-cycle is the simplest nontrivial specified cycle event, and inversion number is a basic measure of permutation disorder. Class-averaged methods collapse all two-cycle labels together; the exact local law reveals large, opposite-signed effects depending on *which* labels are paired. The universal midpoint sign diagram and half-positive-pair limit show a genuine structural dependence that cannot be seen from the known small aggregate covariance. This is not presented as a new formula for unconditional inversion means or for the total two-cycle covariance.

## Limits and closest literature
The exact theorem is restricted to uniform permutations and one selected two-cycle. No claim of complete historical priority is made. The most relevant already known result is Hultman's class-mean theorem, which covers the aggregate identity but not the local conditional claim. The verified first public source used to locate the probabilistic cycle-statistics direction is Maples et al., 2012-03-19 (primary MSC 60C05). Pinsky's later fixed-point results are compared as supporting literature but are not used to move the source-date boundary.

Self-review: passed. Independent audit: not yet performed.
