# Isomorphism-type census of maximum intersecting 3-families on [6] (EKR n=2k degeneracy): N=13

## Context
For n=2k the Erdős–Ko–Rado theorem gives the bound |F| ≤ (1/2)C(2k,k) with no uniqueness: every choice of exactly one member from each complementary pair {T, [n]\T} is maximum. The Hilton–Milner theorem requires n>2k and is inapplicable. McKenna (2005) proves the number of isomorphism classes of maximal intersecting k-families is bounded by a function of k, without determining exact values. No prior source records the exact isomorphism-type count at the smallest degeneracy (n,k)=(6,3).

## Definitions
- Ground set [6]={1,...,6}. Family F ⊆ C([6],3) is intersecting if A∩B≠∅ for all A,B∈F.
- Maximum means |F|=10=(1/2)C(6,3). The size bound itself is classical EKR, not claimed new.
- Isomorphism is via S₆ (permutations of [6]); types are S₆-orbits.
- Star S={F:1∈F}. Triangle T={A:|A∩{1,2,3}|≥2}. Shifted means fixed under all Frankl ij-shifts for natural order 1<...<6.

## Result
There are exactly N=13 S₆-orbits of maximum intersecting 3-families on [6]. Representatives (shorthand abc={a,b,c}), orbit sizes, and stabilizer orders:

| # | representative | orbit | |Stab| | shifted? |
|---|---|---|---|---|
| 0 | 123,124,125,126,134,135,136,145,146,156 | 6 | 120 | yes (star) |
| 1 | 124,125,126,134,135,136,145,146,156,456 | 60 | 12 | no |
| 2 | 125,126,134,135,136,145,146,156,356,456 | 180 | 4 | no |
| 3 | 125,126,135,136,145,146,156,256,356,456 | 20 | 36 | no (triangle up to iso) |
| 4 | 126,134,135,136,145,146,156,346,356,456 | 60 | 12 | no |
| 5 | 123,124,126,135,136,145,146,156,256,346 | 90 | 8 | no |
| 6 | 124,126,135,136,145,146,156,256,346,456 | 180 | 4 | no |
| 7 | 134,135,136,145,146,156,345,346,356,456 | 6 | 120 | no (all C(5,3)=10 triples of {1,3,4,5,6}) |
| 8 | 123,124,135,136,145,146,156,256,345,346 | 180 | 4 | no |
| 9 | 124,135,136,145,146,156,256,345,346,456 | 90 | 8 | no |
| 10 | 123,125,136,145,146,156,246,256,345,356 | 120 | 6 | no |
| 11 | 123,145,146,156,245,246,256,345,346,356 | 20 | 36 | no |
| 12 | 123,124,135,146,156,236,245,256,345,346 | 12 | 60 | no |

Orbit sizes sum to 6+60+180+20+60+90+180+6+180+90+120+20+12=1024. Star (type #0, stab 120) and triangle (type #3, stab 36) are maximum, non-isomorphic, distinguished by stabilizer order. Only the star is shifted. Types #10/#11 share degree sequence (6,6,6,4,4,4) and intersection profile (27×1,18×2) but differ in stabilizer order (6 vs 36); all 13 triples (degree sequence, intersection multiset, stabilizer order) are pairwise distinct. Type #12 is regular of degree (5⁶) with profile (30×1,15×2).

## Proof / evidence
Size bound: the 20 triples partition into 10 complementary pairs; an intersecting family takes at most one per pair, so |F|≤10 with equality iff exactly one per pair. On 6 points two 3-sets are disjoint iff complementary, so all 2^10=1024 transversals are intersecting and these are all labeled maxima. Enumeration: all 1024 transversals grouped by lexicographically minimal image under all 720 perms of S₆ (canonical form) yield 13 classes; stabilizer orders by brute force over S₆ satisfy |orb|=720/|Stab| per class and orbit sizes sum to 1024, proving completeness and pairwise non-isomorphism. Independent Katona-circle recheck from stored lists: on each of the 60 distinct 6-arc circle systems every representative contains at most 3 of the 6 circle 3-arcs (maximum exactly 3). Shifting-status by direct Frankl ij-shift test. Machine-checked in stdlib Python in seconds; see Reproducibility.

## Limitations
- Classification up to S₆ only (standard notion); complement maps absorbed via relabeling.
- Shifting-status relative to natural vertex order 1<...<6.
- Size bound 10 is classical EKR, not new; novelty is N=13 with representatives/certificates.
- No claim beyond (n,k)=(6,3); no general criterion or completed census at other parameters.

## Reproducibility
```
python3 output/artifacts/verify.py
# VERIFY_OK: 13 types, 1024 labeled families, all certificates replay
```
Stdlib only. Verifier checks from census.json alone: size 10, pairwise-intersecting, one-per-complementary-pair, canonical-form match and distinctness, stabilizer orders and orbit sizes summing to 1024, Katona ≤3 arcs on all 60 circles. Independently re-enumerated by auditor (fresh 2^10 enumeration + canonical grouping) with byte-for-byte agreement on N, stabs, orbits, and representatives.

## References
- P. Erdős, C. Ko, R. Rado, Intersection theorems for systems of finite sets, Quart. J. Math. 12 (1961). Size bound at n=2k.
- P. Frankl, Z. Füredi, A new short proof of the EKR theorem, arXiv:1108.2179 (2011). Uniqueness only for n>2k.
- A. J. W. Hilton, E. C. Milner, Some intersection theorems for systems of finite sets, Quart. J. Math. 18 (1967). Requires n>2k.
- OEIS A325982, Hilton–Milner triangle (n>2k only). https://oeis.org/A325982
- G. McKenna, Isomorphism classes of maximal intersecting uniform families are few, Electron. J. Combin. 12:R67 (2005). https://doi.org/10.37236/1964
