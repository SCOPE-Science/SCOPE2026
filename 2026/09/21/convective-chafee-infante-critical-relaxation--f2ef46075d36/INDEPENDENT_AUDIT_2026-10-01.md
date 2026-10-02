# Mathematical audit — 2026-10-01

## Final claim assessed

Transport-renormalized critical relaxation in a convective Chafee-Infante equation

## Correctness — PASS

PASS. The energy identity is exact because the Burgers term integrates to zero under homogeneous Dirichlet data. Poincaré gives exponential decay below the first Dirichlet eigenvalue, the quartic term gives the critical algebraic envelope, and the first linear eigenvalue is positive above threshold. Independently recomputing the sine-mode invariance equations gives the cubic coefficient \(-\beta_c(r^2+9)/12\), the quintic coefficient \(-\beta_c(r^2+9)(7r^2-9)/3456\), and the logarithmic coefficient \((7r^2-9)/288\), exactly matching the repository symbolic artifact. The reciprocal-square reduction then gives the stated generic \(t^{-1/2}\) law, logarithmic correction, norm limit and second-harmonic wake.

## Originality — PASS

PASS to the best of current knowledge. Resultary searches for the exact convective Chafee--Infante/Burgers--Huxley critical coefficients and relaxation law returned only the assigned record. The official Mohan--Khan article page confirms a broad treatment of generalized Burgers--Huxley well-posedness, attractors, stationary solutions and exponential stability, but the accessible material contains no center-manifold or critical-coefficient statement; a direct search of that page found no center-manifold terminology. No earlier published record was located with the unchanged sharp Dirichlet threshold together with the transport-renormalized cubic/quintic coefficients, logarithmic correction and second-harmonic limit.


### equivalent_formulations

Searches: Resultary: convective Chafee Infante Burgers transport critical center manifold cubic damping logarithmic relaxation; web: generalized Burgers-Huxley critical relaxation transport center manifold

Evidence: The exact semantic searches returned only the assigned record among published findings. The official 2021 generalized Burgers-Huxley page describes well-posedness, attractors and stationary-solution stability but exposes no center-manifold formula.

Reasoning: Burgers-Huxley and convective Chafee--Infante are equivalent parameterizations for the symmetric cubic case, and the searches covered both descriptions.
### broader_coverage

Searches: https://doi.org/10.3934/dcdsb.2020270; classical Chafee--Infante bifurcation and Henry center-manifold framework

Evidence: Mohan--Khan supply general global dynamics/stability context, while classical center-manifold theory supplies methodology.

Reasoning: General methodology and stability results do not mechanically determine the transport-dependent cubic, quintic and logarithmic coefficients.
### exact_database_or_table

Searches: Resultary semantic search for the coefficient \((7r^2-9)/288\) in convective Chafee--Infante dynamics

Evidence: No earlier exact record was located.

Reasoning: The coefficients are analytic normal-form invariants rather than database values.
### claim_vs_prior_implication

Searches: Mohan--Khan official article page and abstract; assigned symbolic normal-form calculation

Evidence: The accessible primary material does not state a critical center reduction; the coefficients require solving the stable-mode invariance equations.

Reasoning: The final claim is not a direct consequence of the inspected prior statements without the new model-specific normal-form calculation.

## Scientific value — PASS

PASS. The result identifies a natural mechanism at a canonical bifurcation: conservative transport leaves the global threshold unchanged but quantitatively changes the critical nonlinear relaxation and post-threshold profile. The explicit cubic correction, logarithmic crossover and second-harmonic wake are motivated dynamical invariants, not arbitrary coefficients.

## Source inspections

- **On the generalized Burgers-Huxley equation: Existence, uniqueness, regularity, global attractors and numerical studies** — https://doi.org/10.3934/dcdsb.2020270. Material read: Official article page, abstract, introduction-level indexed material and references; the available extraction did not expose complete theorem-level full text. Assessment: PLAUSIBLE_PRIMARY_SOURCE_WITH_ACCESS_LIMITATION. Evidence: It treats well-posedness, global attractors, stationary solutions and exponential stability, but no center-manifold or critical-relaxation coefficient was exposed in material actually read.
- **Published-record search for convective Chafee-Infante critical relaxation** — Resultary semantic search. Material read: Ranked results for convective Chafee--Infante, Burgers--Huxley, critical relaxation and center-manifold coefficients. Assessment: NO_EARLIER_EXACT_COVERAGE_FOUND. Evidence: The assigned record was the only exact match; other hits concerned different dynamical systems.

## Limitations and residual risks

The sharp critical asymptotics exclude the strong-stable exceptional class; the post-threshold branch statement is local; homogeneous Dirichlet data are essential to the exact convection cancellation. The closest generalized Burgers-Huxley long-time paper was inspectable at its official abstract and article page but not at complete theorem-level text through the available interface, so hidden overlap remains a residual originality risk.

- The complete theorem-level text of the 2021 Mohan--Khan article was not available through the extraction interface and remains a genuine originality risk.
- Older model-specific Burgers--Huxley literature may contain an equivalent normal-form calculation under different normalization.

## Disposition

**passed**
