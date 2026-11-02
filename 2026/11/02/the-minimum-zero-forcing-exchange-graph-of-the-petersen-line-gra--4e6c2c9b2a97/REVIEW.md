# Scientific review

## Correctness — PASS

The result is an exact finite theorem, not a conjectured formula inferred from small samples. The graph has exactly fifteen vertices, so testing all \(2^{15}=32{,}768\) subset masks is complete. The force-closure lemma shows simultaneous forced bits implement the ordinary zero-forcing rule. Both independent certificates reconstruct the input graph and test the complete minimum layer, all legal one-token exchanges and all shortest-path metrics; one uses natural \(S_5\)-orbits and the other starts BFS from each of the \(2{,}280\) configurations. They separately verify the exact census, connectivity, degree distribution, radius, diameter, distance profile and sharp one-move detour bound. The proof relies on finite exhaustive computation with transparent source and complete loops, not a sample or a timeout.

## Originality — PASS (best knowledge)

Eroh–Kang–Yi (arXiv:1207.6127, 2012) study the zero forcing number on line graphs, but not this graph's exchange state space. Fallat–Soltani (2016), Theorem 3.4, already imply \(Z(L(P))=7\); this size is **not** new. Geneson–Haas–Hogben (arXiv:2009.00220, 2020) introduce exactly the exchange-graph definition and study other families. Primary texts were inspected, including direct checks for the word Petersen. Relevant research-record and published-literature searches for line Petersen forcing, edge forcing, symmetry classes, optimum-set counts and Johnson-distance defects found no equivalent census or stronger theorem implying it. Potential unindexed coverage remains an identified risk; search failure is not proof of novelty.

## Value — PASS

This determines a natural exact optimum-space invariant for a canonical highly symmetric graph, rather than recomputing only its known zero-forcing number. The complete degree and distance distributions, 21 symmetry orbits and near-isometry theorem give detailed transformation geometry. Precisely 18,540 unordered pairs must take a one-move detour from the unavoidable token-replacement distance, while no pair needs a longer detour. This supplies a well-defined benchmark for forcing/reconfiguration methods and a motivated structural question for broader families. The finite scope is explicitly acknowledged.

## Limits and status

All claims are confined to the fifteen-vertex Petersen line graph, not an infinite family. The minimum cardinality seven is prior work; the full 2008 foundational publisher paper was not accessible, and no full-document exclusion is claimed for it. Two independent *algorithms* were checked, not an independent scientific review.

Self-review: passed. Independent audit: not yet performed.
