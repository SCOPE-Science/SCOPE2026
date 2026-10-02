# Scientific audit — SCOPE-20260908-056 — 2026-09-30

## Final claim assessed

For every rank-3 matroid, including matroids with loops or parallel classes, every compatible ordered pair of bases can be transformed to every other compatible ordered pair by at most three symmetric exchanges; the bound is sharp. The simple rank-3 types on 3 through 6 elements also have the recorded exact per-type diameters.

## Correctness — PASS

The support of two compatible ordered basis pairs has at most six elements. Restriction to that support preserves the relevant bases and exchanges, and padding by loops embeds smaller supports in the six-element exhaustive check. The committed lemma_check.py enumerates all 2^20 triple families on six labels, filters exactly by the basis-exchange axiom, and BFS-checks every compatible-pair component for the 2053 surviving rank-3 families; census_m3_m6.json independently records the simple-type cases and explicit shortest paths. The reduction is finite and the sharp lower bound is supplied by the disjoint swap in U(3,6).

## Originality — PASS

Prior work already covers important neighboring statements: Kashiwabara proves White-type connectivity for rank at most 3, and Bérczi-Schwarcz give a sharp exchange-distance upper bound for split matroids, hence for paving matroids and therefore for simple rank-3 matroids. Those results mean the original emphasis on the simple rank-3 upper bound was overclaimed. The repaired claim instead isolates the all-rank-3 constant diameter bound, including non-simple rank-3 matroids, plus the exact small simple-type census. Searches of Resultary and the closest primary literature inspected did not locate that stronger all-rank-3 distance bound or the per-type census.

## Value — PASS

A uniform sharp constant bound for all rank-3 matroids strengthens mere connectivity into quantitative reconfiguration information. This is a structural rank-boundary lemma rather than just a finite table, while the exact small-type census supplies calibration examples.

## Residual risks and limitations

- A distance bound may be implicit in an older proof of rank-3 White connectivity even if not stated as such; no such implication was found in the inspected sources.
- The central finite lemma is computational rather than a hand proof.
- The simple-matroid part alone would be too close to prior split/paving bounds; value rests on the non-simple all-rank-3 extension and its sharpness.
- The verifier contains one vacuous start-witness assertion (`or True`), although edge legality and the exhaustive lemma computation do not depend on that assertion.

## Sources inspected

- Bérczi-Schwarcz 2022 frames basis-pair exchange distance as a central quantitative problem.
- Bérczi-Schwarcz, Exchange distance of basis pairs in split matroids, arXiv:2203.01779v3
- Git tree 2026/09/08/056 at source tree 224642e877c64a17d1a640ecd6e05ecb264e10fd
- Kashiwabara, The toric ideal of a matroid of rank 3, EJC 17 (2010) R28
- Resultary query: rank 3 matroid symmetric basis exchange distance diameter
- output/artifacts/census_m3_m6.json
- output/artifacts/lemma_check.py
- output/artifacts/verify.py
