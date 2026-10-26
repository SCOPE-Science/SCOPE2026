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

# Verification steps and boundaries

Run `python3 verify.py` with Python 3 and SymPy. Expected output is archived in `verification_output.txt`.

The checker constructs seven harmonic cubics, verifies linear independence, defines their general seven-parameter real linear combination, forms the associated fully symmetric traceless tensor by third derivatives, and calculates its tensor-contraction matrix. The surface integrals are determined with exact rational even monomial moments. The two moment formulas are then compared as polynomial identities, including all 210 quartic coefficient slots. Direct exact moments of the equality witness \(xyz\) are also checked.

The checker requires finite symbolic algebra only; it verifies identities over all real parameter choices because polynomial coefficient vanishing is exhaustive. The remaining Frobenius-square lower bound is a direct matrix identity, independently readable in `RESULT.md`. No approximate optimization is used. This establishes the stated sharp bound for real cubics only, not complex harmonics, other degrees or an independent literature-priority guarantee.
