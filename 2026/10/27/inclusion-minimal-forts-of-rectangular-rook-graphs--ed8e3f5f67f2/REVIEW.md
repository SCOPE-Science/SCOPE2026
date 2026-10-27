# Scientific review: inclusion-minimal forts of rectangular rook graphs

## Correctness — PASS

For an unselected cell, its count of selected neighbors equals its row degree plus its column degree, which gives an if-and-only-if fort condition. The exhaustive proof splits according to empty rows and columns: an edge-cover case, two asymmetric degree-two forest cases, and a cycle case. The minimal-edge-cover argument forces the star-forest structure and its degree boundary; Cayley's labeled-tree generating function and alternating-cycle counts enumerate the four disjoint types. The separately implemented finite verifier agrees with all subsets of boards up to sixteen cells and with the minimal-fort sets for a twenty-cell board. The written argument, not the finite computation, supplies the universal quantifiers.

## Originality — PASS, with identifiable residual risks

The most directly related theorem of Fetchie, Jacob and Saavedra (2015), restated by Abara and Pelayo (2022, Theorem 3.7), already implies the size of smallest rook-graph forts whenever one factor has order at least four; this scalar fact is **not** asserted as new. Becker et al. (2024) count minimal forts in other families and study operations, while Cameron et al. (2023) and Brimkov et al. (2025) study forts under Cartesian products and explicit constructions. Their inspected material does not state the complete four-family characterization or its coefficientwise generating function for rectangular rook graphs. Search and semantic comparisons of published records found no implication covering those two claims; missing unindexed literature remains a genuine risk.

## Value — PASS

Minimal forts are inclusion-minimal certificates that obstruct ordinary zero forcing, and their full hypergraph is finer than the previously calculated largest failed zero-forcing cardinality. The four incidence-graph mechanisms distinguish covered star forests, acyclic row/column subdivisions, and genuine alternating cycles. The resulting exact polynomial counts each minimum and nonminimum obstruction for every rectangular board, including boundary cases. This full description can support exact obstruction-transversal and zero-forcing investigations without claiming to have solved the zero-forcing polynomial itself.

## Limits and nearest literature

The theorem covers finite, simple rook graphs with both side orders at least two. A computed finite set of checks does not prove infinite assertions, and full published bibliographic priority has not been independently certified. The 2015/2022 failed-zero-forcing extremum subsumes the four-vertex minimum-fort consequence; it does not subsume the new full classification and counting expression. See the accompanying RESULT.md for definitions, proof, coefficients, and original literature citations.

Self-review: passed. Independent audit: not yet performed.
