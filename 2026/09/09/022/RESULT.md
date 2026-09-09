# Exact rank-profile census of antichains in T5 and M6 with Dilworth width certificates

## Context
Width, shadows, and rank profiles of Boolean lattices underlie Sperner theory,
Peck-poset phenomena, Kruskal–Katona shadows, and monotone-Boolean-function
classification, where exact small-n profiles serve as conjecture tests and
benchmarks. Only Dedekind totals and size-only counts were tabulated for these
scopes; the joint rank-layer distribution was missing.

## Definitions
Let B_n be the Boolean lattice of subsets of [n] under inclusion.
- T5 = {S subset of [5] : 1 <= |S| <= 4} (30 elements; rank sizes 5,10,10,5).
- M6 = {S subset of [6] : 2 <= |S| <= 4} (50 elements; rank sizes 15,20,15).
For an antichain A, its rank profile is the vector (a_i) with
a_i = |A intersect rank i|. Elements are integer bitmasks on {0,...,n-1}.

## Result
1. T5 has exactly 7579 antichains in exactly 94 distinct rank profiles
   (a1,a2,a3,a4). Full table: output/artifacts/t5_profiles.csv
   (SHA-256 d9d3ee25e6a1d1afe7628c15b382d718cb0851aeca5e3d0026659950a9b280bf).
   Size distribution (s:n_s): 0:1, 1:30, 2:285, 3:1090, 4:2020, 5:2146,
   6:1380, 7:490, 8:115, 9:20, 10:2. Largest cell (0,2,2,0) -> 390.
   The two size-10 antichains are the full rank-2 and rank-3 layers.
2. M6 has exactly 7741776 antichains in exactly 362 distinct rank profiles
   (a2,a3,a4). Full table: output/artifacts/m6_profiles.csv
   (SHA-256 d538c23cb1095e30088010b7963a3c85b31aeddeb3256f4c4d0787727b46689d).
   Size distribution: 0:1, 1:50, 2:1015, 3:10990, 4:70435, 5:282150,
   6:734395, 7:1291890, 8:1607400, 9:1482850, 10:1067531, 11:635020,
   12:326990, 13:147440, 14:57675, 15:19238, 16:5325, 17:1170, 18:190,
   19:20, 20:1. Largest cells (1,8,0) and (0,8,1) -> 193050 each;
   (0,10,0) -> 184756 = C(20,10); unique maximum (0,20,0) -> 1.
3. width(T5) = 10, witnessed by the full rank-3 layer, with an explicit
   10-chain partition covering all 30 elements (output/artifacts/t5_chains.csv).
   width(M6) = 20, witnessed by the full rank-3 layer, with an explicit
   20-chain partition covering all 50 elements (output/artifacts/m6_chains.csv).
Complement symmetry holds on every cell:
N(a1,a2,a3,a4) = N(a4,a3,a2,a1) (T5); N(a2,a3,a4) = N(a4,a3,a2) (M6).

## Proof / evidence
Computed enumerations with machine verification (not hand proofs):
(a) C backtracking enumerator output/artifacts/enum.c (rank-major order,
include/exclude with comparability mask, NE <= 50 in uint64_t), deterministic;
(b) independent pure-Python T5 re-enumeration agreeing bit-for-bit
(7579 antichains, 94 cells); (c) stdlib verifier output/artifacts/verify.py
checking every stored witness (94+362) by pairwise incomparability and profile
consistency, symmetry, row-sum/size arithmetic, Dedekind cross-check
T5+2 = 7581 = D5, chain-cover validation (coverage exactly once, chains totally
ordered, #chains = layer width), Sperner-gap residuals; prints VERIFY_OK;
(d) clean-room recompile-and-rerun reproduces all tables bit-for-bit
(REPLAY_BITFORBIT_OK, FNV-1a T5 90874e3a3522b945, M6 d7721c7214b2e724).
Width claims are proofs: Dilworth upper bound from the chain cover plus the
middle-layer antichain lower bound.

## Limitations
- M6 is verified by witness re-checking, symmetry, and marginal arithmetic,
  not by a second independent full enumeration (T5 has one).
- Only the stated slices T5, M6 are covered; no claim about full B6, maximal
  antichains, or asymptotics.
- Width values 10 and 20 alone follow from layer sizes; the new content is the
  complete profile-frequency tables plus the certificate bundle.

## Reproducibility
```sh
cd output/artifacts
gcc -O2 -o enum enum.c
./enum 5 1 4 t5        # -> t5_profiles.csv, t5_witnesses.csv, t5_summary.txt
./enum 6 2 4 m6        # -> m6_profiles.csv, m6_witnesses.csv, m6_summary.txt
python3 chains.py      # -> t5_chains.csv, m6_chains.csv
python3 verify.py      # expect VERIFY_OK
```
Expected hashes: t5_profiles.csv
d9d3ee25e6a1d1afe7628c15b382d718cb0851aeca5e3d0026659950a9b280bf;
m6_profiles.csv d538c23cb1095e30088010b7963a3c85b31aeddeb3256f4c4d0787727b46689d.

## References
- OEIS A000372 (Dedekind numbers / antichains; totals only).
- OEIS A059119 (size-only triangle a(n,m); no joint rank-layer distribution).
- P. De Causmaecker, S. De Wannemacker, On the number of antichains of sets in
  a finite universe, arXiv:1407.4288 (interval-decomposition totals to n=8).
- L. Ilinca, J. Kahn, Counting maximal antichains and independent sets,
  Order 30(2) (2013) 427-435; arXiv:1202.4427 (log-asymptotics, maximal-only).
