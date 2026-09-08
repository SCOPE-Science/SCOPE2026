# Symmetric/alternating splitting of Kronecker squares around the staircase square: exact table at n=10 with maximal-gap witnesses for n=8-12

## Context

The Kronecker coefficient `g(lam,mu,nu)` is the multiplicity of `[nu]` in
`[lam][mu]` for complex irreducible characters of `S_n`. The Saxl conjecture
states that for triangular `n=k(k+1)/2` the staircase square
`[rho_k]^2`, `rho_k=(k,...,2,1)`, contains every irreducible. Bessenrodt-Bowman
(arXiv:2202.03066) refine this into a symmetric/alternating splitting program:
`[lam]^2 = S^2[lam] + A^2[lam]`, with connections to 2-modular decomposition
numbers, Catalan combinatorics, and a refined Saxl Conjecture C (the symmetric
part `S^2[rho_k]` should contain all irreps except the sign when `k=2 mod 4`).
They declare splitting results scarce and prove only family theorems (hooks,
small depth, sign, 2-part `[k,k]`/`[k+1,k]`, homogeneous, multiplicity-free).
No window-complete `(s,a)` table for the staircase square `rho(4)=(4,3,2,1)`
at `n=10` or per-`n` maximal-gap census for `n=8-12` existed.

## Definitions

Let `chi^lam` be the irreducible `S_n` character, `g(lam,lam,nu)` the Kronecker
coefficient. Write `s_nu = mult([nu],S^2[lam])`, `a_nu = mult([nu],A^2[lam])`.
By the standard symmetrization identity (Frobenius characteristic of
`S^2`/`A^2`; Bessenrodt-Bowman Lemma 2.1):

- `s_nu = (g + m_nu)/2`, `a_nu = (g - m_nu)/2`,
- `g(lam,lam,nu) = (1/n!) sum_C |C| chi^lam(C)^2 chi^nu(C)`,
- `m_nu(lam)    = (1/n!) sum_C |C| chi^lam(C^2) chi^nu(C)`,

sums over conjugacy classes `C`, where `C^2` is the class of `g^2` for `g in C`.
Hence `s_nu + a_nu = g`, `s_nu - a_nu = m_nu`, and the splitting gap
`|s_nu - a_nu| = |m_nu|`. Maximizing the gap means maximizing `|m_nu|`.

All character values are computed from scratch by the Murnaghan-Nakayama
rim-hook recursion and committed as integer tables with class sizes and the
square-type map `C -> C^2`. Every derived number is an exact integer class sum.

Certification identities checked exactly for every `lam`, `n=8..12`:
(i) row and column orthogonality; (ii) `sum_nu dim(nu)^2 = n!`;
(iii) `g,m` integers, `s,a` nonnegative integers with correct parity;
(iv) `sum_nu s_nu dim(nu) = d(d+1)/2`,
`sum_nu a_nu dim(nu) = d(d-1)/2`, `d = dim lam`.
Cross-checks: all dimensions match the hook formula, the standard character
`(n-1,1)` equals `m_1-1`, sign rows and conjugate duality
`chi^{lam'} = sgn * chi^{lam}` hold, and the `C^2` map agrees with explicit
permutation squaring for every class.

## Result

### A. Complete splitting table for `rho(4)=(4,3,2,1)`, `n=10`

`dim rho(4) = 768`. Verified:
`sum s*dim = 768*769/2 = 295296`, `sum a*dim = 768*767/2 = 294528`.

| nu | g | m | s (sym) | a (alt) |
|---|---|---|---|---|
| [10] | 1 | 1 | 1 | 0 |
| [9,1] | 3 | 3 | 3 | 0 |
| [8,2] | 8 | 8 | 8 | 0 |
| [8,1,1] | 9 | -3 | 3 | 6 |
| [7,3] | 15 | 7 | 11 | 4 |
| [7,2,1] | 31 | 3 | 17 | 14 |
| [7,1,1,1] | 18 | -8 | 5 | 13 |
| [6,4] | 15 | 9 | 12 | 3 |
| [6,3,1] | 54 | 0 | 27 | 27 |
| [6,2,2] | 39 | 15 | 27 | 12 |
| [6,2,1,1] | 62 | -10 | 26 | 36 |
| [6,1,1,1,1] | 24 | 0 | 12 | 12 |
| [5,5] | 6 | 2 | 4 | 2 |
| [5,4,1] | 45 | 3 | 24 | 21 |
| [5,3,2] | 71 | 5 | 38 | 33 |
| [5,3,1,1] | 92 | -12 | 40 | 52 |
| [5,2,2,1] | 86 | 8 | 47 | 39 |
| [5,2,1,1,1] | 76 | -6 | 35 | 41 |
| [5,1,1,1,1,1] | 24 | 8 | 16 | 8 |
| [4,4,2] | 38 | 10 | 24 | 14 |
| [4,4,1,1] | 47 | -5 | 21 | 26 |
| [4,3,3] | 32 | -6 | 13 | 19 |
| [4,3,2,1] | 117 | 1 | 59 | 58 |
| [4,3,1,1,1] | 86 | -2 | 42 | 44 |
| [4,2,2,2] | 47 | 15 | 31 | 16 |
| [4,2,2,1,1] | 92 | -8 | 42 | 50 |
| [4,2,1,1,1,1] | 62 | 4 | 33 | 29 |
| [4,1,1,1,1,1,1] | 18 | 2 | 10 | 8 |
| [3,3,3,1] | 32 | -6 | 13 | 19 |
| [3,3,2,2] | 38 | 0 | 19 | 19 |
| [3,3,2,1,1] | 71 | 1 | 36 | 35 |
| [3,3,1,1,1,1] | 39 | 5 | 22 | 17 |
| [3,2,2,2,1] | 45 | 3 | 24 | 21 |
| [3,2,2,1,1,1] | 54 | -6 | 24 | 30 |
| [3,2,1,1,1,1,1] | 31 | 3 | 17 | 14 |
| [3,1,1,1,1,1,1,1] | 9 | -3 | 3 | 6 |
| [2,2,2,2,2] | 6 | 4 | 5 | 1 |
| [2,2,2,2,1,1] | 15 | -3 | 6 | 9 |
| [2,2,2,1,1,1,1] | 15 | 1 | 8 | 7 |
| [2,2,1,1,1,1,1,1] | 8 | 0 | 4 | 4 |
| [2,1,1,1,1,1,1,1,1] | 3 | -1 | 1 | 2 |
| [1,1,1,1,1,1,1,1,1,1] | 1 | 1 | 1 | 0 |

Consequences (exact):
- Unsplit Saxl containment at `n=10`: all 42 `g > 0` (minimum 1 at `[10]` and sign).
- Symmetric positivity: `s_nu > 0` for 42/42 (confirms Conjecture C instance
  `k=4`, where `k=0 mod 4` predicts full `S^2` containment).
- Alternating census: `a_nu > 0` for 38/42; zeros exactly at
  `[10],[9,1],[8,2],[1^10]` (trivial row: `s=1,a=0`).
- Self-pair `([4,3,2,1],[4,3,2,1])`: `g=117, s=59, a=58`.

### B. Maximal splitting-gap witnesses, `n=8..12`

Gap `= |s-a| = |m|`, maximized over all ordered pairs `(lam,nu)` of partitions
of `n` (exhaustive scan over `p(n)^2` pairs; `p = 22,30,42,56,77`).
Lex-first maximizer shown; ties disclosed and fully enumerated.

| n | max gap | lam | nu | g | s | a | maximizers |
|---|---|---|---|---|---|---|---|
| 8 | 6 | [4,2,1,1] | [4,2,2] | 12 | 9 | 3 | unique (1) |
| 9 | 8 | [4,3,1,1] | [5,2,2] | 16 | 12 | 4 | tied x2 (also lam=[4,2,2,1]) |
| 10 | 15 | [4,3,2,1] | [6,2,2] | 39 | 27 | 12 | tied x2 (also nu=[4,2,2,2]: g=47,s=31,a=16) |
| 11 | 24 | [5,3,2,1] | [5,2,2,2] | 110 | 67 | 43 | tied x2 (also lam=[4,3,2,1,1]) |
| 12 | 43 | [5,3,2,1,1] | [6,2,2,2] | 237 | 140 | 97 | unique (1) |

Top-five gap tables (verified replay):
- n=8: (6;[4,2,1,1],[4,2,2],s9a3), (5;[4,3,1],[4,2,2],s6a1),
  (5;[4,2,1,1],[6,2],s5a0), (5;[4,2,1,1],[4,2,1,1],s6a11),
  (5;[3,2,2,1],[4,2,2],s6a1).
- n=9: (8;[4,3,1,1],[5,2,2],s12a4), (8;[4,2,2,1],[5,2,2],s12a4),
  (7;[5,2,1,1],[5,2,2],s10a3), (7;[4,2,1,1,1],[5,2,2],s10a3),
  (6;[5,3,1],[5,2,2],s9a3).
- n=10: (15;[4,3,2,1],[6,2,2],s27a12), (15;[4,3,2,1],[4,2,2,2],s31a16),
  (12;[4,3,2,1],[5,3,1,1],s40a52), (11;[5,3,1,1],[6,2,2],s18a7),
  (11;[4,2,2,1,1],[6,2,2],s18a7).
- n=11: (24;[5,3,2,1],[5,2,2,2],s67a43),
  (24;[4,3,2,1,1],[5,2,2,2],s67a43),
  (21;[5,3,2,1],[6,3,1,1],s77a98),
  (21;[4,3,2,1,1],[6,3,1,1],s77a98), (20;[5,3,2,1],[7,2,2],s39a19).
- n=12: (43;[5,3,2,1,1],[6,2,2,2],s140a97),
  (38;[5,3,2,1,1],[6,4,2],s188a150),
  (34;[5,3,2,1,1],[7,3,1,1],s132a166),
  (33;[5,4,2,1],[6,2,2,2],s89a56),
  (33;[4,3,2,2,1],[6,2,2,2],s89a56).

Staircase connection: at `n=10` both gap maximizers lie in the `rho(4)` square;
at `n=11,12` the `lam`-witnesses are staircase-adjacent
(`[5,3,2,1]`,`[4,3,2,1,1]` at `n=11`; `[5,3,2,1,1]` at `n=12`).

### C. 2-modular / Catalan comparison column (benchmark data, not a new proof)

- Sign column (BB Sec.6): sign constituent of `rho(4)^2` is `(s,a)=(1,0)`;
  the full hook sub-table above supplies exact `S^2`/`A^2` inputs for BB hook
  formulas. Spot-confirmed BB Theorem D instance at `n=10`:
  `m_{rho4}(lam)=0` for every `lam != rho4`.
- Catalan (BB Theorem B): the committed `(g,m,s,a)` rows are exact data against
  which Catalan-identity predictions can be checked; no new proof of Theorem B.
- 2-modular (BB Theorem D/Sec.3): the `m_nu` column is the character-theoretic
  input to decomposition-number relations; provided as certified data only.

## Proof / evidence

From-scratch Murnaghan-Nakayama tables `n=8..12` with exact row and column
orthogonality and `sum dim^2=n!`; stored tables equal freshly recomputed tables;
all dimensions match the hook formula; standard/sign/conjugate-duality and
`C^2`-vs-explicit-squaring checks pass. All 42 `rho(4)` rows replayed from
stored tables (0 mismatches) with dimension-sum identities. Per-`n` exhaustive
ordered-pair rescans from scratch reproduce the claimed maxima, maximizer sets,
and top-five tables. Independent replay: `verify.py` (from stored tables only)
reports orthogonality+dimsum 5/5, `rho4` 42/42, gap-maximality 5/5, top-five 5/5.

## Limitations

- Exact finite census for `n=8..12` only; no asymptotics or general-`n` theorem.
- Gap-maximality is exhaustive conditional on the committed tables (certified by
  orthogonality/dimsum/hook/standard/duality identities, no external library).
- Maximum tied x2 at `n=9,10,11`; uniqueness only at `n=8,12`.
- 2-modular/Catalan column is benchmark data, not a derivation of BB results.

## Reproducibility

Artifacts: `mn.py` (from-scratch Murnaghan-Nakayama, orthogonality, class
sizes, square-type map), `char_tables.json` (committed integer tables),
`rho4_split.json` (42 rows), `gap_summary.json` (maxima + top-five),
`split.py` (full splits with `S^2`/`A^2` dimension-sum assertions),
`verify.py` (independent replay from stored tables only). Run
`python3 mn.py`, `python3 split.py`, `python3 verify.py` with stdlib-only
Python 3; `verify.py` must print `ALL VERIFICATIONS PASSED`.

## References

- C. Bessenrodt, C. Bowman, Splitting Kronecker squares, 2-decomposition
  numbers, Catalan Combinatorics, and the Saxl conjecture, arXiv:2202.03066.
- I. Pak, G. Panova, E. Vallejo, Kronecker products, characters, partitions,
  and the tensor square conjectures, arXiv:1304.0738.
