# Certified non-stability witness pair for Fano-free linear 3-graphs at density one (v0 = 63)

## Context

For linear 3-uniform hypergraphs let `rho(G) = 6e(G)/n^2`.
Pair counting gives `e <= n(n-1)/6`. Bohman–Warnke (arXiv:1808.01065)
produce partial Steiner triple systems with `(1/6-o(1))n^2` triples and
arbitrary fixed girth, hence the linear-host Fano density `pi_L(F_7) = 1`.
This density fact is background, not claimed as new. The new content is a
same-vertex-set separation between two near-complete Fano-free regimes,
refuting single-template `o(n^2)`-stability at the exhibited order.

## Definitions

- `V0 = {0,...,62}`, `v0 = 63 = 3 mod 6` (Steiner-admissible, PG(5,2) scale).
- STS bound `M = v0(v0-1)/6 = 651`; allowed defect `2v0 = 126`.
- Linear: every vertex pair lies in at most one triple.
- Fano-free: no 7-vertex / 7-triple Fano-plane subhypergraph.
- Edit distance: `|E(G*) triangle E(H*)|` (symmetric difference of triple sets).
- Success threshold: `v0^2/200 = 19.845`.

## Result (exact preset fallback, completed)

At `v0 = 63` there are two explicit Fano-free linear 3-graphs `G*`, `H*`
on the same `V0`, archived in `output/artifacts/baselines.json`, with:

- `e(G*) = 574`, defect `77 <= 126`, `rho = 0.8677`;
- `e(H*) = 621`, defect `30 <= 126`, `rho = 0.9388`;
- `|E(G*) triangle E(H*)| = 1177 >= 19.845` (factor ~59).

Provenance (labeled exactly): `G*` = random-order greedy maximal
Pasch-free partial STS (seed 20260907; high-girth-regime proxy, Pasch-only
rejection); `H*` = Bose-priority greedy maximal Pasch-free partial STS
(algebraic/weaving-regime proxy; retains 603/651 of the fixed Bose STS
triple set B). `H*` is NOT a certified Prazmowska weave product.

Structural certificate independent of exact counting: with the fixed Bose
STS(63) set `B` (`|B| = 651`, linear, covering all 1953 pairs),
`|G* cap B| = 9`, `|H* cap B| = 603`, so
`symdiff >= 603 - 9 = 594` by set arithmetic (x30 over threshold).

## Proof / evidence (replayable, stdlib only)

```
python3 output/artifacts/pasch_fano_census.py        # must print UNIT_TESTS_OK
python3 output/artifacts/verify2.py output/artifacts/baselines.json   # VERIFY_OK
python3 output/artifacts/skeleton_cert.py output/artifacts/baselines.json  # SKELETON_CERT_OK
```

- `pasch_fano_census.py` unit tests: lone Pasch -> Pasch 1, Fano 0;
  Fano plane -> Fano 1 with 7 Pasch; empty -> 0.
- `verify2.py` at v0=63: linearity OK both; Pasch count 0/0; Fano count 0/0
  direct (vertex-anchored search); defects 77, 30 <= 126;
  symmetric difference 1177 >= 19.845; sort-merge cross-check confirms 1177.
- Fano-freeness rests on direct Fano search (0/0) plus the machine-checked
  lemma that the Fano plane contains the Pasch
  `{(0,1,2),(0,3,4),(1,3,5),(2,4,5)}`, so Pasch-free implies Fano-free.
- Independent audit-time naive census (brute-force third-vertex search and
  independent transversal enumeration) agrees: 0 Pasch, 0 Fano in both lists.
- `skeleton_cert.py` replays Bose-retention arithmetic (594 lower bound)
  and a fixed type-6 flag rule with opposite signs
  (`F(G*) = -0.1271`, `F(H*) = +0.1385`).
- Descriptive distinguishing layer (not part of the binary criterion):
  cherry/variance rule `Var-0.8`: `+0.3429 / -0.2694`;
  Lagrangian link comparison: mean degree `27.333 / 29.571`,
  max-degree bounds `0.2339 / 0.2500`.
- Multi-order support (same greedy rules, independently verified):
  V=39 (211/247, symdiff 444), V=45 (289/330, 597),
  V=57 (471/532, 997), V=69 (696/782, 1454); H* is a full
  Pasch-free STS (defect 0) at 39/45/57/69.

## Limitations

- The infinite-sequence target (`liminf >= 1/200` with `rho -> 1` on both
  sides, asymptotic opposite-sign inequality) is NOT proved; five-order
  ratios (.29–.31) are evidence, not a theorem.
- `G*` is Pasch-free but not C3-free; no high-girth claim is made.
- `H*` is a Bose-order proxy, not a certified weave product.
- The full Bose STS(63) itself contains 126 Pasch copies; only the archived
  greedy `H*` subfamily is Pasch-free. Use archived `H*`, not full `B`.

## Reproducibility

All scripts use Python 3 stdlib only. Construction provenance:
`output/artifacts/build.py`. Archived headline logs:
`output/artifacts/verify2_63.log`, `output/artifacts/skeleton_cert63.log`.

## References

- T. Bohman, L. Warnke, Large girth approximate Steiner triple systems,
  arXiv:1808.01065.
- M. Prazmowska, K. Prazmowski, Operation of weaving partial Steiner
  triple systems, arXiv:1403.4916.
- A. C. H. Ling et al., Construction Techniques for Anti-Pasch Steiner
  Triple Systems (single-regime existence; no paired separation).
- D. DeBiasio, T. Jiang, On the co-degree threshold for the Fano plane
  (adjacent codegree cell).
- Collier-Cartaino, Graber, Jiang, Linear Turan numbers of r-uniform
  linear cycles (adjacent linear-cycles cell).
