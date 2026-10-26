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

# Verification
The accompanying standalone `verify_joint.py` computes the closed formula by exact Gaussian-binomial arithmetic, and independently enumerates all \(q^{sr^2}\) structure tensors for \((q,r,s)=(2,1,1),(2,2,1),(2,2,2),(2,3,1),(2,3,2),(3,2,1),(3,2,2)\). For each map it determines onto rank, central radical rank, and joint left/right radical rank. All predicted coefficients match the exhaustive distributions, including the \(260610\) surjective maps for \((q,r,s)=(2,3,2)\). The independent code check is limited to prime fields; the written proof handles prime powers and arbitrary dimensions. No external independent audit was performed.
