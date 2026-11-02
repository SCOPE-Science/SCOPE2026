---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

At the known witness X*=((-1,1,1),(1,-1,1),(1,1,-1)) the deficit F_{p*} vanishes because 3^{1/p*}=3/2 and all pair sums have norm 2; differentiation of the seven nonzero terms gives zero first derivative. For p*>2 the l_p norm is C2 even at vectors with zero individual coordinates; pair sums 2e_i have vanishing Hessian. Rebuilt exact rational projection-block matrix M with blocks P_u+delta_ij P_vi, and independently computed characteristic polynomial z(z-1)^4(3z²-12z+4)^2/9, kernel exactly span X*. Multiplying eigenvalues by (p*-1)/2 yields stated spectrum, hence Taylor expansion off scaling ray yields sharp transverse ratio (p*-1)(1-sqrt6/3)/2. Uniform C2 Taylor estimates ensure local positivity for all perturbation directions, not just sampled ones. Positive-definite restricted Hessian on H={X·X*=9} gives IFT unique nearby normalized minimizer and derivative -6 log(3)/p*²; positive one-sided p<p* cone follows from homogeneity. No global Hornich-Hlawka endpoint theorem is asserted.

## originality

PASS

Best-of-knowledge: compared the concrete final statement and implications to the actual primary literature, equivalent formulations, general frameworks and mathematical record searches. No decisive preexisting theorem subsuming the full submitted result found; classical ingredients and residual risks are credited explicitly.

## value

PASS

The critical real 3D inequality is a highlighted open reduction. The previously known symmetric zero witness is a natural candidate source of endpoint counterexamples; its exact positive transverse Hessian and optimal curvature certify local rigidity and rule out local counterexamples below the critical exponent. This is a motivated structural obstruction to a plausible solution strategy, not an arbitrary tiny negative test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
