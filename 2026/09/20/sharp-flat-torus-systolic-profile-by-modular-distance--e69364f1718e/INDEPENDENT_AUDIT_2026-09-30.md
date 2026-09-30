# Independent audit — 2026-09-30 UTC

Record: `2026/09/20/sharp-flat-torus-systolic-profile-by-modular-distance--e69364f1718e`  
Assigned and audited source tree: `2370acb2d8cf353443d623e984d58df37a8fa295`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `5a1fd278b1fb7e0c4e0b6858f02abc1d9fcc580b`  
Disposition: **passed**

## Correctness

**independently_supported**. The modular-distance profile is correct. In the reduced half-domain F_+, a flat torus has normalized systolic ratio q=(sqrt(3)/2)/Im(tau), and the Coxeter-chamber geometry makes rho=e^{pi i/3} the nearest lift of the hexagonal orbifold point. A hyperbolic circle of radius d about rho is the stated Euclidean circle. Its maximal feasible height lies on Re(tau)=1/2 and yields q_min=e^{-d}. The minimum feasible height lies on |tau|=1 until the circle reaches i at d=log sqrt(3), then on Re(tau)=0; these intersections give exactly the two branches of M(d). Both branches agree at the square torus with value sqrt(3)/2. Algebraic inversion gives the displayed D(q), and continuity along the connected feasible arc supplies every intermediate value.

## Originality

**qualified_best_of_knowledge_modular_profile**. Loewner/Pu supplies the global systolic maximum at the hexagonal torus, and modern flat-torus moduli references identify the modular quotient and the reduced-coordinate formula for the systolic ratio. Targeted searches in systolic stability, modular-surface, Hermite-invariant and lattice-shape language did not locate the audited two-sided fixed-distance profile, inverse profile, or rhombic-to-rectangular transition. The derivation is elementary once the modular chamber is chosen, so older reduction-theory or geometry-of-numbers folklore remains a material attribution risk; originality is therefore asserted only for the explicit complete profile to the best of current knowledge.

## Scientific value

**meaningful_global_stability_profile**. The theorem upgrades the equality case of Loewner's flat-torus inequality to a complete global sharp diagram on the natural moduli orbifold, identifies the square-torus phase transition, and provides an exact inverse bound from a measured systolic ratio to modular distance.

## Independent checks

- Re-derived q=(sqrt(3)/2)/y from shortest-vector reduction in the modular fundamental domain.
- Re-derived the Euclidean equation of a hyperbolic circle centered at rho.
- Evaluated both M(d) branches at d=log sqrt(3) and verified they agree at sqrt(3)/2.
- Checked the algebraic inversions giving both branches of D(q) and the e^{-d} lower envelope.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/20/sharp-flat-torus-systolic-profile-by-modular-distance--e69364f1718e
- https://doi.org/10.2140/pjm.1952.2.55
- https://arxiv.org/abs/0803.0690
- https://doi.org/10.5802/ahl.223
- https://arxiv.org/abs/1003.1532
## Limitations

- Flat two-tori up to similarity only; arbitrary Riemannian torus metrics are outside scope.
- The distance normalization is the curvature -1 hyperbolic quotient metric.
- Only the systolic ratio is profiled; other lattice-shape observables are not controlled.
- The short modular-coordinate derivation creates genuine folklore/older-reduction-theory priority risk.
