# Independent mathematical audit

## correctness

PASS

Independently derived the Jacobian on the moving equilibrium and characteristic polynomial λ³+22λ²+b(k+2)λ/(k+1)+24b. The positive coefficients and Routh first-column signs give no right-half-plane roots below 10 and two above 10; above 10 neither a positive real root nor an imaginary pair is possible. At 10 the factors are λ+22 and λ²+12b/11, with simple roots for every b>0. Implicit differentiation with respect to k on the moving equilibrium gives the crossing b/(5324+12b). Independently recomputed the Lyapunov coefficient from the field Hessians and the resolvents by adjugates. In the replay, if ν=iω and A is the critical Jacobian, Π=(A+22I)(A+νI)/((ν+22)2ν) is the spectral projector. Normalize q=Πe_z/Π_zz; the row e_zᵀΠ then gives the correctly paired left functional with value 1 on q. This gives exactly the frozen positive formula for ℓ₁ as well as the crossing. The positive radial cubic and positive crossing give a nondegenerate subcritical branch for k<10 sufficiently close to 10 at each fixed b. The critical equilibrium itself is unstable by the repelling cubic on its center manifold. The small branch has radial expansion and contraction in the transverse direction continuing −22, in addition to the neutral orbit direction. The reflection maps the entire branch to the one near the other distinct equilibrium. No uniform k-neighborhood in b is asserted; b=0 is excluded and the critical frequency vanishes there. Replay: python review_evidence/finite_checks.py, section labelled 1, for the crossing and coefficient; local branch and Floquet claims use the Hopf theorem, not direct orbit numerics.

## originality

PASS

Pass for the nonlinear exact subcritical Hopf theorem, including the uniform sign, normalized coefficient and local saddle-cycle consequence. The linear stability cutoff k=10 is already implied exactly by the original DOI's general Routh–Hurwitz criterion, not merely suggested by its numerical scan. The original and strongest same-flow recurrence comparator do not supply the nonlinear conclusion in the inspected passages. Do not count the equilibrium formula, linear criterion, or its cutoff specialization as original. One named related Physica D source remains a priority risk.

## value

PASS

For a fixed published model the exact all-b sign distinguishes a local saddle branch on the stable-equilibrium side from supercritical stable-cycle onset or a change of Hopf criticality as b varies. That geometric information is not supplied by the known linear boundary, sweep, or coded attractor orbits. It informs local stability and future basin questions without claiming a basin boundary or chaos theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
