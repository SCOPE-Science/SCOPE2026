# Review

## Correctness — PASS

Every subset of the twenty graph edges is tested, and the exact row-and-column degree predicate defines the intended complex. The reproducible checker enumerates all 37,440 nonempty faces, all 2,490 maximal faces, and the full 217,580 incidences of the Hasse graph. Its 18,697 pairs form an acyclic discrete-Morse matching; the surviving CW model has one vertex, 42 six-cells and three seven-cells. The signed integer Morse boundary has every one of its 126 entries equal to zero. The five-connected six-skeleton is a wedge of 42 six-spheres, so the degree-zero attaching maps are nullhomotopic. Independently computed mod-two simplicial ranks give the predicted Betti numbers. All of these calculations were executed successfully from the supplied verifier; no experimental extrapolation is used.

## Originality — PASS (best available evidence)

The primary readable text of Singh's higher-matching paper [2] limits its complete-bipartite homotopy results to hypotheses excluding this case; it notes earlier general rational homology [3], not an integral homotopy classification. Exact publicly indexed neighboring cases [4,5] concern different rectangular graphs, with no proved implication to this one. Direct searches for the \(K_{4,5}\) bounded-degree complex, its line-graph three-clique-free equivalent, and corresponding homotopy and homology groups returned no covering result. The newer clique-free paper [1] addresses sufficient shellability hypotheses, while the relevant rook graph is nonchordal. Its complete manuscript could not be read, so an unrecognized computation or appendix remains a risk. Search absence is not treated as a uniqueness proof; confidence rests on statement-level distinctions and the directly inspected Singh theorem.

## Mathematical value — PASS

The result resolves the natural first \(4\times5\) case of a familiar family of two-matching complexes, neighboring the already evaluated \(4\times4\) and \(3\times5\) cases. Unlike those single-degree examples, it has integral homotopy in two adjacent dimensions and gives a structural nonshellability obstruction for a pure complex. The integer attaching-map calculation determines much more than its Euler characteristic or rational Betti numbers. This natural exact finite classification is useful as a check on general bounded-degree and clique-free predictions.

## Limitations and comparison

A general representation-theoretic method may already predict some Betti numbers; this report does not claim priority for them. Only ordinary homotopy is computed. The complete recent manuscript [1] was inaccessible; no claim is made that its full text was inspected, nor that unindexed results were exhaustively excluded.

Self-review: passed. Independent audit: not yet performed.

## References

[1] R. Ghosh and S. Selvaraja, *Shellability in Clique-Free Complexes of Graphs*, arXiv:2602.09623 (2026-02-10).

[2] A. Singh, *Higher matching complexes of complete graphs and complete bipartite graphs*, arXiv:2006.13632, Theorem 1.2.

[3] V. Reiner and J. Roberts, *Minimal resolutions and the homology of matching and chessboard complexes*, J. Algebraic Combin. 11 (2000), 135–154.

[4] Publicly indexed result ID `2026/10/11/SCOPE-the-two-matching-complex-of-k-4-4-is-a-wedge-of-fifteen-five-sph--915eed6b65e5`.

[5] Publicly indexed result ID `2026/10/11/SCOPE-the-two-matching-complex-of-k-3-5-is-a-wedge-of-91-five-spheres--ea5e14157f12`.
