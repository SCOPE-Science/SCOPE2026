# Self-review

## Correctness
**PASS.** Every burning sequence on a star is exhausted by two structural cases. A centre-first sequence finishes at the next spread with natural colour-class sizes \(p+1\) and \(q\). A leaf-first sequence forces the centre at the next spread; all remaining leaves then have only the centre as a burned neighbour, while exactly one second ignition may override one leaf's natural colour. This proves the upper bound and simultaneously gives constructions attaining \(p+2\) or \(q+1\) when both edge signs occur. The all-negative and all-positive endpoints are treated separately. Direct exhaustive simulation of all \(504\) star signatures with three through eight leaves agrees with the formula and with the switching-class minimum.

## Originality
**PASS.** The primary full text arXiv:2610.02506v1 was inspected at the process definition, plurality definition, switching/code relation, signed-path results, introduction, and conclusion. It gives exact results for signed paths, states that more complex graph classes remain open, and explicitly points toward classes of signed trees; it contains no star or \(K_{1,m}\) result. Targeted semantic-index and public-web searches under plurality-number, signed-burning, signed-star, \(K_{1,m}\), and covering-radius formulations located no equivalent or stronger statement. The closest indexed items use different burning processes or different invariants on stars. The residual risk is the recency of the invariant: an equivalent result may exist in material not yet indexed.

## Value
**PASS.** Stars are the canonical nonpath tree family, while the initiating paper's exact structural theory is concentrated on signed paths and explicitly identifies signed-tree classes as a direction for further work. The theorem gives the full dependence on the signature, not merely a bound or a special signing, and it also resolves the switching-class minimum and associated covering radius. This supplies an exact, reusable benchmark for the new parameter and its coding-theoretic formulation.

Self-review: passed. Independent audit: not yet performed.
