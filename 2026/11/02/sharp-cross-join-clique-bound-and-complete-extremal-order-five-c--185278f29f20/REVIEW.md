# Scientific review

## Correctness: PASS

The all-order clique bound follows from the representation of a single cross-join as exactly two toggled interior feedback entries and the elementary classification of pairwise-intersecting two-element sets into stars or triangles. Fixed endpoint feedback bits reduce the available positions to \(2^{n-1}-2\). For order five, an exhaustive sweep of all 65536 Boolean tables gives 2048 full cycles and 224 ordered universal-star certificates; each fourteen-vertex clique is counted exactly fourteen times, proving sixteen. A separately implemented Euler-tour enumeration yields precisely the same valid tables, and direct six-mer factor-set intersections with a general maximal-clique algorithm independently yield the same sixteen cliques. The embedded checker printed `VERIFY_OK`, and the supplied fourteen-mask witness was verified pairwise.

## Originality: PASS (with limitations)

Mykkeltveit and Szmidt establish cross-join construction and connectivity, not an extremal complete-subgraph classification. Alhakim (2018) analyzes the cross-join graph and supplies the exact order-five degree-frequency table, not the clique number or clique inventory; relevant full-text sections and its conclusion were examined. Ezerman, Fahreza, and Szmidt (2018) supply perturbation-distance patterns, not pairwise adjacency among each set of neighbors. The degree distribution and Fryers-type single-reference distance polynomials do not by themselves imply which sets of vertices form cliques. Targeted searches for clique extremality, feedback-table star cliques, 14-cliques and cross-join graph triangles returned no covering statement. The complete extracted text of the 2013 original eleven-page manuscript was examined, including its cross-join theorem and order-four examples, without finding the order-five clique classification. The later 2026 source was not fully retrievable; unindexed historical priority remains possible and no independent certification is asserted.

## Value: PASS

The cross-join graph is a natural reconfiguration space for binary de Bruijn cycles. Its clique number measures the largest family where every pair of sequences is a single cross-join apart; the answer is directly relevant to the simultaneous local alternatives available from multiple sequence designs. A uniform all-order upper bound together with a sharp order-five extremizer and a complete classification of all sixteen extremal families is more informative than existing degree-only descriptions, rather than an arbitrary subfamily or a routine isolated value. No larger-order equality or cryptographic application is claimed.

## Closest literature and residual limitations

- J. Mykkeltveit and J. Szmidt, 2013 ePrint / 2014-2015 versions: binary cross-join constructions and connectivity.
- A. Alhakim, 2018, arXiv:1805.12059: full text examined; cross-join graph connectivity, Hamiltonicity, and order-five degree counts.
- M. F. Ezerman, A. A. Fahreza, and J. Szmidt, 2018 BFA presentation: perturbation patterns; not a complete-subgraph inventory.
- Residual priority risk: unindexed clique analyses, later publisher full text unavailable for full scrutiny, and other work that may exploit the same feedback-coordinate structure.
- Scientific limit: the exact order-five classification is finite; sharpness for all larger orders remains open in this work.

Self-review: passed. Independent audit: not yet performed.
