# Scientific review

## Correctness — PASS
The exact Hilbert-vector reduction to a scalar inner product is valid for all unit vectors. Strict concavity of the weighted two-square-root function forces an angular saddle-to-boundary switch exactly when the smaller coefficient ratio crosses \(\delta\). The two resulting exact scalar branches are differentiated with endpoint and exponent conventions checked. Cauchy equality yields all high-exponent maximizers; a direct equality analysis handles \(p=1\), \(p=2\), balanced weights, and infinite exponent. The derivative jump is the binary entropy deficit from its strict maximum. Standard-library randomized and explicit-witness tests give 18,867 checks but do not prove the quantified theorem.

## Originality — PASS (best-knowledge, not priority certification)
The introducing paper, arXiv:2608.00933, Definition 2, Theorem 14 and Example 4, states a general balanced-weight theorem and the possibility of oblique directions for asymmetric linear weights, without evaluating their full norm for all exponents. Ni–Liu–Zhou (2025), Propositions 1 and 6, compute differently weighted *internal* vector combinations, not the external-weight/variable-exponent supremum here. The 2019 symmetric family uses a different vector pair. Searches for equivalent conjugate-exponent, Hölder, and weighted Hilbert skew formulations found no statement covering the complete two-branch formula plus equality and strict-corner classification. Risk: earlier implicit or differently named two-dimensional matrix-norm literature, and uninspected full text of the 2019 background paper. This is not an independent priority determination.

## Mathematical value — PASS
The exact solution addresses the asymmetric weight singled out by the introducing article as departing from its balance theory. It determines the full two-parameter natural invariant, including every extremizer, and exposes a sharp transition between collinear and genuinely noncollinear geometry at \(p=2\), with an explicit nonzero entropy-based derivative jump. This is structural information absent from the cited bounds and cannot be read off merely from a balanced value or a two-vector Cauchy inequality.

## Limits
Real Hilbert dimension at least two, strictly positive external weights, and exponents \([1,\infty]\) only. Numerical tests are not infinitary certificates. Literature coverage may be incomplete; publication priority remains unverified.

Self-review: passed. Independent audit: not yet performed.
