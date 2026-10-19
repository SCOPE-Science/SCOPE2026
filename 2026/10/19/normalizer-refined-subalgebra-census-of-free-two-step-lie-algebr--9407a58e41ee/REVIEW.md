# Scientific review: normalizer-refined subalgebra census

## Correctness

PASS. Closure of a subalgebra with projection \(U\) and central part \(W\) is equivalent to \(\Lambda^2U\subseteq W\), with exactly \(q^{a(c-b)}\) graph lifts. The normalizer of a rank-one projection subalgebra is controlled by \(W\cap(u\wedge V)\), giving dimension \(c+1+t\). The complete three-generator polynomial follows by an exhaustive projection-dimension partition \(a=0,1,2,3\), with no characteristic restriction. The standalone checker separately enumerates all six-dimensional subspaces for \(q=2,3\) and tests the Lie closure and normalizer rank. Finite tests supplement but do not replace the proof.

## Originality

PASS within the inspected primary-literature and mathematical-result coverage. Seungjai Lee, arXiv:2010.02268, Theorem 5.1 and Example 5.2, already determines the ideal-zeta count, which is recovered precisely by setting \(Y=0\); it does not present the non-ideal normalizer-index layers. Lee and Voll, arXiv:2006.12346, studies subrepresentation and ideal enumerators rather than this invariant. The Gaussian subspace-intersection identity is classical. Noncommuting-graph and endomorphism-orbit invariants have different mathematical definitions and do not imply the joint normalizer count. Residual risk: unindexed normalizer enumeration could cover part or all of the formula. Searches alone do not certify priority.

## Value

PASS. The normalizer-index polynomial is a natural strengthening of the ordinary and ideal subalgebra enumerators. The result computes the entire first six-dimensional case over all finite fields and separately establishes all rank-one projection strata in arbitrary generator rank, including exact ideal boundary cases. The distinction between the two nonideal normalizer-index layers is not visible in existing dimension-only data.

## Limitations

The complete all-subalgebra polynomial is not claimed beyond three generators. The extension to arbitrary generator number counts only projection-rank-one strata. No external independent validation or historical uniqueness certificate has been issued.

Self-review: passed. Independent audit: not yet performed.
