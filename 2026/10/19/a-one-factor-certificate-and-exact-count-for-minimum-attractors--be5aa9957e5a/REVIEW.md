# Scientific review

## Correctness — PASS
The exact scope is all \(q\ge2\), \(k\ge1\) and \(0\le r<q\) for injectively labeled periods. The proof first forces one position per alphabet letter in any optimal set. It then exhausts *all* possibilities for a missed factor by separating nonwrapping short factors, wrapping short factors, and factors of length at least one full period. These cases imply the same explicit boundary condition. The canonical crossing factor has exactly the exclusions prescribed, so the equivalence is both necessary and sufficient. Count and first-cycle boundary follow without limits or asymptotics. The standalone checker independently enumerates the complete factor occurrence masks of 117132 candidate sets across 108 finite parameter instances; this is corroborative evidence.

## Originality — PASS (with stated uncertainty)
Compared by implication with the 2023 morphic-string-attractor theorems, the 2022 episturmian minimum-size result, and the 2026 complete attractor classifications for Fibonacci and period-doubling words. These concern different families or existence/size rather than the exact count and single-factor certificate for all finite prefixes of injective periodic words. An existing binary complete-period special case yields \(k^2-1\) but does not imply the claimed general alphabet and truncated-prefix classification. Search of public research records gave that binary case as the closest hit and no displayed stronger coverage. Its original complete text was not accessible during this comparison; this is a residual originality risk, not a claim that it was fully inspected. Other unindexed work remains possible.

## Mathematical value — PASS
The count and the one-factor criterion solve the *complete* minimum-attractor classification for a canonical infinite family over arbitrary alphabet size and at every finite cutoff. The exceptional-condition geometry quantifies how a newly appended partial period changes the optimal solutions, with a sharp transition at suffix length \(q-1\). Every candidate optimal set can be checked against one explicit factor despite the number of distinct factors growing with length. This is not a mere recomputation of minimum cardinality or a single arbitrary finite instance.

## Limitations
No assertion about noninjective periods, general morphic sequences, or independent validation. The published binary case and existing minimum-cardinality observations are not claimed novel.

Self-review: passed. Independent audit: not yet performed.
