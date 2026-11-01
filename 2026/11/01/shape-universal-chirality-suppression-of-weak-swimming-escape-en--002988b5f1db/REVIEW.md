# Self-review

## Correctness — PASS

The hypothesis specifies a bounded connected smooth fully absorbing domain, independent uniform initial position and heading, and strictly positive translational diffusion. The backward operator is coercive despite nonreversible angular drift, and spatial Dirichlet Poincaré estimates bound the swimming perturbation operator. Uniform angular symmetry eliminates odd powers. The signed quadratic variation follows by the skew spatial drift and the adjoint unperturbed Poisson equation. The first two angular harmonics give a Lorentzian factor for each Dirichlet mode; Parseval controls convergence and differentiation, with strictness guaranteed by the nonconstant passive torsion function. The global mean-speedup inequality follows separately by energy Cauchy–Schwarz. Checks of interval and disk normalizations and 126 deterministic computational checks passed. A finite verification run is not an infinite proof.

## Originality — PASS, qualified

The 2026 chiral MFPT source treats specific intervals and partially absorbing disk exit windows, mainly through high-angular-speed matched expansions and finite-speed numerics, without a fully absorbing arbitrary-domain quadratic susceptibility theorem. The 2025 two-dimensional MFPT study stops at first order in weak activity, whereas the 2026 chiral splitting study computes exit-side probabilities, not total mean times. The 2025 absorbing-half-space perturbation work studies a divergent mean and the 2023 absorbing-disk spectral scheme is achiral; the special achiral disk coefficient is treated only as verification. Standard advection and resolvent machinery are explicitly credited. The claim-to-prior comparisons, primary-text passages and remaining broader-operator-theorem risk are documented in AUDIT.json. Absence of a database match is not proof of uniqueness.

## Value — PASS

The source literature demonstrates orientation- and boundary-dependent optimal chirality, leaving an interpretable prediction for a physically natural uniform ensemble and fully absorbing arbitrary confinement. The strict complete-monotonicity hierarchy is stronger than one positive perturbative coefficient: it classifies all squared-chirality derivatives, for every shape, including zero rotational diffusion. The exact spectral weights connect observable escape response to passive domain geometry, while clearly exposing why mixed absorbing/reflecting boundaries fall outside the theorem. The result has a natural use in weak-swimming transport comparisons and is not a parameter renaming or finite table lookup.

## Sources and limitations

Primary motivating source: Iyaniwura–Qiu–Peng, arXiv:2605.23095v1, especially 1D high-chirality results and the partially absorbing disk section. Close comparisons: Iyaniwura–Peng arXiv:2506.15813v1 (first-order nonchiral MFPT); Iyaniwura–Peng arXiv:2603.13621v2 (splitting probabilities); Baouche et al. arXiv:2503.05401v1 (achiral half-space FPT); Di Trapani et al. arXiv:2306.12702 (achiral disk propagator); Iyer et al., DOI:10.1137/090776895 (incompressible drift). The limit concerns only the quadratic swimming coefficient and assumes a uniformly sampled position and heading. Broader unlocated functional-analytic response statements remain a priority risk. No independent mathematical audit was performed.

Self-review: passed. Independent audit: not yet performed.
