# Refutation of the 11a1 height-5000 Selmer-moment / high-rank target

## Context
Goldfeld's conjecture and the Poonen–Rains heuristics predict rank and
Selmer distributions in quadratic twist families (in particular, first
moment average \#Sel_2 = 3 in the limit). Certified curve-specific
replayable data points with full descent provenance are scarce. The curve
`E = 11a1 : y^2 + y = x^3 - x^2 - 10x - 20` (conductor 11, minimal
canonical example, torsion Z/5) is the admitted benchmark. The admitted
target to height 5000 was the disjunction: Poonen–Rains first-moment
confirmation `|M_5000 - 3| <= 0.15`, OR one explicit twist with certified
rank >= 4.

## Definitions
- `E_d`: quadratic twist of `E = 11a1` by squarefree `0 < |d| <= 5000`
  (6084 twists), twist convention `Ed = elltwist(E, quaddisc(d))`
  (`d = 1` gives `E` itself; `D = quaddisc(d)`).
- `s(d) = dim_{F_2} Sel_2(E_d/Q)`: exact 2-Selmer dimension (PARI/GP
  2.15.4 `ellrank` full 2-descent semantics `s(d) = r_hi + T_dim + s_sha`).
- `w(d)`: root number of `E_d`.
- `M_5000 = mean_d 2^s(d)`: empirical first moment of `#Sel_2`.
- `r_lo(d) <= rank(E_d(Q)) <= r_hi(d)`: rank bounds; `(r_lo, r_hi) = (3,3)`
  means closed rank 3 with three logged independent points and nonzero
  regulator.

## Result
Let `E = 11a1` and `E_d` as above with `s(d)`, `w(d)`, `M_5000` defined as
above. Then:

1. `M_5000 = 12136/6084 = 3034/1521 = 1.9947403...`, so
   `|M_5000 - 3| = 1.0052597... > 0.15`. The Poonen–Rains first-moment
   confirmation disjunct is **false**.
2. `max_d r_lo(d) = 3`, attained at exactly nine twists
   `d in {-4399, -1799, -1007, -206, 1393, 1766, 2362, 2878, 4582}`,
   each closed `(r_lo, r_hi) = (3, 3)` with three logged independent
   points and nonzero regulator; **no** twist has certified rank >= 4
   (indeed none even has `r_hi >= 4`). The high-rank-witness disjunct is
   **false**.

Hence the admitted target claim
("(moment confirmation) OR (rank >= 4 witness)" over this window) is
**false**. Supporting census data:
`sel_dim: {0: 2106, 1: 3011, 2: 932, 3: 35}` (no `sel_dim >= 4`);
rank pairs `(0,0): 2549, (1,1): 3037, (2,2): 313, (3,3): 9, (0,2): 176`
(closed 5908/6084); parity `(sel_dim - T_dim) mod 2 = (1-w)/2` on
**6084/6084** rows with `T_dim = 0` throughout. The `|d| <= 1500` prefix
(1830 rows) has `M_1500 = 3528/1830 = 588/305 ~= 1.9279`, likewise
refuting `|M - 3| <= 0.15`, with max certified rank 3 at `d = 1393`;
the preset fallback table is subsumed by this 5000-window census.

## Proof / Evidence (computational)
- Full 2-descent on every twist via direct `ellrank(Ed)`: 6084/6084
  success, 0 failures, deterministic byte-identical rerun (as reported;
  pinned engine/scripts cited in draft, not re-executed at audit).
- Auditor independently re-derived from `output/artifacts/T5000.csv`
  with stdlib code: d-set equals exactly all squarefree `0<|d|<=5000`
  (0 missing/extra); `D == quaddisc(d)` on all rows; j-invariant
  constant at the 11a1 value on spot checks; exact moment fraction
  `3034/1521`; max `r_lo = max r_hi = 3` with the exact nine-element
  witness list; coherence `sel_size == 2^sel_dim`,
  `sel_dim == r_hi + T_dim + s_sha`, and 100% parity agreement.
- `verify.py` (stdlib only, no PARI): d-set completeness, moment
  fraction, parity recompute, max-rank scan, exact-rational on-curve
  check of all 1977 logged points against per-twist models, and
  height/regulator positivity (1681/1681 nonzero regulators)
  -> `VERIFY_OK` (reproduced by auditor).
- Cross-checks reported: root numbers 100% parity agreement; analytic
  ranks (`ellanalyticrank`) 25/25 agreement on spots (unlogged);
  torsion `elltors` on every twist (`T_dim = 0`).

## Limitations
- "Rigorous" means exact finite computation through PARI's published
  `ellrank` 2-descent + Cassels-pairing implementation, with the
  cross-checks above. It is not a hand proof and inherits trust in
  PARI/GP 2.15.4 `ellrank`/`ellrootno`/`ellanalyticrank` correctness.
- Rank upper bounds on the 176 `(0,2)` rows rest on the Selmer bound
  plus analytic-rank-0 evidence on samples (not a per-row analytic
  certificate for all 176).
- Point independence beyond logged nonzero regulator determinants was
  not re-proved by a second implementation; saturation (index) was not
  separately certified — only the `r_lo` (>=) direction is claimed,
  which is what the witness disjunct needs.
- No asymptotic claim: this finite window (mean ~= 1.99) does not refute
  the Poonen–Rains *limit* prediction, only the window's
  `|M - 3| <= 0.15` decision as stated.

## Reproducibility
1. Extract the pinned engine per draft (`.deb` retained with research
   outputs; run used `tools/pari-extract/usr/bin/gp -s 512M`).
2. `gp -s 512M output/tools/census5000.gp` -> `output/artifacts/T5000.csv`
   (~33 s as reported; expect `done nok=6084 nfail=0`).
3. `gp -s 512M output/tools/models5000.gp` -> models/heights logs.
4. `python3 output/artifacts/verify.py` -> `VERIFY_OK` (auditor
   reproduced `VERIFY_OK` from the archived artifacts alone).

## References
- Klagsbrun–Mazur–Rubin, Disparity in Selmer ranks of quadratic twists
  of elliptic curves, Annals 2013.
- Poonen–Rains, Random maximal isotropic subspaces and Selmer groups.
- Bhargava–Kane–Lenstra–Poonen–Rains, Modeling the distribution of
  ranks, Selmer groups, and Shafarevich–Tate groups.
- Watkins, Distribution of the 2-Selmer rank under twisting, PMB 2022
  (survey of Heath-Brown / Swinnerton-Dyer / Kane / Smith for
  y^2 = x^3 - x and full-2-torsion families).
- Chao Li, Level raising mod 2 and arbitrary 2-Selmer ranks
  (11a1 as example); Kriz, Goldfeld's conjecture and congruences
  between Heegner points (X0(11) running example).
