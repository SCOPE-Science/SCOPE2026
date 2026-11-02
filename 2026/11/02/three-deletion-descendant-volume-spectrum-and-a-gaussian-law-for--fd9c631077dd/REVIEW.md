# Mathematical review

## Correctness — PASS

Every descendant is indexed uniquely by its deleted multiplicity vector. Stars-and-bars counts the admissible input centers after imposing one or two deletion constraints; the pair-distance identity is quoted accurately from [1, Theorem 9]. Three-deletion patterns partition into three disjoint types, and coordinate-count strata are counted with a correct stars-and-bars residual. The exact formulas were checked against independent direct enumerators: 38,665 inputs for the three-deletion histogram and 24,505 for all-parameter first and second moments. The fixed-\(t\) Gaussian theorem uses the exact hypergeometric support law, a uniform \(O_t(q^{t-1})\) repeated-deletion bound, and classical hypergeometric CLT and moment concentration. These finite checks do not prove the infinite claims, which follow from the displayed combinatorial and probabilistic arguments.

## Originality — PASS, with priority limitations

The primary paper arXiv:2603.18322v1 proves the distance-pair enumerator and the mean *same-level metric ball volume*, and these are explicitly credited. It does not state the complete distribution of *one-sided three-deletion descendants* or the joint growing-alphabet Gaussian fluctuation law. arXiv:2601.05636v1 studies code sizes rather than random-descendant-volume distributions. Searches under deletion sphere, descendant count, weak composition, hypergeometric support and variance terminology found related but not dominating results, including fixed-length ordered-word sphere variances and the three-survivor optimum code size. The existing pair-count theorem is acknowledged instead of represented as new. An unindexed or implicit equivalent theorem remains possible.

## Value — PASS

In an unordered-symbol deletion channel, sphere-size heterogeneity influences packing and reconstruction, while averages alone omit the spread and multiplicity profile. The complete exact three-deletion histogram gives every volume and number of sources realizing it, for any alphabet size and source length. Exact general-\(t\) variance and a nondegenerate joint-length/alphabet Gaussian limit identify the fluctuation scale in a natural high-dimensional regime. These are motivated channel invariants, not arbitrary isolated finite evaluations.

## Scope and evidence

No claim is made of complete distributions for other deletion counts, multinomially sampled source words, growing \(t\), or independent validation. Both companion checkers can be run directly with Python 3.

Self-review: passed. Independent audit: not yet performed.
