# Scientific review: Petersen token-swapping census

## Correctness — PASS

The domain is the complete finite state space of all \(10!\) bijections on Petersen vertices, with each of the \(15\) permitted edge swaps generated explicitly. FIFO breadth-first-search invariants imply that the first-found depth is the true shortest number of swaps, and left translation proves that identity eccentricity equals Cayley diameter. The \(14\) nonempty distance shells sum to \(3{,}628{,}800\). Two independently written verifiers with two Petersen graph realizations, two different permutation representations, and two neighbor operations yield exactly the same shells, diametral cycle types and transport-gap histogram; both report `VERIFY_OK`. This proves finite exactness, not any infinite-family statement.

## Originality — PASS, with limitations

The 2014 original token-swapping paper was inspected in full-text relevant sections; its scope is general search bounds and algorithms for trees, tree spanners and complete bipartite graphs. The separate Cayley-diameter source arXiv:1111.3114 is explicitly restricted to generators arising from trees, so it does not imply exact numbers for a cyclic Petersen generating graph. ArXiv:1607.07676 studies complexity and general search, not this complete spectrum. The 2016 review of paths, stars, cliques and rings was inspected from accessible abstract/excerpts only; its full manuscript could not be downloaded from a plausible postprint link. Semantic research-record searches for Petersen swapping and equivalent Cayley metrics found no statement implying \(13\) or the exact enumerator. These negative searches do not prove absolute novelty; an unindexed or inaccessible prior census remains possible.

## Value — PASS

The Petersen graph is a canonical highly symmetric cubic test graph. Its entire \(3{,}628{,}800\)-state token-swapping Cayley metric is a natural exact sorting-network benchmark: the diameter is sharp, all diametral permutation cycle types are determined, and the complete lower-bound deficiency distribution has a nontrivial maximum of four despite base-graph diameter two. The numeric facts cannot be obtained from generic connectivity, complexity or coarse sorting bounds, and the complete census is reusable for validating shortest-swap methods on a natural non-tree topology. No general downstream result is claimed.

## Limitations

All results concern this one finite graph and use exhaustive computation. Neither an infinite-family extension nor independent expert certification is asserted. Specific unindexed literature may contain the same numeric data.

Self-review: passed. Independent audit: not yet performed.
