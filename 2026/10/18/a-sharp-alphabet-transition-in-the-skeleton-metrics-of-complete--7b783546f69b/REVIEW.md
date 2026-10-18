# Scientific review

## Correctness — PASS

The network model and its arc-coordinate vertex representation are explicit. An exposed support face contains exactly the two-route branch recombinations, so the consecutive-disagreement adjacency criterion holds in both directions, including the nonadjacency midpoint certificate. Neighbour counts are indexed by a unique disagreement interval. The adjacency matrix is an exact sum of interval-supported tensor products of complete-graph adjacency matrices, proving every Laplacian eigenvalue and multiplicity; connectivity and Kirchhoff prove the tree product. For binary layers a padded transition count gives both lower and upper graph-distance bounds; for larger uniform alphabets the third-symbol intermediate route gives the diameter-two upper bound and a two-run pair witnesses sharpness. Checker replay verifies 17 finite uniform profiles, six independent small midpoint-LP profiles, eleven spectral instances, and exact small spanning-tree cofactors. Boundary cases with one or two internal layers are handled. Computational samples are not the universal proof.

## Originality — PASS, with qualifications

Rispoli's 1992 criterion, as expressly quoted in Blanchard–De Loera–Louveaux (2020, Section 3), already characterizes adjacent shortest-path vertices by one support cycle; it is not newly claimed. The 2020 work studies heights and monotone simplex paths of a different (complete-graph) shortest-path polytope, and its full accessible manuscript was inspected in the directly relevant Sections 1, 3 and later simplex bounds; searches for layered networks, spectra and binary words in that manuscript located no stronger coverage. Borgwardt–De Loera–Finhold (2016) gives broad Hirsch bounds, not full finite layer-profile Laplacian spectra or pair-distance counts. The binary graph is explicitly identified as the classical halved cube; its known distance and spectral invariants are credited, not claimed independently new. The specific all-layer-size spectral/tree formula and the alphabet-two versus alphabet-three diameter/distribution classification were not found in these sources or the comparison searches. The Rispoli source was not available in full; equivalent unindexed formulations remain possible.

## Value — PASS

The result gives an exact, nontrivial all-parameter spectral classification of the one-skeletons of a canonical family of network-flow polytopes, including nonuniform layer sizes and exact spanning-tree complexity. The uniform-alphabet metric shows a sharp unbounded-versus-two combinatorial diameter transition triggered by adding one state to every layer, with exact graph-distance distributions and Wiener indices. These invariants describe fundamentally different shortest-pivot behavior for complete layered networks with exponentially many path vertices. The theorem is a focused complete natural-family classification, not an arbitrary parameter-table census.

## Limits and closest literature

Published general path-adjacency theory and halved-cube graph theory cover two key structural ingredients. The present contribution is their particular path-polytope realization together with full mixed-layer spectra/tree counts and the three-symbol collapse. The 1992 Rispoli full text could not be compared directly. The checker uses standard scientific Python packages and finite examples; no independent audit or external certification is represented.

Self-review: passed. Independent audit: not yet performed.
