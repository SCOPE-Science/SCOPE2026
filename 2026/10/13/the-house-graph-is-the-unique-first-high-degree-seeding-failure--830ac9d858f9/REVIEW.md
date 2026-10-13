# Self-review

## Correctness
**PASS.** The complete connected labeled graph domain through five vertices is exhausted. Connectivity is independently checked by breadth-first search and transitive closure. Every two-seed strict-majority cascade is independently reconstructed by synchronous activation rounds and an incremental queue algorithm, with exact agreement. The lower bound is also transparent structurally: among connected four-vertex graphs, only \(P_4\) and \(K_4-e\) have an unambiguous high-degree pair, and that pair activates all four vertices in both cases. At five vertices, exactly \(60\) failures occur and full permutation canonicalization identifies all of them with the house graph.

Risk: the exhaustive theorem stops at five vertices, as stated.

## Originality
**PASS.** Prior work already establishes high-degree seeding as a standard influence heuristic and strict-majority irreversible diffusion as a standard threshold model; those ingredients are not claimed as new. The inspected primary sources do not state the sharp two-seed boundary, the \(60\)-of-\(728\) labeled count, the conditional \(6/29\) incidence, or the one-class house-graph obstruction. Claim-level searches by standard aliases, exact graph size, the house graph, and the heuristic/model combination did not locate equivalent coverage.

Risk: failed search is not proof of bibliographic uniqueness. An unindexed small-graph table, thesis, or software corpus could contain the same finite observation.

## Value
**PASS.** The high-degree rule is a canonical influence heuristic, while strict-majority thresholds model genuinely reinforcing adoption. A single seed is structurally degenerate in this model because it cannot activate a vertex of degree at least \(2\); two seeds are therefore the first budget at which neighbor reinforcement matters. The sharp first failure is not an arbitrary slice: it completely identifies the smallest network where the standard unambiguous high-degree choice loses to diffusion-aware targeting, and the entire obstruction layer collapses to one familiar graph type. On that graph the heuristic reaches only \(3\) vertices while an optimal pair reaches all \(5\).

Self-review: passed. Independent audit: not yet performed.
