# Scientific review

## Correctness — PASS

The theorem quantifies over every finite rooted tournament of orders one to eight. The canonical-augmentation proof covers all rooted isomorphism types, and canonicalization is justified by the invariance of outdegrees under isomorphism. Directed refinement is implemented exactly: in-counts are determined from colour-cell sizes and out-counts for tournaments. Backtracking enumerates all and only root-preserving automorphisms, and the rooted orbit comparison is exact. The first program finds zero failures through order seven and two rooted types at eight. The independently implemented all-labelled search tests all 2,097,152 seven-vertex orientations with root fixed, also finding zero; a third implementation verifies the exceptional automorphism groups and stable partitions. Complete programs, expected output, and their limits are included.

## Originality — PASS (priority not independently certified)

The directly inspected 2015 colour-refinement paper develops general refinability and its graph-class hierarchy but gives neither the directed-tournament sharp eight-vertex theorem nor this rooted classification. The inspected 2016 vertex-individualization paper develops complexity results without an equivalent finite directed-tournament table. McKay's tournament catalogue supplies isomorphism-type counts, not the rooted refinement/orbit invariant. Comparisons with published mathematical records and earlier classifications of different structures did not disclose an implication covering the present result. See structured searches, inspections, and residual risks in AUDIT.json. This is a best-knowledge novelty judgment, not a universal priority proof.

## Value — PASS

One-point individualization is a standard strengthening of colour refinement for symmetry detection. This classification determines its exact first failure within all finite directed tournaments and classifies every rooted counterexample at the sharp boundary. The appearance of just the source/sink additions of one asymmetric regular tournament identifies the structural mechanism, while the exhaustive completeness argument rules out unrelated eight-vertex mechanisms. The result is a motivated finite theorem, not only a single example or a known tournament-count reprint. Its scope is deliberately finite; no higher-order theorem is implied.

## Limits and closest literature

The first background source is Arvind et al. (2015, arXiv:1502.01255); individualization is treated by Arvind et al. (2016, arXiv:1606.04383). McKay's exact tournament counts independently corroborate the isomorphism-class enumeration but do not compute this property. Specialized earlier tournament refinability literature may not have been indexed or accessible. All verification is reproducible from the included files; it remains a self-review rather than an independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
