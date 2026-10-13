# Scientific review

## Correctness — PASS

The model is an exact positive-parameter specialization of the cited original system. The nonnegative domain and finite bounds follow from mass balance. Strictly monotone log-biomass ratio forces periodic trajectories onto the symmetric plane. A strictly convex scalar nutrient–biomass intersection function proves the exact fold census; the determinant of the symmetric Jacobian has the sign of the branch derivative. The antisymmetric eigenvalue is strictly negative. On the upper branch, any hypothetical nonnegative trace requires \((d-D)u>dD\) although \(0<u<d\), yielding the sharp \(d>2D\) necessity. A positive family realizes every greater ratio with transversal imaginary eigenvalues. The rational example has exactly computed transversality and negative cubic normal form coefficient, proving a small stable periodic orbit. The global no-cycle proof for \(d\le D\) uses a strictly negative Dulac divergence and planar omega-limit alternatives. Exact symbolic derivative checks were replayed from the included verifier. The proof does not confuse a spectral crossing with a nondegenerate Hopf event.

## Originality — PASS, within the stated scope

The complete 2026 source (arXiv:2603.11002v1) develops the broader chemostat, generic Routh–Hurwitz inequalities, and numerical oscillations, but does not isolate identical Monod mutualists with equal biomass removal \(d\ne D\) and derive the sharp \(d>2D\) feasible-Hopf boundary or provide the exact cubic-sign example. The full 2009 El Hajji et al. study concerns common hydraulic removal (\(d=D\)), and thus its endpoint convergence and Dulac ideas are antecedents, not new contributions here. The 2020 Vet–Gelens–Gonze work addresses metabolite-mediated cross-feeding, a different nutrient system. Direct semantic comparisons to chemostat findings in the published mathematical research database revealed only a sequential two-reactor AM2 no-Hopf result and a reversible mutation chemostat, neither implying the present result. Generic source-local spectral inequalities are acknowledged as already available; novelty is not assigned to their routine reformulation, but to the exact sharp threshold plus constructive supercritical witness and global synchronization/non-oscillation structure.

## Value — PASS

A major point of the 2026 ecological paper is that mortality and distinct removal introduce oscillations. This classification answers a more precise mechanistic question: are **different** removal rates necessary, or is a common rate exceeding dilution enough? It proves the latter, supplies the exact necessary-and-feasible Hopf inequality, the broad global no-cycle subregime, and an explicit stable-cycle witness. These are natural structural distinctions for the same ecologically motivated parameter family rather than an unmotivated numerical slice. The result does not purport to be an experimental prescription.

## Closest literature and residual limitations

Mtar–Fekih-Salem (2026) is the motivating complete primary text; El Hajji et al. (2009) is the strongest endpoint global precedent. General chemostat stability inequalities overlap elementary local arguments. The 2020 cross-feeding model and literature on mortality-driven cycles in predator–prey systems provide conceptual context, not the same equations. Unindexed or inaccessible transferable general bifurcation theory remains an originality risk. The theorem proves no global no-cycle result in \(D<d\le2D\), and full Hopf nondegeneracy is asserted only for the checked rational example.

Self-review: passed. Independent audit: not yet performed.
