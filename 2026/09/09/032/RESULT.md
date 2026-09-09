# Certified joint (fp, exc, des) census for 123-avoiding permutations to n = 10

## Context
Elizalde (math/0311211) solved the joint fixed-point/excedance law for all
multi-pattern cases of length-3 patterns but left single-pattern 123 as
partial results (Section 3.1: at most two fixed points, summation formulas,
no descent variable, no closed generating function). Barnabei–Bonetti–
Silimbani (arXiv:0910.0963) solved only the Eulerian (descent) marginal over
S_n(123) via Krattenthaler's 123-to-Dyck bijection, with
des = valleys + triple-falls (Prop 1) and closed form E(x,y) = A(x,y,y)
(Thm 6, table printed to n = 7). The trivariate joint law, the bivariate
joints (exc,des) and (fp,des), extended Eulerian rows, and the explicit
123-vs-132 separation were not recorded.

## Definitions
Let S_n(123) be 123-avoiding permutations of {1,..,n}. For sigma:
fp = #{i: sigma(i)=i}, exc = #{i: sigma(i)>i}, des = #{i<n: sigma(i)>sigma(i+1)}.
Define N_{n,k,j,d}(123) = #{sigma in S_n(123): fp=k, exc=j, des=d}.
Let kappa be Krattenthaler's map: write sigma = x_1 w_1 ... x_s w_s with
x_i the left-to-right minima (123-avoidance forces w_1...w_s decreasing);
map x_i to U^{x_{i-1}-x_i} (x_0=n+1) and w_i to D^{|w_i|+1}.
For a Dyck path D, v(D) = number of valleys (DU occurrences),
tf(D) = number of triple-falls (DDD occurrences).

## Result
The complete tables N_{n,k,j,d}(123) for 0 <= n <= 10 were regenerated from
scratch and certified. Marginal sums are the Catalan numbers
1,1,2,5,14,42,132,429,1430,4862,16796 (C_10 = 16796;
sum_{n<=10} C_n = 23714 objects). In particular:

- Trivariate tables (39 cells at n=10), e.g. n=3:
  (0,1,1):1, (0,2,1):1, (1,1,1):2, (1,1,2):1;
  n=10 includes (0,5,6):3384, (1,4,6):1429, (1,5,6):1429, (2,4,6):673
  (full machine-readable table in tri_123_n10.json).
- Joint (exc,des) and (fp,des) tables for 123-avoiders, n <= 10
  (joint_123_n10.json); neither joint is recorded in the prior sources.
- New Eulerian (des) rows, certified against Barnabei Thm 6:
  n=8: {3:14, 4:364, 5:804, 6:247, 7:1};
  n=9: {4:210, 5:1800, 6:2349, 7:502, 8:1};
  n=10: {4:42, 5:1770, 6:7515, 7:6455, 8:1013, 9:1}.
- Divergence 123 vs 132: 572 trivariate cells with N(123) != N(132) for
  n <= 10 (per-n: 3:2, 4:11, 5:22, 6:41, 7:66, 8:99, 9:140, 10:191).
  Minimal cells at n=3: (fp,exc,des)=(1,1,1) has N_123=2 vs N_132=1,
  and (3,0,0) has 0 vs 1; S_3(123)={132,213,231,312,321} contains
  132=(1,3,2) and 213=(2,1,3) with (1,1,1), while S_3(132) contains
  only 213 with (1,1,1) plus the identity with (3,0,0).

## Proof / evidence
Exhaustive backtracking over values 1..n with incremental O(k) pruning
(123: some j<k has min-before < cur[j] < cur[k]; 132: min-before < cur[k]
< cur[j]) generated S_n(123) and S_n(132) to n=10; statistics computed
directly per permutation. Checks, all passing:

1. Independent brute-force (all n! perms, direct triple test) reproduces
   the trivariate tables cell-for-cell for n <= 7 for both patterns.
2. Marginal sums equal Catalan numbers to n=10 for both patterns.
3. Every 123 cell has fp <= 2 (Elizalde Sec 3.1 constraint).
4. Per-object Krattenthaler replay: kappa(sigma) Dyck-valid and
   des(sigma) = v(kappa(sigma)) + tf(kappa(sigma)) on every object
   (independently reimplemented and rechecked for n <= 7; stored
   dyck_ok=replay_ok=True to n=10 on the same code path).
5. Exact-rational power-series expansion of Barnabei E(x,y) matches the
   census des marginals termwise for n=0..10; rows n<=7 reproduce the
   printed Barnabei table (e.g. n=7 {3:56,4:252,5:120,6:1}).

This is experimental/certified-enumeration evidence for the finite census,
not a proof of a general-n formula.

## Limitations
- Exhaustive only to n=10; no general-n trivariate generating function or
  fp/exc Dyck-statistic dictionary is proved (the target closed trivariate
  GF remains open).
- The 132 comparison census shares the backtracking engine with a different
  pattern predicate and is not Krattenthaler-123 certified.
- Krattenthaler transport certifies only the des coordinate; fp/exc rest on
  direct computation plus Catalan-sum and GF-marginal consistency.
- n=8..10 acceptance rests on the audited engine plus Catalan/GF anchors,
  not on n! brute force (infeasible at n=10).

## Reproducibility
Stdlib-only Python. From the output/artifacts directory:

    python3 enumerate.py 10 123
    python3 enumerate.py 10 132
    python3 analyze.py
    python3 gfcheck.py

`enumerate.py` writes tri_{123,132}_n10.json with per-n counts, cells, and
dyck_ok/replay_ok flags; `analyze.py` checks Catalan marginals, fp<=2,
the n=7 Barnabei row, writes joint_123_n10.json and
divergence_123_vs_132.json; `gfcheck.py` expands Barnabei Thm-6 E(x,y) by
S^2=D coefficient recursion over Q[y][[x]] to order 10 and compares des
marginals (adjust the hard-coded tri_123_n10.json path if run outside
output/artifacts). Runtime is seconds per n=10 census on one core.

## References
- S. Elizalde, Multiple pattern avoidance with respect to fixed points and
  excedances, math/0311211 (Sec 3.1, Thms 3.5/3.8).
- M. Barnabei, F. Bonetti, M. Silimbani, The descent statistic over
  123-avoiding permutations, arXiv:0910.0963 (Prop 1; Thms 5-6).
- S. Fu, Z. Lin, Y. Wang, Refined Wilf-equivalences by Comtet statistics,
  arXiv:2009.04269 (different Comtet statistics).
