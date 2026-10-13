# Self-review

## Correctness — PASS

The full-column-rank assumption makes both polar factors unique and ensures positive alignment. The common denominator follows from column orthonormality. A directly checked positive-semidefinite spectral polynomial proves the sharp unit-vector bound; a rank-one nuclear-norm decomposition lifts this bound to the relevant matrix. An explicit full-rank two-dimensional family approaches the critical constant. The commuting equality condition uses uniqueness of the polar optimizer and the symmetry of the positive factor. The verifier's exact-rational and randomized calculations agree, but finite testing is not treated as a universal proof.

## Originality — PASS

The motivating original preprint (Du and Su, arXiv:2604.01472v1, Section 4 and Appendix E) defines the quadratic score and the preconditioned direction, and proves nonnegative alignment, but does not give the sharp score-ratio interval or its equality/sharpness classification. The PolarGrad analysis (Lau, Long, and Su, arXiv:2505.21799) treats matrix polar optimizers and quadratic objectives, without the same identified theorem in the inspected passages. The scalar Kantorovich angular inequality and nuclear variational characterization are known inputs, not new discoveries. Older operator-inequality coverage remains a genuine search limitation.

## Mathematical value — PASS

The proof quantifies a model-specific limitation of right-preconditioned matrix polar descent: with isotropic output curvature and exact line searches, it can never outperform the unpreconditioned polar direction, but its worst relative loss is exactly bounded by a condition-number factor that approaches zero for strong anisotropy. A concrete invertible near-rank-one family realizes the sharp frontier, and the commuting condition identifies when preconditioning is harmless. The result does not depend on arbitrary tuning constants and answers a directly motivated one-step performance question.

## Limitations and references

The real full-column-rank, SPD input-covariance, exact-polar, output-isotropic, and exact-line-search assumptions are essential to the stated proof. There is no multi-step, anisotropic-output, finite-precision or practical runtime guarantee. Relevant source passages are Du--Su (arXiv:2604.01472v1, Proposition 2, Section 4, Appendix E) and Lau--Long--Su (arXiv:2505.21799, Sections 3–4). An older general matrix Kantorovich statement could subsume the result under another name; that possibility has not been eliminated.

Self-review: passed. Independent audit: not yet performed.
