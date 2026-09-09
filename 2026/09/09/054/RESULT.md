# Positive linear Turán density window for the 4-uniform Fano-plane expansion

## Context

Exact Turán densities for Fano-type configurations are a recognized frontier
since de Caen/Sós and Keevash. The 3-uniform Fano number is settled
(Keevash–Sudakov; explicit stability Hoppen–Lefmann–Odermann), and expansion
densities are known for complete 2-graphs (Mubayi program; Pikhurko), but no
density window was recorded for the 4-uniform linear expansion of the Fano
plane. This record certifies the first explicit positive-density
(non-degeneracy) window for that object.

## Definitions

- Let `F` be the Fano plane: 3-graph on `{0,...,6}` with the 7 triples of
  STS(7):
  `(0,1,2),(0,3,4),(0,5,6),(1,3,5),(1,4,6),(2,3,6),(2,4,5)`,
  covering each of `C(7,2)=21` pairs exactly once.
- Let `F+` be its 4-uniform linear expansion: `V(F+)` = 7 core vertices plus
  7 private vertices `7+i` (`i=0..6`); `E(F+)` = 7 quadruples
  `triple_i ∪ {7+i}` on 14 vertices. `F+` is linear and every two distinct
  edges meet in exactly one (core) vertex.
- Let `ex_lin(n,F+)` be the maximum number of edges in a linear 4-graph
  (any two edges share at most one vertex) on `n` vertices with no
  subhypergraph isomorphic to `F+`.

## Result

`1/144 ≤ liminf ex_lin(n,F+)/n² ≤ limsup ≤ 1/12.`

Finite-`n` form, for every `n`:

`ex_lin(n,F+) ≥ n²/144 − n/12 − 1/2187` and `≤ n(n−1)/12.`

In particular `F+` is non-degenerate in the linear 4-uniform setting
(positive asymptotic density), with first explicit constants on both sides.

## Proof / evidence

**Upper bound 1/12.** Each edge of a linear 4-graph covers `C(4,2)=6` pairs
with disjoint pair-sets across edges, so `6·e(H) ≤ C(n,2)`,
`e(H) ≤ n(n−1)/12`, hence limsup `≤ 1/12`. Independent of `F+`.

**Conflict-pair lemma.** Let `N_conf(n)` count unordered pairs of distinct
4-sets on `[n]` sharing `≥ 2` points. For each 2-set `S` there are
`C(n−2,2)` quads containing `S`, hence at most `C(n−2,2)²/2` pairs sharing
(at least) `S`; summing over `C(n,2)` choices of `S` counts every conflicting
pair at least once, so `N_conf(n) ≤ C(n,2)·C(n−2,2)²/2 ≤ n⁶/16`.
Exact values at `n=7..12` (`525,1820,5040,11970,25410,49500`) are
machine-checked below the bound.

**Lower bound (optimized alteration).** Take `G ∼ G^(4)(n,p)` with
`p=α/n²`. Let `X=e(G)`, `Y` = number of conflicting edge-pairs in `G`,
`Z` = number of `F+`-copies in `G` (labelled 7-edge subhypergraphs, bounded
by injective placements). Then `EX=C(n,4)·p`,
`EY ≤ N_conf(n)·p² ≤ α²n²/16`, `EZ ≤ n¹⁴·p⁷=α⁷`.
Deleting one edge per conflicting pair and per `F+`-copy leaves a linear
`F+`-free 4-graph `H` with `e(H) ≥ X−Y−Z`, so
`E[e(H)] ≥ C(n,4)·p − n⁶p²/16 − n¹⁴p⁷`.
With `C(n,4) ≥ (n⁴−6n³)/24`,
`E[e(H)] ≥ n²(α/24−α²/16) − αn/4 − α⁷`.
The bracket is `α/24−α²/16 = 1/144−(α−1/3)²/16`, maximized at `α=1/3`
with value `1/144`. At `α=1/3`, `E[e(H)] ≥ n²/144−n/12−1/2187`, so some
`H` attains this. This gives the finite-`n` bound and
liminf `≥ 1/144`.

**Machine verification** (`python3 output/artifacts/verify.py` → `VERIFY_OK`,
stdlib only): STS(7) pair cover; `F+` certificate (7 edges, 14 vertices,
linear, pairwise intersections exactly 1); planted detection/count
(exactly 1); exact `N_conf(n) ≤ n⁶/16` for `n=7..12`; exact rational
optimizer identity; seeded `n=60` alteration demo producing a certified
linear `F+`-free 29-edge hypergraph above the floor (19 edges).

## Limitations

- Window has gap factor 12 (`1/144` vs `1/12`); the exact density
  `π_lin(F+)`, the conjectured value `c*=1/12`, and any
  stability/uniqueness-gap statement are NOT proved.
- No container or supersaturation inequality above `c*` is claimed.
- Existence of the limit `lim ex_lin(n,F+)/n²` is not established; only the
  stated liminf/limsup window.
- The `n=60` demo is illustration, not proof; its `F+`-freeness relies on
  the `find_Fplus` detector whose general completeness is unproved.

## Reproducibility

Run `python3 output/artifacts/verify.py` (Python standard library only;
expected `VERIFY_OK`). Sources: `output/artifacts/fano.py` (Fano/expansion
objects, linearity, detector), `output/artifacts/fcount.py` (exact counter),
`output/artifacts/verify.py` (all checks).

## References

- Bellmann–Reiher, Turán's Theorem for the Fano plane.
  https://arxiv.org/abs/1804.07673
- Hoppen–Lefmann–Odermann, A note on a stability result for the Fano plane.
  https://arxiv.org/abs/2004.11828
- Saxton–Thomason, Hypergraph containers. https://arxiv.org/abs/1204.6595
- Pikhurko, Exact Computation of the Hypergraph Turan Function for Expanded
  Complete 2-Graphs. https://arxiv.org/abs/math/0510227
- She–Fan–Kang–Hou, Linear spectral Turán problems for expansions of graphs
  with given chromatic number. https://arxiv.org/abs/2211.13647
- Gyárfás–Sarkozy, Turán and Ramsey numbers in linear triple systems.
  https://arxiv.org/abs/2011.13678
- Hou et al., A step towards a general density Corradi–Hajnal Theorem.
  https://arxiv.org/abs/2302.09849
