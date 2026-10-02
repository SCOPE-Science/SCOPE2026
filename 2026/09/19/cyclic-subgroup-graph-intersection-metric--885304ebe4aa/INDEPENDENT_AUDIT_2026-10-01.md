# Independent audit — 2026-10-01

**Record:** Exact intersection metric and sharp induced-subgraph corrections for cyclic subgroup graphs  
**Disposition:** passed

## Correctness — PASS

Across a cover edge of the cyclic-subgroup Hasse graph, subgroup order gains one prime factor and the intersection with a fixed cyclic subgroup either stays fixed or gains the same prime factor, so the intersection potential changes by exactly one. This proves the distance lower bound; saturated chains through the cyclic intersection attain it and have no chords. The \(C_4\times C_2\) counterexample follows directly from its six cyclic subgroups. For \(C_n\), the product-of-paths model makes the induced-cycle classification a grid argument: prime powers are paths, one-cell-wide rectangles have only induced squares, two-dimensional rectangles of both widths at least two have induced outer boundaries, and opposite coordinate-filling paths give the required cycle in at least three dimensions.

## Originality — PASS

The audited theorem strictly sharpens the bound and supplies the missing intersection correction, so the prior results do not imply it.

Equivalent-formulation search: The graph-specific exact formula and corrections are not equivalent to the source bounds or the product-of-paths special case.

Broader-coverage search: Even if the lower-level poset lemma is known abstractly, applying it to obtain the exact metric/diameter and to refute the current propositions is an implication-independent mathematical correction.

Exact-database/table check: Not applicable.

## Scientific value — PASS

An exact metric and diameter formula for every pair of cyclic subgroups is a natural invariant of the graph, and the theorem gives precise corrections and minimal counterexamples to two live induced-subgraph claims in the defining literature.

## Source inspections

- https://arxiv.org/abs/2409.13796v2: Primary full text inspected at Proposition 2.3, Proposition 2.5 and Theorem 2.11. It gives the product-of-paths model for cyclic groups, asserts the two induced-subgraph claims corrected here, and provides only r<=diameter<=2r rather than the intersection metric.
- https://arxiv.org/abs/2503.12184v1: Related primary work classifies when the cyclic subgroup graph is a line graph; it does not provide the exact intersection-distance formula.

## Residual risks

- The abstract rank/meet lemma may exist in general poset folklore; novelty is claimed for the cyclic-subgroup-graph statement and corrections.
- The elementary nature of the rank/meet argument raises a modest folklore-overlap risk.
