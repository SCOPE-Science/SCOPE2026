# Exact small-n hexagon Turán numbers: ex(n,C6) = 13, 16, 20, 21 for n = 7, 8, 9, 10, with certified C6-free witnesses through n = 14

## Context

The even-cycle Turán problem asks for ex(n,C_{2k}), the maximum edges in an
n-vertex simple graph with no 2k-cycle as a (not necessarily induced)
subgraph. For C6 the Bondy–Simonovits / Bukh–Jiang / He machinery gives
ex(n,C6) = Theta(n^{4/3}) asymptotically, but the implied constants do not
determine exact values at small orders. No prior source publishes a closed,
replayable ex(n,C6) table with extremal edge lists for these small orders:
He (2020) gives only an asymptotic upper bound; Győri et al. (2022) treats
large-n generalized counts; Mukherjee (2021) and Conlon (2020) give
asymptotic constructions; Füredi–Simonovits (2013) surveys the frontier
without a small-n table; Backelin (2015) closes a different forbidden
family (girth 5) at n = 40–49.

## Definitions

- Graphs are simple and undirected.
- A C6-subgraph is six distinct vertices v0..v5 with all six cycle edges
  present; chords are allowed (not necessarily induced).
- ex(n,C6) = maximum edge count over C6-free n-vertex graphs.
- Key lemma: adding an edge (a,b) to G creates a C6-subgraph iff a and b
  are already joined in G by a simple path of length exactly 5.

## Result

**Theorem.** ex(7,C6) = 13, ex(8,C6) = 16, ex(9,C6) = 20, ex(10,C6) = 21.

**Certified lower bounds (witnesses, not optimality).**
ex(11,C6) ≥ 23, ex(12,C6) ≥ 26, ex(13,C6) ≥ 30, ex(14,C6) ≥ 31.

Extremal / witness edge lists (vertices 0-based):

- n=7, 13 edges: 01,03,04,05,13,14,15,25,26,34,35,45,56.
- n=8, 16 edges: 01,02,03,05,12,13,14,15,16,17,23,25,35,46,47,67.
- n=9, 20 edges: 01,02,06,08,12,16,18,23,24,25,26,27,28,34,35,37,45,47,57,68.
- n=10, 21 edges: 05,06,07,08,16,23,24,25,29,34,35,39,45,49,56,57,58,59,67,68,78.
- n=11, 23 edges: 01,02,03,08,09,010,18,23,24,25,26,27,29,210,39,310,45,46,47,56,57,67,910.
- n=12, 26 edges: 04,06,07,12,13,15,16,23,25,26,28,29,210,211,35,36,46,47,56,67,89,810,811,910,911,1011.
- n=13, 30 edges: 01,04,07,012,14,17,112,25,26,29,211,37,38,310,311,47,412,56,59,511,69,611,78,710,711,712,810,811,911,1011.
- n=14, 31 edges: 01,02,03,04,08,09,012,013,14,18,113,23,25,26,27,29,210,212,39,312,48,413,56,57,510,67,610,710,813,912,1011.

All eight graphs are C6-free (0 C6-subgraphs) and have girth 3.

## Proof / evidence

Lower bounds: the edge lists above, rechecked by an independent
C(n,6)×60-cycle enumerator (`verify.py`), reporting 0 C6-subgraphs for all
eight (see `verify.log`).

Exactness (upper bounds matching the witnesses for n = 7..10):

- n=7: full edge-branching branch-and-bound (`solver.py`) from the empty
  graph with C6-forcing propagation and cardinality pruning: heuristic LB
  13, BB optimum 13, 49133 nodes, timeout False.
- n=8,9,10: max-degree-split decision search (`solver2.py`). Fix a
  maximum-degree vertex 0 with N(0) = {1,…,d} and cap all degrees at d;
  for target T = LB+1, UNSAT in every feasible d proves ex = LB:
  - n=8: T=17 UNSAT for d=5,6,7; nodes 3975/4683/4335, total 12993.
  - n=9: T=21 UNSAT for d=5,6,7,8; nodes 13657/16679/14529/14935,
    total 59800.
  - n=10: T=22 UNSAT for d=5,6,7,8,9; nodes
    219343/221471/205435/211991/194493, total 1052733.
  - All runs: timeout False. The auditor independently re-ran all four
    closures (including n=10) and reproduced every node count byte-for-byte.

The max-degree fixing is a standard labeled-graph symmetry reduction and
the d-range [ceil(2T/n), min(n−1,T)] is complete here (T > n−1 in all
closed cases, so the cap is n−1). C6-forcing and degree-cap propagation
are monotone-sound; branching is exhaustive.

## Limitations

- Exactness is claimed only for n = 7..10. Values for n = 11..14 are
  certified lower bounds only; the true maxima may be larger (attempted
  n=11 closure with T=24 finished only d=5 before the session budget
  expired).
- Optimality replay is by re-running the committed standard-library
  scripts; no per-node search-tree archive is stored. Only the
  witness-side log is archived.
- Witness extremality means "some extremal graph", not uniqueness or a
  classification; no isomorphism census is claimed.

## Reproducibility

Python 3 standard library only:

1. `python3 output/artifacts/verify.py` — fresh C(n,6)×60 enumeration of
   all witnesses (seconds; expected output in `output/artifacts/verify.log`).
2. `timeout 100 python3 output/artifacts/solver.py 7 90` — closes n=7 (~10 s).
3. `timeout 100 python3 output/artifacts/solver2.py 8 90` — closes n=8 (~10 s).
4. `timeout 200 python3 output/artifacts/solver2.py 9 180` — closes n=9 (~30 s).
5. `timeout 500 python3 output/artifacts/solver2.py 10 480` — closes n=10 (~2 min).

## References

- Z. He, New upper bound on extremal number of even cycles (2020).
  https://arxiv.org/abs/2009.04590
- Z. Füredi, M. Simonovits, The history of degenerate (bipartite)
  extremal graph problems (2013). https://arxiv.org/abs/1306.5167
- E. Győri et al., Exact results for generalized extremal problems
  forbidding an even cycle (2022). https://arxiv.org/abs/2208.02538
- S. Mukherjee, Extremal numbers of hypergraph suspensions of even
  cycles (2021). https://arxiv.org/abs/2101.06743
- D. Conlon, Extremal numbers of cycles revisited (2020).
  https://arxiv.org/abs/2011.11064
- J. Backelin, Sizes of the extremal girth 5 graphs of orders 40–49
  (2015). https://arxiv.org/abs/1511.08128
