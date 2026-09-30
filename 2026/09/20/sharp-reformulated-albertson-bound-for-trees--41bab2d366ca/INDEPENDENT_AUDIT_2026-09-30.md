# Independent audit — 2026-09-30

**Record:** `2026/09/20/sharp-reformulated-albertson-bound-for-trees--41bab2d366ca`  
**Audited source tree:** `a9a8b846d76284c327dd5cb7dcc72e7512178c14`  
**Disposition:** passed

## Correctness — PASS

PASS. Writing x_v=d(v)-1, the contribution at a vertex v is the pairwise spread of the neighboring x-values. For k nonnegative numbers, sum_{i<j}|a_i-a_j| <= (k-1)sum_i a_i, with positive-case equality only when at most one entry is nonzero. Summing gives RAlb(T)<=2 sum_{uv in E}x_u x_v. For the tree bipartition (A,B), the edge sum is at most X_A X_B and X_A+X_B=n-2, so the sharp numerical bound is 2 floor((n-2)^2/4). Equality in the local inequality forces every vertex to have at most one nonleaf neighbor; because the nonleaf-induced subgraph of a tree is connected, a positive extremizer has exactly two adjacent nonleaves and is a double star. Its index is 2pq, maximized exactly by balanced p,q. Independent enumeration of every nonisomorphic tree through order 12 reproduced the formula and a unique maximizing isomorphism class for every n>=4.

## Originality — PASS

PASS, to the best of the inspected literature. The directly relevant 2025 Cutinha--D'Souza--Nayak paper introduces the reformulated Albertson index, proves sharp lower bounds in constrained tree classes, and gives parameter-dependent upper bounds; its indexed statement does not give this exact order-only maximum or balanced-double-star equality classification. Searches using both 'reformulated Albertson' and line-graph irregularity terminology did not locate the same theorem. This is still subject to unindexed graph-index literature or equivalent statements under a different name.

## Scientific value — PASS

PASS. The theorem gives a simple exact extremal law and complete equality characterization for a newly studied irregularity index, and equivalently solves the Albertson-index maximum over line graphs of trees. The proof also supplies a compact local-to-bipartite extremal method rather than relying on enumeration.

## Independent checks

- Proved the local pairwise-spread inequality and tracked its equality condition.
- Rechecked the bipartition product step and total excess-degree identity X_A+X_B=n-2.
- Enumerated all nonisomorphic trees through order 12 and evaluated RAlb directly.

## Literature evidence

- https://doi.org/10.1080/09728600.2025.2458263 — Cutinha, D'Souza and Nayak (2025), directly relevant reformulated-Albertson paper; indexed results are lower bounds and general parameter upper bounds, not this exact order-only maximum.
- https://combinatorialpress.com/ars-articles/volume-046-ars-articles/the-irregularity-of-a-graph/ — Albertson (1997), original graph irregularity index.
- https://doi.org/10.1007/s40819-015-0069-z — De, Pal and Nayeem, irregularity under graph operations, relevant line-graph context.

## Limitations

- The theorem is restricted to trees (equivalently line graphs of trees).
- Originality search cannot exclude an unindexed equivalent theorem phrased only as line-graph or block-graph irregularity.
- Finite enumeration corroborates but does not replace the symbolic proof.

No GitHub write was performed by the audit chat. This file is staged by the guarded `scope-audit-change-set-v1` plan only.
