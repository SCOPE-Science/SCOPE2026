# Same-model review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.** The explicit path and cycle constructions were checked directly against the graph-CFF definition. The finite nonexistence searches enumerate all admissible block sequences after complete ground-set-symmetry reductions: the graph-CFF singleton conditions force a global antichain, every completed edge permanently forbids all third blocks contained in its endpoint union, and each newly formed edge is checked against all previously chosen blocks. The wheel search additionally fixes the center by cardinality and the first rim block by cardinality and intersection cardinality under the center stabilizer. Positive-control searches reproduce previously known feasible boundary cases. The deductions from P_11 to larger paths/cycles use graph-subgraph monotonicity, and W_12 uses the published universal-vertex corollary.

## Originality

**PASS, to the best of our knowledge.** The May 2026 Parida--Moura preprint is the directly relevant primary source. It gives exact small values only up to P_10, C_9, and W_10, displays the later n<=12 entries as upper bounds unless separately proved exact, and asks whether the P_10 subset-elimination idea can improve the general path/cycle construction. Searches using the source identifier, exact parameter notation, path/cycle/wheel graph-CFF terminology, and neighboring structured group-testing terminology did not locate a later source establishing the values in this record. The June 2026 hypergraph-CFF paper is neighboring background and did not provide the path/cycle/wheel equalities found here. Residual risk remains from differently named structured group-testing, superimposed-code, or hypergraph-CFF formulations that may not be well indexed.

The originality claim excludes standard Sperner bounds, graph-subgraph monotonicity, the universal-vertex lemma, and all small exact values already proved in the source paper.

## Value

**PASS.** The result completes all previously unresolved path/cycle/wheel entries in the source paper's small-value table through n=12 and extends exact path and cycle values through n=15. For n=13,14,15 it improves the source paper's general upper bound from 8 to the exact value 7, providing concrete benchmarks for subsequent constructions and classifications.

## Verification and access limitations

The primary preprint was inspected at theorem/table/open-problem level. The computational certificate is standalone and deterministic. The negative finite cases are computational proofs rather than independent formal proofs, and no independent validation is asserted. Literature coverage is necessarily incomplete and originality is qualified accordingly.
