# Scientific review — phylogenetic rarefaction moment identifiability

## Correctness — PASS

Rooted phylogenetic diversity is the sum of inclusion indicators for exactly \(2n-2\) unit-length edges. Expanding its first two moments gives the stated histograms of descendant-clade sizes and pairwise descendant-union sizes. Triangular binomial inversion recovers every histogram entry, including the last pair count by its known total. The tree-generator recursion covers all non-plane rooted full binary shapes with no omissions, and exact signatures give zero duplicate excess through fifteen leaves and one pair among the 10,905 sixteen-leaf shapes. A separate exhaustive sample-subset implementation confirms identical means and variances at every depth for the witness, and detects the exact third-binomial-moment gap \(1/120\). Nonisomorphism and larger-size extension are proved directly. Limits: no claim for weighted trees, empirical finite-sample estimates, or collision uniqueness beyond sixteen leaves.

## Originality — PASS

Nipperess–Matsen (arXiv:1208.6552, full accessible text) already proves the general rarefaction mean/variance formulas. Schwob (arXiv:2606.12129v1, Section 5.1, full accessible text) and OEIS A382440 already contain binary-tree subtree-size-multiset comparisons: they cover the **mean-only** fingerprint and earlier nonidentifiability, not the joint second-moment inversion and sharp sixteen-leaf collision. The closest prior result is mathematically compared, rather than treated as novel under different wording. Searches of relevant mathematical records and accessible previous findings found no implication that establishes the sixteen-leaf result. Residual risks include unpublished, obscure, or differently named paired-clade overlap invariants, so external bibliographic checking remains worthwhile; a failed database search does not by itself establish novelty.

## Value — PASS

The problem is motivated by the ecological use of full PD rarefaction expectation and variance curves as compressed biodiversity measurements. The exact lower threshold identifies when these statistics cease to distinguish phylogenetic branching shape, while the single smallest witness shows why matching the first two moments need not determine the full law. Exact restoration by one third-binomial-moment measurement and constructive ambiguity at arbitrarily large sizes explain which extra information can matter. The numerical threshold is a complete classification of a natural inverse invariant, not an arbitrarily selected small example. The scope deliberately fixes unit edge lengths and cannot directly predict performance on noisy or molecular-clock trees.

## Closest literature and reproducibility

- Nipperess & Matsen, 2012, arXiv:1208.6552: exact PD rarefaction moments, no proved shape-identifiability cutoff in the inspected full work.
- Schwob, 2026, arXiv:2606.12129v1, Section 5.1: already-known subtree-size multisets, exchanges and their enumeration, no comparison of joint PD variances.
- OEIS A382440: previously known mean-only equivalence class counts, used as an external exact cross-check.
- See `verify.py` and `CERTIFICATE.json` for exhaustive unlabelled-tree enumeration and a separate full leaf-subset calculation.

Self-review: passed. Independent audit: not yet performed.
