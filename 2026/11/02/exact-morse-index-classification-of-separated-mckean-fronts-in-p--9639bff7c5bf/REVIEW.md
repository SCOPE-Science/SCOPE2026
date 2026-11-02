# Scientific review: exact spectral index of separated necklace McKean fronts

## Correctness — PASS

The precise mathematical object is the selfadjoint transmission linearization with quadratic form \(-\int(p|v_x|^2+|v|^2)+\sum_i |v(\rho_i)|^2/|u_x(\rho_i)|\) on \(H^1(\mathbb R)\). It is **not** asserted to be an independently established Frechet derivative of the nonlinear discontinuous-reaction flow. The proof derives the finite Green matrix directly from the resolvent eigen-equation, proves its strict monotonicity in the nonnegative spectral parameter, and counts positive eigenvalues by crossings of 1. The zero-eigenvalue test follows from the same resolvent equivalence. The essential spectrum is bounded by \(-1\).

At each isolated threshold phase, direct differentiation of the half-line resolvent solution gives \(|V_s'(s)|=G(s,s)-b'(s)\), so a P phase yields a Green ratio below 1 and a Q phase yields a ratio above 1. The sourced matching theorem provides exponentially close separated crossing locations; the same exponential Floquet estimates bound the off-diagonal Green entries and the contributions to crossing slopes. A strict finite diagonal gap around 1 therefore survives at large separation. Consequently the Morse index equals the number of Q letters, and the nullity is zero. No numerical extrapolation substitutes for this proof.

The standalone numerical program independently reconstructs profiles from transfer matrices for all eight three-crossing and all 32 five-crossing words at two in-range thresholds. It verifies threshold residuals, transverse slopes and Green-matrix eigenvalue indices. These computations are corroboration, not proof of the infinite-parameter theorem.

## Originality — PASS under inspected evidence

Mori, Ogawa and Sintavanuruk [1, Theorem 5.3] establish the family and \(2^m\) multiplicity but explicitly leave nonmonotone-front stability unproved [1, Sections 1 and 6]. Their theorem and estimates do not themselves give the count of positive eigenvalues for each of the \(2^m\) fronts, nor the finite-dimensional zero-energy resolvent index test. The present theorem supplies a **spectral** resolution in the paired-edge-symmetric scalar channel; it does not claim the stronger nonlinear stability problem has been solved.

Bastiaansen, Doelman and Kaper [2, Theorem 6.1] establish a closely analogous small-eigenvalue selection principle for a smooth cubic Allen--Cahn equation with *small-amplitude topographic forcing*. That is a serious thematic antecedent and explains why one stable word may be expected. However, it does not include discontinuous McKean kinetics or the fixed order-one two-zone diffusion contrast, and its asymptotic regime does not imply this Green-matrix formula. Classical Birman--Schwinger reduction is an acknowledged standard method, not claimed as original.

Semantic searches for the same source identifier, moving-crossing linearization, Green-resolvent point-interaction index, and all-P/Q exact Morse counts returned no equivalent published result in the available records. This is an evidence-bounded priority assessment, not uniqueness certification. Historic contributions on discontinuous-reaction eigenvalue transmission and pinned multi-fronts could still overlap.

## Mathematical value — PASS

The new theorem closes a specifically identified *spectral* gap for all of the source's exponentially separated multi-front solutions at **fixed, nonperturbatively strong diffusion contrast**, and it does so with an exact non-asymptotic finite Green-matrix criterion for *every* finite set of simple crossings. It distinguishes a single spectrally stable word, gives the entire binomial Morse-index distribution across \(2^m\) patterns, and proves the absence of neutral modes. The integer-index classification is structurally relevant to stability, bifurcation and nonlinear analysis of pinned fronts, and is not a generic small numerical improvement or a relabeling of the source's existence theorem.

## Closest literature and limitations

[1] Y. Mori, T. Ogawa and C. Sintavanuruk, *Stationary bistable fronts on a periodic necklace graph: existence, stability and multiplicity*, arXiv:2610.32917v1 (23 October 2026), https://arxiv.org/html/2610.32917v1, especially Lemma 3.5, Theorem 5.3 and Section 6.

[2] R. Bastiaansen, A. Doelman and T. J. Kaper, *Multi-front dynamics in spatially inhomogeneous Allen--Cahn equations*, arXiv:2501.16195 (27 January 2025), https://arxiv.org/abs/2501.16195, especially Section 6.3 and Theorem 6.1.

Limitations: formal/transmission linearization only; paired-edge-symmetric sector only for the necklace graph; no nonlinear Lyapunov stability, asymmetric graph spectral theorem, optimal gap, or fully independently verified priority claim. Related older jump-heterogeneity models have not all been examined in complete full text.

Self-review: passed. Independent audit: not yet performed.
