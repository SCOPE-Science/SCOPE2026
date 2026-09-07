# Exact maximal covering density for nine distinct moduli in [7,20], with certified interval for [7,60]

## Context
Distinct covering systems lie between textbook CRT exercises and the deep
minimum-modulus theorem (Hough 2015; Balister et al. 2022), which give only
qualitative upper bounds on the least modulus of a full distinct covering.
For k=9 with minimum >=7, full covering is already impossible by the
reciprocal-sum test: the largest possible union bound is
sum_{m=7..15} 1/m = 62575/72072 approx 0.86823 < 1, attained at 7,...,15 by
1/m monotonicity. The sharp quantitative question — how close can nine
distinct moduli >=7 come? — had no published exact table. This record closes
the sub-stratum [7,20] exactly and gives a certified interval for [7,60].

## Definitions
Let M=[7,20] (census) and M60=[7,60] (interval). For distinct
m_1<...<m_9 in M and residues a_i, let L=lcm(m_i) and
D(a,m)=|{x mod L : exists i with x=a_i mod m_i}|/L, the natural density
covered. Put D*(9;M)=max D over modulus choice and residue choice,
U*=1-D*. Density of any candidate is computed exactly by enumeration over
its LCM period.

## Result
**Theorem (exact [7,20] census).** Over distinct m_i in [7,20], |S|=9,
D*(9;[7,20])=1817/2772 approx 0.655483405, U*=955/2772 approx 0.344517,
attained e.g. at S*=[7,8,9,10,11,12,14,15,16] with
a*=[0,4,1,1,0,2,1,0,0], L=55440, covered 36340.
No 9-set in [7,20] exceeds this. Runner-up is 47/72 approx 0.652778
(3290/5040) at [7,8,9,10,12,14,15,16,18] (residues [0,4,1,1,2,1,0,0,5])
and the 20-variant [7,8,9,10,12,14,15,16,20]; gap 0.002706.

**Corollary (certified interval for [7,60]).**
0.655483 <= D*(9;[7,60]) <= 0.868229,
0.131771 <= U* <= 0.344517.
Lower bound is the [7,20] witness (hence in [7,60]); upper bound is the
union bound with maximizer 7,...,15. Prime-max elimination (Lemma 3 below)
is rigorous progress toward closing [7,60].

**Conjecture (not proved).** D*(9;[7,60])=1817/2772.

## Proof / Evidence
**Lemma 1 (Translation fixing).** Let C subset S be pairwise coprime. For any
residues there is t mod L with a_c+t=0 mod c for all c in C (CRT, since
product C divides L), and x->x+t preserves density. Hence max density is
attained with a_c=0 on a max-product such C. Verified empirically on
[7,8,9,10] (full optimum equals C-fixed optimum).

**Lemma 2 (Prime peeling).** Let p in S be prime with no multiples in S
(equivalently p not dividing L0=lcm(S\\{p\})). Write L=L0*p. Each y mod L0
lifts to p values; since gcd(L0,p)=1 they run through all residues mod p,
so uncovered=U0*(p-1), D=D0+U0/p independent of a_p. Thus
Dmax(S)=1-(1-Dmax(S0))(p-1)/p. Iterates for distinct new primes. In [7,16],
11,13 always peelable (2p>16); in [7,20], 11,13,17,19 always peelable.
Verified empirically ([7,8,9,10]+11 gives predicted 12840/27720 for all lifts).

**Lemma 3 (Prime-max exchange).** If |S|=9 with m_max prime, Lemma 2 gives
Dmax(S)=D0+U0/m_max. Let m* be smallest unused in [7,24] (<=16 since
|[7,24]|=18; any prime-max set has max>=17 so m*<m_max). For
S'=S0 union {m*}, averaging over m* residues gives Dmax(S')>=D0+U0/m*.
Hence Dmax(S')>Dmax(S): no optimal set has prime maximum. In particular no
optimal [7,60] set has prime maximum.

**Exact core solver.** After peeling, core K (|K|<=9, L<=5040) is solved by
Lemma-1-fixed enumeration with memoization over 544 distinct cores (numpy
bitsets), plus hierarchical affine-stabilizer orbit branching for large-R
cores (worst 43M brute combos -> 67k leaves). Cross-checked: hierarchical vs
direct brute force agree on small cores; [7,16] dual-backend (numpy + stdlib
bytearray) agrees on all 10 optima. Independent audit re-proved all 2002
optima with a different union-bound branch-and-bound (106s, zero table
entries beaten), including brute-force confirmation of best core 3130/5040
and runner-up 3290/5040.

**Computed evidence.** [7,16]: C(10,9)=10 sets. [7,20]: C(14,9)=2002 sets,
544 cores, deterministic replay ~27s (<30s). Best 36340/55440 and runner-up
3290/5040 reproduced by independent stdlib LCM enumeration in <2s; 20
scattered table rows re-enumerated exactly; max-sum 62575/72072 verified by
Fraction. [7,60] total C(54,9)=5317936260; union-competitive counts are
motivational only.

## Limitations
Exactness proved only for [7,20], not [7,60]. Full [7,60] upper bound here
is only union 0.868; no D*<=0.70 claim is made. Hierarchical enumeration
relies on Lemmas 1-2 (proved) and deterministic orbit branching
(code-reviewed, dual-backend checked on [7,16], independently re-proved by
B&B on all [7,20] cores by audit). Large-prime peeling assumes distinct
primes (holds as moduli distinct). Conjecture D*(9;[7,60])=1817/2772 is
heuristic (support: [7,20] optimum + Lemma 3 + marginal 1/m<=1/21 with
coprime overlaps), not a proof.

## Reproducibility
Requires numpy only (stdlib otherwise). `python3 verify_Ustar.py` (<2s,
stdlib bytearray) reproduces best, runner-up, max-sum, and top-5 rows.
`python3 reproduce_census_7_20.py` deterministically regenerates the full
2002-row `census_7_20_table.csv` in ~27s and asserts best=1817/2772.
Artifacts: `census_7_20_table.csv`, `census_7_20_summary.json`,
`best_witness_7_16.json`, both scripts.

## References
- B. Hough, Solution of the minimum modulus problem for covering systems,
  Ann. Math. 181 (2015), 361-382. arXiv:1307.0874.
  https://arxiv.org/abs/1307.0874 , https://doi.org/10.4007/annals.2015.181.1.6
- P. Balister, B. Bollobas, R. Morris, J. Sahasrabudhe, M. Tiba,
  On the Erdos covering problem: the density of the uncovered set,
  Invent. Math. 228 (2022), 377-414.
  https://doi.org/10.1007/s00222-021-01087-5
  (Note: draft citation URL arXiv:1904.09667 is erroneous and resolves to an
  unrelated scheduling paper; corrected here.)
- J. Zhang, S. Zhang, A Distinct Covering System with Minimum Modulus 7 and
  Minimal Least Common Multiple 10080, arXiv:2607.19029 (2026).
  https://arxiv.org/abs/2607.19029
- Covering system — Wikipedia (Mirsky-Newman, classic 2,3,4,6,12).
Searches performed: distinct covering maximal density nine moduli; Hough
Balister minimum modulus; Erdos covering bounded moduli census (no prior
D*(9;[7,60]) table found).
