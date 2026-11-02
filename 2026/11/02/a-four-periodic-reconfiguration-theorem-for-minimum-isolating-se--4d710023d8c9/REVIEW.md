# Self-review

## Correctness

**PASS.** The condition that no cycle edge survives deletion of the selected closed neighborhoods is equivalent to forbidding four consecutive unselected vertices. This makes every cyclic selected-vertex spacing at most four. The deficit composition gives an exact count without duplicate rooted configurations. The replacement interval is of length between five and eight, and has precisely one plus the sum of the adjacent deficits valid insertion sites. Counting each uniquely deleted selected vertex proves regular degree. Unit transfers connect all nonzero-deficit compositions, and a circulating deficit translates all selected vertices by one, closing the possible phase obstruction. Independent direct and composition-based finite programs corroborate all parameters in their stated ranges. The separate order-four exception is explicit.

## Originality

**PASS, with residual historical risk.** Caro and Hansberg's 2015 first-public preprint already gives the cycle isolation number, which is expressly excluded from novelty. Mynhardt and Nasserasr's 2020 survey describes reconfiguration of domination sets, not the complete minimum-isolating-set exchange graph. Boyer and Goddard's 2024 isolation paper addresses disjoint sets and order-bound equality, not this complete minimum-set configuration graph. The closest related historical configuration claim concerns maximal independent sets on cycles, with a different feasibility condition and different gap restrictions. No inspected prior source implies the new cardinality, uniform-degree, and divisibility-sensitive connectedness theorem. Unindexed work using the alias “vertex-edge domination” is a residual risk.

## Value

**PASS.** Minimum isolating sets are optimal edge-monitor placements that permit some undominated vertices. The theorem determines how many optimal placements there are, exactly how many one-sensor replacements are possible from *every* placement, and precisely when all optimal placements can be converted into one another without ever increasing their cardinality. The sharp transition between a four-component frozen family and regular connected families—and the complete cycle isomorphism in one congruence class—is a natural structural result rather than a restatement of the known isolation number. The full cyclic-gap exchange description permits further metric or sampling questions without asserting results not established here.

## Scope and limitations

The result covers every labelled ordinary cycle of order at least five, but neither nonminimum sets nor other graph families. Complete diameters of the connected degree-four and degree-six families are not claimed. Both verifiers are finite corroboration, not independent external assessment. The known cycle isolation number and generic replacement-graph definitions are credited explicitly.

Self-review: passed. Independent audit: not yet performed.
