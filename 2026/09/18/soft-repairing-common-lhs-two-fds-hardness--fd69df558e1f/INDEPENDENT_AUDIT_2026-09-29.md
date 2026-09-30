# Independent audit — 2026-09-29

Record: `2026/09/18/soft-repairing-common-lhs-two-fds-hardness--fd69df558e1f`  
Assigned and audited source tree: `83b681dbd86270dadc319a5556616ec62639418b`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `013b006da5ec3c7759aca4164274eba37d6e9710`  
Disposition: **passed**

## Correctness

**independently_supported**. The CLIQUE reduction checks algebraically. With a common A-value, the two soft-FD violation counts sum to s^2-(1/2)sum_v x_v^2-(1/2)sum_c y_c^2. In the padded incidence graph every right degree is at most two, so the utility is (W+1/2)s-s^2+(1/2)sum_v x_v^2+z. For D0=2m+1 and the stated uniform integer weight, the convex degree bound gives a loss of at least m+1 whenever s differs from rD0, while at s=rD0 every nonsaturated degree vector loses at least 2m in the base term. Since z<=m, every optimizer is exactly the union of r full left stars, after which z is the number of graph edges induced by the selected r vertices. The threshold therefore detects an r-clique. I independently checked the critical gap formula over multiple D0 and r values, and the committed exhaustive checker is consistent with the closed form.

## Originality

**supported_named_open_case**. Carmeli--Grohe--Kimelfeld--Livshits--Tibi explicitly list {A->B,A->C} among the simplest unresolved soft-repair FD sets in the open-access 2024 TODS article. Searches through 29 September 2026 did not locate a later exact classification of this fixed set. Recent approximation and quadratic degree-sequence results do not supply the cardinality-locking step needed here. The originality assessment is therefore supported for closing this named exact-complexity case, subject to normal very-recent indexing risk.

## Scientific value

**high_value_complexity_classification**. The result closes a concrete open classification case and shows hardness even with unit FD weights, one A-block, and uniform tuple weight. It sharply separates soft semantics from the logically equivalent single hard FD A->BC. It does not determine the best approximation factor or hardness under unit tuple weights.

## Literature and evidence checked

- https://doi.org/10.1145/3651156
- https://arxiv.org/abs/2009.13821
- https://doi.org/10.1109/TKDE.2026.3689023
- https://arxiv.org/abs/2608.05827
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/18/soft-repairing-common-lhs-two-fds-hardness--fd69df558e1f
## Limitations

- The reduction uses a common tuple weight depending on the CLIQUE instance; it does not prove hardness for unit tuple weights.
- The theorem concerns tuple deletion under the pairwise-violation soft-FD semantics, not update repairs.
- The source open problem is recent enough that a simultaneous or poorly indexed resolution cannot be ruled out.
