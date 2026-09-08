# Exact symmetric-exchange diameters of compatible basis pairs in simple rank-3 matroids on ≤8 points

## Context

Let M be a matroid of rank 3 with basis family B. Two ordered basis pairs
P = (A1, A2), Q = (C1, C2) are *compatible* if A1 ∪ A2 = C1 ∪ C2 as multisets.
This is White's basis-sequence formulation (length two): compatibility is
necessary for reachability by symmetric exchanges. Reachability (White's
conjecture) is increasingly settled — paving matroids (Yu–Yuen), split
matroids with a polynomial shortest-sequence algorithm and the general bound
min{r, r − |A1 ∩ C1| + 1} (Bérczi–Schwarcz) — but exact shortest-path distances
are NP-hard to approximate within c log n in general (Hanaka et al.), so exact
small-scope distance ground truth is needed to calibrate routing algorithms
and toric-quadric rewriting bounds. No prior source tabulates exact
symmetric-exchange diameters or extremal basis pairs for rank-3 matroids.

## Definitions

A *symmetric single-element exchange* replaces, for x ∈ A1, y ∈ A2,
P = (A1, A2) ↦ (A1 − x + y, A2 − y + x),
requiring both outcomes to be bases (a no-op move is not an edge).
The *exchange graph* has ordered compatible pairs as vertices in each
multiset-union class and these exchanges as edges; distance is BFS distance,
and the *diameter* of M is the maximum distance over all classes.
Dm is the maximum diameter over all simple rank-3 matroids on m points;
D* is the global maximum over m ≤ 8. Pairs are ordered throughout.

## Result

**Lemma (rank-3 diameter bound, proved).** Every matroid of rank exactly 3 on
any ground set has connected ordered compatible-pair exchange graphs of
diameter at most 3.

**Theorem (exact spectrum on m ≤ 8 points, simple rank 3).**
D3 = 0, D4 = 1, D5 = 2, D6 = D7 = D8 = 3,
so the global maximum over the whole window is D* = 3.

**Extremal witnesses (all at distance exactly 3, shortest paths logged).**
- U(3,6): P = ({0,1,2},{3,4,5}) → Q = ({3,4,5},{0,1,2}) (disjoint swap),
  path ((012),(345)) → ((123),(045)) → ((234),(015)) → ((345),(012)).
- U(3,7), U(3,8): same labelled pair, BFS distance exactly 3 (same path,
  valid in the restriction and the full matroid).
- Fano matroid F7 (non-uniform extremal): same pair at BFS distance 3,
  e.g. ((012),(345)) → ((125),(034)) → ((135),(024)) → ((345),(012)).
- Every m = 6 simple type except the near-pencil (line [1,2,3,4,5]) attains
  diameter 3 (8 of 9 types); full per-type table below.

**Per-type diameter census (m ≤ 6 complete; m = 7, 8 via the Lemma).**
m = 3: 1 type, D = 0. m = 4: 2 types, diameters {1,1}, D4 = 1.
m = 5: 4 types, all diameter 2, D5 = 2.
m = 6: 9 types; near-pencil (line [1,2,3,4,5]) diameter 2, other eight
diameter 3, so D6 = 3. Restriction argument extends D7 = D8 = 3 without
enumerating all ~68 8-point types.

| m | lines | |B| | diam | witness |
|---|---|---|---|---|
| 3 | [] | 1 | 0 | — |
| 4 | [1,2,3] | 3 | 1 | ((012),(013))→((013),(012)) |
| 4 | [] | 4 | 1 | same |
| 5 | [1,2,3,4] | 6 | 2 | ((012),(034))⇝((034),(012)) |
| 5 | [2,3,4] | 9 | 2 | same shape |
| 5 | [] | 10 | 2 | same shape |
| 5 | [0,3,4],[1,2,4] | 8 | 2 | ((012),(134))⇝((134),(012)) |
| 6 | [1,2,3,4,5] | 10 | 2 | ((012),(034))⇝((034),(012)) |
| 6 | [2,3,4,5] | 16 | 3 | ((023),(145))⇝((145),(023)) |
| 6 | [3,4,5] | 19 | 3 | ((013),(245))⇝((245),(013)) |
| 6 | [] | 20 | 3 | ((012),(345))⇝((345),(012)) |
| 6 | [1,4,5],[2,3,5] | 18 | 3 | ((012),(345))⇝((345),(012)) |
| 6 | [0,4,5],[1,3,5],[2,3,4] | 17 | 3 | same |
| 6 | [0,4,5],[1,2,3] | 18 | 3 | same |
| 6 | [0,1,2,5],[3,4,5] | 15 | 3 | ((013),(245))⇝((245),(013)) |
| 6 | [0,2,5],[0,3,4],[1,2,4],[1,3,5] | 16 | 3 | ((012),(345))⇝((345),(012)) |

Representatives by nontrivial lines (rank-2 flats of size ≥ 3); [] = uniform.
Full shortest paths stored in output/artifacts/census_m3_m6.json.

## Proof / evidence

Lemma: let P, Q be compatible with support T (|T| ≤ 6). Both are bases of the
restriction M|T (rank exactly 3, loops/parallel allowed), and the pair-graph
coincides with that in M. Hence it suffices to check all rank-3 triple
families on fixed ground set [6]: C(6,3) = 20 triples, 2^20 = 1,048,576
families; filtering by the basis exchange axiom and excluding the empty family
leaves exactly 2053 nonempty rank-3 families. For each, every
multiset-union class of ordered basis pairs was built with exact symmetric
exchange adjacency and BFS from every vertex: every class connected, every
diameter ≤ 3, maximum 3 attained (901 families). Runs ~7 s in pure Python
(output/artifacts/lemma_check.py).

Census m ≤ 6: simple rank-3 matroids encoded by nontrivial line families F of
subsets of size ≥ 3 with pairwise intersections ≤ 1; bases are triples in no
member. Backtracking enumeration plus brute-force Sm canonical dedup gives
labeled families 1/5/31/352 and types 1/2/4/9 (classical sequence; verifier
recomputes them). Pair-graph BFS per type gives D3..D6 = 0,1,2,3.

Orders m = 7, 8: Dm ≤ 3 by the Lemma. Lower bound from U(3,m), m ≥ 6, with the
disjoint-swap pair P = ({0,1,2},{3,4,5}), Q = ({3,4,5},{0,1,2}): each exchange
moves exactly one element across, so ≥ 3 moves needed; the displayed 3-step
path shows 3 suffice; direct BFS confirms distance exactly 3. Hence D7 = D8 = 3
at the uniform matroid; Fano gives a non-uniform attainer at m = 7.

Independent stdlib verifier (output/artifacts/verify.py) recomputes type
counts and Dm, edge-checks all stored paths, BFS-replays U(3,7)/U(3,8)/Fano
witnesses, and replays the Lemma finite check: all checks pass.

## Limitations

- The Lemma's finite half is computer-verified (2053 families), not
  hand-checked; program is short, bitmask-exact, shipped and replayed.
- Census isomorphism rejection is brute-force Sm canonical minimum (m! ≤ 720),
  feasible here but not a general method.
- No enumeration of all types at m = 7, 8; only D7 = D8 = 3 is claimed (Lemma
  upper bound plus uniform witnesses). Which 8-point types attain 3 beyond the
  uniform matroid is not classified.
- Ordered (not unordered) pairs per White's formulation; unordered diameters
  would be ≤ these values.

## Reproducibility

Stdlib Python only. Artifacts: output/artifacts/census_m3_m6.json (all types +
witnesses + paths), output/artifacts/lemma_check.py (2^20 enumeration + BFS),
output/artifacts/verify.py (independent replay). Re-run: python3
output/artifacts/lemma_check.py (~7 s); python3 output/artifacts/verify.py
with output/ as working directory context (paths output/artifacts/...).

## References

- Yu–Yuen, White's Conjecture for Paving Matroids, arXiv:2510.04163
  (reachability only, no distances).
- Bérczi–Schwarcz, Exchange distance of basis pairs in split matroids,
  arXiv:2203.01779 (bound min{r,r−|A1∩B1|+1} + algorithm; no D_m spectrum).
- Bérczi–Mátravölgyi–Schwarcz, Reconfiguration of basis pairs in regular
  matroids, arXiv:2311.07130 (different class, asymptotic bound).
- Hanaka et al., Basis sequence reconfiguration in the union of matroids,
  arXiv:2409.07848 (reachability polynomial; shortest c log n-hard).
