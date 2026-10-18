# Scientific review

## Correctness — PASS

The Gaussian sketch decomposition is exact: orthogonal input directions give independent Gaussian sketch images. Conditional normality establishes independence of the scalar numerator from the chi denominator. The spectral variance inequality is derived directly as a positive semidefinite quadratic form with equality only on the extreme spectral eigenspaces. Exact Student/chi tail differentiation proves the sharp fixed-mean envelope, unique balanced minimizer (for two or more rows), and universal half-probability supremum. The incomplete-beta tail and asymptotic follow from standard integral manipulations. The standalone verifier executed 115 numerical and distribution-convention assertions, but finite tests are not substituted for the analytic argument.

## Originality — PASS (self-review)

The source algorithmic papers introduce Gaussian sketch-orthogonal subspace projections and restarted Arnoldi, not the exact one-dimensional fixed-mean sharp spectral escape envelope in the inspected material. Classical Gaussian Student-ratio and spectral variance facts are acknowledged as standard. The sharp combined statement additionally identifies the extremal directions, the universal half barrier, strict unattainment for two or more sketch rows, and the balanced incomplete-beta risk. A related calculation of reciprocal harmonic Ritz values concerns a different random scalar and its singular inverse; a previously recorded two-dimensional complex-Ritz event concerns a two-dimensional compression. Neither implication yields this one-dimensional ordinary-Ritz sharp spectral-interval law. Semantic mathematical-record searches using aliases for Student t, Gaussian sketch, Bhatia--Davis, Rayleigh--Ritz and spectral interval uncovered no dominating theorem. Full priority verification beyond the inspected source sections is not claimed; some primary material remained inaccessible.

## Value — PASS

Randomized Rayleigh--Ritz and Arnoldi methods use sketched orthogonality to accelerate eigensolvers. Symmetric matrices' ordinary Ritz values have the classical spectral enclosure. The theorem makes the cost of dropping exact Euclidean orthogonality quantitatively precise, with a sharp worst-case obstruction that does not vanish with sketch dimension, and a contrasting explicit exponential bound in the balanced orientation. The extremizer classification and discontinuity at exact eigenvectors identify the particular input configurations requiring care when interpreting finite-sketch estimates. This is a motivated, exactly reproducible benchmark, not a general convergence claim.

## Literature and limitations

The closest source is de Damas--Grigori (2024), arXiv:2407.03208. Foundational projected random compression is in Nakatsukasa--Tropp (2021), arXiv:2111.00113; sketch-and-select Arnoldi in Güttel--Simunec (2023), arXiv:2306.03592. Their inspected general frameworks do not supply the exact extremal envelope. The earlier reciprocal harmonic Ritz Student-law and two-dimensional complex-Ritz findings have different statements and no dominating implication. Actual full-text inspection was achieved for the two foundational sources and introductory material of the motivating paper, but later material of the latter could not be fully retrieved; an equivalent specialized result remains a residual risk. The result is restricted to independent real Gaussian sketches, one-dimensional fixed input subspaces and unconditioned sketch draws. Independent audit was not performed.

Self-review: passed. Independent audit: not yet performed.
