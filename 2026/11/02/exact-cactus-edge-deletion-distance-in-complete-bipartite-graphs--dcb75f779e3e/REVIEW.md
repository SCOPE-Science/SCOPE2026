# Scientific review

**Correctness — PASS.** The block-cut-tree proof bounds the number of cycles independently by the two bipartition sizes and total vertex count. The construction takes the minimum of the three bounds, solves an integer attachment-capacity inequality, and realizes that many edge-disjoint four-cycles in a connected spanning cactus; the edge-count identity then gives the claimed deletion optimum. The tree boundary, including one-vertex bipartition classes, is included. A separate checker exhaustively tested twenty small inputs and checked 900 constructive witnesses; these are corroboration, not a substitute for the infinite proof.

**Originality — PASS, historical priority provisional.** The inspected source by Koch, Pardal, and dos Santos establishes the total-vertex cycle bound for bipartite cacti, so that bound is credited. Akhtar–Philip and Song provide exact general algorithms but do not supply the closed formula or the three simultaneously sharp biclique constraints. Queries for maximum spanning cacti, edge deletion on complete bipartite graphs, cyclic rank, and related wording returned no stronger theorem covering the claimed complete family. The exact same conclusion might exist in unindexed literature; no uniqueness or independent priority certification is asserted.

**Mathematical value — PASS.** Complete bipartite graphs are a canonical dense subclass of a problem proved hard even on bipartite inputs. The theorem determines the full two-parameter edge-deletion distance, separates three structural bottlenecks, and gives a linear-size optimal witness in every regime. It is more than the universal four-cycle bound or an instance recomputation, and can serve as an exact benchmark for cactus-deletion algorithms.

**Limitations.** The result is unweighted, does not enumerate every optimizer, and does not extend to arbitrary bipartite graphs. The source comparisons do not exclude all unindexed work. Computations do not certify the infinite proof.

Self-review: passed. Independent audit: not yet performed.
