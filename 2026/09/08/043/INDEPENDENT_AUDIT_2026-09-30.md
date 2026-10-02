# Independent audit — 2026-09-30

**Record:** `2026/09/08/043`  
**Audited source tree:** `48bb1fc950ff27bab3cae2f5afde7aab24f16335`

## Final claim assessed

Exact small-n hexagon Turan numbers ex(7..10,C6)=13,16,20,21 with certified C6-free witnesses through n=14

## Correctness — PASS

The eight committed witnesses were checked from their edge lists against explicit six-cycle constraints. Independently, a binary mixed-integer formulation with one inequality for every six-cycle gives exact optima 13, 16, and 20 for n=7,8,9. For n=10, the same model was split by the maximum degree d, fixing a maximum-degree vertex by relabeling; the independent optima for d=5,6,7,8,9 are 21,20,20,21,21, so no 22-edge C6-free graph exists. This independently proves ex(10,C6)=21 and agrees with the committed branch-and-bound logic.

## Originality — PASS

The inspected primary C6 extremal paper proves asymptotic upper bounds and does not determine any of the finite values n=7 through 10. Survey/construction papers cited by the record address asymptotics or different forbidden families. Exact-phrase web searches and Resultary searches did not identify an earlier table containing 13,16,20,21 with C6-free witnesses. The originality conclusion is based on non-implication of the inspected theorems plus database searches, not on search failure alone.

The comparison explicitly checked equivalent formulations, broader coverage, exact database/table matches, and whether prior results logically imply the claim. An unsuccessful search was not treated as proof of novelty.

## Scientific value — PASS

Exact small Turán numbers are natural boundary data for a central extremal problem. Four consecutive exact values with explicit extremal witnesses are useful calibration cases for future theory and exact solvers; the n=11 through 14 rows are correctly limited to lower bounds and do not carry the value judgment.

## Source inspections

- **He — New Upper Bound on Extremal Number of Even Cycles** — Full-text PDF: abstract, introduction, Theorem 1, and the scope of the even-cycle upper bound. Asymptotic/general upper bounds; no exact small-n C6 table or implication of 13,16,20,21. https://arxiv.org/abs/2009.04590
- **Füredi and Simonovits — The history of degenerate (bipartite) extremal graph problems** — Record-cited survey scope was compared with the finite claim. Historical/asymptotic survey context, not a finite ex(n,C6) database covering n=7 through 10. https://arxiv.org/abs/1306.5167
- **Resultary semantic search for exact small C6 Turán numbers** — Top ranked result set and related extremal records. The exact n=7 through 10 C6 table is this record; other hits concern different forbidden graphs or hypergraphs. https://github.com/Resultary/2026/tree/main/2026/9/8/SCOPE043

## Residual risks

- The optimality certificates are computational and the committed package does not archive an entire branch-and-bound search tree.
- The originality search cannot exclude an obscure unpublished database; no covering published table was located.

## Disposition

**PASS.** Correctness, originality, and scientific value each pass for the final claim stated above.
