# Same-model scientific review

## Correctness
PASS. The stopping-time reduction is exact for every zero-free rank-two generator matrix. A zero column is strictly dominated by replacing it with a nonzero column. Conditional on the first projective class, the remaining waiting time is geometric with success probability \((n-m_i)/n\), giving \(\mathbb E[G]=1+\sum_i m_i/(n-m_i)\). The discrete increment of \(t/(n-t)\) is strictly increasing, so pairwise balancing is strictly improving until all projective multiplicities differ by at most one. Exact exhaustive checks for small \(q\) and \(n\) reproduce the closed formula and equality cases.

## Originality
PASS, with residual literature risk. The 2025 small-alphabet paper formulates the optimal-coverage problem and only gives computational evidence for a different parameter point, \([7,3]_2\). Its 2026 extension still states simplex optimality as conjectural and develops evaluation formulas for fixed families rather than an all-code optimizer theorem. The earlier MDS theorem implies the rank-two optimum only for \(n\le q+1\); it does not determine the non-MDS regime \(n>q+1\). Focused semantic-index and literature searches for rank-two coverage-depth optimization and balanced projective multiplicities found no statement implying the all-\(n\) formula or optimizer classification.

## Value
PASS. The result completely solves the natural optimal coverage-depth problem in the first nontrivial dimension, including every small-field non-MDS length, and gives both the exact optimum and a structural classification of all optimizers. It also supplies a clean baseline for higher-dimensional small-field optimization.

The main limitation is scope: dimension two has a special one-step projective-state reduction that is unavailable in higher dimension.

Same-model review: passed. Independent audit: not yet performed.
