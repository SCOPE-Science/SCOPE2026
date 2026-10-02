# Independent mathematical audit — 2026-10-01

## Final claim
For every connected complete multipartite graph, outer multiset resolving sets are exactly those omitting at most one vertex from each part and only from parts of pairwise distinct sizes; the dimension and basis count follow exactly.

## Correctness — PASS
For a vertex omitted from part i, its distance multiset to the selected set contains exactly s_i entries equal to two, where s_i is the number selected from that part. Thus two omitted vertices collide exactly when they lie in the same part or in two equally sized parts after the at-most-one-omission condition is enforced. This proves the complete characterization, the dimension formula, and the basis count. Fresh brute-force checks on mixed repeated part sizes reproduced the formula.

## Originality — PASS
Best-of-knowledge originality passes for the mixed repeated-part classification and enumeration.

### Equivalent formulations
Searches: outer multiset dimension complete multipartite mixed part sizes resolving sets; complete multipartite outer multiset basis repeated sizes
Evidence: The 2023 primary source states the balanced case and the pairwise-distinct-size case, but not the mixed repeated-size classification. A later 2026-09-19 record gives an equivalent partition-matroid formulation and is subsequent to this 2026-09-18 record.
Reasoning: The formula can be phrased as order minus the number of distinct part sizes, while the structural statement says the omitted vertices form an independent set of a partition matroid indexed by equal-sized parts.

### Broader coverage
Searches: Further contributions on the outer multiset dimension of graphs; 2019 foundational outer multiset dimension paper
Evidence: The inspected literature covers equal part sizes and strictly increasing part sizes as endpoint regimes.
Reasoning: Neither endpoint theorem mechanically determines what happens when some, but not all, part sizes repeat.

### Exact database or table
Searches: Resultary semantic search for arbitrary complete multipartite outer multiset dimension
Evidence: The only exact-topic earlier-or-same record located was the assigned result; the equivalent 2026-09-19 record is later.
Reasoning: No prior exact mixed-size table or theorem was found.

### Claim versus prior implication
Searches: 2023 complete multipartite consequences
Evidence: Equal-size parts force all but one vertex selected in the whole graph, whereas pairwise-distinct parts allow one omission per part; the mixed collision rule across equal-size classes is an additional implication not supplied by either endpoint statement.
Reasoning: The final all-set characterization and exact basis count require the mixed collision analysis.

### Source inspections
- **Further Contributions on the Outer Multiset Dimension of Graphs** (arXiv:2207.06834): Closest prior endpoint results; no mixed repeated-size classification located. Material read: Full-text passage stating the balanced complete multipartite value and the pairwise-distinct part-size value. Evidence: The source gives the balanced value and separately the strictly increasing part-size formula.

Checked sources: arXiv:2207.06834; Applied Mathematics and Computation 363 (2019), 124612; Resultary published-record search
Residual risks: A poorly indexed older note could contain the mixed formula under different terminology.

## Scientific value — PASS
The theorem closes the natural missing mixed-multiplicity regime between two published endpoint cases and gives a full resolving-set classification and exact basis enumeration, not merely another isolated dimension value.

## Conclusion
The unchanged scientific claim passes correctness, best-of-knowledge originality, and scientific-value review.
