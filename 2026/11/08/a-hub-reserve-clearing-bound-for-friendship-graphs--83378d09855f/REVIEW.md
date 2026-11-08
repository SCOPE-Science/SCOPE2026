# Review of the hub-reserve clearing bound

## Correctness
PASS. The local pair-clearing sequences were reconstructed and their occupancies and move budgets checked. At the hub-positive critical weight, pigeonholing produces a pair of total occupancy at most three; removing it uses at most four moves while preserving a positive hub and leaves enough pebbles for induction. The two-triangle base has a separate four-pebble-pair case, addressed explicitly. At larger weights, either a peripheral-to-hub move reduces total weight or all peripheral occupancies are at most one. In the latter case the per-pair clearing budget leaves a sufficient hub stack; the residual three-pebble exception is removed by clearing one full pair in two shuttles. The final hubless case reduces in one move. The two small sharpness cases are checked by complete labelled occupancy enumeration using the included standalone verifier. The finite checks do not prove the unbounded statement.

## Originality
PASS on available evidence, subject to historical-priority uncertainty. The motivating 2026 paper defines stacking and clearing and computes complete and complete multipartite cases, but does not state the friendship hub-reserve bound. The complete multipartite theorem is inapplicable to \(F_r\) for \(r\ge2\), because the glued triangles form a graph with nonadjacent vertices having different neighbourhoods. Indexed claims about zero forcing, general-position and dissociation polynomials on windmills concern different invariants, and no indexed pebbling claim with the proposed bound was found. Exact small-case computations could have appeared independently outside the inspected sources.

## Value
PASS. This is a structural, uniform reachable-state theorem for a natural infinite family of connected non-bipartite block graphs, not merely one small census or a renamed standard parameter. It replaces the general diameter-two bound \(2|V|2^{\operatorname{diam}}=8(2r+1)\) by \(4r\), using a constructive local-to-global reduction. The hub-reserve condition describes why a positive hub pebble acts as a catalyst; the exact first nontrivial cases also show the bound can be tight. The unresolved all-\(r\) sharpness problem is expressly left open.

## Limits and closest work
Main source: Csernák and Soukup, *Stacking and clearing in graph pebbling*, arXiv:2604.22341 (2026-04-24), especially its parameter definitions, general upper bounds, and exact cases of Sections 7–8. New statements are for triangular friendship graphs only; this does not resolve stacking or clearing for general cacti. Computational verification is exhaustive only for \(r=2,3\). Unindexed priority conflicts remain possible.

Self-review: passed. Independent audit: not yet performed.
