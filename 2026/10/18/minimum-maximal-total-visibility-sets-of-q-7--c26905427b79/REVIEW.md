# Review of the seven-cube minimum-maximal total-visibility finding

**Correctness — PASS.** The proof reconstructs the known distance-two characterization, splits the seven-cube into two halfcubes, and establishes exact closed-neighborhood intersection sizes. Inclusion-exclusion forces the two distance-six pairs in each minimum halfcube configuration; a direct double count gives 1,120 per parity and 1,254,400 combined. A standalone verifier independently enumerates all independent four-sets and checks actual shortest paths for representative examples. The construction and all dimensions are explicit.

**Originality — PASS (best-knowledge, with residual priority risk).** Brešar–Yero (arXiv:2307.02951) explicitly ask for lower total-visibility numbers of hypercubes. Bujtás–Klavžar–Tian (arXiv:2307.05168) establish the underlying Hamming-graph equivalence, which is excluded from novelty. OEIS A355226 tabulates all independent sets of each cardinality but not their inclusion-maximal subset, and the 2026 *Visibility in Hypercubes* article bounds maximum rather than minimum-maximal visibility. Relevant indexed research summaries and published statements do not imply the four-word matching characterization or its 1,120 count. Equivalent unindexed classifications of small covering codes remain a genuine risk.

**Value — PASS.** The 2023 open problem naturally asks for this lower invariant. The result resolves an explicit finite dimension with a closed human-verifiable classification and exact multiplicity, and establishes a factor-two difference between smallest-maximal and maximum visibility sets. That gap measures the possible loss from greedily growing feasible sensor sets and identifies nonpurity of the associated complex.

**Scope and limits.** No claim is made about general dimensions, all maximal-set sizes, or novelty of the known distance-two criterion and coding-theoretic maximum bound. Independent validation is not claimed.

Self-review: passed. Independent audit: not yet performed.
