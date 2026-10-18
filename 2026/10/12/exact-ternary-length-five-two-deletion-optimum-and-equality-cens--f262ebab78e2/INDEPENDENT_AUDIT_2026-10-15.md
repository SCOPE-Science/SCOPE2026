# Independent mathematical audit

## correctness

PASS

Define distinct two-deletion shadows D2(x)⊂Σ³ for all 243 words in Σ⁵. Code legality is exactly pairwise disjointness, equivalently LCS≤2 and compatibility-graph clique. Independent exhaustive enumeration using Python itertools and NetworkX maximal-clique search (not the packaged verifier) regenerated all 243 shadows; found largest clique size 6 and exactly 478 size-six cliques among 181053 maximal cliques. Direct second enumeration over natural S3 symbol permutations and coordinate reversal gave 46 orbits, with size distribution 2^1,4^2,6^8,12^35. Shadow-cardinality histogram over all 478 maximum codes was 18:2,19:12,20:54,21:100,22:144,23:96,24:52,25:18. All cover fewer than 27 received words. Finite exhaustive graph search is a valid proof for this finite case because the entire finite 3^5 graph was built and enumerated; it is not extrapolated to other lengths. The packaged checker separately cross-checks 29403 pairwise LCS constraints, maximum clique search and fixed-size recursion.

## originality

PASS

Chee–Ge–Ling (2010) treat perfect deletion correcting code size spectra, particularly (3,1) and (4,2) at t=n−2; they do not provide unrestricted (5,2)_3 equality census. Kulkarni–Kiyavash general multiple-deletion upper bound specializes to 14 codewords here, which neither establishes exact 6 nor determines 478 labeled maxima, 46 natural orbits or the coverage distribution. Published Resultary ternary length-five single-deletion code result solves a different t=1 problem; no dominating t=2 table or exact 478 census was found. Remaining risk is an unindexed finite enumeration.

## value

PASS

The exact A_3(5,2)=6 closes a real finite extremal gap (published general upper bound 14) at the first length beyond the classical q=3 length-four t=n−2 design setting. Enumerating all equality cases and orbit/coverage distributions identifies nonperfect optimal configurations and furnishes a reproducible benchmark for deletion-correcting code classification, a motivated natural finite invariant even without an all-n formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
