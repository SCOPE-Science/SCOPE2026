# Dawson's Kayles Heaps 0..120: Exact Shortest/Longest Game-Length Spectrum with Longest-Game Extremal Witness

## Context
Dawson's Kayles (octal game .07) is a flagship impartial taking-and-breaking game
whose Sprague-Grundy periodicity (period 34 from heap 52) is settled and databased
in OEIS A002187. What was untabled alongside those Grundy values is game timing:
how many total moves Dawson heaps last under shortest and longest play. Game
lengths (birthdays / remoteness) are classical combinatorial-game-theory invariants
(ONAG; Winning Ways) used for endgame-timing references and solver/search-benchmark
calibration, and are not a function of Grundy numbers.

## Definitions
A heap of size `n >= 2` moves to an ordered pair of heaps `(a,b)` with
`a + b = n - 2`, `a,b >= 0` (bowling two adjacent pins also removes both immediate
neighbours from play). Heaps `0` and `1` are terminal (no moves). Total game length
is the number of moves until every heap is `0` or `1`. For a single heap of size `n`:
- `L(n)` = maximum possible total moves to termination (longest game);
- `S(n)` = minimum possible total moves to termination (shortest game);
- `L(0) = L(1) = S(0) = S(1) = 0`, and for `n >= 2`:
  `L(n) = 1 + max_{a+b=n-2}(L(a)+L(b))`,
  `S(n) = 1 + min_{a+b=n-2}(S(a)+S(b))`.

## Result
For every `0 <= n <= 120` (proof uniform in `n`):
`L(n) = floor(n/2)`, `S(n) = floor((n+1)/3)`.
Consequences:
- (a) Unique longest-game extremal heap in range: `n* = 120` with `L(120) = 60`.
- (b) Maximal shortest-game value is `40`, attained exactly at `{119, 120}`.
- (c) Duration distributions on `0..120`: each `L`-value `0..59` occurs exactly
  twice and `60` once; `S`-value `0` occurs twice, each of `1..39` exactly three
  times, and `40` twice.
- (d) Witness splits: `(0,n-2)` attains the `L`-maximum for every `n >= 2`;
  `(0,n-2)` attains the `S`-minimum except when `n = 1 mod 3` (`n >= 4`), where
  `(1,n-3)` does. Explicit maximal line from `120`: `120 -> 118 -> ... -> 2 -> 0`
  (60 moves). An explicit minimal line from `120` following the argmin rule replays
  to exactly `40` moves.

## Proof / Evidence
Strong induction. Lemma L: `floor((n-2)/2) = floor(n/2) - 1` for `n >= 2`.
Assuming `L(k) = floor(k/2)` for `k < n`, every split gives
`floor(a/2)+floor(b/2) <= (a+b)/2 = (n-2)/2`, hence `<= floor((n-2)/2)` as an
integer, with equality at `(0,n-2)`; so `L(n) = floor(n/2)`.
For `S`, write `f(k) = floor((k+1)/3)`. Key inequality `f(a)+f(b) >= floor((a+b)/3)`
holds on all 9 residue pairs mod 3 (since `f(3q+s) = q + 1[s=2]`). With
`floor((n-2)/3)+1 = floor((n+1)/3)` and bases `S(0)=S(1)=0, S(2)=S(3)=1`, every
split gives `S(n) >= floor((n+1)/3)`, and splits `(0,n-2)` (when `n%3 != 1`) or
`(1,n-3)` (when `n%3 == 1`, `n >= 4`) attain equality. Extremal and distribution
counts follow algebraically from the closed forms on `0..120`. The maximal line
uses only legal `(0,k-2)` splits with 60 steps `= L(120)`.
Machine replay: stdlib-only DP over 121 heaps checks closed-form equality at every
`n`, recurrence replay under logged witnesses, full max/min agreement over all
splits, extremal uniqueness, both witness lines (60/40 moves), and a Grundy-prefix
sanity check reproducing the OEIS A002187 opening terms
`0,0,1,1,2,0,3,1,1,0,3,3,2,2,4,0,5,...` under the same split family (confirming the
Dawson rule). Run `python3 output/artifacts/verify.py` → prints `VERIFY_OK`; it
also writes `output/artifacts/dawson_durations_0_120.csv`
(columns `n,S,L,argS_a,argS_b,argL_a,argL_b`).

## Limitations
- Certified dataset and extremal claim scoped to heaps `0..120` (the assigned
  preperiod-plus-post-cutoff window); the induction proof is in fact uniform in `n`
  but no dataset claim beyond 120 is made.
- No new Grundy-periodicity or outcome-class (P/N) novelty is claimed.
- Only single-heap `S(n),L(n)` certified; disjunctive-sum lengths over multi-heap
  positions are additive and not separately tabulated.

## Reproducibility
`output/artifacts/verify.py` (stdlib only) recomputes `L,S` from the move rule,
replays all recurrences and witness lines, and regenerates the CSV. Independent
re-run returned `VERIFY_OK`.

## References
- OEIS A002187 — Sprague-Grundy values for Dawson's Chess. https://oeis.org/A002187
- OEIS A002187 b-file b002187.txt — Table of n,a(n) for n=0..1000.
  https://oeis.org/A002187/b002187.txt
- Plambeck, Taming the wild in impartial combinatorial games, math/0501315.
  https://arxiv.org/abs/math/0501315
- OEIS searches “Dawson remoteness”, “Dawson birthday Kayles” (no hits);
  arXiv all-fields “Dawson's Kayles game length” (no results).
