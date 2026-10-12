# Scientific review

## Correctness — PASS

For any nonsingular real two-by-two input, the sole remaining LU cross residual is a determinant divided by its selected pivot. This gives the exact normalized squared-error identity for entry-squared pivoting. Cauchy–Schwarz and the independently reconstructed Gaussian conditional-regression and inverse-chi-square calculation show why the sketch distribution is dominated only for at least three Gaussian columns. Direct Beta integrations give the exact \(b=1\) and \(b=2\) failures. Row-exchange symmetry gives the same pivot law across all Gaussian sketch widths on a well-conditioned positive-definite family, establishing an exact sharp higher-moment obstruction and tail frontier. The embedded verifier exercises the stated finite checks; the proof, not experiments, establishes universal assertions.

## Originality — PASS, with limitations

Gilles–Wilber arXiv:2601.22344v1 proves expected Frobenius guarantees for the exact squared-entry randomized pivot law. Divan–Gilles arXiv:2609.06287v1 gives sufficient bounds for Gaussian sketch size at least three, without a converse small-sketch obstruction or a classification of higher moments on uniformly conditioned inputs. The present necessity proof, exact divergent second moments for widths one and two, and sharp polynomial tail lower bound are not consequences of either published expected-error *upper bound* alone; their sampling formulas are used as acknowledged starting definitions. Distinct adaptive randomized pivoting and deterministic complete-pivoting records do not dominate these Gaussian sketch-width statements. An equivalent unindexed prior derivation is a residual originality risk.

## Value — PASS

Gaussian sketch dimension is a practical algorithmic design choice. The minimal admissible width distinguishes a genuine uniform mean-square approximation guarantee from an algorithm with unbounded normalized mean-square error, even in dimension two. The higher-moment and sharp-tail theorem proves that mean-square guarantees cannot be automatically converted into faster-than-quadratic tail control, even on nearly identity matrices. This gives a motivated structural boundary for uncertainty quantification and robust randomized factorization, not simply a recomputation of a known expectation.

## Scope and limitations

Single update, real nonsingular two-by-two matrices, exact arithmetic, independent Gaussian sketch, Frobenius residual normalized by the smaller singular value. The width-one and width-two obstruction uses ill-conditioned diagonal matrices; the no-higher-moments obstruction uses well-conditioned SPD matrices. No long-run algorithmic, backward-stability, or runtime guarantee is asserted. Independent literature uniqueness has not been certified.

Self-review: passed. Independent audit: not yet performed.
