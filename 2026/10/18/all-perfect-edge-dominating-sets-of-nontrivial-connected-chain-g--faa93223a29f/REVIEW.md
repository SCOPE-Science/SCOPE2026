# Review: perfect edge domination in nontrivial connected chain graphs

## Correctness — PASS

The argument is an exhaustive, two-sided case split on the set of zero selected-degree vertices \(W\). Every unselected edge \(uv\) obeys \(d_F(u)+d_F(v)=1\), and the selected edge set is exactly the subgraph induced by nonwhite vertices. Universality of \(A_p\) and \(B_1\) forces all possible nontrivial sets to be either complete stars, or the unique exceptional central edge. The complete-bipartite one-level case is separately deduplicated. In addition to the unrestricted proof, an independent implementation tested 137,303,442 edge subsets across 1,049 profiles, without disagreement. The finite test is not an infinite proof.

## Originality — PASS (with documented access risk)

The inspected full HTML of Grippo–Lin–Vera, arXiv:2509.04598v2, already provides a cubic-time **algorithm to count PED-sets for all \(P_6\)-free graphs**, including chain graphs, as well as the general white/yellow/black structural encoding. That general computational result **covers countability** and is explicitly credited. It does not state the complete chain-graph optimizer classification or the sparse exact polynomial. The 2026 Grippo–Lin–Moyano–Vera abstract describes extremal and counting methods for other named classes, but its full text could not be inspected; an equivalent chain specialization hidden there is a residual risk. Targeted searches for chain graphs, Ferrers graphs and \(2K_2\)-free bipartite graphs and semantic research-record comparisons found no covering closed form.

## Value — PASS

Every individual PED-set is characterized for arbitrary positive twin-class sizes and arbitrarily many levels. The theorem also gives all edge-cardinality coefficients, a closed numerical count, minimum sizes/optimizer counts, and the exact existence/uniqueness boundary for dominating induced matchings. The unexpectedly sparse polynomial and sharp two-level exception offer structural information not supplied by a generic polynomial-time counting routine.

## Literature and limitations

A general black/yellow/white PED-set encoding is prior (Grippo–Lin–Vera, arXiv:2509.04598v2, §2.1). The general counting routine is prior (§6). The 2026 paper arXiv:2607.03894v1 was available in abstract only. The present contribution does not assert a new broad complexity result or independent validation. Finite enumeration supports, but does not replace, the proof.

Self-review: passed. Independent audit: not yet performed.
