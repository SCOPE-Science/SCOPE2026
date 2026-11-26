# Independent mathematical audit

## correctness

PASS

For a nonempty simple k-regular graph as in the finding (the bipartite case expressly has c≥1), full-degree domination is exactly vertex-cover status. A maximum partition has no dominating size-k block: splitting it preserves all other partnerships and creates a new partner pair, since a subset of size <k cannot dominate. Each remaining block misses an edge and each of its partners hits one of the edge's two endpoints, bounding its partner degree by two. The partner graph has no isolated vertices; for at least four blocks, a path or cycle on at least four vertices or two nontrivial components furnish disjoint partner pairs. Their two disjoint covers cannot leave a vertex outside both (k>0), and as they are complementary covers they are independent. Thus at most four blocks occur, and four requires bipartiteness. An edge and the two endpoints split off as singletons give three blocks, and splitting both regular bipartition sides gives four, since each omitted vertex has all k neighbors across the bipartition. Each of the 2^(c−1) unordered bipartitions has balanced sides of size m, with 2^(m−1)−1 splits per side. Two distinct successful pairings of the blocks force edges only between opposite blocks A–D and B–C after relabeling, so both pairs of opposite blocks consist of unions of whole components. A third pairing would forbid every edge. The duplicate partitions are in bijection with the 2^(c−1)−1 nontrivial unordered component-group splits and the 2^(c−2) choices of independent unordered bipartitions of those groups. This proves the correction and includes the connected and smallest k=2 cases. A separate bounded reproduction used restricted-growth labels for all 115,975 set partitions of C4 disjoint union C6 and checked the original neighbor rule and partner clause directly, with 449 four-block partitions and none larger, as predicted. The frozen code and transcript were read, not executed; its direct checker filters block counts to 3 and 4, so its recorded maxima rely on the analytic ceiling. The frozen larger disconnected check uses the proven orientation parametrization, not a separate proof of exhaustiveness.

## originality

PASS

The assessed distinct result is the exact enumeration of all unlabeled optimal four-block partitions across connected and disconnected regular bipartite graphs, especially the component correction. The existing scalar bounds and exact cubic classification are credited. The known scalar or partner-degree results and the nearby enumerative findings do not count the critical multiplicities in this model.

## value

PASS

Once the motivating regular-graph coalition bounds are known, asking how many partitions attain the maximum is natural. The count shows precisely how disconnectedness, but not component shape, changes an unlabeled enumeration. It requires a genuine double-count correction and yields a concise invariant applicable even where explicit partition enumeration is infeasible. The value credited is the complete four-block enumeration, not simply recovering a known cubic number or treating the connected split count in isolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
