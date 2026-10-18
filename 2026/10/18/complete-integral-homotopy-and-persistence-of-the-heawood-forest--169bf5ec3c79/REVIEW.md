# Scientific review: Heawood forest-filtration classification

## Correctness
PASS. The precise Fano incidence rule and forest degree predicates are reconstructed independently in the supplied programs. `verify_morse.py` enumerates all 16,384 vertex subsets, constructs all four complete discrete-Morse matchings, checks every codimension-one face relation, and directly proves acyclicity by topologically sorting the entire oriented Hasse graph. The only unmatched faces are one vertex and, respectively, six 3-cells, thirteen 5-cells, one 6-cell, and eight 8-cells. Forman's discrete Morse theorem and the absence of intermediate cells give the four integral sphere wedges. An independent program calculates all mod-two boundary ranks. The persistence maps vanish because the adjacent nonzero homology degrees differ. No experimental extrapolation is used.

## Originality
PASS for the claim of the higher stages and complete persistence, not for the known independence-complex stage. The published Heawood independence classification already gives the first homotopy term. Perarnau and Perkins independently give the first stage's face counts. Carnero Bravo introduces the forest filtration and treats paths, cycles, cactus graphs, stars, joins and selected products, not this point-line incidence graph. His polyhedral-join paper likewise does not imply the higher stages. Searches for the exact graph, degree-one dissociation/2-independence aliases, induced degree-two forests, stage three's acyclic induced subsets, full persistence and stronger general results found no indexed equivalent. Unindexed and unpublished calculations remain a residual risk; search absence is not a proof of uniqueness.

## Value
PASS. The Heawood graph is the smallest cubic graph of girth six and the incidence graph of the Fano plane, so its forest filtration is a canonical motivated object rather than an arbitrary parameter slice. The result classifies *every* stage of a natural filtration integrally, exhibits three distinct changes of sphere dimension after its known first stage, and determines all inclusion-induced integral persistence modules. Exact homotopy is stronger than face counting or homology over one field. The theorem is finite-object specific; it does not claim an infinite-family classification.

## Closest literature and limits
Carnero Bravo (arXiv:2307.13271, 2023) supplies the filtration and general tools but no Heawood evaluation. His arXiv:2307.14321 applies polyhedral joins to different graph families. The 2018 independence-polynomial computation and the published 2026 first-stage Heawood homotopy classification are credited as existing results. The new conclusion rests on executable, exhaustive directed-Hasse acyclicity checks and still lacks independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
