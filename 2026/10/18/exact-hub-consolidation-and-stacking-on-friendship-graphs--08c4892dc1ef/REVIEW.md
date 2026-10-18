# Scientific review

## Correctness — PASS
The proof reconstructs the entire pebbling model, the exceptional parity indicator, and the one-step monotone surplus. Local elimination sequences are explicit for every parity and zero-coordinate case. The order of elimination is feasible whenever the surplus is positive, and the converse for arbitrary destinations handles the three-pebble terminal exception by inspecting its immediate predecessor. The sharp threshold is proved for every integer \(k\ge2\) by a strict surplus inequality and an explicit nonstackable configuration of size \(4k-1\). Independent finite dynamic programming checked 2,094,681 configurations over four friendship-graph orders, including both reachability predicates; it is not used as an infinite proof.

## Originality — PASS, subject to bibliographic limits
The initiating 2026 paper's Sections 1, 3, 5, 8, 9 and 11 and its specific graph-family statements were compared at statement and implication level. It obtains \(\operatorname{stack}(K_n)=n+1\), \(\operatorname{stack}(K_{m,n})=3\max\{m,n\}+1\), complete multipartite formulas, and a general independence-number lower bound. None covers the nonmultipartite friendship graphs with \(k\ge2\) or their configurationwise hub-consolidation criterion. The earlier 2021 friendship-graph paper concerns cover pebbling, a logically distinct target requirement. Targeted published-finding corpus and mathematical-literature searches found no equivalent or stronger covering claim; searches alone are not uniqueness proofs. Residual risk: unindexed literature or unpublished results may exist.

## Value — PASS
The finding solves a natural infinite-family case of a newly defined graph pebbling parameter and provides a complete configuration-level obstruction, not just a scalar formula. It identifies a sharp \(4k\) threshold, strictly larger than the previously available \(3k+1\) lower bound for every \(k\ge2\), and a constructive algorithm to consolidate all applicable configurations at a prescribed hub. The center-sharing triangle structure makes the parity penalty mathematically natural rather than an arbitrary small example.

## Limits and nearby literature
Finite checks do not certify infinite statements; the mathematical lemmas supply the infinite proof. The result does not determine clearing numbers or general cactus classes. The main source is arXiv:2604.22341v1 (2026-04-24); the earlier same-graph, different-target paper is DOI:10.1088/1742-6596/1770/1/012064 (2021). The potential existence of an unindexed equivalent result remains the main originality risk.

Self-review: passed. Independent audit: not yet performed.
