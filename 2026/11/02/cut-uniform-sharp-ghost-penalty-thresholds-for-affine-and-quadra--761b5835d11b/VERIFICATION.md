---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For the one-dimensional aligned two-cell symmetric Nitsche form with 0<kappa<1, gamma>0, p=1 or 2, varying the common trace reduces nonnegativity to delta>=z^T H^{-1}z in the derivative variables. The p=1 energy matrix gives T1=(1+gamma)/(kappa(1+gamma)+gamma). Independently rebuilt the p=2 4x4 Gram matrix from the integral and face jump and calculated T2=N/Q, matching the supplied positive polynomials. The difference p^2+gamma^{-1}-T_p is strictly positive at each kappa>0, while the kappa->0 limit is p^2+gamma^{-1}; hence uniform nonnegativity iff delta>=p^2+1/gamma, with individual-cut positive definiteness at the uniform boundary. These are exact algebraic arguments for the isolated model; no uniform coercivity constant/full assembled mesh is claimed.

## originality

PASS

Best-knowledge PASS: the relevant Wichrowski aligned two-cell derivation supplies the vanishing-cut necessary threshold and explicitly identifies the positive-cut matching upper bound as open, whereas the present exact inverse-matrix result proves it for p=1,2 and gives fixed-kappa thresholds. Foundational ghost-penalty and immersed-FEM work supplies general coercivity, not these formulas. Primary full-text access to the very relevant Wichrowski paper failed, so priority remains qualified and the exact open-question wording was available only in third-party excerpt / original package citation, not independently confirmed from the entire primary text.

## value

PASS

Sharp stabilization parameters for lowest polynomial degrees are a mathematically and numerically motivated missing CutFEM two-element coercivity boundary; the exact dependence on cut fraction and face penalty answers a specific published matching-bound question, not a mere numerical table. The theorem appropriately does not claim assembled-mesh guarantees.

The dated certificate retains the supplied scientific assessment, sources and limitations.
