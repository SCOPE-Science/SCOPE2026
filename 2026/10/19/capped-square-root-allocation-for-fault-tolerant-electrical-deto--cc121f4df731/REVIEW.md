# Scientific review: capped square-root allocation for electrical detours

## Correctness — PASS

For an edge of a cactus, its replacement path is the rest of its unique cycle; pendant blocks transmit no injected current, giving an exact edge-deletion resistance as a sum of reciprocal conductances. The normalized one-cycle expenditure is strictly convex in the edge resistances. The stated threshold has a unique positive root, and the explicit nonnegative multipliers satisfy feasibility, complementary slackness, and stationarity. The convex KKT theorem therefore gives the unique solution; homogeneous scaling and cyclewise budget accounting give the global lower bound and an attaining allocation. Exact threshold equality is covered. The reproducibility program provides 945 finite checks; the infinite-family proof is analytical.

## Originality — PASS, with residual risk

The inspected material of Ghosh–Boyd–Saberi (2008) treats nominal effective-resistance objectives over intact networks, not post-outage endpoint detours. Johnson–Chertkov (2010) analyzes a general network design problem with one-line failure, but their power-flow dissipation objective and inspected optimization statements do not give the stated arbitrary-cost cactus formula or the exceptional-price cutoff. Suliman–Weinstein (2023) treats maximum effective resistance on intact edges, and its design criterion is not the replacement-path resistance studied here. Semantic searches for edge-deletion endpoint resistance, cactus design, alternate-path minimax allocation and square-root pricing found no matching exact classification. An unindexed equivalent result or a special case of a stronger unpublished optimization theorem remains possible; searches do not certify novelty.

## Value — PASS

Worst-case electrical detour after one connection fails is a natural fault-tolerance criterion: it quantifies the resistance of the replacement route. The theorem supplies the exact globally optimal conductance of every edge on all finite bridgeless cacti with arbitrary positive prices, including a unique price-truncation rule, a budget decomposition across cycles, and a sharp equal-conductance plateau on heterogeneous cycles. These are complete structural rules rather than a numerical example or routine restatement of the intact-network problem.

## Scope and limits

Single failures only; no bridges or overlapping cycles; linear conductance cost; no claim about post-failure all-pairs resistance or arbitrary network topology. Independent scientific validation is still required.

Self-review: passed. Independent audit: not yet performed.
