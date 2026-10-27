# Scientific review

## Correctness — PASS

The zero-forcing upper bound is realized by the explicit complete chronological sequence in RESULT.md, including center and final-arm propagation. The integer matrix has exact prescribed off-diagonal support because sliding length-\((k+1)\) windows cover every pair on one arm at separation at most \(k\), and positive entries prevent cancellation. Its kernel has \((m-1)k\) independent synchronized-arm difference vectors, whose center and cross-arm equations vanish through the shared first \(k\) coordinates. Combining the standard real nullity bound with zero forcing proves both equalities and the minimum rank formula. The standalone verifier independently checked graph support, matrix kernel, forcing schedules, and five bounded exhaustive minimum-size tests.

## Originality — PASS, qualified

The initiating 2026 graph-power paper's spider conjecture and upper bound are restricted to equal arm lengths. Earlier exact uniform-spider results for powers three and higher do not logically cover unequal arm lengths without an additional argument; earlier graph-squares-of-trees results cover power two, and powers-of-path results cover two-arm spiders. The new synchronization lemma applies to arbitrarily and independently varying arm lengths. Literature searches using nonuniform, unequal-arm, variable-length, maximum-nullity, minimum-rank, spider powers, graph power and zero-forcing terminology found no exact broader formula. Residual risk: hidden prior formulations under graph powers of subdivided stars, general tree path-cover or minimum-rank terminology may exist.

## Mathematical value — PASS

Long-legged subdivided stars are the natural full variable-length extension of the equal-leg family singled out by a recent open conjecture. The theorem gives an exact structural invariant uniformly over every nonuniform arm-length tuple and simultaneous equality for two nontrivial graph parameters, rather than a small numerical improvement or isolated example. The common-initial-data window-kernel method explains why large and unbalanced arm lengths do not change maximal nullity, and may inform analysis of other variable-branch graph powers.

## Boundaries and verification status

No claim is made for shorter arms, arbitrary multi-branch trees, or a classification of all optimum forcing sets. The finite executable tests do not replace the infinite proof. Historical priority has not been independently certified.

Self-review: passed. Independent audit: not yet performed.
