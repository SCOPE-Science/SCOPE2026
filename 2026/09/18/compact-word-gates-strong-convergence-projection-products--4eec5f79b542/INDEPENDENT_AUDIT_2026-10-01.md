# Independent mathematical audit — 2026-10-01

## Final claim

If products of orthogonal projections converge weakly to the projection \(P\) onto the common intersection and a finite word recurs infinitely often with word product \(W\) satisfying \(W-P\) compact, then the products converge strongly to \(P\); in particular this gives finite-excess and genuinely multi-letter compact-gate criteria for countably infinite products.

## Correctness — PASS

PASS. On the orthogonal complement of the common intersection, the product vectors are weakly null and their norms are nonincreasing. At every endpoint of a recurring gate word, the endpoint vector equals \((W-P)\) applied to the corresponding pre-word vector. Those pre-word vectors are bounded and weakly null, so compactness sends that subsequence to norm zero. Monotonicity then forces the entire norm sequence to zero. The reduction by \(P\) and the two-letter block example in the frozen result were checked directly; no finite experiment is used as an infinite proof.

## Originality — PASS

PASS. The full 2026 Eskandari--Moslehian paper proves weak convergence for infinite-periodic countable products and gives a different strong-convergence corollary based on positivity of a subsequence. It does not state a compact recurrent-word, Calkin, or finite-excess gate criterion. Earlier finite-family random-product literature concerns different global geometric or convergence conditions. Targeted searches and the published-record repository search found no theorem with the audited quantifiers. The compactness argument is elementary, but it is not mechanically supplied by the inspected projection-product theorems.

### Equivalent formulations

The compact-word formulation cannot be obtained by merely renaming the positivity criterion.

### Broader coverage

Those results do not dominate the one-recurring-word hypothesis for a countable generating family.

### Exact database or table

The lack of a hit is only supporting evidence; the implication comparison with the full closest source is the main originality basis.

### Claim versus prior implication

Neither inspected prior conclusion implies the audited gate theorem without the new compactness step and recurrence alignment.

## Scientific value — PASS

PASS. The lemma upgrades a new countable-family weak-convergence theorem by a natural operator-ideal hypothesis and isolates exactly where compactness enters. A single recurring finite-dimensional-excess gate can certify strong convergence even when no individual reduced projection is compact, as the explicit two-letter example shows. That is a motivated structural criterion rather than a parameter slice.

## Sources inspected

- **Rasoul Eskandari and Mohammad Sal Moslehian, Convergence of Random Products of Projections Under Infinite-Periodic Selections** (arXiv:2609.13957): CLOSEST_SOURCE_NOT_COVERING. The general theorem is weak convergence; the paper's explicit strong criterion is positivity of a subsequence, not compactness of a recurring word or finite excess.
- **Eva Kopecká, When products of projections diverge** (doi:10.1112/jlms.12322): BROADER_FINITE_FAMILY_CONTEXT. It concerns fixed finite families and global convergence characterizations, not the countable-family recurring compact-word implication.

## Residual risks

- The compactness step uses standard functional analysis, so an older lemma with essentially the same formulation could exist under different terminology.
- No claim is made that the compact-word condition is necessary or gives a convergence rate.

## Disposition

**passed**
