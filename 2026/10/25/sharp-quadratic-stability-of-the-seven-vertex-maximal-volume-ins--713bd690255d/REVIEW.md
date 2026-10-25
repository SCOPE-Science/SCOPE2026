# Self-review

## Correctness

**PASS.** The seven spherical vertices are explicitly specified, and the twelve tetrahedral facets follow from the strict supporting-hyperplane inequalities of the free-sum model. The exact oriented-determinant volume identity gives \(V(P_*)=\sqrt3/4\). Each Hessian entry is reconstructed from finite determinant replacement formulas and the unit-sphere normalization; symbolic arithmetic independently verifies the full degree-21 characteristic polynomial and the vanishing first derivative. Six independent infinitesimal rotations account for all six zero modes, with strict negative spectrum transverse to the rotation orbit. A normal-tubular Taylor argument supplies the sharp quadratic gap. The packaged verification program computes this from the stated geometry and checks it against direct four-dimensional hull volumes. Risk: readers must trust or rerun an exact but nontrivial finite symbolic determinant calculation; numerical checks alone do not prove the theorem.

## Originality

**PASS within the accessible literature, with residual priority uncertainty.** The closest primary works are Medgyes's 2026 global seven-vertex optimum and Horváth–Lángi's older structural classification. They establish the maximal volume and optimizer but do not state a complete constrained Hessian spectrum, a rotational-kernel characterization, or the sharp quadratic vertex-distance coefficient. Relevant local-stability calculations for different polytopes and constrained-section problems concern mathematically different functions and cannot specialize to this result. Searches included exact configurations, aliases such as orthogonal free sums and signed facet volumes, second variation, Morse–Bott stability and numerical coefficients. Unindexed historical results remain possible; no independent novelty review was performed.

## Value

**PASS.** In dimension four with seven vertices the 2026 source resolves a natural first open global inscribed-volume optimization problem. Its uniquely characterized optimizer makes quantitative *local rigidity* mathematically motivated. The full multi-eigenspace spectrum detects anisotropic deformation stiffness; the explicit sharp constant identifies the slowest genuine instability-free mode and quantifies second-order loss under arbitrary seven-vertex spherical perturbations. This is not simply the pre-existing global optimum or a renormalization of its volume.

## Remaining limitations

The result is local for ordered configurations and does not provide an effective neighborhood radius or global quantitative gap. Earlier inaccessible or unindexed stability work could affect priority; the finite exact calculation and argument still require independent scrutiny.

Self-review: passed. Independent audit: not yet performed.
