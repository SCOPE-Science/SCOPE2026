# Review status

Independent audit date: 2026-09-30 UTC.

Disposition: **passed**.

Correctness: PASS. The eight committed witnesses were checked from their edge lists against explicit six-cycle constraints. Independently, a binary mixed-integer formulation with one inequality for every six-cycle gives exact optima 13, 16, and 20 for n=7,8,9. For n=10, the same model was split by the maximum degree d, fixing a maximum-degree vertex by relabeling; the independent optima for d=5,6,7,8,9 are 21,20,20,21,21, so no 22-edge C6-free graph exists. This independently proves ex(10,C6)=21 and agrees with the committed branch-and-bound logic.

Originality: PASS. The inspected primary C6 extremal paper proves asymptotic upper bounds and does not determine any of the finite values n=7 through 10. Survey/construction papers cited by the record address asymptotics or different forbidden families. Exact-phrase web searches and Resultary searches did not identify an earlier table containing 13,16,20,21 with C6-free witnesses. The originality conclusion is based on non-implication of the inspected theorems plus database searches, not on search failure alone.

Scientific value: PASS. Exact small Turán numbers are natural boundary data for a central extremal problem. Four consecutive exact values with explicit extremal witnesses are useful calibration cases for future theory and exact solvers; the n=11 through 14 rows are correctly limited to lower bounds and do not carry the value judgment.

Evidence: `INDEPENDENT_AUDIT_2026-09-30.md` and `INDEPENDENT_AUDIT_2026-09-30.json`.
