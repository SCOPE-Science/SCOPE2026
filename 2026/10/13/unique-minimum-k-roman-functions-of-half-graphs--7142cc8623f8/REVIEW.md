# Review of Unique minimum \([k]\)-Roman functions of half graphs

## Correctness
PASS. The proof starts from exact leaf-support inequalities and treats every equality case. If one endpoint pair has weight \(k\), the zero support forces an additional label of at least \(2\); combining this with the opposite leaf and the existence of the interior vertex \(a_2\) gives the global lower bound \(2(k+1)\). The equality analysis rules out any endpoint pair of weight \(k\), after which both endpoint pairs have weight \(k+1\) and all interior labels are zero. The constraints at \(a_2\) and \(b_{n-1}\) then force labels \(k+1\) at \(b_n\) and \(a_1\), respectively. The proposed labeling directly satisfies every constrained vertex with equality. The included checker independently exhausts \(1{,}035{,}068\) bounded-weight labelings for \(2\le k\le5\) and \(3\le n\le5\), matching the theorem exactly.

## Originality
PASS. The strongest direct prior result is the 2020 double-Roman theorem for chain graphs, which already yields the scalar value \(6\) when \(k=2\) and \(n\ge3\). That covered scalar is expressly excluded from the novelty claim. The 2020 source does not classify minimum double-Roman functions. The 2023 general \([k]\)-Roman paper gives bounds, tree results, and complexity results but no half-graph or chain-graph specialization in the inspected full text. The 2024 continuation and the latest 2026 exact-family paper were also checked for the same object and aliases without finding the endpoint-rigidity theorem. Searches under half-graph, chain-graph, double-Roman, triple-Roman, and \([k]\)-Roman formulations found no statement implying the unique optimum for all \(k\ge2\).

## Value
PASS. Half graphs are canonical connected chain graphs, so they are a natural benchmark for any domination invariant on nested neighborhoods. The theorem lifts the known double-Roman scalar result to every robustness level \(k\ge2\) and, more importantly, completely identifies the equality structure. The optimum is independent of graph order and is rigid: the only minimum defense is concentrated at the two opposite universal endpoints. This provides a concise structural reference case for general \([k]\)-Roman domination rather than a routine numerical substitution.

Self-review: passed. Independent audit: not yet performed.
