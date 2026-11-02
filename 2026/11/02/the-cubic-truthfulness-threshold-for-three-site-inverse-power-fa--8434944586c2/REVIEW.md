# Scientific review

## Correctness: PASS

The claim covers exactly three agents and two facilities on arbitrary metrics, with all nonnegative real powers and coincident-report conventions explicitly defined. The proof first rules out distant deviations, then exhausts the closest-pair and far-member cases. The key critical boundary case uses a nonnegative explicit bivariate polynomial, whose exact identity is checked independently by the packaged `verify.py`. The strict negative derivative on a three-agent line profile proves every exponent above three is manipulable. Repeated reports and nearest-neighbor ties are included. The script additionally checks 196,608 exact rational finite-metric incentive comparisons; finite checks do not establish the infinite theorem.

## Originality: PASS (qualified)

Chan, Lin and Wang (arXiv:2608.22484, first released 2026-08-23, Section 4 and Theorem 3) establish inverse-square strategyproofness for arbitrary agent counts, but do not state the inverse-cube positive result. Escoffier et al. (ADT 2011, Section 2) establish the inverse-first-power result. An earlier distinct power-law welfare analysis gives exact ratios for every exponent and the negative incentive counterexample for all powers above three, but explicitly leaves positive strategyproofness for powers above two unproved. Thus those stronger welfare results do **not** imply the new truthful cubic endpoint. The proof here completes a sharp three-agent incentive threshold, not a new all-exponent approximation formula. Searches for aliases, equivalent formulations and stronger coverage did not locate a dominating prior statement. The residual risk is unindexed or inaccessible equivalent work; a failed database search cannot establish global novelty.

## Mathematical value: PASS

Three agents with two facilities is the smallest nontrivial omission game. A sharp universal exponent threshold distinguishes effective incentive-compatible rules from locally manipulable rules in this natural mechanism family. At the newly proved strategyproof endpoint, the already-established welfare expression gives worst-case ratio approximately \(1.06527445\), improving upon approximately \(1.11237244\) for the published inverse-square mechanism. Establishing attainable truthfulness exactly at the critical exponent is a substantive all-metric theorem, not a finite-sample extension or routine substitution.

## Closest literature and limits

1. H. Chan, J. Lin, C. Wang, *Randomized Strategyproof Facility Location: Two Facilities and Beyond*, arXiv:2608.22484 (2026), Section 4, Theorem 3: inverse-square positive theorem for all population sizes. https://arxiv.org/abs/2608.22484
2. B. Escoffier, L. Gourvès, N. K. Thang, F. Pascual, O. Spanjaard, *Strategy-Proof Mechanisms for Facility Location Games with Many Facilities*, ADT 2011, Section 2: inverse-first-power positive theorem. https://doi.org/10.1007/978-3-642-24873-3_6
3. D. Fotakis and C. Tzamos, *Strategy-Proof Facility Location for Concave Cost Functions*, arXiv:1305.3333, for a distinct randomized selection mechanism (abstract inspected; entire full text not asserted to have been checked).

The positive result is limited to three agents. It does not imply arbitrary-population cubic strategyproofness, group-strategyproofness or optimality among unrelated mechanisms. The quoted power-family welfare ratio is previously established and is background, not an additional new claim.

Self-review: passed. Independent audit: not yet performed.
