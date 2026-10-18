# Scientific review: Moore-space summands in bidirected complete-bipartite multipath complexes

## Correctness — PASS

The domain is a fixed four-member family of explicitly defined bidirected digraphs. Every valid simplex has at most four arcs, permitting exhaustive enumeration of all faces and boundaries. The arc-toggle matching is checked as a disjoint matching over every face and certified acyclic by topological sorting of the entire directed Hasse graph. An independent implementation cancels every matched chain generator with a signed unit coefficient. The resulting integral matrices are zero in the first and last cases and have content exactly two in the middle cases. Because the remaining CW models consist only of a vertex and one or two consecutive low-dimensional cell degrees, their attaching maps are classified by degree, and unimodular changes yield precisely the asserted Moore-space or sphere-wedge homotopy types. The dynamical-module argument uses actual directed two- and four-cycles, applies uniformly to all four digraphs, and verifies that every vertex is unstable. See `RESULT.md` and both bundled Python programs.

## Originality — PASS, qualified

The 2026 bidirectional-polygon study treats path and cycle hosts, not the present bidirected complete bipartite hosts. The 2022 complete bipartite computation uses one-way oriented arcs and computes Euler characteristics of chessboard complexes, not the bidirected multipath homotopy types. Its introduction does contain the exact torsion/stability conjecture which these examples contradict. The 2024 weak categorical quiver-minor paper establishes torsion boundedness and gives a matching-complex correspondence for acyclic digraphs, not this cyclic family. Mathematical record comparisons identify graph Morse and higher matching complexes on the same underlying graph, but those have different defining simplices. No published result was located that implies the present four exact integral homotopy types or the explicit unstable-module counterexamples. Unindexed or unpublished prior computations remain a genuine qualification. Details of comparison and source reading are in `AUDIT.json`.

## Value — PASS

These are small, natural, highly symmetric bidirected hosts outside the previously classified bidirected path and polygon families. The two consecutive torsion-bearing cases exhibit a precise Moore-space mechanism, rather than just an unexplained finite-field discrepancy. Moreover, the torsion occurs in unstable dynamical modules and directly resolves a stated proposed torsion criterion in the negative. The explicit four-case classification is a useful finite cutoff; there is no unsupported claim for larger values or an all-parameter formula.

## Scientific limitations

The proof uses exhaustive finite computation with complete source programs, not an infinite extrapolation. No assertion is made about \(n\ge7\). Priority remains qualified by the reach of public source retrieval and mathematical indexing. The 2026 conjecture for bidirectional polygons is not addressed because the graphs here are not polygons.

Self-review: passed. Independent audit: not yet performed.
