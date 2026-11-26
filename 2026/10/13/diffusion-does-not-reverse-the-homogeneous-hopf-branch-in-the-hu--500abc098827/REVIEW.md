# Independent mathematical audit

## correctness

PASS

The constant Neumann subspace solves exactly the planar equations for all d1,d2, and its periodic solutions therefore occur at the same a values with or without diffusion. For sigma=1 the positive equilibrium is (1/sqrt(a),(sqrt(a)-1)/a); the kinetic trace 1-2/sqrt(a) gives crossing speed 1/16 at a=4. The Jacobian at (1/2,1/4) has rows (-1/2,-3/2) and (1/2,1/2), and frequency omega=1/sqrt(2). For a direct planar normal-form check set X=V-1/4 and Y=-(U-1/2+V-1/4)/sqrt(2). Then the canonical linear part is (-omega Y,omega X) and the nonlinear terms are F=-X^2-3sqrt(2)XY-4X^3-4sqrt(2)X^2Y and G=(X+sqrt(2)Y)^2/sqrt(2). The planar cubic radial formula gives -24/16+2sqrt(2)/(16omega)=-5/4 in physical time and this real linear amplitude. The convention in the checker has X=2 Re z to first order and scales time by omega, giving 4(-5/4)/omega=-5sqrt(2). The negative coefficient and positive crossing put the small homogeneous cycles at a>4. In the H1 criteria as recorded, the ratio 5/2 lies between 1^2 and 2^2 and substitution gives r1=2<10. For mode 1 the matrix is the kinetic Jacobian minus diag(10,1/5), with trace -51/5 and determinant -12/5. Its positive simple eigenvalue gives a limiting Floquet multiplier >1 and persists by continuity for small homogeneous cycles; modes k>=2 have positive determinants 1/2-(49/10)k^2+2k^4 and negative traces. This independently establishes the branch side, transverse instability, and the contradiction with positive determinants if the primary assertion is as reported. Inspected but did not run the supplied symbolic script. The primary theorem wording is recorded in the frozen package and was not independently retrieved.

## originality

PASS

Credit the source-specific exact local diagnosis: the recorded H1 parameter conditions are met and the homogeneous cycles are on the supercritical side while a specified spatial mode is unstable. The invariant-subspace principle, general Hopf theory and the model itself are not new. No distinct checked statement covers that simultaneous diagnosis or the indicated modal-sign conflict. The reported wording of the two primary statements remains a material access limitation; this decision credits the independently proved mathematical witness, not an independently authenticated quotation or an exhaustive erratum search.

## value

PASS

The parameters are motivated by the stated H1 classification, not a random test slice. A branch-side correction with an exact unstable spatial mode changes how one interprets emergence of homogeneous oscillations in this regime: the supercritical kinetic cycle exists but is not a local PDE attractor. Reporting both instead of just a generic invariant-subspace observation resolves a source-specific distinction at bifurcation onset.

The dated certificate retains the supplied scientific assessment, sources and limitations.
