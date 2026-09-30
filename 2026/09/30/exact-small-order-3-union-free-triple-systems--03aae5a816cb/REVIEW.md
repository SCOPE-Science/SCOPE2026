# Review
## Correctness assessment
PASS. The pair-star lower bound is direct. For the upper bound, the insertion test records exactly every union created by a new edge together with up to two earlier edges, so rejecting collisions is equivalent to maintaining 3-union-freeness. Heredity reduces the bound to excluding exactly \(n-1\) edges, and vertex symmetry justifies fixing one edge. Two independently written exact implementations agree for every \(n=4,\ldots,9\). The equality count is then converted to the global classification by a transparent incidence double count.
## Originality assessment
PASS on a best-of-knowledge basis. Targeted semantic searches were repeated against the final theorem, the pair-star equality description, the constant-weight separable-code formulation, and the small orders. The closest current literature treats \(U_3(n,3)\) as an exceptional asymptotic regime rather than giving these exact finite values. The closest retrieved constant-weight result concerns the stronger 2-cover-free condition and does not state this theorem or classification.
## Value assessment
PASS. The result gives exact initial values and a complete equality classification in a regime explicitly excluded from a current general theorem and known to become superlinear asymptotically. The finite transition data and reproducible certificates can serve as benchmarks for future structural or computational work on 3-union-free triple systems.
## Closest literature
The principal comparison is Liu–Shangguan–Zhang, arXiv:2605.11949v1, together with the overlapping earlier arXiv:2411.07908v1. A nearby but non-equivalent result identifies extremal 3-uniform 2-cover-free families with maximum triple packings. No located source states the exact values \(U_3(n,3)=n-2\) for all \(4\le n\le9\) together with unique pair-star equality.
## Scientific limitations
The theorem is finite and computer-assisted, with no statement beyond nine vertices. The literature check is substantial but cannot prove the absence of every historical small-order computation under all terminology.
Same-model review: passed. Independent audit: not yet performed.


The revised package received a same-model three-axis review on 2026-09-30 UTC. See AUDIT.json for actual comparisons, replay scope and residual risks. No independent audit or external certification is asserted.
