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

`python3 verify.py` (standard Python 3) yields `VERIFY_OK: 61 integer equalities; m in 2..4`. The checker separately performs complete labeled-stack enumeration, a maximum-height weighted-skeleton dynamic program, and formal coefficient extraction from the exact generating function. It exhausts all labeled strings for \(m=2\) through \(n=8\), \(m=3\) through \(n=6\), and \(m=4\) through \(n=5\); generating-function and dynamic-program coefficients are compared through \(n=12\) in each case.

For all \(m\ge2\), correctness additionally relies on the proof of the stack-digit correspondence, the first-passage decomposition \(f=pz+qzf^2\), and the pole/square-root singularity analysis. These are analytical arguments, not conclusions inferred from sampled cases. Exact coefficient extraction contains no floating-point computations. Independent validation has not been performed.
