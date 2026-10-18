---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

The original mathematical conclusion (missing k and counterexample) survives a necessary precision repair: with F=[[0,kappa k M2],[0,0]] and V=[[D+delta,0],[-b delta,D+kM2]], direct multiplication yields rho(FV^-1)=b delta kappa k M2/((D+delta)(D+kM2)), NOT its square root as stated in original RESULT. Final replacement RESULT.md correctly distinguishes cycle spectral radius and source-convention square-root R, preserving threshold at one. Independently sympy-checked matrix identity and exact witness: rho=5/22, printed-square=250/11, Jacobian [[-2,1/20],[10,-11/10]] trace -31/10 and determinant 17/10. E3 would require M3=200/3 but resource balance forces M3<10. No unsupported claim of full five-dimensional stability.

## originality

PASS

This is not a general new theorem on next-generation matrices; van den Driessche and Watmough provide that theory. The inspected published 2017 source defines k’=kappa k and uses infected gain kappa k M P but drops k in the printed resistant reproduction number. The later equilibrium coefficient A2 and G(lambda2) rely on k, establishing a source-specific inconsistency not previously corrected in accessible literature. The strict admissible witness is a new explicit counterexample to using printed threshold literally.

## value

PASS

A literal reproduction threshold in a published bifurcation/existence theorem changes from supercritical to subcritical at an admissible positive parameter point. Independent linear stability and equilibrium nonexistence demonstrate mathematically consequential rather than cosmetic normalization error. The repaired claim carefully separates spectral radius and its square-root convention and limits implications to source statements actually affected.

The dated certificate retains the supplied scientific assessment, sources and limitations.
