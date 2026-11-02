---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and scientific scope

Run `python3 verify_b3.py` with Python 3 and SymPy installed. The exact program checks reduction modulo three, the three cube-gradient identities, vanishing at the marked and Frobenius points, the strange tangent relation, the complete translated local polynomial, the nine-point evaluation rank, the six-jet determinant and nonzero minor, and an explicit finite-field parameter witness. The expected success line is `B3_CHAR3_FROBENIUS_GRADIENT_LENGTH9_UNIQUE_JET_AND_WILD_CUSP_OPEN_PASS`.

The general proof additionally uses a saturated complete intersection of cubed linear forms, a coprime Newton edge for a plane branch, projection from a triple point, the genus formula, and the degree-three inseparability of projection from the smooth strange point. The exact symbolic identities support but cannot replace those infinite-field geometric arguments. Historical priority and geometric assertions have not been independently audited.
