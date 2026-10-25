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
The attached executable `check_gaussian.py` was run directly from its packaged source. `checks.txt` records its output. The independent numerical integration uses the exact saddle eigenvector and decreasing positive \(\mu\), at scaled heights \(U=\pm0.14\) and \(U=\pm0.28\). Errors of the two-term logarithmic approximation, divided by \(\mu\), remain bounded in the tested range. Symbolic identities check the limiting graph and the linear-in-\(\sqrt\mu\) coefficient exactly.

The theorem for every sufficiently small \(\mu\) and every fixed compact scaled-height interval uses the proof's smooth parameter-dependent strong-stable foliation; finite tests do not certify the infinite quantifiers. Ordinary SciPy, NumPy, and SymPy are needed only to replay the supplemental checker, not the proof. No independent audit has been performed.
