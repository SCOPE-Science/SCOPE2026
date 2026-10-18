# Review: hidden quadratic dependence of word coincidence counts

## Correctness (C): PASS
The forest-edge equality argument proves both binomial marginal laws and every pairwise cross-indicator independence. Conditional on the complete adjacent-equality pattern, a lag-two equality is certain across two adjacent equalities, impossible across exactly one, and has probability \(1/(q-1)\) across two adjacent inequalities. Uniform conditioning on the binomial sum yields the regression. The independent centered-pair expansion proves the exact variance ratio and the triangle expansion gives the third mixed moment. All boundary cases \(q\ge2\), \(n\ge3\) are covered; 18 complete finite word-space censuses passed all checked identities. Finite checks do not certify the infinite parameter range independently of the proof.

## Originality (O): PASS on inspected sources, with residual priority risk
The accessible primary papers arXiv:1905.05646v1 and arXiv:2203.14773v1 address distinct word-pattern counting problems. Their inspected abstracts, main-result statements and relevant sections do not state the present finite conditional regression or correlation ratio; neither standard binomial marginal formulas nor generic finite pattern counts imply this conditional expectation without the additional computation. The nearest published research-record matches concern fixed-composition transitions and distinct-substring complexity, rather than iid word lag-one/lag-two equality counts. An older word-moment or automata computation could imply the same formula, and independent priority verification has not been performed.

## Value (V): PASS
The result detects a concrete, universal nonlinear statistical dependence invisible to covariance, identifies the exact optimal variance explained using one natural pattern count to predict another, and describes its sharp finite-length and alphabet-size scale. The all-parameter classification and orthogonal quadratic mechanism are meaningful for statistical diagnostics of word-pattern counts, beyond a solitary numerical example.

Self-review: passed. Independent audit: not yet performed.
