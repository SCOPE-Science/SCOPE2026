# Scientific review: two-step randomly pivoted Cholesky orientation law

## Correctness — PASS

The complete six-history probability calculation starts with Algorithm 1's actual sequential residual-diagonal law. For a positive-definite three-dimensional input, each ordered-pair probability is the principal two-by-two minor divided by the initial trace and first-residual trace, while the corresponding final scalar Schur complement is the determinant divided by that minor. The exact cancellation produces the orientation formula. Strict concavity on the probability simplex gives both sharp extrema and their complete equality cases, including all complex phases. The first-step identity and the dimension-two exact-recovery observation establish minimality. An independent rational verifier enumerated the actual two-pivot updates and checked the identities for several exact inputs. No numerical approximation is used as proof of the global assertions.

## Originality — PASS, qualified best knowledge

Closest primary comparison: Chen–Epperly–Tropp–Webber, arXiv:2207.06503, Algorithm 1, Section 5.1 and Appendix C. Their one-step map and general trace bounds do not provide the exact two-step orientation extremizers. Their nonlinear-map iteration is an upper bound on the actual expected residual, not an equality. Accelerated RPCholesky (arXiv:2410.03969) generates the same pivot law but analyzes implementation and block/rejection sampling. Epperly's 2026 analysis (arXiv:2608.20633) sharpens general trace and probability guarantees without deriving this complete fixed-spectrum extremal formula. Searches for rotations, eigenvector orientation, rank-one spikes, two-pivot RPCholesky, and equivalent principal-minor calculations did not locate a prior statement implying the sharp classification. The remaining risk is an earlier specialized identity buried in subset-sampling or Schur-complement literature; search absence alone is not a proof of uniqueness. Independent priority review has not occurred.

## Value — PASS

The claim isolates the first point at which the popular adaptive pivoting algorithm becomes sensitive to the *orientation* of an input at fixed eigenvalues. The complete extrema and sharp factor \(3/2\) quantify a natural performance distinction not controlled by the spectrum or the best rank-two error. The equal-modulus extremizer exactly matches the size-two determinantal-sampling expected residual, giving a concrete comparison benchmark. This is a structural finite-dimensional diagnostic, not a general guarantee for arbitrary matrix sizes or finite precision.

Self-review: passed. Independent audit: not yet performed.
