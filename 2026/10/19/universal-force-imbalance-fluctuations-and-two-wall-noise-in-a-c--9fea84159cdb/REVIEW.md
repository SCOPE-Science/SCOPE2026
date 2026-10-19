# Scientific review

## Correctness

PASS. The model and wall sticking convention are explicit, as are parameter quantifiers and normalization. Stationary mass balance gives the uniform bulk densities and two boundary atoms. The bounded pathwise force-imbalance coboundary reduces the signed contact large deviations to the known two-state telegraph tilted-generator eigenvalue; the endpoint rate function follows by Legendre duality. An explicitly stated wall-boundary Poisson equation is solved and evaluated at both wall atoms to obtain every entry of the integrated covariance matrix. The positive minorization proves the mixing needed for the Green–Kubo step. The monotonicity and noncommutation of limits follow from differentiated rational expressions and a fixed-time occupancy bound. Finite-generator and symbolic checks are reproducible in `verify.py`, but finite calculations alone do not establish the theorem.

## Originality

PASS, with access risk. Angelani (2017; full open arXiv preprint 2206.03123, inspected) already analyzes **the same** sticking-at-hard-wall process and explicitly derives one-time wall-pressure and stationary-occupancy laws. Li, Eichhorn and Dabelow (2026, arXiv:2610.01287v1, indexed abstract inspected) analyze the finite-box active ideal-gas law, again focused on mean pressure; their inaccessible full text could contain additional relevant analysis. Bressloff (2025, arXiv:2508.20473, primary paper sections 2–5 inspected) studies weighted boundary local times and first passage for a different or broader model. Mukherjee, Le Doussal and Smith (2024, arXiv:2405.07032v1, full paper inspected) treat local and interior occupation-time large deviations without a two-wall hard-contact force observable. Roberts and Pruessner (2022, arXiv:2206.06105, full paper inspected) model boundary-only tumbling with added diffusion. None of the materially inspected papers states or implies the complete two-wall covariance, the pathwise signed-force telegraph equivalence, and the resulting noncommuting infinite-volume/time limits. General Green–Kubo/Poisson-equation theory can imply the method but does not supply these evaluated physical observables without specialization. Remaining coverage risks from the unavailable 2026 full text and broad reflected-telegraph literature are acknowledged, not treated as proof of uniqueness.

## Value

PASS. Active-gas pressure equations give mean wall force but cannot infer two-wall force noise or its large deviations. The exact matrix distinguishes correlated noise at opposite walls; its signed eigenmode is size-invariant, whereas total occupancy noise increases with box size despite a vanishing mean and exhibits noncommuting observation/size limits. This is a physically motivated fluctuation diagnostic, not a parameter relabeling or a finite table value.

## Limitations

The force observable counts contact impulses as time spent exerting a fixed stall force, not impact kicks. Strictly positive speed, box length, and flipping rate are essential. The original October 2026 paper was accessible only at abstract level; a full-text comparison therefore remains a literature risk. All review judgments here are internal to the present work and are not independent certification.

Self-review: passed. Independent audit: not yet performed.
