# Finite quadratic-twist census for 11a1 through height 5000

## Context
Goldfeld's conjecture and the Poonen–Rains heuristics predict rank and
Selmer distributions in quadratic twist families (in particular, first
moment average \(\#\operatorname{Sel}_2=3\) in the limit). Certified curve-specific
replayable data points with full descent provenance are scarce. The curve
\(E=\mathrm{11a1}: y^2+y=x^3-x^2-10x-20\) (conductor 11, minimal
canonical example, torsion \(\mathbb{Z}/5\mathbb{Z}\)) is the benchmark. The finite-window
question at height 5000 is the disjunction: Poonen–Rains first-moment
confirmation \(|M_{5000}-3|\le 0.15\), OR one explicit twist with certified
rank \(\ge 4\).

## Definitions
- \(E_d\): quadratic twist of \(E=\mathrm{11a1}\) by squarefree \(0<|d|\le 5000\)
  (6084 twists), twist convention `Ed = elltwist(E, quaddisc(d))`
  (\(d=1\) gives \(E\) itself; `D = quaddisc(d)`).
- \(s(d)=\dim_{\mathbb{F}_2}\operatorname{Sel}_2(E_d/\mathbb{Q})\): exact 2-Selmer dimension (PARI/GP
  2.15.4 `ellrank` full 2-descent semantics \(s(d)=r_{\mathrm{hi}}+T_{\mathrm{dim}}+s_{\mathrm{sha}}\)).
- \(w(d)\): root number of \(E_d\).
- \(M_{5000}=\operatorname{mean}_d 2^{s(d)}\): empirical first moment of \(\#\operatorname{Sel}_2\).
- \(r_{\mathrm{lo}}(d)\le\operatorname{rank}(E_d(\mathbb{Q}))\le r_{\mathrm{hi}}(d)\): rank bounds; \((r_{\mathrm{lo}},r_{\mathrm{hi}})=(3,3)\)
  means closed rank 3 with three logged independent points and nonzero
  regulator.

## Result
Let \(E=\mathrm{11a1}\) and \(E_d\) as above with \(s(d)\), \(w(d)\), \(M_{5000}\) defined as
above. Then:

1. \(M_{5000}=12136/6084=3034/1521=1.9947403\ldots\), so
   \(|M_{5000}-3|=1.0052597\ldots>0.15\). The Poonen–Rains first-moment
   confirmation disjunct is **false**.
2. \(\max_d r_{\mathrm{lo}}(d)=3\), attained at exactly nine twists
   \(d\in\{-4399,-1799,-1007,-206,1393,1766,2362,2878,4582\}\),
   each closed \((r_{\mathrm{lo}},r_{\mathrm{hi}})=(3,3)\) with three logged independent
   points and nonzero regulator; **no** twist has certified rank \(\ge 4\)
   (indeed none even has \(r_{\mathrm{hi}}\ge 4\)). The high-rank-witness disjunct is
   **false**.

Hence the finite-window claim
("(moment confirmation) OR (rank \(\ge 4\) witness)" over this window) is
**false**. Supporting census data:
`sel_dim: {0: 2106, 1: 3011, 2: 932, 3: 35}` (no \(\texttt{sel\_dim}\ge 4\));
rank pairs `(0,0): 2549, (1,1): 3037, (2,2): 313, (3,3): 9, (0,2): 176`
(closed 5908/6084); parity \((\texttt{sel\_dim}-T_{\mathrm{dim}})\bmod 2=(1-w)/2\) on
**6084/6084** rows with \(T_{\mathrm{dim}}=0\) throughout. The \(|d|\le 1500\) prefix
(1830 rows) has \(M_{1500}=3528/1830=588/305\approx 1.9279\), likewise
refuting \(|M-3|\le 0.15\), with max certified rank 3 at \(d=1393\);
this shorter-window comparison is subsumed by the 5000-window census.

## Proof / Evidence (computational)
- Full 2-descent on every twist via direct `ellrank(Ed)`: 6084/6084
  success and 0 failures in the archived census. An independent full
  PARI/GP 2.15.4 sweep of the same 6084 squarefree signed parameters
  reproduced the Selmer histogram, sum 12136, maximum upper bound 3,
  and the nine rank-three twists. This reuses PARI's descent engine,
  not an independent implementation of 2-descent.
- Independent arithmetic checks of `artifacts/T5000.csv`
  with standard-library code show: d-set equals exactly all squarefree \(0<|d|\le 5000\)
  (0 missing/extra); `D == quaddisc(d)` on all rows; j-invariant
  constant at the 11a1 value on spot checks; exact moment fraction
  \(3034/1521\); max \(r_{\mathrm{lo}}=\max r_{\mathrm{hi}}=3\) with the exact nine-element
  witness list; coherence \(\texttt{sel\_size}=2^{\texttt{sel\_dim}}\),
  `sel_dim == r_hi + T_dim + s_sha`, and 100% parity agreement.
- `verify.py` (stdlib only, no PARI): d-set completeness, moment
  fraction, parity recompute, max-rank scan, exact-rational on-curve
  check of all 1977 logged points against per-twist models, and
  height/regulator positivity (1681/1681 nonzero regulators)
  -> `VERIFY_OK` (reproduced from the archived files).
- Cross-checks reported: root numbers 100% parity agreement; analytic
  ranks (`ellanalyticrank`) 25/25 agreement on spots (unlogged);
  torsion `elltors` on every twist (\(T_{\mathrm{dim}}=0\)).

## Limitations
- "Rigorous" means exact finite computation through PARI's published
  `ellrank` 2-descent + Cassels-pairing implementation, with the
  cross-checks above. It is not a hand proof and inherits trust in
  PARI/GP 2.15.4 `ellrank`/`ellrootno`/`ellanalyticrank` correctness.
- Rank upper bounds on the 176 \((0,2)\) rows rest on the Selmer bound
  plus analytic-rank-0 evidence on samples (not a per-row analytic
  certificate for all 176).
- Point independence beyond logged nonzero regulator determinants was
  not re-proved by a second implementation; saturation (index) was not
  separately certified — only the \(r_{\mathrm{lo}}\) (\(\ge\)) direction is claimed,
  which is what the witness disjunct needs.
- No asymptotic claim: this finite window (mean \(\approx 1.99\)) does not refute
  the Poonen–Rains *limit* prediction, only the window's
  \(|M-3|\le 0.15\) decision as stated.

## Reproducibility
The committed package contains `artifacts/T5000.csv`,
`artifacts/verify.py`, `artifacts/points5000.txt`,
`artifacts/models5000.txt`, `artifacts/heights5000.txt`, and
`artifacts/fail5000.txt`. From the package root, run
`python3 artifacts/verify.py`; from another working directory, use the full
path to that script. The script locates data beside itself and reports
`VERIFY_OK`. This verifies
the archived finite table, point equations, parity, and summaries; it does
not execute a fresh 2-descent.

For a fresh Selmer-rank cross-check, use PARI/GP 2.15.4 with
`E=ellinit([0,-1,1,-10,-20])`; for each squarefree positive integer
\(m\le 5000\) and both signs \(s\), put `D=quaddisc(s*m)`,
`R=ellrank(elltwist(E,D))`, and tabulate `2^(R[2]+R[3])`.
The complete rerun gave 6084 cases, Selmer-size sum 12136, histogram
`[2106,3011,932,35,0,0]`, and maximum rank upper bound 3.
The historical generator scripts `census5000.gp` and
`models5000.gp`, and the originally cited local PARI executable path,
are not in this committed tree and are not presented as replay paths.
The existing point/model files remain preserved evidence.

## References
- Klagsbrun–Mazur–Rubin, Disparity in Selmer ranks of quadratic twists
  of elliptic curves, Annals 2013.
- Poonen–Rains, Random maximal isotropic subspaces and Selmer groups.
- Bhargava–Kane–Lenstra–Poonen–Rains, Modeling the distribution of
  ranks, Selmer groups, and Shafarevich–Tate groups.
- Watkins, Distribution of the 2-Selmer rank under twisting, PMB 2022
  (survey of Heath-Brown / Swinnerton-Dyer / Kane / Smith for
  \(y^2=x^3-x\) and full-2-torsion families).
- Chao Li, Level raising mod 2 and arbitrary 2-Selmer ranks
  (11a1 as example); Kriz, Goldfeld's conjecture and congruences
  between Heegner points (\(X_0(11)\) running example).
