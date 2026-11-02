# Self-review

## Correctness — PASS

The theorem quantifies over every finite positive sequence with two identical additive agents and three possible item values. Its fundamental inequality compares the myopic value imbalance with the absolute signed imbalance of an *arbitrary* competitor, not just an optimally selected competitor. The displayed 24-entry potential is nonnegative and starts at zero. All 408 small signed transitions were checked from the standalone file, while the analytically bounded complement covers every signed imbalance of magnitude at least nine. Telescoping proves the universal bound for all horizons. The repeating explicit sequence gives a valid limiting lower bound; its comparison allocation need not be optimal. A separate exact DP confirmed all 29,523 sequences through length nine and the certificate checker confirmed 501 witness parameters.

Risks: finite verification cannot replace the unbounded-state argument; that argument is explicitly given. The theorem does not cover zero/negative items, arbitrary item magnitudes, or more than two agents.

## Originality — PASS (qualified self-review)

The natural prior model is Goldberg, Robinson and Teh (arXiv:2610.09843v1, public posting 2026-10-07). Its accessible abstract discusses unrestricted fixed-order hardness and an approximation for a **reorderable** variant. Those statements neither establish nor refute the fixed-order ternary-alphabet ratio. The original full text could not be materially inspected, so it is NOT marked as proved non-covering. Earlier mathematical results for item values in two levels establish greedy exactness, and an exact formula for sequences with one exceptional item does not entail a sharp worst-case ratio for arbitrarily many alternating 1,2,3 items. published-finding corpus semantic searches on the full theorem and aliases found no claim with matching implications among the returned results; this is not considered a proof of originality.

Residual risk: the original forty-page source or unpublished/unindexed literature could already contain a comparable ternary-alphabet guarantee. Independent priority evaluation is warranted.

## Value — PASS

The result gives a global sharp performance guarantee for an elementary real-time fair-allocation rule in the first small integer value range beyond the exactly greedy-solvable two-level case. Arbitrarily long sequences amplify the cost of short-term balancing but the total penalty remains uniformly bounded by 5/3, with an explicit extremal family. This is a structural online-versus-offline frontier, not a finite census or a numerical improvement measured at a single chosen horizon.

## Scope and literature limitations

The source of the cumulative-maximum-envy objective was inspected at the abstract level only; the relevant original full paper could not be read. The comparison concerns a fixed order and multiplicative cumulative-envy cost. No stronger claim about all value alphabets, reordering, or the complexity of offline optimization is made.

Self-review: passed. Independent audit: not yet performed.
