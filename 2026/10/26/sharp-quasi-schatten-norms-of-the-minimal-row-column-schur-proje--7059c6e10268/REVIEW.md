# Scientific assessment

## Correctness — PASS

For every exponent \(0<p\le1\), the Schatten \(p\)-power triangle inequality and singular-value decomposition reduce the exact multiplier norm to unit rank-one inputs. The masked rank-one operator has rank at most two, with squared singular-value sum \(s+t-st\) and singular-value product \(\sqrt{st(1-s)(1-t)}\). At fixed \(s+t\), increasing the product \(st\) strictly increases both the smaller singular value and the sum of the singular values, while reducing the larger one. This forces symmetrization for \(0<p\le1\), with strict inequality away from equality. The one-variable derivative has exactly one zero by two monotonicity arguments, yielding the stated sharp constant and attained positive rank-one extremizer. Endpoint identities and exact \(p=1/2\) optimization follow by elementary differentiation. The accompanying standard-library checker produced 15,007 finite diagnostic assertions; finite tests were not substituted for the proof.

## Originality — PASS, residual priority risk

McDonald–Sukochev–Zanin (arXiv:2605.07564, first available 8 May 2026) characterizes bounded support patterns for quasi-Schatten ideals and includes a finite-row/column boundedness lemma, but the inspected definitions, lemma, classification theorem and neighboring proofs contain no sharp \(p\)-dependent constant or optimizer for the two-sided cross. Aleksandrov–Peller (arXiv:math/0101264) studies structured Hankel and Toeplitz Schur multipliers, not this cross mask. Banks–Harcharras (2004) studies the Banach exponent range \(1<p<\infty\); the trace-class endpoint is treated here as a check, not a separate novelty claim. Database searches located a related sharp \(p=4\) three-entry two-by-two mask result, which cannot imply a quasi-Schatten \(p<1\) sharp profile without further proof. Originality remains best-knowledge rather than guaranteed priority; a previously published equivalent two-by-two quasi-norm optimization is a residual risk.

## Mathematical value — PASS

This computes a natural, smallest non-product row–column Schur projection's full sharp quasi-Banach norm profile, moving from a qualitative boundedness criterion to a dimension-free exact constant and attainment mechanism. It resolves all nonlocally-convex Schatten exponents within this family, establishes symmetric extremizer rigidity, and gives a nontrivial closed algebraic value at exponent \(1/2\). This is a motivated complete exact model result, not a repeated qualitative boundedness assertion. The contribution excludes larger unions of rows/columns and other masks.

Self-review: passed. Independent audit: not yet performed.
