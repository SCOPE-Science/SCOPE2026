# Scientific review: the Fermat-quartic line-graph critical group

## Correctness — PASS
The object is the graph of all 48 complex Fermat-quartic lines. Shimada–Shioda give the exhaustive line equations; the independent exact determinant test in `verify.py` matches all 1128 possible pairs. Connectivity, valency, edge count and exact adjacency-spectrum certificate were replayed. The matrix-tree order and all three local Smith valuation lists give matching determinant valuations; combining their sorted local valuations establishes the claimed group, not merely its order. The spectral and local algebra are finite exact proofs for this fully specified matrix.

## Originality — PASS, subject to historical-priority risk
Schütt–Shioda–van Luijk determine line generation of the Néron–Severi group, whose divisor-lattice discriminant is not the present graph critical group. Shimada–Shioda describe the 48 lines and their incidence-orbit sizes; Bouyer treats quartic Picard lattices. In the inspected passages and searched documents no reduced graph Laplacian Smith form was stated. Exact mathematical-record searches for the Fermat 48-line graph, Smith normal form, sandpile group, graph Jacobian and Laplacian found nearby results on different 64-line and 85-line graphs, not an equivalent group or a general theorem specializing to it. An unindexed calculation or unpublished table could still anticipate these factors. Absence of search hits alone is not evidence of uniqueness.

## Mathematical value — PASS
The complete critical group is a canonical integral invariant attached to one of the most studied configurations of lines on a K3 surface. It resolves every integral chip-firing obstruction rather than recording only the known incidence counts or a spectral spanning-tree number. Its nontrivial 3- and 5-primary structure is distinct from the 2-primary discriminant of the surface's Néron–Severi lattice and gives a meaningful, non-obvious refinement of the same natural configuration. This is a specific complete finite classification, not an arbitrary parameter slice or a claimed global theorem.

## Scope and remaining risks
The result is not about torsion in the Picard group, positive-characteristic 112-line configurations, or other quartic embeddings of the same abstract K3 surface. Historic priority and independent expert verification remain open. The included standard-library verifier supplies the exact finite mathematical certificate.

Self-review: passed. Independent audit: not yet performed.
