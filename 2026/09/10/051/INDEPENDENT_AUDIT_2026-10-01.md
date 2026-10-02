# Independent mathematical audit — Deep four-row Kronecker vanishing ray disproved: g((9,7,5,3),(8,7,5,4),(7,6,6,5))=134682 at n=24

Outcome: **PASSED**.

## Correctness
**PASS** — A fresh computation using a Jacobi–Trudi/Frobenius-character route, independent of the package's Murnaghan–Nakayama recursion, reproduced the exact integer coefficient 134682 for the stated triple at n=24. The class count is 1575 and 671 conjugacy classes contribute nonzero terms. The package's own character orthogonality, hook-dimension, permutation-symmetry and tensor-dimension checks are consistent with this result.

## Originality
**PASS** — Statement-level comparison found no prior source giving this exact coefficient or a stronger theorem forcing it positive. Mishna–Trandafir give general vector-partition formulas, vanishing conditions and stable faces, but their Theorem 4.5 does not determine this four-row triple. Exact-tuple web and mathematical-record searches returned the present record rather than an earlier covering result.

## Value
**PASS** — The result falsifies an infinite structured vanishing-ray claim with a deep four-row counterexample, rather than merely reporting an isolated random coefficient. Exact positivity at the first tested ray point is a meaningful boundary datum for Kronecker vanishing geometry and atomic-vanishing heuristics.

## Originality comparison
- Equivalent formulations: Exact positivity of the stated S_24 Kronecker coefficient is equivalent to occurrence of the irreducible indexed by (7,6,6,5) in the tensor product indexed by (9,7,5,3) and (8,7,5,4).
- Broader coverage: General Kronecker vanishing inequalities and vector-partition formulas were inspected; none determined this target value.
- Exact database or table: Exact semantic searches for the triple and value found no prior covering table/result beyond the present record.
- Claim versus prior implication: The inspected prior work supplies tests and formulas, not a theorem forcing the target coefficient; the exact positive value therefore is not a corollary of those statements.

## Sources inspected
- **Mishna and Trandafir, Estimating and computing Kronecker Coefficients: a vector partition function approach, Australas. J. Combin. 90 (2024), 121–154** (https://ajc.maths.uq.edu.au/pdf/90/ajc_v90_p121.pdf) — Full-text sections around Lemma 4.4 and Theorem 4.5, plus the stable-face discussion. General vanishing inequalities and stable faces were compared at statement level; they do not state or mechanically imply the exact target coefficient.
- **Resultary mathematical research index** — Semantic search for the exact three partitions, value 134682, and four-row vanishing ray; nearest returned exact hit was the present record, with other Kronecker records not covering the same triple. No stronger prior record was found; this search is supplementary, not a proof of novelty.

## Residual risks
- The audit proves the single m=6 counterexample; it does not classify other members of the proposed ray.
- Kronecker-coefficient literature is broad; absence of an exact hit is not itself novelty proof. The conclusion rests on the inspected general vanishing results not implying the target value.
- Value is attached to the structured ray/vanishing question, not to the bare integer 134682 in isolation.
