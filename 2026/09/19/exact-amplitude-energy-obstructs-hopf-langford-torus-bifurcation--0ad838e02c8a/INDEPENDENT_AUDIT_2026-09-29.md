# Independent audit — 2026-09-29

Record: `2026/09/19/exact-amplitude-energy-obstructs-hopf-langford-torus-bifurcation--0ad838e02c8a`  
Assigned and audited source tree: `394ebaf9b953568655a2074084a905824a07f59d`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `7d0b2c778e882a7ba409cd6ce464eeca23621c30`  
Disposition: **passed**

## Correctness

**independently_supported**. The exact reduction is correct. Polar coordinates give rdot=r(z-a), thetadot=beta and zdot=mu z-gamma(r^2+z^2); the off-axis periodic orbit is the equilibrium (b,a) of the amplitude system. Its Jacobian has trace T=(2gamma+1)mu-2gamma alpha and determinant 2gamma b^2, so the nontrivial Floquet multipliers have unit modulus exactly on T=0. Independently substituting w=r^gamma reproduces w''-T w'=gamma^2 b^2 w-gamma^2 w^(1+2/gamma), hence E'=T(w')^2 exactly. A surrounding invariant circle of the angular return map is therefore impossible for T≠0 by an energy extremum argument; at T=0 the positive equilibrium is a nonlinear center and nearby energy levels suspend to invariant two-tori. For alpha=epsilon,beta=gamma=1,mu=nu epsilon, the exact crossing is nu=2/3, while the current source curve has the nonzero O(epsilon) correction stated in the record, so it lies at T≠0 and cannot support the claimed torus.

## Originality

**qualified_source_specific_correction**. Classical Hopf–Langford work and Vassilev–Nikolov already contain polar/amplitude reductions and integrable/first-integral cases, so those mechanisms are not new. The current Domingues arXiv entry still publicly claims a smooth Neimark–Sacker curve with a unique surrounding invariant torus and positive first Lyapunov coefficient. Targeted searches found no public erratum or source-specific correction deriving the exact trace surface and strict energy obstruction for this four-parameter system. Originality is therefore supported narrowly as a correction of the 2026 theorem and its displayed bifurcation curve.

## Scientific value

**high_value_source_correction**. The exact energy identity rules out the central qualitative conclusion of a very recent bifurcation theorem on an open parameter set and replaces the claimed generic Neimark–Sacker crossing with an exact conservative-center degeneracy. The correction is structurally decisive rather than a small coefficient adjustment.

## Literature and evidence checked

- https://arxiv.org/abs/2609.18010
- https://doi.org/10.3390/axioms14010008
- https://doi.org/10.1016/j.cnsns.2020.105464
- https://doi.org/10.1007/s11071-017-4012-1
- https://doi.org/10.1137/0137003

## Limitations

- The statement assumes gamma>0, beta≠0, and existence of the positive off-axis orbit b^2>0.
- Earlier Hopf–Langford literature already contains the reduction and integrable-center mechanisms.
- The audit did not attempt a classification of generalized Langford systems with additional nonlinear terms.
- The originality verdict is intentionally source-specific, not a claim that the energy form is new in the broader Langford literature.
