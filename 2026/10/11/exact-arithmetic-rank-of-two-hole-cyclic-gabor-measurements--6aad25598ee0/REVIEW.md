# Scientific review: exact arithmetic rank of two-hole cyclic Gabor measurements

## Correctness — PASS
The proof starts with the established rank/ambiguity theorem [1] and computes each deleted-character sum in the three overlap geometries, including the degenerate order-two difference. The only possible cancellations are order-two or order-three character values; exact congruence counting yields the divisor sum \(H_N\), the correction involving \(J_d\), and the \(4d\) order-three term. The packaged `CHECK.py` was executed from the included path, reproducing all \(589\) exact cases with no floating-point criterion; the unrestricted theorem is separately proved by the character and congruence argument.

## Originality — PASS, with residual risk
The exact general Gabor Gram rank criterion is [1, Theorem 1]; difference-set based injectivity criteria and antecedents are [2]. The coprime-gap case follows under affine relabelling from the previously known adjacent two-hole rectangle, and is not claimed as independent novelty. The all-dimensional nonunit-gap computation is additional: \(N=15\) with gaps \(1\), \(3\), and \(5\) has rank deficiencies \(4\), \(0\), and \(20\), which the adjacent case alone cannot determine. The checked public index descriptions for two-supported-point windows compute other invariants and do not state a two-missing-point rank formula. The possibility of an unindexed equivalent treatment remains.

## Value — PASS
Exactly two failed coordinates are a canonical minimally damaged all-ones Gabor fiducial; the rank reveals whether the resulting measurement determines arbitrary operators. Resolving every cyclic modulus and deleted-site gap, rather than an arbitrary finite example, exposes a meaningful torsion and relative-spacing boundary. The full rank formula quantifies the lost operator directions even where reconstruction fails. No conditioning, erasure recovery, or nonlinear phase-retrieval guarantee is inferred.

## Sources and scientific limits
[1] A. Goldberger, S. Kang, K. A. Okoudjou, *Towards a classification of incomplete Gabor POVMs in \(\mathbb C^d\)*, arXiv:2106.01509v1, Theorem 1.

[2] I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800v2, Section 2.

Relevant indexed two-supported-point window studies were compared by accessible titles and summaries only, not certified as wholly non-covering. Unindexed older coverage remains an originality risk. All claims are scoped to \(N\ge5\) and full operator-Gram rank.

Same-model review: passed. Independent audit: not yet performed.
