# Review: full-palette singleton rainbow domination on rectangular rook graphs

## Correctness — PASS
A degree-sized palette forces every uncolored vertex to have only colored neighbors, hence an independent, nonattacking-rook support. Every pair of absent row-column intersections yields exactly two colored cells simultaneously adjacent to the corresponding two uncolored vertices. The resulting color-conflict multigraph is \(2K_j\). The requirement is necessary and sufficient because all remaining neighbor cells touch exactly one uncolored vertex and can receive the remaining distinct labels independently. The matching-size bound and explicit factorization constructions prove \(\chi'(2K_j)=2j-2\) for positive even \(j\) and \(2j\) for odd \(j\ge3\). Substitution yields precisely the stated exceptional maximum supports. All support coefficients and minimum values follow from standard matching counts. No finite experiment is used to infer an infinite theorem.

## Originality — PASS (qualified by bibliographic risk)
Lange, arXiv:2610.06906v1 (2026-10-01), defines the same singleton parameter, proves its general lower bound from independence number and provides exact results for other regular families, but no rook-graph classification or uncolored-support polynomial. Mertens, *Domination Polynomial of the Rook Graph* (2024), studies ordinary domination and its different polynomial, so neither result implies the coloring constraint, its doubled-clique obstruction, or all-support enumeration. Žerovnik (2026) studies singleton 3-rainbow domination for path-cycle cylinders rather than arbitrary rook boards at the full degree palette. Relevant semantic record searches returned related but noncovering results on multipartite 2-rainbow domination, rook graph topology, and rainbow connection. An unindexed equivalent result remains a genuine bibliographic risk.

## Value — PASS
This is a complete support-level classification over every rectangular rook graph with two nontrivial sides, not a single numerical special case. It pinpoints a sharp parity-and-aspect-ratio phase transition not resolved by the usual independence-number bound and supplies the precise parity correction to the classical rook-matching support enumerator and the multiplicity of optimal supports. The edge-coloring reduction explains the obstruction, supports constructive recovery and illustrates a reusable distinction between independent uncolored configurations and globally consistent neighboring colors.

## Limits
The colorings themselves are not counted, and the statement does not cover the multicolor-per-vertex model or general Cartesian products. The accompanying finite verification is corroborative. Independent mathematical review and definitive bibliographic priority remain outstanding.

Self-review: passed. Independent audit: not yet performed.
