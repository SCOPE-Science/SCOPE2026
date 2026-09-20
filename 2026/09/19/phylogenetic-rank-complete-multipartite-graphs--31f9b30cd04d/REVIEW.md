# Same-model scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The statement reduces the complete-multipartite graph metric to a two-level distance pattern: distance \(2\) within a non-singleton part and distance \(1\) across different parts.

The upper bound is explicit. Each non-singleton part is assigned a unit-edge star coordinate, which realizes distance \(2\) within that part and distance \(1\) from that part to its complement. If there are at least two singleton parts, one additional half-edge star realizes all singleton--singleton distances \(1\). Direct case checking shows the coordinatewise supremum is exactly the graph metric.

The lower bound is the substantive point. Every chosen same-part pair has graph distance \(2\), so some coordinate must realize that distance. Two such pairs from different non-singleton parts cannot be realized in the same tree coordinate: the corresponding four-point sums would be \(4,\le2,\le2\), contradicting the tree four-point condition. Thus distinct non-singleton parts require distinct coordinates. When there are at least two singleton vertices, a coordinate realizing their distance \(1\) cannot realize any same-part distance \(2\), because the four-point sums would be \(3,\le2,\le2\). Hence exactly one further coordinate is necessary.

Potential failure modes were checked explicitly: coordinate maps may collapse vertices, but the four-point inequality remains valid for the induced tree pseudometric; the supremum is over finitely many coordinates, so every graph distance is attained by some coordinate; and the exceptional all-singleton case is handled separately by the standard half-edge star embedding of a complete graph.

The standalone verifier checked all 259 connected complete multipartite isomorphism types through order 12 and found no discrepancy.

## Originality

**PASS, to the best of our knowledge.**

The principal recent source is Ashworth--Clarke--Giansiracusa--Jones--Quijas-Aceves--Ren, arXiv:2609.19372. Its accessible full text was inspected. It explicitly proves rank \(2\) for complete bipartite graphs and rank \(N/2\) for \(K_N\) minus a perfect matching, and it asks for characterizations of graphs of rank at most \(k\ge2\). A full-text search found no occurrence of “multipartite” and no theorem covering arbitrary complete multipartite graphs.

External searches used the terms and variants “phylogenetic rank”, “tree rank”, “complete multipartite”, “complete bipartite”, “product of metric trees”, “supremum metric”, “tree metric rank”, and combinations with Pachter--Sturmfels and tropical geometry. These searches did not locate the stated formula or an equivalent classification.

Known prior ingredients are excluded from the originality claim: the four-point condition is classical; the tree-rank notion is due to Pachter--Sturmfels; complete graphs, complete bipartite graphs, and complements of perfect matchings are already covered in the 2026 graph paper.

The most plausible inaccessible source capable of weakening originality is:

- L. Pachter and B. Sturmfels (eds.), *Algebraic Statistics for Computational Biology* (Cambridge, 2005), Section 3.5, DOI 10.1017/CBO9780511610684. This is the original tree-rank source. The available web material exposed bibliographic metadata and the chapter structure but not the complete relevant section. The 2026 graph paper cites this section and nevertheless treats complete bipartite graphs and complements of perfect matchings as separate graph-family results, which lowers but does not eliminate the risk that a broader multipartite metric formula appears there.

A 2021 paper on ultrametrics and complete multipartite graphs and a 2025/2026 paper on star-generated ultrametric embeddings were also identified. Their subject is ultrametric/diametrical-graph characterization rather than supremum products of ordinary metric trees; their abstracts and accessible descriptions do not imply the present phylogenetic-rank formula.

Residual risk remains from very recent or not-yet-indexed parallel work and from differently phrased finite-metric literature.

## Value

**PASS.**

The result gives an exact closed formula on a standard graph class for a rank invariant introduced into systematic graph-theoretic study only days earlier. It simultaneously extends two separate families in the source paper—complete bipartite graphs and complements of perfect matchings—and exposes a new singleton-part correction that is not visible in either family. It also gives an exact complete-multipartite slice of the paper's open problem on characterizing rank at most \(k\).

The proof is short, structural, and reusable: distance-\(2\) pairs generate a packing problem for tree coordinates via four-point incompatibility, while explicit star coordinates meet the lower bound.

## Limitations

- The theorem classifies only complete multipartite graphs, not all graphs of rank at most \(k\).
- Several special cases are prior work and are not claimed as new.
- Full inspection of Pachter--Sturmfels (2005), Section 3.5 was not available; this is the main residual originality risk.
- Finite verification supports but does not replace the symbolic proof.
- Independent audit has not been performed.
