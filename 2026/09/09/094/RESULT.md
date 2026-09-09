# Refutation of the sharp hexagon-incidence C8 window: z(63,63;C8) >= 360 > 189

## Context

The admitted target claimed that every C8-free bipartite graph with part
sizes 63+63 has at most 189 edges (z(63,63;C8) = 189), to be proved by a
pre-specified flag-algebra plus spectral even-walk certificate tight on the
split Cayley hexagon H(2) incidence graph (63+63, 189 edges, girth 12).
Bukh–Jiang and He give only asymptotic even-cycle upper bounds; no surveyed
source certifies a sharp (63,63) C8 window.

## Definitions

- Parts `X, Y` with `|X| = |Y| = 63`. Vertices `0–62` left, `63–125` right.
- `z(63,63;C8)` = maximum edges in a C8-free bipartite graph on `(X,Y)`.
- `K(a,b)` = complete bipartite graph; `C8` = 8-cycle as a subgraph
  (not necessarily induced).

## Result

**Theorem.** There exists a C8-free bipartite graph `G` with bipartition
`63+63` and `e(G) = 360`. Hence `z(63,63;C8) >= 360 > 189`: the universal
bound `e(G) <= 189` is false, and no sound certificate of any kind
(flag-algebra, spectral, or otherwise) can prove it. The H(2) incidence
graph is unaffected as a C8-free construction; it is simply not extremal.

**Witness.** Split `X = X1 + X2`, `|X1| = 60`, `|X2| = 3`, and
`Y = Y1 + Y2`, `|Y1| = 3`, `|Y2| = 60`. Let block 1 be `K(60,3)` on
`(X1,Y1)` (180 edges) and block 2 be `K(3,60)` on `(X2,Y2)` (180 edges);
`G` is their disjoint union: `|X| = |Y| = 63`, `e(G) = 360`.
Full edge list: `artifacts/witness_edgelist.txt`.

## Proof / Evidence

Lemma: every cycle in `K(a,b)` alternates sides, so it uses at most
`2·min(a,b)` vertices. Both blocks have `min = 3`, so every cycle in
either block has length at most 6 < 8. A subgraph C8 is connected, hence
lies in one block; neither block contains one, so `G` is C8-free. The
same argument rules out an induced C8: any 8-set hosting a subgraph C8
needs 4+4 vertices per side inside one component whose small side has 3
vertices — impossible.

Closed-form census `#C(2k) in K(m,n) = C(m,k)C(n,k)k!(k-1)!/2`: per block
`#C4 = 5310`, `#C6 = 205320`, `#C8 = 0`; both blocks: 10620 C4, 410640 C6,
0 C8.

Machine corroboration (stdlib-only; proof above is self-sufficient):
`counterexample_check.py` → bipartition 63+63, 360 edges, two 63-vertex
components, structural max-cycle 6/block, orbit-representative C8 DFS 0;
`exhaustive_verify.py` → closed-walk census from all 126 starts:
directed C8 = 0, directed C6 = 4927680 = 410640·12 exactly;
`controls_check.py` → positive control finds C8 in `K(4,4)`, C6
calibration consistent by hand. Auditor independently re-parsed the edge
list (360 unique edges, exact block structure) and re-ran a from-scratch
all-starts DFS (C8 = 0, C6 = 4927680). Exact DP over block partitions
with `min(a,b) ≤ 3` gives block-family optimum 360, so the witness is
best among disjoint-complete-bipartite-block constructions.

## Limitations

- Proved: `z(63,63;C8) ≥ 360` (hence `≠ 189`, `> 189`). The exact value
  of `z(63,63;C8)` is NOT determined; non-block C8-free graphs could push
  it higher. 360 is optimal only within the block family.
- The H(2) parameters are taken from standard generalized-hexagon theory,
  not re-derived; unchallenged and irrelevant to the refutation.
- Preset ER_7 fallback was assessed and deliberately NOT claimed
  (Hoffman ceiling 17 vs exact MIS 15); not part of this result.

## Reproducibility

- `artifacts/witness_edgelist.txt`: all 360 edges (`0–62` / `63–125`).
- `artifacts/counterexample_check.py`, `artifacts/exhaustive_verify.py`,
  `artifacts/controls_check.py`: stdlib-only verification (~1 min).
- `artifacts/counterexample_result.json`,
  `artifacts/exhaustive_result.json`: logged outputs.

## References

- Bukh–Jiang, A bound on the number of edges in graphs without an even
  cycle. https://arxiv.org/abs/1403.1601
- He, New Upper Bound on Extremal Number of Even Cycles.
  https://arxiv.org/abs/2009.04590
- Tait–Timmons, Independent sets in polarity graphs.
  https://arxiv.org/abs/1601.05058
- Peng–Tait–Timmons, On the chromatic number of the Erdős–Rényi
  orthogonal polarity graph. https://arxiv.org/abs/1408.4065
- Lazebnik–Ustimenko–Woldar, A new series of dense graphs of high girth.
  https://arxiv.org/abs/math/9501231
