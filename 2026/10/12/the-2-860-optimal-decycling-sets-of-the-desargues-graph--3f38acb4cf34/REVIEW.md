# Independent mathematical audit

## correctness

PASS

Reconstructed the incidence graph of 2- and 3-subsets of [5] directly (20 vertices, degree 3, 30 edges). For a removed k-set S leaving c tree components, edge counting proves 2k=10+e(S)+c, hence k≥6 and at k=6 only (e(S),c)=(0,2) or (1,1). Wrote a separate union-find forest/cycle enumerator over all C(20,6)=38,760 choices, obtaining exactly 2,860, with counts 760/2100 and forest profiles (1,13):360,(2,12):180,(3,11):120,(4,10):20,(7,7):80,(14):2100. Generated all 120 symbol permutations times subset-complementation (240 distinct automorphisms), proved they preserve adjacency and cover 2,860 sets in 19 orbits with claimed sizes. Conversely side-preserving aut induces an automorphism of T(5), whose five maximum stars force S5, so Aut(D) has no further elements. Full finite enumeration is exhaustive at this graph order, not a bound extrapolated to other graphs.

## originality

PASS

Wei–Li 2013 and Gao et al 2015 establish the decycling-number six for generalized Petersen GP(10,3); the regular cubic bound is also known. The retained result is exact 2,860 optima with profiles and 19 full automorphism orbits. Resultary nearest Desargues reports concern cut complexes and independence complexes, not feedback vertex census. Best-of-knowledge PASS; direct original generalized-Petersen articles only accessible as abstracts/metadata, so a hidden old census remains a genuine risk.

## value

PASS

A complete and reproducible natural finite graph invariant: not merely the already known scalar decycling number, but all minimizers, induced residual forest shapes and automorphism orbits. Exact orbit decomposition is independently useful for combinatorial optimization and symmetry reductions; complete finite classification is a legitimate substantive result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
