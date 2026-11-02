# Scientific review

**Correctness — PASS.** The three-star symmetric-difference lemma classifies all triangles directly from pairwise relative-order comparisons. The two types are disjoint and exhaust the graph; each is counted without overlap. The independently implemented literal-deletion verifier checks every vertex through length six and canonical vertices through length fourteen. The proof, not these experiments, establishes the universal quantifier.

**Originality — PASS, with residual uncertainty.** Wang et al. (arXiv:2406.16656, Section III, Lemma 4) give a general big-O triangle estimate for the same permutation deletion graph, rather than an exact formula or two-type classification. Kong (arXiv:1712.03639, Proposition III.2) gives radius-one sphere sizes but not neighbor-neighbor adjacency counts. Farnoud et al. (arXiv:1202.0932) give translocation and coding definitions and capacity results. Relevant mathematical-record searches did not surface the exact formula in the labeled-permutation model. A possible unindexed result about translocation Cayley graphs or three-way read intersections remains the priority risk.

**Value — PASS.** The triangle count is a natural local density invariant of the exact permutation-confusability graph already used to derive improved Gilbert–Varshamov-type bounds. Its exact cubic polynomial, the sharp constant, and the complete classification of failure of common-read Helly behavior supply information not obtainable from the published asymptotic triangle estimate or the sphere size alone.

**Scope and reproducibility.** Symbols are distinct and retained under deletion; this does not claim results for standardized permutation patterns, repeated symbols, larger deletion budgets or maximum independent sets. Run `python3 verify.py` for finite corroboration. Exact evidence, source comparisons and residual risk are recorded in AUDIT.json.

Self-review: passed. Independent audit: not yet performed.
