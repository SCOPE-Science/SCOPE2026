# Scientific audit — SCOPE-20260908-057 — 2026-09-30

## Final claim assessed

For the stated bounded 3 by 3 and 3 by 4 ordered-margin windows, the complete fiber graphs under 2 by 2 Diaconis-Sturmfels moves have the tabulated exact diameters, including the unique 3 by 3 diameter-12 maximum and the 22 diameter-8 3 by 4 classes.

## Correctness — PASS

The committed generator enumerates every margin class in scope, every table in each fiber, builds exactly the signed 2 by 2 rectangle moves, and computes all-pairs BFS diameters. The independent verifier uses a different fiber enumerator and rebuilds the moves/BFS. Independent audit parsing of the committed CSVs confirmed 9331 and 7140 rows, the complete diameter histograms, the unique 3 by 3 maximum (666,666,size 406,diameter 12), all 22 3 by 4 diameter-8 rows, and the unique size-415 3 by 4 uniform fiber with diameter 6.

## Originality — PASS

Diaconis-Sturmfels and later fiber-graph literature establish the move-set/connectivity framework and study mixing/connectivity, while the Markov Bases Database stores bases rather than these bounded fiber-diameter tables. Resultary searches returned the matching record but no prior exact census matching these windows or extrema. No inspected primary source implied the full per-margin diameter table.

## Value — PASS

Fiber-graph diameter is directly tied to the geometry and mixing behavior of Markov-basis walks. A complete exact census over the two smallest nontrivial two-way table shapes, with extremal witnesses and thousands of fibers, is a natural finite benchmark rather than an arbitrary isolated computation.

## Residual risks and limitations

- Both implementations share the same mathematical definition of adjacency; this common-mode risk is mitigated by explicit per-step rectangle checks and agreement with the classical move set.
- Exact small-fiber computations could exist in unpublished software or supplementary tables not indexed by the searches.
- The margin cutoffs 6 and 4 remain finite and do not yield a general diameter law.

## Sources inspected

- 2026/09/08/057/artifacts/census.py
- Diaconis-Sturmfels 1998
- Diaconis-Sturmfels, Annals of Statistics 26 (1998), DOI 10.1214/aos/1030563990
- Markov Bases Database
- Resultary query: Markov basis contingency table fiber diameter exact 3x3 3x4
- Windisch 2016
- Windisch, Rapid Mixing and Markov Bases, SIAM J. Discrete Math. 30 (2016)
- census_3x3.json
- census_3x4.json
- table_3x3.csv
- table_3x4.csv
- verify.py
