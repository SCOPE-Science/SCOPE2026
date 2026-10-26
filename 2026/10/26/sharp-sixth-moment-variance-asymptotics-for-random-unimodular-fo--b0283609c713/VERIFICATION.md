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

# Verification record
The exact checker in `check_variance.py` reconstructs Fourier-character multiplicities by grouping triples of indices with equal sum, in exact integer arithmetic. Sizes 4 through 16 were checked for the two generic multiplicity classes. Analytically, the cubic-order pair-sum count is \(2n^3/3+O(n^2)\); the fifth-order triple-sum count follows from a piecewise quadratic convolution whose squared integral is \(11/20\). These establish the stated two sharp variance contributions; finite enumeration alone is not a proof for arbitrary size.

No independent audit or validation has been performed.
