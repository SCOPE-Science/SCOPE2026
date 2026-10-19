# Scientific review

## Correctness — PASS

For a two-state row-stochastic transition, the first-state probability evolves by an affine map with slope equal to the matrix determinant. Nonnegative determinants make the upper-envelope optimum a monotone orbit. A unique winner must follow the unique active line at each step; an affine difference cannot switch sign positive–negative–positive along a monotone orbit, so no letter can reappear in a disjoint run. Conversely, the explicit rational lines have strictly increasing slopes, strictly increasing crossing positions, and small perturbation from a baseline contraction. The stated separation bound proves the desired run schedule is uniquely optimal for every parameter, including a singleton run and unused letters. Direct stochastic-matrix and exhaustive finite checks corroborate the proof; their scope is explicitly finite.

## Originality — PASS within examined evidence

Gill's arXiv:2402.13376 classifies unrestricted binary two-state witnesses and in Section 4.4 extends already-binary witnesses to larger alphabets, not an exact arbitrary-alphabet positive-determinant subclass. Kjos-Hanssen's arXiv:2607.26275 establishes an unrestricted three-state upper bound and expressly leaves two-state classification over three or more letters unresolved. Searches for monotone two-state PFAs, affine upper envelopes, nonnegative transition determinants, and symbol-run classifications did not locate an equivalent or broader theorem. Related public mathematics-record results on Parikh ambiguity and deterministic synchronization do not imply the present stochastic classification. Semantic-search incompleteness and unindexed monotone iterated-function literature remain risks; an unsuccessful search alone is not priority proof.

## Value — PASS

This completely classifies a structural, natural subclass of the unresolved nonbinary two-state probabilistic automatic-complexity problem, gives an explicit rational witness with linear-in-word-length parameter bit complexity for every admissible word, and determines the exact cardinality and growth rate over every finite alphabet. The restriction is mathematically meaningful: it is the order-preserving versus order-reversing dichotomy of two-state stochastic dynamics, and dropping it admits recurring-letter patterns. The argument uses a controlled series of upper-envelope crossings rather than an arbitrary finite pattern count.

## Limits

The full classification allowing negative determinants is open over larger alphabets. Historical priority is not certified; the cited sections and available mathematical records have been compared, not the whole historical literature. The checker tests representative finite parameter ranges, whereas the theorem is supported by its general proof.

Self-review: passed. Independent audit: not yet performed.
