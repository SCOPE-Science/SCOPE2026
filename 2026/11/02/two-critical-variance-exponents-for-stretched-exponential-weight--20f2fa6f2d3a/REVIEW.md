# Review of the variance phase diagram

## Correctness

**PASS (self-review).** The proof defines the weighted recursive tree and its filtration, derives the orthogonal-increment identity and conditional variance recurrence directly, and analyzes the latter in three distinct regimes. The kernel proof gives the critical \(\gamma=1/2\) coefficient, while beta-integral asymptotics give both polynomial regimes and the logarithmic \(\gamma=2/3\) boundary. The almost-sure limit uses martingale convergence and Kronecker's lemma with explicitly summable second moments. Exact enumeration of orders two through seven and five large finite recurrence calculations passed 32 executable assertions. The finite calculations are checks, not substitutes for the asymptotic proof.

## Originality

**PASS (provisional priority).** Gałązka--Wdowicka (arXiv:2610.00614v1) already established the general exact variance identities; those identities are explicitly credited. Their linear-scale theorem assumes \(p_j=O(j^{-1})\), while the present attachment fractions \(p_j=cj^{-\gamma}\) violate this for every fixed \(\gamma<1\). The derivation of the three variance-innovation asymptotics, the five explicit total-variance regimes, and the extended threshold \(\gamma>2/3\) were not found as statements in the inspected sources. Sénizergues (arXiv:1904.07115v3) concerns primarily polynomial cumulative weights and profiles. The closest claim-record matches involve root degree versus path length in other recursive-tree laws, not this variance diagram. An older or implicit derivation based on the general recurrence remains a residual historical-priority risk; absence from searches cannot certify uniqueness.

## Mathematical value

**PASS.** Global path-length fluctuations in heavily recent-biased recursive trees are naturally governed by the competition between forgetting of ancestral depth noise and accumulation of new depth noise. The two sharp thresholds separate the stationary-innovation, accumulating-innovation, and summable-martingale regimes; the logarithmic boundary is mathematically substantive rather than a finite-parameter curiosity. The result quantifies exactly when linear-scale \(L^2\) convergence survives beyond the standard attachment-weight hypothesis and provides the leading constants on both sides.

## Scope and risks

The claim is restricted to fixed \(0<c<1\), \(0<\gamma<1\). Neither a distributional limit below the second threshold nor parameter-uniform critical-window laws have been proved. The general-weight formula credited to the motivating paper is essential prior work, and independent mathematical and historical-priority review has not occurred.

Self-review: passed. Independent audit: not yet performed.
