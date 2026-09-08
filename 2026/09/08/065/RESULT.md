# Frontier extension and certified non-closure scan for open 5-digit octal games .13337 and .13137

## Context

An octal game `.d1...dk` is a take-and-break heap game. A recognized open
program (Guy–Smith eventual periodicity; Berlekamp–Conway–Guy; Flammenkamp
census) asks for the classification of unsolved octals. The Flammenkamp hub
systematically covers at most 3-place codes `0.???`/`4.???` (plus `0.6111...`,
Grundy, `0.0n7` families); the 5-digit games `.13337` and `.13137` lie outside
that census. Published tables (OEIS A071449 for `.13337`, A071448 for `.13137`)
give Sprague–Grundy values only for `n = 1..10000` with no period/preperiod
formula. Comments pin dependent shifts (`.026`/`.027` = `a(n-2)` of `.13337`;
`.024`/`.025` = `a(n-2)` of `.13137`).

## Definitions

Heap size `n`, `G(0) = 0`. For octal code `.d1 d2 d3 d4 d5` and each `k = 1..5`
with digit `dk`: bit 0 (`dk & 1`): if `n == k`, `0` is reachable; bit 1
(`dk & 2`): if `n > k`, `G(n-k)` is reachable; bit 2 (`dk & 4`): if `n > k`,
`G(a) ^ G(b)` is reachable for all `a + b = n - k`, `a,b >= 1`. Then
`G(n) = mex(reachable)`. Here `.13337` = digits `1,3,3,3,7` and `.13137` =
digits `1,3,1,3,7`; only `k = 5` splits (digit 7 has bit 2 set) in both games.
A heap with `G(n) = 0` is cold (P-position). A candidate eventual period
`(q, p)` (preperiod `q`, period `p`) satisfies window equality
`G(n) = G(n+p)` for all `n` in `[q, N-p]` through table length `N`.

## Result

Through `N = 12000`, computed from scratch from each code's recursion:

1. **Exact tables.** `G(0..12000)` for both games; rows `10001..12000` are 2000
   new values per game beyond the published 10000-tables. Samples:
   `.13337`: `G(10001..10010) = 65,46,40,132,64,42,128,68,11,102`;
   `.13137`: `G(10001..10010) = 28,64,142,16,86,34,67,145,25,83`.
2. **Certified non-closure box.** For every candidate `(q,p)` with `q <= 8000`
   and `p <= 2000` (16,002,000 candidates per game), window equality through
   `N = 12000` fails at an explicit logged first-failing index; witness
   matrices `W[q][p-1]` contain zero closure entries. Latest first failures:
   `.13337`: `n = 8002` at `(7999,348)` (`G(8002)=131`, `G(8350)=128`);
   `.13137`: `n = 8001` at `(8000,125)` (`G(8001)=94`, `G(8126)=174`).
   Hence any eventual period closing within this table has `q > 8000` or
   `p > 2000`. No candidate closed.
3. **Cold censuses on `[0,12000]`.** `.13337` (11): `0,6,20,42,82,88,96,116,
   138,146,1524` (none new in `10001..12000`). `.13137` (18): `0,6,20,56,70,
   106,114,208,324,350,724,1426,1614,1620,1700,4860,6100,11796` (one new cold
   `11796`; reachable set size 240 has minimum 1, so mex is 0).
4. **Extremal.** `.13337`: new overall record nimber **187 at `n = 10736`**
   (prior max through 10000 was 163 at 9975; reachable set size 203 contains
   `0..186` and excludes 187). `.13137`: global max 229 at 7310 stands;
   new-interval maximum 222 at 11579.

## Proof / evidence

- From-scratch compiled-C DP (`artifacts/octal_dp.c`): timestamped-`seen`
  mex, `O(N^2/2)` split pairs via `a <= b` symmetry; no external tables
  ingested. Recompilation and rerun to `N = 12000` reproduces both committed
  tables byte-for-byte.
- OEIS b-file gate: committed tables agree on all 10000 published values per
  game (0 mismatches; `G(10000) = 128` resp. `89`).
- Independent pure-Python from-scratch mex replay agrees on all `0..12000`
  for both games (different loop structure).
- 2000 random witness entries per game re-verified (`f >= q`,
  `G(f) != G(f+p)`, firstness over `[q,f)`); global maxima confirmed by
  argmax (`.13337`: max 8002 in 2 rows; `.13137`: max 8001 in 19 rows).
- Mex transcripts re-derived from committed tables for 187@10736 and cold
  11796 (sizes 203 and 240 as above).

## Limitations

Finite frontier result only: values through 12000; exclusion box as stated;
cold lists on `[0,12000]`. Claims nothing about eventual periodicity beyond
the boxed window, proves no upper bound on nimbers, and does not classify the
dependent shift families beyond anchoring their parent tables.

## Reproducibility

```
gcc -O2 -o octal_dp artifacts/octal_dp.c
./octal_dp 13337 12000 g13337.txt [b071449.txt as gate]
./octal_dp 13137 12000 g13137.txt [b071448.txt as gate]
python3 artifacts/verify.py   # stdlib-only gate + slice replays; prints VERIFY OK
python3 -c "import numpy as np; W=np.load('artifacts/witness_13337.npz')['W']; print((W==-1).sum())"  # 0
```

## References

- OEIS A071449, Sprague-Grundy values for octal game .13337 (table 1..10000).
  https://oeis.org/A071449
- OEIS A071448, Sprague-Grundy values for octal game .13137 (table 1..10000).
  https://oeis.org/A071448
- OEIS b-files b071449.txt / b071448.txt (1..10000). https://oeis.org/A071449/b071449.txt
- A. Flammenkamp, Sprague-Grundy Values of Octal-Games.
  http://wwwhomes.uni-bielefeld.de/achim/octal.html
- E. R. Berlekamp, J. H. Conway, R. K. Guy, Winning Ways, ch. 4.
