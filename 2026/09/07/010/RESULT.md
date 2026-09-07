# Certified top-five Delta=1 catalog for one-dimensional bin packing at capacity C=24, with exact Gilmore–Gomory duality certificates

## Context
One-dimensional bin packing / cutting stock has LP relaxation LP_GG (Gilmore–Gomory pattern LP) and integer optimum OPT. The integer round-up property (IRUP) is OPT = ceil(LP_GG); the additive gap Delta = OPT − ceil(LP_GG) measures failure. The modified IRUP (MIRUP) is Delta ≤ 1. Prior work stratifies by number of types n (Kartak et al.: n≤9 proper IRUP, n=10 non-IRUP, gap>1 at n=11) or constructs asymptotic large-gap families (Rietz et al.), but publishes no capacity-stratified certified table for small C. Small-C hard instances are directly citable as solver benchmarks for arc-flow, branch-and-price, and column-generation codes.

## Definitions
Fix C=24. Stratum box: k distinct integral sizes a_1<…<a_k, k≤6, each a_i ∈ {2,…,12}, demands b_i ∈ [1,8], N=∑b_i ≤30, S=∑a_i b_i ≤240. Feasible patterns: {x∈Z_+^k : ∑a_i x_i ≤24}, enumerated completely by knapsack DP (never priced heuristically). LP_GG: pattern LP optimum (primal min ∑λ_p s.t. ∑_p x^{(p)}_i λ_p ≥ b_i, λ≥0; dual max b^T y s.t. A^T y ≤1, y≥0). Delta = OPT − ceil(LP_GG). Sizes 1 and 13…24 are out-of-scope by definition (scope, not proved reduction).

## Result
**Theorem A (k≤3 IRUP).** Every instance in the box with k≤2 (3,520 instances) and k=3 (84,465 instances) satisfies Delta=0.

**Theorem B (benchmark catalog).** The following five instances each satisfy Delta=1 (proper non-IRUP):

| # | sizes a | demands b | N | S | LP_GG | ceil | OPT | Delta |
|---|---------|-----------|---|---|-------|------|-----|-------|
| E1 | 5,8,9,12 | 5,8,7,7 | 27 | 236 | 299/30 | 10 | 11 | 1 |
| E2 | 2,7,8,10,11,12 | 6,3,5,4,5,4 | 27 | 216 | 9 | 9 | 10 | 1 |
| E3 | 3,7,8,10,12 | 2,8,5,3,5 | 23 | 187 | 8 | 8 | 9 | 1 |
| E4 | 2,7,8,10,11 | 3,5,5,3,3 | 19 | 144 | 6 | 6 | 7 | 1 |
| E5 | 5,6,8,9 | 1,3,8,1 | 13 | 96 | 4 | 4 | 5 | 1 |

**Theorem C (local maximality).** All 63 Hamming-1 neighbors (demand ±1; size ±1 keeping distinctness in 2…12; N,S bounds respected) of E1–E5 have Delta=0; each entry is a strict local Delta-maximum.

**Observation (conjecture, not theorem).** Across ~250k evaluations (exhaustive k≤3, seeded random k=3…6, hill-climbing, neighbors) max observed Delta is 1; no Delta≥2 seen. MIRUP on the stratum (G*(24)=1) is conjectured but not proved (~1e8 combos).

## Proof / Evidence
*Pattern completeness:* depth-first knapsack DP re-enumeration matches stored lists (25,107,61,39,90 patterns); exact set equality checked.
*LP exactness:* per-instance rational primal λ and dual y with equal objectives (Fractions), e.g. E1 y=(1/5,1/3,2/5,1/2), b^T y=299/30; primal 7/2·(0,0,0,2)+8/3·(0,3,0,0)+16/5·(1,0,2,0)+3/5·(3,0,1,0) covering (5,8,7,7); A^T y≤1 verified entrywise, hence optimal by strong duality. E2–E5 analogous with LP 9,8,6,4.
*OPT upper bound:* explicit packings (e.g. E1: [12,12]×3, [12,9], [9,9,5]×3, [8,8,8]×2, [8,8,5], [5]; all loads ≤24) with correct multisets.
*OPT lower bound:* item-branching DFS with duplicate-load skipping, empty-bin symmetry break, memoization proves K=OPT−1 infeasible (nodes 2248,7690,7420,828,97), cross-confirmed by independent bin-completion brancher and by auditor's independent re-search.
*k≤2:* auditor exactly re-proved all 3520 via Fractions vertex enumeration + DFS. *k=3:* auditor reproduced 84465-instance screening with independent simplex + FFD (3925 candidates, exact match) and exactly closed 100/100 sampled candidates. *Neighbors:* auditor regenerated 63 neighbors and exactly proved all Delta=0 via Fractions simplex + DFS.

## Limitations
1. Full-stratum maximality not proved (partial coverage; k=4 exhaustive alone 1.35M combos).
2. Size-1 / >C/2 exclusions are scope, not proved reductions for mixed cases.
3. OPT lower bounds rely on DFS completeness + independent agreement and rerunnable verifier, not a proof-assistant certificate.
4. Five entries are top-by-OPT-size k-diverse selection among 14 found Delta=1 instances: a benchmark, not an extremal classification; not claimed minimal/unique.

## Reproducibility
Stdlib-only `artifacts/recheck.py` + `artifacts/catalog.json`: re-enumerates patterns, checks dual/primal with Fractions, ceil/Delta integers, packing multiset/capacity, and re-runs OPT−1 DFS. Prints ALL 5 ENTRIES VERIFIED in seconds on a laptop. Search seeds, pattern DP, dual simplex with rational polish, and DFS branchers are documented for independent replay.

## References
- Kartak–Kurz–Ripatti–Scheithauer, Minimal proper non-IRUP instances of the 1D Cutting Stock Problem, Discrete Appl. Math. 187:120–129 (2015). arXiv:1405.5988. doi:10.1016/j.dam.2015.02.020 — n-stratification, orthogonal.
- Scheithauer–Terno, The modified integer round-up property of the 1D cutting stock problem, EJOR 84:562–571 (1995). doi:10.1016/0377-2217(95)00022-I — MIRUP definition.
- Rietz–Dempe, Large gaps in 1D cutting stock problems, Discrete Appl. Math. 156:1929–1935 (2008). doi:10.1016/j.dam.2007.08.052 — asymptotic families, complementary.
- Nitsche–Scheithauer–Terno, New cases of the cutting stock problem having MIRUP, Math. Methods OR 48:105–115 (1998). doi:10.1007/s001860050015 — sufficient MIRUP cases.
