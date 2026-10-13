# Review of Outer-independent double Italian domination of half graphs

## Correctness
PASS. The proof converts every matched pair into a baseline contribution \(1\) plus a nonnegative surplus. The two leaf ends each force surplus at least \(2\) across their adjacent two pairs; for \(n\ge4\) those blocks are disjoint, so every feasible function has weight at least \(n+4\). At equality, the only possible one-unit leaf exceptions are eliminated by the next constrained vertex and outer independence. This forces all interior pair sums to equal \(1\), after which the Ferrers adjacency order makes the zeros a prefix-suffix staircase. The endpoint constraints leave exactly two choices at each end. Direct exhaustive computation on \(H_4\) and \(H_5\) agrees with the proof and with the exact counts \(12\) and \(16\).

## Originality
PASS. The closest direct primary theorem gives \(\gamma_{oidI}(K_{n,n})=n+2\) for balanced complete bipartite graphs, but a half graph is not complete multipartite and the statement does not imply either the \(n+4\) value or the staircase optimizer family. The inspected 2021 full text contains no “half” or “chain” occurrence. Later same-parameter sources focus on tree bounds, complexity and extreme-value characterizations, or graph products. Searches under half-graph, chain-graph, Ferrers-graph, and OIDIDF formulations did not locate an equivalent theorem. The inaccessible full text of the graph-products source is retained as a residual literature risk rather than treated as negative evidence.

## Value
PASS. Half graphs are canonical chain/Ferrers graphs whose nested neighborhoods make them a standard stress test for domination parameters. The result is structural rather than a numerical recomputation: it identifies a sharp two-unit gap from the complete-bipartite value and completely classifies all minima by a single staircase breakpoint and two endpoint choices. The exact count \(4(n-1)\) exposes the equality geometry of the parameter on a natural infinite family.

Self-review: passed. Independent audit: not yet performed.
