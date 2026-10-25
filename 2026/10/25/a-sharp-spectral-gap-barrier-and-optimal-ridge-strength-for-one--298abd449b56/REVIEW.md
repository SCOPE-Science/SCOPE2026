# Scientific review

## Correctness — PASS

The claim fixes the ridge-augmented matrix, the one-row unbiased sketch distribution, the right preconditioner and the strict spectral condition-number comparison. Its derivation reduces the condition-number ordering to the sign of one explicit quadratic \(P_{r,\ell}(t)\); the discriminant and the endpoint factors give exhaustive parameter boundaries. Monotonicity of the two angular roots and a strictly signed derivative identity give the probability law and the unique optimal ridge parameter. The packaged standalone script passes 276 finite independent consistency checks; these support, rather than establish, the universal statement. Risk: the theorem only applies to the declared exact-arithmetic two-dimensional geometry.

## Originality — PASS (best knowledge)

The primary 2022 paper presents regularized partial sketch preconditioning and sufficient regularized-embedding conditioning estimates. The fully inspected relevant passages do not state or imply the exact rank-one improvement event or probability-maximizing ridge strength. Full primary texts of Avron–Clarkson–Woodruff (arXiv:1611.03220) and the sketch-and-precondition finite-precision study (arXiv:2302.07202) were also compared by regimes and implications. Searches for rank-one ridge preconditioning, sketch spectral gap, exact improvement probabilities and equivalent arcsine/angular criteria found no covering theorem in accessible indexed records. This is evidence of no identified overlap, not an exhaustive uniqueness proof. Risk: an equivalent calculation may exist outside indexed or accessible sources.

## Value — PASS

Minimal one-row sketching of a two-column Tikhonov problem is the first setting in which the source's sketched normal factor cannot be a full subspace embedding. The exact \(3+2\sqrt2\) spectral-gap impossibility theorem separates intrinsic rank deficiency from favorable angular configurations. The complete ridge-strength probability law identifies a positive onset and a unique finite optimal regularization ratio, which are mathematically motivated design diagnostics, rather than a numerical tweak or a restatement of known embedding bounds. It does not claim improvement in elapsed time or for large matrices.

Self-review: passed. Independent audit: not yet performed.
