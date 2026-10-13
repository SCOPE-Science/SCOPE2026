# Review of Minimum perfect Roman functions of complete prisms

## Correctness
PASS. A matched cross-layer pair labeled \(2\) gives a weight-\(4\) perfect Roman function. Any labeling of weight at most \(3\) has at most one label \(2\); the opposite clique then contains at least \(n-1\ge3\) vertices not adjacent to that defender, which cannot all be made positive with the remaining weight. At weight \(4\), one label \(2\) is still impossible; two same-layer labels \(2\) give a zero vertex two defenders, and two unmatched cross-layer labels \(2\) give a matched-index zero two defenders. Hence only matched pairs remain. The bundled checker exhausts every labeling of weight at most \(4\) for \(4\le n\le12\) and agrees exactly.

## Originality
PASS. The foundational regular-graph source supplies only degree-dependent upper bounds. The fully inspected 2022 Cartesian-product paper treats path/path, path/cycle, and cycle/cycle products and contains no complete-graph factor in its stated exact scope. A 2024 Cartesian-product paper states complexity results and a perfect-Italian upper bound on path/cycle products, not the complete-prism formula. Exact web searches and semantic literature searches for perfect Roman domination of complete prisms and \(K_n\square K_2\) returned no equivalent theorem. The current and prior scientific records contain Roman \(\{3\}\) and mixed-metric results for complete prisms, and perfect Roman results for crowns, but not this claim.

## Value
PASS. Complete prisms are a standard dense Cartesian-product family, directly adjacent to a literature that studies perfect Roman domination on graph products. The theorem gives a constant exact value and a complete optimizer classification, revealing that all minimum mass is forced onto one product-matching edge. The exceptional triangular-prism boundary shows that the rigidity is structural rather than a tautological consequence of weight four.

Self-review: passed. Independent audit: not yet performed.
