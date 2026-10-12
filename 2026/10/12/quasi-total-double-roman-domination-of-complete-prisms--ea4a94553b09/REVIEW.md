# Review of Quasi-total double Roman domination of complete prisms

## Correctness
PASS. For any candidate of weight at most \(6\), each clique layer must have weight at least \(3\). If a layer has weight at most \(2\) and no label \(2\), at least two zero vertices require distinct matched label-\(3\) defenders; if it has one label \(2\), all other vertices require distinct matched labels of value at least \(2\). Thus an optimum of weight \(6\) has layer weights \(3\) and \(3\). A layer profile \(2+1\) forces too much weight in the opposite layer, while a profile \(1+1+1\) either forces multiple matched labels \(3\) or, at the \(n=4\) boundary, leaves its positive labels \(1\) undefended. Hence each layer has one label \(3\). The quasi-total isolated-positive condition forces those two vertices to be adjacent, which across the layers means they form a matching edge. The matched-\(3\) construction proves attainability. Exhaustive definition-level checks for \(n=4,5\) recover exactly the claimed minima.

## Originality
PASS. The initiating 2024 paper defines the exact invariant, solves paths and cycles, characterizes parameter values \(3\), \(4\), and \(5\), gives an exact complete-multipartite result, and proves broad upper bounds. The complete prism is not complete multipartite for \(n\ge3\), and those prior statements do not yield its value-\(6\) equality structure. A 2026 stability paper reuses the small-value and path/cycle results but studies vertex-deletion stability rather than complete-prism optimization. Searches under “complete prism”, “prism graph”, “Cartesian product”, and \(K_n\square K_2\) formulations found no equivalent exact theorem. The residual risk is a differently phrased or non-indexed treatment.

## Value
PASS. Complete prisms are a standard dense Cartesian-product family. The result shows that the new quasi-total double Roman parameter collapses to the constant value \(6\) on an unbounded-order family, while the equality case is rigid: every optimum is supported by one matching edge and there are exactly \(n\) optima. This is strictly finer than a bound or a scalar computation and exposes how the isolated-positive condition interacts with the two-clique product structure.

Self-review: passed. Independent audit: not yet performed.
