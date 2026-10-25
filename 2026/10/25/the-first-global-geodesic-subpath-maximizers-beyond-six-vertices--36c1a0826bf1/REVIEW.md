# Review: Global geodesic-subpath extrema at seven and eight vertices

## Correctness — PASS

The definition counts shortest paths once per unordered vertex pair, including one singleton path per vertex. The seven-vertex upper bound enumerates every \(2^{21}\) labelled simple graph with an exact integer breadth-first path counter and rejects disconnected cases; maximizer masks equal the full permutation orbits of \(K_{3,4}\) and its one-edge deletion. An independently implemented Graph Atlas test confirms its two classes. The eight-vertex upper bound combines all 1,044 seven-vertex Atlas representatives with all 128 eighth-vertex neighbourhoods, covering every eight-vertex class. Every attaining extension is explicitly in the permutation orbit of one of two matching-deleted \(K_{4,4}\) graphs. Verification output and source code are embedded. The Graph Atlas completeness theorem and dataset are an essential stated premise.

## Originality — PASS, with residual priority risk

The 2026 founding paper gives small-order global extrema only through six vertices. An earlier exact matching-deletion formula yields the four witness graph values, but does not imply their optimality or completeness over all connected graphs. A materially inspected diameter-two upper-bound theorem does not cover the diameter-three eight-vertex maximizers. Searches for total numbers of shortest paths, the exact proposed values, and related graph family descriptions did not reveal an exact prior unrestricted seven/eight theorem. A separately indexed path-blowup improvement was not fully read, and an uncatalogued earlier census remains possible.

## Mathematical value — PASS

The exact first two new orders beyond the founding paper determine both maximum counts and every maximizer. The first loss of balanced-biclique global optimality occurs at eight vertices: \(K_{4,4}\) yields 72 while its one- and two-matching-edge deletions attain 74. This is a concrete boundary for the broader open extremal problem, not a mere recomputation of the known formulas inside a fixed graph family. No asymptotic or arbitrary-order theorem is asserted.

Self-review: passed. Independent audit: not yet performed.
