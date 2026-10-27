# Scientific review

## Correctness

**PASS.** The claim specifies a two-dimensional symmetric positive-definite quadratic, deterministic start, angular sampling, and two exact sequential line minimizations. After diagonalization the first update is an orthogonal projection in Hessian-energy coordinates. For independent sampling the second normalized-direction covariance is diagonal; for paired sampling its projection has exact angular cosine \(r/\sqrt{DE}\). The four exact rational angular integrals determine the complete quadratic-form expectations, not just one test vector. Their matching coefficient ratios prove the expectation identity for every start and include both \(\kappa=1\) and \(\kappa>1\). Reproducible midpoint quadrature provides additional finite checks but is not the proof.

## Originality

**PASS within available evidence.** Sections 2–5 of the 2011 Random Pursuit primary text develop independently resampled directions; Section 5 of arXiv:2211.09873v1 develops random-subspace Gauss–Newton, but not a two-step perpendicular-versus-independent universal exact factor. The 2021 orthogonal-direction finite-difference analysis and 2018 fixed-axis random-permutation coordinate descent consider related but mathematically different updates. A close published 2026 two-coordinate Gauss–Seidel statement concerns worst-case Euclidean transient and fixed axes; only its indexed summary was accessible and a stronger full-text implication remains a recorded residual risk. Searches under independent directions, paired orthogonal directions, randomly rotated Gauss–Seidel, and the condition-number factor did not identify an equivalent formula. Absence of a search match is not a uniqueness proof.

## Value

**PASS.** The result isolates an analytically exact advantage of structured sketch dependence at equal numbers of one-dimensional solves, even on anisotropic quadratics. That the advantage has a universal condition-number-only ratio independent of the starting direction is not evident from a one-step rate bound. It supplies a precise finite-horizon sampling-design benchmark and the natural degenerate limit at isotropy. It does not claim an arbitrary-dimensional acceleration theorem.

## Literature scope and remaining risks

Relevant accessible primary full texts were compared at the update-rule and guarantee levels. A related published Gauss–Seidel finding was accessible only through an indexed summary and could contain a stronger nonobvious formula; an unindexed exact random-basis averaging computation also remains possible. No claims about particular implementations, cost, higher-dimensional rates, or independent certification are made.

Self-review: passed. Independent audit: not yet performed.
