# Exact mate-stratum deficit boundary for the fixed Egan–Wanless order-10 pair

## Context

Whether three mutually orthogonal Latin squares of order 10 exist
(3-MOLS(10)) is the flagship open case of the MOLS existence program
(Euler and Tarry through Parker–Bose–Shrikhande to the Handbook
maxMOLS tables). Egan–Wanless (arXiv:1406.3681v2) closed the mates and
MOLS classification for n ≤ 9 yet offered only a closest-so-far triple
at order 10. Order 10 is therefore the natural minimal open triple
case. Moore finite-field complete sets do not apply (10 is not a prime
power), and no exhaustive order-10 triple classification exists.

## Definitions

- A Latin square of order 10 uses symbols 0–9, each once per row/column.
- X ⊥ Y means orthogonal: the 100 ordered pairs (X[i][j],Y[i][j]) are
  all distinct.
- A transversal of X is 10 cells, one per row/column/symbol.
  A 1-partition (mate) of X is a partition of its 100 cells into 10
  disjoint transversals, equivalently an orthogonal mate C ⊥ X whose
  symbols label the 10 transversals.
- Fix (A,B) = first two squares of the published Egan–Wanless §8
  closest-to-MOLS order-10 triple (explicit arrays in
  `artifacts/squares.json`, pair sha256
  `d54e15c9ccef6ae7260a6589660adb052e0dedd427128c1edc8dae9156d5976`).
- Baseline: |AB| = 100, |AC_pub| = 100, |BC_pub| = 91, so published
  deficit D0 = (100−|AB|)+(100−|AC|)+(100−|BC|) = 0+0+9 = 9.
- For a mate C ⊥ A, D = 100−|BC|; for C ⊥ B, D = 100−|AC|.

## Fixed objects

A, B, C_pub row strings (symbols 0–9) as in `artifacts/squares.json`:

- A = ["0897564231","9146273805","7425138690","8653921047","6218409573",
  "4932750168","5371086924","3509842716","1760395482","2084617359"]
- B = ["0789123456","9061832547","7204391865","8530217694","6953074218",
  "4176508932","5428960371","3617485029","1842659703","2395746180"]
- C_pub = ["0789123456","6428951370","4953276018","5176438902",
  "3290715684","1037682549","2801349765","9542860137","7365094821",
  "8614507293"]

All three are Latin (checked). A ⊥ B and A ⊥ C_pub.

## Result

1. **Mates of A:** A has exactly 1080 transversals and 305
   1-partitions (mates). Over all mates C ⊥ A, the other-pair deficit
   100−|BC| has exact distribution
   {9:1, 12:3, 15:3, 18:4, 21:6, 24:21, 27:30, 30:36, 33:42, 34:9,
   36:34, 39:45, 42:27, 45:31, 48:6, 78:6, 90:1}.
   Minimum 9, attained by a unique partition. Hence no C ⊥ A beats
   D0 = 9.
2. **Mates of B:** B has exactly 932 transversals and 5 1-partitions.
   Over all mates C ⊥ B, 100−|AC| has exact distribution
   {24:1, 34:3, 90:1}. Minimum 24, unique. Hence no C ⊥ B beats D0.
3. **Explicit witness C\*** (matches D0, anchors the uniqueness):
   C* = [0123456789, 9752384610, 7386519042, 8419762305, 6530148927,
   4061925873, 5204673198, 3875290461, 1698037254, 2947801536].
   C* is Latin, |AC*| = 100, |BC*| = 91, D* = 9.
   BC* duplicate pairs (each ×2): (1,2),(2,3),(3,1),(4,2),(5,3),
   (6,1),(7,2),(8,3),(9,1).
   C* shares the unlabelled 1-partition of A with C_pub and equals
   C_pub cellwise under symbol permutation
   {0→0,7→1,8→2,9→3,1→4,2→5,3→6,4→7,5→8,6→9}.
   Novelty is the census minima/distributions and uniqueness
   certificates, not a new unlabelled partition.

## Proof / evidence

- `verify.py` (stdlib, O(n²) overlay): certifies Latin checks,
  |AB| = 100, |AC_pub| = 100, |BC_pub| = 91 with full duplicate-pair
  tables, D0 = 9; and C* Latin with D* = 9.
- `mate_census.py` (stdlib): exhaustive row-by-row transversal
  backtracking (bitmask) then exact-cover DFS over 1-partitions with
  other-pair deficit accumulation. Replays in ~23 s total
  (~17 s for A, ~5 s for B). Independently cross-checked with
  reverse-column transversal order and highest-bit DFS cell choice
  plus explicit optimal-mate reconstruction (|BC| = 91, Latin).
- Transversal counts re-verified by independent brute-force DFS:
  1080 (A), 932 (B).

## Limitations

- Optimality is proved only within the two single-mate strata
  (C ⊥ A; C ⊥ B). The joint trade-off region with |AC| < 100 and
  |BC| < 100 simultaneously is not exhaustively searched; a global
  D < 9 third square there is left open.
- No D = 0 triple claimed. C* matches rather than beats D0 = 9.
- No claim that D0 = 9 is a global optimum over all third squares;
  the proved statement is conditional optimality within each mate
  stratum.
- Uniqueness counts 1-partitions (mates up to C-symbol permutation);
  labelled-mate counts differ by symbol relabellings.

## Reproducibility

```
cd output/artifacts
python3 verify.py                        # baseline D0=9 + Latin checks
python3 verify.py --cand candidate.json  # candidate D*=9 + tables
python3 mate_census.py                   # exact census (~25 s total)
```

Stdlib only. Pair sha256 printed by `verify.py`:
d54e15c9ccef6ae7260a6589660adb052e0dedd427128c1edc8dae9156d5976.

## References

- J. Egan, I. M. Wanless, Enumeration of MOLS of small order,
  arXiv:1406.3681.
- D. Donovan, M. J. Grannell, E. Ş. Yazıcı, Embedding partial Latin
  squares in Latin squares with many mutually orthogonal mates,
  arXiv:1811.04625.
- S. Bereg, Computing random r-orthogonal Latin squares,
  arXiv:2311.00992.
- C. Barnoff, C. Bright, Improving SAT Solvers on Orthogonal Latin
  Square Problems, arXiv:2605.02132.
