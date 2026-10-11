---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

At the interior equilibrium the Jacobian has zero diagonal and off-diagonal entries \(A_Ax^*(1-x^*)\) and \(A_By^*(1-y^*)\); hence its determinant is the negative product of those entries. The sign classification therefore reverses Proposition 7.1. The source payoff definitions give \(A_I=S_I+\operatorname{exp}^I(0)+\operatorname{exc}^I(0)\ge0\); existence of an interior equilibrium requires the relevant \(A_I\ne0\), so both are strictly positive. The source first integral remains valid but supports the center only when the corrected product sign is negative. The source itself later describes the coordination mixed equilibrium as a saddle, which is consistent with the corrected determinant and inconsistent with its Proposition 7.1.

## originality

PASS

The primary 2026 paper was inspected in the relevant payoff, replicator, Jacobian, Proposition 7.1, strategic-regime, and first-integral passages. It prints the determinant with the wrong sign and assigns center/saddle accordingly, while a later coordination paragraph says saddle. A targeted published-SCOPE search located no earlier correction of this tariff paper. Generic two-population replicator theory explains the sign rule but does not make this source-specific correction, its coefficient-positivity consequence, or the reconciliation of the paper’s contradictory passages redundant.

## value

PASS

The correction changes the local phase portrait of the only interior tariff equilibrium from the paper’s advertised cycling regime to instability and resolves an internal contradiction with its coordination discussion. Although the determinant calculation is elementary, the consequence is substantive for the paper’s central dynamic interpretation, so this is a motivated mathematical correction rather than a cheap sign check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
