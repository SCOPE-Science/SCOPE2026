# Scientific review: maximum induced matchings and the Klein graph

## Correctness — PASS

The Coxeter graph is defined twice, as non-line Fano triples and as the 3-cycle/7-star construction given by Dejter. Each produces 28 cubic vertices and 42 edges. A 42-vertex edge-compatibility graph exactly encodes induced matchings as cliques. The Bron–Kerbosch maximal-clique enumeration returns 84 seven-cliques and none larger; an independently implemented fixed-size recursion checks directly that there are 84 seven-cliques and no eight-cliques. All 84 seven-edge sets are reproduced by the distance-three-sphere formula. Exact integer bit masks yield the pair-intersection histogram, all exchange graphs and all-pairs breadth-first distances. A complete 56-vertex permutation verifies graph isomorphism to an independent, named Klein-graph adjacency source. No reliance is placed on random samples or on external solver certificates. The possible limitation is that finite exhaustive mathematics is not a theorem for a varying graph family; no such claim is made.

## Originality — PASS, with acknowledged risk

Dejter (arXiv:1002.1960; first public February 9, 2010) already constructs the cubic Klein graph from the Coxeter graph using oriented heptagons and short paths. This connection is explicitly credited, not claimed as a discovery. An inspection of its Sections 1–3 and Theorems 1–3 found no induced-matching extremal classification or four-replacement exchange graph. Joos–Rautenbach–Sasse (arXiv:1312.1110; first public December 4, 2013) prove general bounds for cubic induced matchings and do not cover the exact Coxeter family. Accessible research-record searches using Coxeter, strong matching, induced edge-independent set, line-square independence and Klein aliases returned no covering claim. The closest indexed published mathematical result concerns the Coxeter independence complex, a different object. The strongest residual risk is an equivalent older finite computation expressed through seven-cycle incidence or strong-edge-color terminology; the search cannot certify global novelty.

## Value — PASS

The maximum induced matching number alone would be a narrow fact; the classification of all 84 optima, the sharp simultaneous-replacement connectivity threshold at four, the explicit lifted distance-three graph, and the exact identification with \(L(\mathcal K)\) establish meaningful structural geometry. The result supplies the first-described route in the inspected sources by which the classical 56-vertex cubic Klein graph is reconstructed from **optimal strong matchings**, rather than from cycle zipping. It explains which optimal states communicate by legal exchanges and their exact shortest-path costs.

## Reproducibility and risk

The two included standard-library Python programs are complete and independent in graph construction and clique enumeration. The named graph check uses documented SageMath sparse6 data and an explicit vertex bijection; re-running directly from the delivered package checks every edge. Independent scholarly audit and exhaustive unindexed literature coverage are not asserted.

Self-review: passed. Independent audit: not yet performed.
