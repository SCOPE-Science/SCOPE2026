# Exact Markov fiber diameters for small-margin 3x3 and 3x4 contingency tables

## Context

Fixed-margin contingency fibers with the Diaconis–Sturmfels 2x2 moves are the
standard testbed for exact conditional-test MCMC in algebraic statistics
(Diaconis–Sturmfels 1998; Aoki 2016 survey). Fiber-graph diameters govern mixing
behaviour, but the literature provides the connectivity theorem and isolated
examples, not a uniform exact diameter table. This record certifies the complete
diameter census for the two smallest nontrivial 2-way windows where full
fiber-by-fiber BFS is feasible.

## Definitions

Fix shape `nr x nc` in {3x3, 3x4}. For ordered margins `(r, c)` with equal total
sum, the fiber is

`F(r,c) = { T in N^(nr x nc) : row sums = r, column sums = c }`.

The move set M is the Diaconis–Sturmfels 2x2 set: for each row pair `i1<i2` and
column pair `j1<j2`, the two signed moves `±(e_{i1j1}+e_{i2j2}-e_{i1j2}-e_{i2j1})`
(9 undirected rectangles / 18 directed moves for 3x3; 18 / 36 for 3x4). Two
tables are adjacent if they differ by one such move with all entries staying
nonnegative. The fiber graph is `(F(r,c), M)`; its diameter is the maximum over
all-pairs shortest-path distances (0 for a singleton fiber).

Scope: all ordered margin pairs with entries in `{0,...,6}` for 3x3 (9331
classes) and `{0,...,4}` for 3x4 (7140 classes).

## Result

1. Every fiber in scope is connected under M (0 disconnected of 9331 + 7140),
   proved per fiber by BFS, and every listed diameter is exact by all-pairs BFS.
2. Diameter distributions (margin classes per diameter):
   - 3x3: 0:445, 1:969, 2:1411, 3:1668, 4:1687, 5:1383, 6:889, 7:489, 8:241,
     9:102, 10:37, 11:9, 12:1.
   - 3x4: 0:296, 1:840, 2:1420, 3:1714, 4:1405, 5:850, 6:437, 7:156, 8:22.
3. 3x3 maximum: unique class `r=(6,6,6), c=(6,6,6)`, fiber size 406, diameter 12,
   with endpoints `A=[[0,0,6],[0,6,0],[6,0,0]]`, `B=[[0,6,0],[6,0,0],[0,0,6]]`
   and an explicit 13-table shortest path (DRAFT section 3; `census_3x3.json`
   `maxinfo.path`).
4. 3x4 maximum diameter 8, attained on exactly 22 classes (all with `r` a
   permutation of `(4,4,4)`; sizes 120 x4, 255 x12, 312 x6). Exhibited witness:
   `r=(4,4,4), c=(0,4,4,4)`, size 120, diameter 8, endpoints
   `A=[[0,0,0,4],[0,0,4,0],[0,4,0,0]]`, `B=[[0,0,4,0],[0,4,0,0],[0,0,0,4]]`
   with an explicit 9-table shortest path. Largest 3x4 fiber is the uniform
   class `r=(4,4,4), c=(3,3,3,3)`, size 415, diameter 6.
5. Per-class rows `(r, c, |F|, diam)` are tabulated in `table_3x3.csv` and
   `table_3x4.csv`.

## Proof / evidence

Finite exhaustive proof, not heuristic sampling:

- `census.py` enumerates every ordered margin class, enumerates each fiber by
  pruned cell recursion, builds the fiber graph with M, and computes
  connectivity plus exact diameter by all-pairs BFS; the maximal fiber's
  endpoint pair and one shortest path are stored.
- `verify.py` (independent enumerator: product of row compositions filtered by
  column sums; independently rebuilt move set and BFS) replays: margin validity
  of every path table (V1), single-rectangle 2x2 geometry of every step (V2),
  path length equals claimed diameter and is shortest with BFS covering the
  whole fiber, i.e. connectivity (V3/V4), fiber-size agreement, spot diameters
  including `(6,6,6)x(6,6,6)->(406,12)` and `(4,4,4)x(3,3,3,3)->(415,6)` (V5),
  and CSV/histogram totals (V6). Output: `VERIFY_OK sizes=(406,120)
  diams=(12,8)`.
- Auditor independently recomputed: 30 random size<=60 classes, all 47 3x3
  classes with diameter >= 10, all four size-120 diameter-8 3x4 classes, one
  representative each of the diameter-8 size-255/312 groups, and the 415-size
  class — all match the tables exactly with a separately written enumerator,
  move builder, and BFS.

The classical theorem that 2x2 moves connect every 2-way fiber is cited as
prior art; connectivity here is proved per fiber by BFS, not by appeal to it.
No minimality of the move set is claimed.

## Limitations

- Bounded scope only: margins `0..6` (3x3) and `0..4` (3x4). No general
  diameter formula and no claim for larger margins.
- Ordered margin classes are enumerated (row/column permutations count
  separately); the CSV encodes margins as digit strings.
- Correctness rests on two agreeing stdlib scripts; a shared definitional
  misreading of adjacency is mitigated by per-step geometry assertions and
  agreement with the classical theorem, but is the residual common-mode risk.

## Reproducibility

In `output/artifacts/`: `census.py` regenerates everything
(`python3 census.py`, ~15 s stdlib only); `table_3x3.csv` (9331 rows),
`table_3x4.csv` (7140 rows); `census_3x3.json`, `census_3x4.json` (summaries +
maximal witnesses); `verify.py` replays
(`python3 verify.py` -> `VERIFY_OK sizes=(406,120) diams=(12,8)`).

## References (prior art)

- P. Diaconis & B. Sturmfels, Algebraic algorithms for sampling from
  conditional distributions, Ann. Statist. 26 (1998). Foundational
  Markov-basis connectivity theorem.
- S. Aoki, An introduction to computational algebraic statistics (2016),
  arXiv:1607.07600. Survey with Macaulay2/R examples.
- H. Hara, S. Aoki, A. Takemura, Running Markov chain without Markov basis
  (2011), arXiv:1109.0078. Motivation for small-model certified censuses.
- The Markov Bases Database, https://markov-bases.de/ (298 entries: bare
  bases/counts, no fiber-diameter table or witness).
