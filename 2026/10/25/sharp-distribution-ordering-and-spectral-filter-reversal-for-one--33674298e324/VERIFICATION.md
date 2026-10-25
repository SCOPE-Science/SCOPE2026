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

# Verification and scope

The mathematical certificate is the exact pairwise transposition identity, the boundedness of its integrands, and the weighted covariance reduction in `RESULT.md`. The strict extremal statements follow from termwise signs, while the power-iteration bound follows from log-convexity of spectral power sums and an exact pairwise expansion.

Run `python3 verify.py` with Python 3. The standalone test program passed 6,969 deterministic rational checks of symmetrized gap formulas, direct/inverse monotonicity, spectral-power formulas and the factor-two approximation bound, plus planar algebra. The tests are finite and do not substitute for the provided proofs. No external certificate, independent audit, or unrestricted general-matrix guarantee is asserted.
