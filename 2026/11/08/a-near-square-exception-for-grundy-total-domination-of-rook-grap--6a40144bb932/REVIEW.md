# Self-review

## Correctness — PASS
The proof is reconstructed using the open-neighborhood definition: an undominated rook-graph vertex corresponds either to an edge between untouched bipartite endpoints or to an isolated selected edge. An old-endpoint-only legal move must join components, so all selected-edge prefixes are forests. At first one-sided coverage, \(t=s-c\) and at most \(q\) further isolated-edge eliminations are possible. The exceptional equality case forces a matching that touches exactly \(m=n-1\) row/column vertices. Both explicit lower-bound constructions were checked, including the smallest board. Independent exhaustive programs verify finite examples with different dynamic-programming state spaces. No finite observation substitutes for the proof.

## Originality — PASS (qualified)
The January 2016 foundational full text treats general total dominating sequences but not rook-graph exact evaluation. The later 2017 graph-products text gives Cartesian path/cycle bounds, not complete-factor products. The 2022 line-graph formula applies to positive-semidefinite forcing rather than the skew/open-neighborhood invariant; it cannot imply the exceptional \(n=m+1\) value. The known ordinary zero-forcing calculation for rectangular rook graphs is also a different rule. Searches for the stated graph family and for alternative skew-forcing formulations did not reveal an exact prior theorem; this is evidence of a specific gap, not proof of global novelty. Unindexed mathematical tables remain a historical risk.

## Value — PASS
The all-order theorem computes a natural open-neighborhood greedy invariant for a canonical two-parameter graph family. It reveals a sharp square-to-near-square jump and a one-unit exception to the line-graph forcing expression, explained by a forest/isolated-component charging argument. The value lies in exact structure and the exceptional boundary, not in improved numerical bounds alone.

## Source and verification limitations
The available primary full-text inspections cover definitions, relevant theorem statements, graph-product sections, and the positive-semidefinite forcing comparison. They do not certify historical priority against every unindexed work. The supplied scripts are reproducibility checks; no external or independent audit has occurred.

Self-review: passed. Independent audit: not yet performed.
