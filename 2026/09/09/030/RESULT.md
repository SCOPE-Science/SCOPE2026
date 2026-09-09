# Certified periodicity cutoffs and maximal Grundy witnesses for primitive three-move subtraction games with max ≤ 10 to heap 500

## Context

Exact periods, preperiods, and maximal nim-values of subtraction games are
recognized questions going back to Guy, Berlekamp, and Fraenkel. General
eventual periodicity of finite subtraction games is classical but gives
exponential bounds; exact cutoffs are known only case by case. Manabe (2026)
gives a sufficient pure-periodicity criterion for three-move sets with least
periods only for qualifying purely-periodic sets. This record gives the closed
replayable census for all primitive triples with max ≤ 10.

## Definitions

- Family: all primitive triples S = {a,b,c} ⊂ {1,…,10} with gcd(a,b,c) = 1.
  |F| = C(10,3) − 11 = 109 (the 11 excluded sets are the 10 all-even triples
  plus {3,6,9}).
- Sprague–Grundy sequence: G_S(0) = 0,
  G_S(n) = mex{ G_S(n−s) : s ∈ S, s ≤ n }.
- Window: N = 500. Put m = max(S).
- M(S) = max_{0≤n≤500} G_S(n); h(S) = least n with G_S(n) = M(S);
  nP(S) = |{ n ≤ 500 : G_S(n) = 0 }|.

## Result

For every S ∈ F there is a tabled pair (N₀(S), p(S)) with
N₀ + p + m − 1 ≤ 500 such that:

1. **Certified cutoff:** G_S(n) = G_S(n+p) for all n ∈ [N₀, 500−p], hence by
   the Closing-Window Lemma below G_S(n) = G_S(n+p) for all n ≥ N₀
   (true infinite eventual periodicity).
2. **Leastness:** for every 1 ≤ q < p some n ∈ [N₀, 500−q] has
   G_S(n) ≠ G_S(n+q), and if N₀ ≥ 1 then G_S(N₀−1) ≠ G_S(N₀−1+p).
   Hence p is the true least eventual period and N₀ is the least preperiod
   for that p.
3. **Maximal witness:** M(S), h(S), nP(S) are exactly as tabled.

Census statistics: 99 purely periodic sets (N₀ = 0), 10 impure sets
(N₀ ≥ 1); largest N₀ = 21 for {2,8,9}; periods range 2…45 with sole p = 45
for {3,7,10} and sole p = 22 for {2,5,7}; maximal nim-values M ∈ {1,2,3}
(1: 6 sets, 2: 45 sets, 3: 58 sets); no set attains M ≥ 4 on [0,500].
The six binary-valued (M = 1) sets are exactly
{1,3,5}, {1,3,7}, {1,3,9}, {1,5,7}, {1,5,9}, {1,7,9}.
Worked rows: {1,2,3}: (0,4), M=3 at h=3, nP=126; {1,2,4}: (0,3), M=2 at h=2,
nP=167; {3,7,10}: (0,45), M=3 at h=10, nP=135; {2,5,7}: (0,22), M=3 at h=7,
nP=138; {2,8,9}: (21,11), M=3 at h=10, nP=183.
Full 109-row table: `artifacts/census.csv` / `artifacts/census.json`.

## Proof / Evidence

**Lemma (Closing-Window).** Fix S with m = max(S). If for some N₀,p with
N₀+p+m−1 ≤ N one has G(n) = G(n+p) for all n ∈ [N₀, N−p], then
G(n) = G(n+p) for all n ≥ N₀.

*Proof.* The top-m block W = [N−p−m+1, N−p] agrees since N₀ ≤ N−p−m+1.
Induction on k ≥ 0: assume agreement on [N₀, N−p+k]. For n = N−p+k+1,
every predecessor n−s lies in [N−p+k+1−m, N−p+k] ⊂ [N₀, N−p+k], and likewise
n+p−s is in the agreed range with G(n−s) = G(n−s+p) termwise; hence the two
reachable sets coincide and G(n+p) = mex = G(n). Iterate. ∎

Computation: mex DP to heap 500 for each of the 109 sets (≤3 predecessors
per heap, ≈54k mex operations); least-p scan p = 1…200 where least N₀(p) is
one past the last index with G(n) ≠ G(n+p), accepted iff N₀+p+m−1 ≤ 500.
All 109 sets close with p ≤ 200. Independent stdlib verifier recomputes
every G_S from the rules and checks C1 (closing window), C2 (period
leastness), C3 (preperiod leastness), C4 (maximal witness), C5 (cold count),
plus family completeness:
`python3 verify.py census.json` → `VERIFY_OK: 109/109 rows`
(pure N₀=0: 99, max N₀: 21, max period: 45, max M: 3).

Leastness promotion: C1 promotes the finite window to the true infinite
tail; a competing smaller true period q of the infinite tail would satisfy
equality on the observed window and is excluded by C2, so tabled p is the
true least eventual period.

## Limitations

- Maximality M(S) is over [0,500] (windowed), not a theorem about the
  infinite tail.
- Leastness is relative to the committed window as defined above (C2/C3);
  exclusions requiring data beyond heap 500 are not claimed.
- No general periodicity formula or Manabe-necessity theorem is claimed.

## Reproducibility

`python3 artifacts/verify.py artifacts/census.json` reproduces C1–C5 and
completeness in seconds with stdlib Python only. `artifacts/census.csv` is
the CSV rendering; `artifacts/census.json` (sha256
663dcd5a6916b890c20630a99e7986b2dfbbc7e7451d4af1ac586e3f7ece794a)
is the verified table.

## References

- H. Manabe, Purely Periodic Three-move Subtraction Games, arXiv:2609.05358 (2026).
- Z. Qin, G. He, The Period of the subtraction games, arXiv:1208.6134 (2012).
- E. Duchêne, M. Heinrich, U. Larsson, A. Parreau, The switch operators and push-the-button games, arXiv:1707.07966 (2017).
- D. Eppstein, Faster Evaluation of Subtraction Games, arXiv:1804.06515 (2018).
