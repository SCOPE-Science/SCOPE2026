# SPLIT verdict for the separable length-6 Wilf cell Av(2413,3142,123654) vs Av(2413,3142,321654)

## Context

Let U = Av(2413,3142) be the separable permutations (large Schröder numbers:
1, 2, 6, 22, 90, 394, 1806, 8558, 41586, 206098, 1037718, 5293446).
Wilf-equivalence of finitely based length-6 subclasses inside U is an open
classification boundary: length-4 pair classifications are settled while named
length-6 cells remain benchmarks for universality-vs-splitting. The admitted
target asked whether C1 = Av(2413,3142,123654) and C2 = Av(2413,3142,321654)
merge (Wilf-equivalent with bijection and shared growth rate) or split.

## Definitions

- Pattern containment is classical (not necessarily consecutive).
- U = Av(2413,3142). C1 = Av(2413,3142,123654). C2 = Av(2413,3142,321654).
- |C_n| denotes the count of length-n members. C1, C2 are Wilf-equivalent iff
  |C1_n| = |C2_n| for all n.
- Both forbidden length-6 patterns lie in U in disjoint dihedral/inverse
  symmetry orbits (sizes 4 and 2), so non-equivalence is not a symmetry
  tautology. Both contain 132 while avoiding 231, so the
  Albert–Atkinson–Vatter rationality theorem (subclasses of separables not
  containing Av(231) or a symmetry) does not cover these classes.

## Result

C1 and C2 are **not** Wilf-equivalent. They first separate at n = 7, the
earliest index at which length-6 constraints can bite:

| n  | 1 | 2 | 3 | 4 | 5 | 6   | 7    | 8    | 9     | 10     | 11     | 12      |
|----|---|---|---|---|---|-----|------|------|-------|--------|--------|---------|
| U  | 1 | 2 | 6 | 22| 90| 394 | 1806 | 8558 | 41586 | 206098 |1037718 | 5293446 |
| C1 | 1 | 2 | 6 | 22| 90| 393 | 1781 | 8224 | 38311 | 179263 | 841254 |3958066 |
| C2 | 1 | 2 | 6 | 22| 90| 393 | 1785 | 8308 | 39314 | 188371 | 911785 |4451744 |

Gaps C2−C1 at n = 7..12: 4, 84, 1003, 9108, 70531, 493678.
At n = 6 exactly the two forbidden singletons are removed (agreement
393 = 394 − 1 each side), so n = 7 is the first possible and actual
separating index.

Minimal two-sided witnesses (n = 7):

- (4,3,2,7,6,5,1) is separable, avoids 123654, contains 321654 → in C1 ∖ C2.
- (2,3,4,7,6,5,1) is separable, contains 123654, avoids 321654 → in C2 ∖ C1.

Full n = 7 census: |C1 ∖ C2| = 21 and |C2 ∖ C1| = 25 (both directions
nonempty). Higher witnesses (n = 8, 9, 10, both sides) are listed in the
counting log and verified.

## Proof / evidence

Machine-verified finite certificate, replayable from deposited scripts:

- **Engine A (brute force, `brute.py`):** enumerates full S_n for n ≤ 8 with
  direct pattern matching; no insertion logic. Gives U/C1/C2 exactly through
  n = 8, including the decisive 1781 vs 1785 at n = 7.
- **Engine B (C max-insertion, `enum.c` / `enum_seq`):** DFS over the
  max-insertion tree. New 2413/3142 through the new maximum detected by finite
  scan; new 123654/321654 through the new maximum (which must sit 4th in the
  occurrence) detected by the exact test min-triple-max < max-pair-min.
  Counts to n = 12; U matches the large Schröder numbers throughout.
- **Engine C (Python insertion, direct checks, `third_engine.py`):**
  max-insertion tree with full re-matching at every node (shares no filter
  code with B). Agrees with A and B through n = 9.
- **Filter fuzz (`thit_test.py`):** exact incremental T-test vs brute force
  on 5000 random insertions: 0 mismatches.
- **Witness/difference census (`verify_witnesses.py` → VERIFY: OK):** uses
  only full pattern matching on explicit permutations — every witness and the
  n = 6 / n = 7 difference census is hand-checkable.
- **Orbit check (`orbit_check.py`):** both patterns in U, disjoint orbits.
- Auditor independently re-ran all Python checks, reproduced the brute-force
  vectors to n = 8, ran the prebuilt binary through n = 12, and rebuilt
  `enum.c` from source with gcc reproducing identical counts.

What is proved vs observed: non-Wilf-equivalence with minimal index n = 7,
two-sided witnesses, and exact vectors (n ≤ 8 by two engines, n ≤ 9 by three
engines, n ≤ 12 by Engine B anchored to Schröder numbers) are proved
(machine-verified, replayable). The widening gap and successive ratios are
observed only — no growth-rate separation is claimed.

## Limitations

- Machine-verified finite computation, not a hand proof; replay requires
  running the deposited scripts.
- Terms n = 10..12 of the census rest on Engine B alone (Engine C cross-check
  reaches n = 9; Engine A reaches n = 8); the decisive n = 7 refutation is
  triple-verified.
- No growth-rate separation is claimed: gap/ratios are empirical observations
  only.

## Reproducibility

See `artifacts/REPLAY.md`. One-command checks (stdlib-only Python except for
optional rebuild of `enum_seq`):

- `python3 orbit_check.py`
- `python3 thit_test.py` → `done, mismatches: 0`
- `python3 verify_witnesses.py` → `VERIFY: OK`
- `python3 brute.py` → `n=7: U=1806 C1=1781 C2=1785`, `n=8: U=8558 C1=8224 C2=8308`
- `./enum_seq 12` (source `enum.c`; rebuild with `gcc -O2 -o enum_seq enum.c`)
- `python3 third_engine.py` (cross-check to n = 9)

## References

- M. Albert, S. Linton, N. Ruškuc, The Insertion Encoding of Permutations
  (2005). https://doi.org/10.37236/1944 — method framework only.
- M. Albert, M. Atkinson, V. Vatter, Subclasses of the Separable
  Permutations (2011). https://arxiv.org/abs/1007.1014 — rationality theorem
  provably inapplicable here (both classes contain Av(132)).
- I. Le, Wilf Classes of Pairs of Permutations of Length 4.
  https://doi.org/10.37236/1922 — length-4 pairs only.
- Gil, Lopez, Weiner (2026), whole-universe U refinements recovering
  Schröder enumeration. https://doi.org/10.48550/arxiv.2603.25528
- PermPAL database, https://permpal.com/ — no entry for either basis.
