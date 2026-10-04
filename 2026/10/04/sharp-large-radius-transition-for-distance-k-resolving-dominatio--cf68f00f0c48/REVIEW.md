# Review of Sharp large-radius transition for distance-\(k\) resolving domination of balanced spiders

## Correctness
PASS. A resolving set must meet at least \(q-1\) arms, while one noncentral landmark on each of \(q-1\) arms resolves the balanced spider, so the metric dimension is \(q-1\) with the stated basis structure. When \(k\le L\), every metric basis leaves one arm without a landmark and its leaf is at distance at least \(L+1\), forcing one additional vertex. For \(k\ge\lceil L/2\rceil\), one carefully placed landmark on every arm distance-\(k\) dominates the whole spider, proving the \(q\) plateau. For \(k\ge L+1\), depth-one landmarks on \(q-1\) arms already dominate the omitted leaf, proving the drop to \(q-1\). In the stabilized regime the omitted leaf is the only possible domination bottleneck, yielding the exact depth threshold and counting formula. Direct exhaustive tests match all statements on the tested grid.

## Originality
PASS. The primary 2021 all-\(k\) paper gives general bounds, exact path and cycle values, and only the diameter-level guarantee for equality with metric dimension; targeted full-text searches found no spider or subdivided-star result. The earlier distance-\(2\) paper treats stars, paths, complete graphs, and friendship graphs and explicitly poses further distance-\(k\) determinations as open work; its inspected full text also contains no spider or subdivision theorem. Targeted web and published-results searches for distance-\(k\) resolving domination of spiders and subdivided stars found no equivalent phase transition, metric-basis depth criterion, or minimum-set count.

## Value
PASS. Balanced spiders are canonical trees with one branching vertex and arbitrary arm length. The theorem identifies the exact stabilization radius at which the combined parameter becomes the metric dimension, improving the general diameter guarantee from \(2L\) to the sharp threshold \(L+1\), and it quantifies the entire optimum family after stabilization. The one-extra-landmark plateau for \(\lceil L/2\rceil\le k\le L\) also isolates a clean interaction between metric resolution and distance domination rather than merely recomputing either constituent parameter.

Same-model review: passed. Independent audit: not yet performed.
