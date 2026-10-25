# Scientific review: A sharp online proportionality threshold for forest eligibility graphs

## Correctness — PASS

For unit pair-eligible goods, the shortfall is exactly the signed endpoint-degree discrepancy; Prop1 is equivalent to signed shortfall at most two. Under larger-deficit-first allocation, a losing endpoint newly reaching positive deficit \(r\) requires two disjoint prior components with deficits at least \(r-1\), hence a component of size at least \(2^r\). Conversely, an adaptive binary merge of two marked level-\((r-1)\) trees forces one marked endpoint to deficit \(r\), without cycles or reassignment. Padding preserves a previous prefix witness. The proof covers all integer agent counts and all admissible forest horizons. The supplied exact state-game checker confirms the small cases; finite checking is not the proof.

## Originality — PASS (qualified)

The closest primary 2026 eligibility-constrained work proves approximate rather than exact online Prop1 and its general-instance negative construction does not stay in a forest. Published forest-orientation work contains the doubling argument behind a related logarithmic **outdegree** upper bound, which by elementary implication also bounds signed shortfall; that upper fact alone is not claimed as new. A recourse-based discrepancy result can obtain constant discrepancy, but reorients old edges and therefore does not dominate the irrevocable statement. The contribution assessed is the complete exact prefix minimax equality together with the sharp seven-agent feasible/eight-agent impossible threshold for eligibility-aware goods Prop1. Relevant comparisons, source sections, and remaining priority risk from possibly implicit folklore are recorded in AUDIT.json.

## Value — PASS

The recent eligibility-aware online fair-division model distinguishes offline existence from online maintenance. Acyclic pair eligibility is a natural, operationally important restriction; the exact forest threshold tells a designer when **unrevisable** allocations retain exact proportionality up to one good and precisely when an adversary can destroy it despite using no cycles or duplicate pairs. The dimension-free per-prefix proof and seven-edge obstruction are useful structural limits, not an arbitrary finite recomputation.

## Scope and residual risk

Only unit-valued goods with exactly two eligible agents, acyclic cumulative eligibility, immediate irrevocable assignment, and an assignment-observing adversary are analyzed. The lower bound is not claimed for oblivious adversaries; the result concerns one-sided signed deficits, not absolute discrepancy. Priority against unpublished or unsearched combinatorial folklore is not independently certified. Finite validation covers only the sizes specified in VERIFICATION.md.

Self-review: passed. Independent audit: not yet performed.
