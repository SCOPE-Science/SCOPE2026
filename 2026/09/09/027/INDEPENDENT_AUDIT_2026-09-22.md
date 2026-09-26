# Independent audit — 2026-09-22

Record: SCOPE-20260909-027. Examined 2026-09-26.

## Correctness — PASS for intrinsic defects; protocol result bounded
The shipped verifier returned VERIFY_OK on all 73 types: pairwise non-isomorphism in 1,327 same-size pairs, closure under 893 available flips, closed triangulation checks and Willmore replay from stored positions to 1.5e−14. I independently reconstructed all vertex degrees from edges and checked E=3n−6, F=2n−4, each defect multiset 6−degree, and sum of defects twelve. Type counts 1,1,2,5,14,50 and distinct defect counts 1,1,2,5,13,33 agree. The only repeated defect row at n=8 is (0,0,1,1,2,2,3,3), twice; T9_0 is largest only among the stored protocol P0 positions. Flip-closure plus the cited connectivity theorem supplies completeness. Unit edge lengths describe an intrinsic piecewise-equilateral metric; they do not automatically supply a unit-edge Euclidean embedding for every type. The secondary Willmore numbers are realization dependent and the protocol dynamics were not independently regenerated.

## Originality — PASS, narrowly
The 73 triangulation types and their counts are preexisting plantri data, and equilateral defect is simply 6−degree. Plantri even distributes a degree-sequence counting plugin. The checked guide and Bobenko paper do not present this specific per-type defect census and its first repeated multiset at eight vertices with validated representatives. This is a bounded data finding, not a new Gauss–Bonnet law or a geometric Willmore optimum.

## Scientific value — PASS, bounded
The complete defect-degree mapping and the smallest same-defect nonisomorphic pair provide exact small-sphere counterexamples to defect-profile classification. The arbitrary spring-embedding maximum has only reproducibility value under P0 and is not relied upon for the scientific verdict.

Sources: [plantri guide](https://github.com/mishun/plantri/blob/master/plantri-guide.txt), [OEIS A000109](https://oeis.org/A000109), [Bobenko, arXiv:0707.1318](https://arxiv.org/abs/0707.1318). Repository evidence: artifacts/census.json and verify.py.
