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

# Reproduction instructions and scope

Run `python3 verify.py` with Python 3.9+ and the standard library, in the same folder as this document. Its output must match `verification_output.txt` exactly. The code (1) enumerates the original private-neighbor definition over all 25 trees with the two arm parameters from 0 through 4, (2) proves the uniform-in-direct-leaf log-concavity inequalities using exact symbolic quadratic coefficients for all 0–43 length-two arm counts, (3) verifies the separate zero-direct-leaf case, and (4) evaluates the exact three-coefficient counterexample at 44 length-two arms. No outside input or third-party package is needed.

The infinite parameter statement uses an algebraic argument: the certificate checks every integer second-arm count in a finite stated interval **with all** direct-leaf counts simultaneously. Small-graph enumeration is a cross-check only. This is not an independent audit or external certification. The 2024 polynomial chapter was not accessible in full, so bibliographic overlap remains a residual risk.
