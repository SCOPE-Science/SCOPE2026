# Scientific review

## Correctness — PASS

The exact partition by omitted original vertices is disjoint and exhaustive. The forced internal subdivision vertices, nonempty independent choices at induced isolated vertices, and remaining free edges account for every selected vertex exactly once; the graph is arbitrary, including disjoint components and isolated originals. The induced-component inequality bounds the minimum by the maximum induced matching, with an explicit attaining construction. Equality proves the forest classification and counts the minima without duplication. The supplied adjacency-based verifier confirms all coefficients, minima and forest structures on 56 graphs and 104,426 directly checked subsets. A finite test is not treated as an infinite proof.

## Originality — PASS (qualified)

The inspected 2012 domination-polynomial study provides graph recurrences, but no explicit full-subdivision induced-vertex-set transform or induced-matching minimum equality. The fully inspected 2022 central-graph study treats a graph operation that adds complement edges; its scalar complete-root specialization is known and not claimed here. Earlier related induced-matching/vertex-cover work and 2021 subdivision-number work address different statements. The inspected 2024 dominating-induced-matching paper concerns a stronger property of matchings and does not supply this ordinary domination polynomial. The abstract of a plausible 2025 full-subdivision study treats identifying codes; its complete text was not accessible. An independently unpublished or differently indexed equivalent formula remains possible; an unsuccessful search does not prove uniqueness.

## Mathematical value — PASS

This is a complete polynomial for **every** finite simple root graph, not an arbitrary parameter slice. It transforms the enumeration from subsets of \(n+m\) subdivided vertices into a subset sum over the original \(n\) vertices, supplies the exact parameter equality \(\gamma(S(G))=n-\nu_s(G)\), and structurally classifies and counts all minima, including natural complete and complete-bipartite families. These conclusions address sensor-placement and graph-domination structure beyond a previously known scalar for complete central graphs.

## Limitations and remaining risks

No statement is made about weighted variants, repeated edge subdivisions, or arbitrary multigraphs. The identity does not establish a polynomial-time algorithm for general root graphs. A 2025 primary full text and some earlier matching papers were not completely available; publication priority is not independently certified. This report documents a self-review only.

Self-review: passed. Independent audit: not yet performed.
