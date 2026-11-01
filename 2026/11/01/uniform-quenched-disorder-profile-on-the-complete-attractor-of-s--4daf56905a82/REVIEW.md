# Scientific review

## Correctness — PASS
The statement is an all-time estimate on bounded bilateral trajectories, not a claim that finite simulations prove an infinite-time theorem. Positivity of the quenched inputs and convex averaging force positive voltages on every such trajectory. The scalar recovery recursion gives the global upper recovery bound \(Y=c/(1-a)\) and the exponential factor in the activation map gives the explicit derivative bounds \(L_x,L_y\). Orthogonal centering eliminates the common forcing exactly. A backward geometric-series identity for the recovery variable bounds its transverse component; the voltage inequality closes when \(qL<1\). The resulting constants are uniform in time, network size, and longitudinal dynamics. A compact absorbing box guarantees nonempty complete dynamics. The separate finite numerical checker agrees with the analytic bounds; it is not an infinite proof.

## Originality — PASS under inspected evidence
The source introducing these heterogeneous mean-field Chialvo maps (Velez-Rojas and Cosenza, arXiv:2610.03344v1) analyzes chaotic Griffiths clustering numerically. Its equations and main analysis were read in full: it does not give a uniform attraction-set profile, an all-complete-orbits quenched-input expansion, or a size-independent quadratic remainder. The complete article of Lamb and Le, DOI:10.1140/epjp/s13360-026-08264-6, uses two nonidentical electrically diffusive *coupling strengths* rather than the global mean-field averaging at issue and studies fractal basins. The generic 2011 near-identical-systems study of Acharyya and Amritkar was checked at abstract level only and remains a priority risk, as do other general synchronization results. Published-result searches for the present model, parameters, disorder vector, asymptotic variance, and equivalent reductions returned no covering theorem. Absence of a database match is not proof of global novelty.

## Mathematical value — PASS
The problem is motivated by the source's disorder-driven coherence transition. The theorem does not merely give a small coupling-error bound: it identifies one universal, *trajectory-independent* rank-one transverse shape on the entire compact attractor, gives the exact leading coefficient of its spatial variance, and covers high-dimensional dynamics without assuming a synchronized or hyperbolic longitudinal attractor. This separates the residual heterogeneity encoded by quenched parameters from the time-varying collective dynamics and provides a benchmark for spatial coherence in numerical studies. Its source-relevant sufficient coupling window is conservative but explicit, not an asserted optimal onset.

## Closest literature and risks
1. Velez-Rojas and Cosenza (2026), arXiv:2610.03344v1: self-review, numerical clustering; does not prove the present strong-coupling all-orbit expansion.
2. Lamb and Le (2026), DOI:10.1140/epjp/s13360-026-08264-6: different two-neuron electrical coupling; basin geometry rather than universal disorder imprint.
3. Acharyya and Amritkar (2011), arXiv:1111.5408: near-identical network synchronization, abstract inspected; a more general mismatch theorem might imply a related bound. Full theorem-by-theorem comparison was not possible.
The exact rank-one expansion is proved for the complete-graph averaging architecture, not generic graph couplings. Historical novelty requires independent expert evaluation.

Self-review: passed. Independent audit: not yet performed.
