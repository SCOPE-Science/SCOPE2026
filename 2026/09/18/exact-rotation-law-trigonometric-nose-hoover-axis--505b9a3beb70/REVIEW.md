# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

For a=0, H=cos x+cos y is exactly conserved. The source paper gives the mechanical period T(h)=4K(k) and the exact orbit average <cos y>=h/2 on 0<h<2. Integrating the exact z equation over one mechanical period therefore gives Delta z=bT(h)(1-h), with no perturbative remainder. The negative-energy formula follows by the shift (x,y)->(x-pi,y-pi), which changes the sign of cos y and maps energy h<0 to -h>0 while preserving the period.

On any compact regular annulus, the source energy-phase coordinate theta is smooth and satisfies theta'=Omega(h). Subtracting the mean 1-h from g=1-2 cos Y leaves a zero-mean periodic function. The one-dimensional cohomological equation Omega psi_theta=g-(1-h) therefore has a smooth periodic solution, and zeta=z-b psi gives the exact linear system h'=0, theta'=Omega(h), zeta'=b(1-h). The rational/irrational classification is then the standard classification of a linear flow on T^2. On 0<h<2, differentiating the integral representation C(h)=(2/pi)(1-h)K(sqrt(1-h^2/4)) gives a strictly negative integrand derivative -(4 cos^2(phi)+h sin^2(phi))/(4D^3). Hence C decreases bijectively from +infinity to -1, so every admissible rational rotation occurs at exactly one positive energy. The periodic energies are countable and dense, while irrational energies have full Lebesgue measure.

For b nonzero, rho_b(h)=b(1-h)/Omega(h) is analytic and nonconstant on each regular energy family. On the positive family rho_b'(1)=-b/Omega(1) is nonzero; analyticity prevents constancy on any subinterval. Irrational-rotation energies are consequently dense. A continuous first integral must be constant on each irrational torus because a single orbit is dense there, and continuity in h extends constancy to rational tori. Hence every continuous first integral on a full invariant regular annulus factors through H.

The branch monodromy follows directly from constancy of F=z+bP_h along a lifted orbit: after one mechanical circuit z changes by bT(1-h), forcing Delta P_h=-T(1-h).

The compact verification artifact independently integrates representative positive and negative energy orbits. The executed test found maximum mechanical return error 1.284e-11 and maximum z-drift error 8.830e-12, consistent with the exact formulas.

## Adversarial checks

The result does not claim that the source paper's branchwise elliptic formulas are locally incorrect. They are valid on charts with consistent branch choices. The new obstruction concerns a globally single-valued continuous second integral on a full invariant regular annulus of the natural torus phase space.

The separatrix h=0 is excluded. The source itself notes logarithmic singularities there, and the energy-phase coordinate used in the exact conjugacy degenerates at the separatrix. The elliptic critical levels h=+/-2 are also excluded from the annulus statement.

The factorization theorem requires continuity of a candidate first integral across the full invariant annulus. It does not exclude deliberately branch-dependent, discontinuous, multivalued, or covering-space invariants.

The exact normal form is special to a=0. No statement is made that the full a nonzero system remains conjugate to a linear torus flow.

## Originality

PASS, to the best of our knowledge.

The full arXiv:2609.19958v1 HTML text was inspected, in particular the a=0 system and branchwise elliptic first integrals, the energy-phase parametrization, the exact period, the identity <cos y>=h/2, the definition C(h)=(1-h)/Omega(h), and the later averaged equations. The source does not state the finite-b exact return map on the a=0 invariant tori, the rational/irrational orbit classification, the exact cohomological reduction to a linear Kronecker flow, the branch monodromy, or the resulting obstruction to a second globally single-valued continuous first integral on a full regular annulus.

Searches using the exact title and arXiv identifier together with `rotation number`, `return map`, `irrational`, `dense torus`, `monodromy`, `global first integral`, `correction`, and synonymous Nosé–Hoover terminology did not locate a public source-specific derivation or correction. The current arXiv record inspected is v1, submitted 17 September 2026.

General action-angle coordinates, the solution of a zero-mean one-dimensional cohomological equation, and the rational/irrational classification of Kronecker flows are standard dynamical-systems facts and are explicitly excluded from the originality claim. The originality claim is limited to their exact application to this newly introduced trigonometric Nosé–Hoover axis and the resulting global interpretation of the source's branchwise integrals.

Because the source preprint is very recent, an unindexed author revision or discussion remains the principal residual originality risk.

## Value

PASS.

The result upgrades a collection of local formulas into a complete global description of the regular a=0 dynamics. It identifies an exact twist/rotation function, proves strict monotonicity and a one-to-one resonance labeling on the positive-energy family, shows that periodic energy tori are countable dense while irrational tori have full measure, singles out h=1 as an exact period-one mechanical resonance for arbitrary b, and explains the branch dependence of the elliptic primitive through explicit monodromy.

The distinction between local first-integral charts and a global second integral is mathematically substantive on T^3: generic irrational energy tori admit dense trajectories, so no second continuous invariant can separate their orbits. The exact return map also gives a simple benchmark for numerical sections and for perturbative studies away from a=0.

## Scope and limitations

The theorem concerns the a=0, b nonzero trigonometric Nosé–Hoover system of arXiv:2609.19958v1 on regular energy annuli. It excludes the separatrix and critical mechanical equilibria, does not address persistence under nonzero a, and does not rule out local, multivalued, or singular first integrals. Originality is qualified to the best of our knowledge.
