# Self-review of the two-agent Boolean allocation theorem

## Correctness — PASS

The proof reconstructs the utility-vector Pareto frontier from the two possible utility levels. The disagreement construction separately handles both orientations of a differing subset, and the identical-function argument distinguishes zero valuations, complementary valued pairs, and the remaining obstructions. Exhaustive checks from `check.py` recompute envy and Pareto efficiency directly over all pairs of valuations for one, two, and three items (65,808 profiles), including all normalization strata. The exhaustive test is not relied on for unbounded item count.

## Originality — PASS, with publication-priority qualifications

The closest original manuscript, Shah and Verma, arXiv:2608.29497, already proves EF and PO existence for exactly one agent with zero empty-bundle value, and contains a negative construction for PO with EF1 under a different normalization hypothesis. Neither gives the complete pointwise two-agent exact EF+PO iff nor its independent-truth-table enumeration. Bérczi et al., arXiv:2006.04428v1, prove Boolean EF1/EFX relaxations, which do not imply exact EF. Precise claim comparisons, complementary-support equivalences, and published-result searches did not locate the full statement. A short obstruction lemma could nevertheless occur in unindexed fair-division work; this remains a genuine priority risk, not a proven claim of uniqueness.

## Value — PASS

The theorem converts a coarse normalization-based existence picture into a complete two-agent structural dichotomy, distinguishes nonexistence of EF from incompatibility of EF with efficiency, and computes exact probabilities and normalization-stratum obstruction counts. Its parameter regime is the full finite Boolean preference domain, not a selectively chosen family of configurations. The artificial uniform truth-table model and the two-agent restriction limit empirical and higher-population claims.

Self-review: passed. Independent audit: not yet performed.
