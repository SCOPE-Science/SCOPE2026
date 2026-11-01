---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS: The Szego Cauchy identity gives det S=uvw for the three squared pseudohyperbolic separations. Since Bergman B is the entrywise square of S, elementary 3x3 Hermitian expansion gives det B=uvw(6-2(u+v+w)+uvw). Its polynomial factor P>0 on (0,1)^3, and partial log derivatives (u'/u)C_u have C_u>0 with C_u-C_v=-2(u-v)/P. For angular gaps α>β both <π, u(α)>u(β) and the positive ratio u'/u decreases; for α≥π its derivative ≤0 while β<π gives positive. Thus strict Schur-Ostrowski criterion applies throughout positive gaps summing to 2π. Coincident nodes give zero. At equal 2π/3 gaps the sharp determinant equals 81t³(t³+2)(2t³+1)/(1+t+t²)^6, approaching 162r^6 at r→0 and deficit (1-t)^4/3 at t→1. Independently verified exact algebra/limit and nine complex direct Gram determinants; finite samples not substituted for the derivative proof.

## originality

PASS

PASS, qualified: Bergman Schwarz-Pick Loewner comparisons are not the same as node-position determinant maximization. General Gaussian-kernel approximate Fekete work concerns another kernel and approximate sites. The published Resultary Szego-orbit determinant is for power-one Szego kernels and its result alone does not show strict gap Schur concavity for the entrywise-square exponent-two Bergman matrix. The new three-point polynomial coupling and derivative inequality supply the missing comparison. Classical exact Fekete configurations could overlap.

## value

PASS

PASS: Optimal kernel Gram determinant and strict gap order are natural stability/design invariants for reproducing-kernel interpolation. A unique optimum at every radius, not merely a stationary symmetric guess, and a strict majorization law with sharp boundary asymptotics are reusable precise facts for the Bergman space.

The dated certificate retains the supplied scientific assessment, sources and limitations.
