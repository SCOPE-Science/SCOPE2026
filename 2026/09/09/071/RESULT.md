# Schreier–Aigner Conjecture 4.1 is unauditable as stated: missing QSPP definition, a=5-column irreproducibility under the natural reading, a=2 formula/predicate inconsistency, and absence of a QSPP LGV determinant

## Context

Schreier-Aigner, *Fully complementary higher dimensional partitions*,
arXiv:2301.12272v1 (28 Jan 2023), proves a generating function for fully
complementary partitions (Theorem 1.1) and equinumerosity of quasi
transpose-complementary plane partitions with symmetric plane partitions
(Theorem 1.2). Section 4 states three conjectures "found by computer
experiments" for new quasi symmetry classes of ordinary plane partitions,
with data in Appendix A. Conjecture 4.1 concerns `qspp(a,c)`, the number of
*quasi symmetric plane partitions* (QSPP) in an `(a,a,c)`-box:

- `qspp(a,c-a) = c*binom(c+a-1,2a-1)*p_a(c)` if `a` even,
- `qspp(a,c-a) = binom(c+a-1,2a-1)*p_a(c)` if `a` odd,

where `p_a(c)` in `Q[c]` is irreducible, even (`p_a(-c)=p_a(c)`), with
small-prime common denominator. Appendix A.1 tabulates `qspp(a,c)` for
`a <= 6, c <= 10` and lists guessed formulas for `1 <= a <= 6`.
The admitted target was to test Conjecture 4.1 at the first unfitted slice
`a=7` via the paper's LGV determinant plus a definitional cross-check, with a
single-cell `qspp(7,7)` two-route agreement fallback.

## Definitions

- Plane partition in an `(a,a,c)`-box: array `(pi_ij)`, `1<=i,j<=a`, with
  `0 <= pi_ij <= c`, weakly decreasing along rows and columns.
- Neighbouring defined classes: QTCPP (Theorem 1.2):
  `pi_ij + pi_{n+1-j,n+1-i} = c` for `i != n+1-j`; QTC2 (Conjecture 4.2):
  transpose-complementary except on the diagonal (`i != j`).
- Section 3.1 QCPP quasi-symmetry: `pi_ij = pi_ji` for `i != 2a+1-j`
  (all off-anti-diagonal pairs).
- Reconstruction **D2** (the unique natural transfer of Section 3.1 to
  ordinary plane partitions): symmetric except possibly on the anti-diagonal,
  `pi_ij = pi_ji` for all `i+j != a+1` (1-indexed).
- Reconstruction **D1** (alternative): symmetric except on the main diagonal,
  `pi_ij = pi_ji` for all `i != j`.

## Result

1. **QSPP is undefined in the paper.** Section 4 gives no defining equation
   for "quasi symmetric plane partition". The only defined neighbours are
   QTCPP and QTC2 above; the closest defined analog is Section 3.1 QCPP
   quasi-symmetry, whose transfer is D2.
2. **Under D2, the paper's a=5 column is irreproducible — exact gaps.**
   Exact backtracking enumeration under D2 (MacMahon-validated engine:
   all plane partitions in `(5,5,3)` = 731808) agrees with every probed
   Appendix-A.1 cell for `a in {1,3,4,6}` (e.g. `(2,2)=20`, `(3,3)=272`,
   `(4,3)=3052`, `(3,4)=846`, `(6,1)=164`) but strictly exceeds the
   table/formula at every probed `a=5` cell with height `h >= 1`:

   | cell (a,h) | D2 exact | paper table = formula(C=h+5) |
   |---|---|---|
   | (5,1) | 64 | 60 |
   | (5,2) | 1442 | 1312 |
   | (5,3) | 18544 | 16572 |
   | (5,4) | 164686 | 145428 |
   | (5,5) | 1118080 | 979068 |

   Formulas evaluated in exact rational arithmetic, so no rounding is
   involved. D1 fails everywhere probed (e.g. `(2,2)`: 10 vs 20), so D2 is
   the unique natural reading — and it still fails exactly at `a=5`.
3. **Supporting numerology (not a universal proof).** At `(5,1)` there are 252
   plane partitions; full-symmetric count 32, D1 32, D2 64 — none gives 60.
   The candidate's broader scan over symmetric-pair exemption predicates found
   ad-hoc predicates hitting 60 at `(5,1)` but none reproducing `(5,2)=1312`;
   that scan log was not forwarded to the auditor, so this is reported as
   documented numerology supporting, not proving, the "no natural
   symmetry-exception repairs a=5" reading.
4. **The printed a=2 formula forces `p_2 = 1/2`, contradicting
   "irreducible".** The Appendix formula `qspp(2,c-2) = c*binom(c+1,3)`
   (identical in HTML and PDF) yields exactly twice the table values at all
   tested cells (`(2,1)`: 12/6, `(2,2)`: 40/20, `(2,3)`: 100/50), so the
   fitted even polynomial is the constant `1/2` — a unit of `Q[c]`, not an
   irreducible polynomial. A dropped `/2` typo would itself confirm the
   empirical basis needs correction.
5. **No QSPP LGV determinant exists in the paper.** Equations (4.4)–(4.6) count
   the Theorem-1.2 QTCPP class via Lindström–Gessel–Viennot plus
   Krattenthaler Eq. (3.13). Hence neither the target nor the fallback
   LGV-vs-definitional agreement criterion has a citable referent as written.
6. **Conditional first anchors under D2 (replayable):** `qspp_D2(7,0)=1`,
   `qspp_D2(7,1)=328`, `qspp_D2(7,2)=29297`.

**Consequence.** The target verdict (verify/refute Conjecture 4.1 at `a=7` via
the paper's LGV determinant plus definitional cross-check) is not auditable as
specified, and the same defect blocks the fallback criterion as written
(it demands an archived LGV matrix for cell (7,7) that does not exist). Any
`p_7` fit-test today would test the prover's own invented class. The finding
redirects the FCP programme to first defining QSPP (and publishing the
enumeration program), after which the `a=7` test — with the conditional
anchors above — can run.

## Proof / evidence

- `output/artifacts/verify.py` (stdlib only) + `output/artifacts/enum_qspp.py`.
  Run from `output/artifacts/`: `python3 verify.py` → `VERIFY_OK`
  (~1.3 s in audit): V1 engine-vs-MacMahon; V2 five D2-vs-table agreements;
  V2b/V2c the `a=5` gaps (both D2 counts and exact-`Fraction` formula values);
  V3 the `a=2` factor 2 at three heights; V4 the three `a=7` D2 anchors.
- Auditor independently recomputed: MacMahon `(5,5,3)=731808` via the product
  formula; `F5(C)` for `C=6..10` → 60, 1312, 16572, 145428, 979068;
  `F2` → 12, 40, 100 (= 2× table); and a separate generate-then-filter
  counter confirming total/D2 = 20/20 at `(2,2)`, 980/272 at `(3,3)`,
  252/64 at `(5,1)`, 3432/328 at `(7,1)`.
- Paper-text audit of arXiv HTML v1: Section 4 states the conjectures from
  computer experiments without defining QSPP; (4.4)–(4.6) sit in the
  Section 4.1 proof of Theorem 1.2 (QTCPP); Appendix A.1 scope is `a<=6`.
- arXiv all-fields search "quasi symmetric plane partitions qspp" returns no
  results (2026-09-09): no follow-up publishes `a=7` values or a correction.

## Limitations

- The obstruction claim is conditional on "every natural reconstruction": D2
  is the unique natural transfer matching all non-`a=5` probed data, but the
  author's undisclosed program rule is unknown.
- Whether the `a=5` column reflects a program bug, a dropped-`/2`-style typo
  (as in `a=2`), or an undisclosed extra condition cannot be decided from the
  paper alone.
- The `(7,3),(7,4)` D2 values in the draft (1294136, 35427994) are
  single-enumerator supplements, not in the quick verifier, and are not
  claimed here.
- No LGV determinant for QSPP is derived here; inventing one would be new
  uncited method work, not the paper's route.
- The `2^10` exemption-predicate scan and second symmetry-orbit enumerator
  were not forwarded to the auditor; the "no repair" point is therefore
  supporting numerology, not a certified universal.

## Reproducibility

- Pinned source: arXiv:2301.12272v1 HTML (Sections 4, 4.1, Appendix A.1).
- From `output/artifacts/`: `python3 verify.py` → `VERIFY_OK` (stdlib only:
  `fractions`, `math`, `sys`, `time`; no external packages).
- `enum_qspp.py:count_qspp(a, c, mode)` with `mode='D2'` implements the D2
  backtracker; `mode='none'` reproduces the MacMahon check.

## References

- F. Schreier-Aigner, *Fully complementary higher dimensional partitions*,
  arXiv:2301.12272v1 (2023), Sections 4, 4.1, Appendix A.
  https://arxiv.org/html/2301.12272v1
- M. Ciucu, *Four factorization formulas for plane partitions*,
  arXiv:1503.07915 (classical symmetry classes — different family).
