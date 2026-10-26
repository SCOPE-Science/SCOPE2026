# Scientific assessment: minimal forts of triangular graphs

## Correctness — PASS

For a selected edge set \(F\) in \(K_n\), an unselected edge \(uv\) has exactly \(d_F(u)+d_F(v)\) selected neighbors in the triangular graph. The defining fort condition is therefore equivalent to the absence of a simultaneous isolated vertex and degree-one vertex in the spanning graph \(([n],F)\). In the nonspanning case, any fort contains a cycle and minimality forces exactly one nonspanning cycle. In the spanning case, minimality forces a minimal edge cover, equivalently a spanning star forest without isolates; the converse uses the degree-one obstruction for every proper nonspanning edge subset. The labeled exponential formula counts components correctly, giving one choice for a two-vertex star and \(m\) choices of center for component order \(m\ge3\). Direct independent adjacency enumeration of all subsets through \(n=6\) agrees with the classification and a separate component recursion.

## Originality — PASS, with bibliographic uncertainty

The directly relevant 2024 Becker–Cameron–Hanely–Ong–Previte preprint develops minimal-fort counts and general graph-product constructions, but its full text and family summary do not treat \(J(n,2)\) or the stated cycle–star-forest classification. The 2023 Cameron–Hogben–Kenter–Mojallal–Schuerger work gives general fort-hypergraph and zero-forcing connections, not this all-size classification. Afzali–Ghodrati–Maimani (2024) already provide the minimum-fort size by determining the Johnson-graph failed zero-forcing number; that previously implied endpoint is explicitly excluded from the new contribution. Their full article could not be read, so an unobserved stronger classification remains a residual bibliographic risk. Related indexed records concern different graph families or different invariants, and the accessible local literature and research-record searches found no statement implying the full generating polynomial.

## Value — PASS

This is a complete combinatorial classification, not a narrow isolated computation. It identifies two distinct mechanisms for minimal obstructions to zero forcing on a canonical infinite family—edge covers and cycles—and enumerates every constraint by cardinality. Since every standard zero-forcing set must intersect each minimal fort, the classification supplies the complete minimal obstruction family for fort-cover formulations. The gap-free size spectrum and explicit number of the largest minimal forts are structural consequences with no analogous information supplied by a minimum-only parameter result.

## Verification and limitations

The proof is valid for all integers \(n\ge3\). Exhaustive direct verification covers \(n=3,4,5,6\); larger tabulated counts use only exact recurrence arithmetic and are not complete enumerations of vertex subsets. The argument does not determine all forts, all zero-forcing sets, or the analogous invariant on higher Johnson graphs. Bibliographic priority is provisional and independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
