---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Fresh derivation confirms the boundary law. Yeo's standard-teleportation criterion is sinh x>cosh(ηx); equality rearranges exactly to tanh((1−η)x/2)=exp(−(1+η)x), with a unique positive root because the two sides are strictly increasing/decreasing. Setting δ=1−η, u=δx/2 and κ=(1+η)/δ gives \(\tanh u=e^{-2\kappa u}\). As κ→∞, u→0, so \(2\kappa u\,e^{2\kappa u}=2\kappa(1+o(1))\) and (1+η)x~W(2κ). Substituting the equality into the source concurrence yields \(C_r=\frac12-e^{-x}-\frac12e^{-2x}\). Since \(e^{-(1+\eta)x}\sim \delta(1+\eta)x/4\) and \(\delta(1+\eta)x\to0\), the concurrence gap has the claimed (1/2)sqrt(δ W(4/δ)) scale. Independent numerical roots at η=.9,.99,.999,.9999 show the temperature asymptotic ratio tending to 1 (about 1.000446, 1.0000077, 1.00000012, 1.000000002) and the gap ratio tending to 1.

## originality

PASS

Yeo already gives the exact fidelity/concurrence formulas, the threshold inequality and a finite table through η=.9; those are expressly prior. The audited contribution is the singular η↑1 analysis: the monotone tanh form, Lambert-W collapse scale and limiting concurrence/gap law. Targeted searches combining the XX thermal teleportation model, magnetic-field boundary and Lambert W found Yeo and later XX/XXZ/impurity papers but no matching endpoint theorem.

## value

PASS

The η↑1 point is a natural physical boundary where the useful standard-teleportation temperature window collapses. The exact asymptotic separates two effects that a finite table obscures: inverse-logarithmic temperature collapse and a residual concurrence tending to 1/2. This is a motivated boundary law, not an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
