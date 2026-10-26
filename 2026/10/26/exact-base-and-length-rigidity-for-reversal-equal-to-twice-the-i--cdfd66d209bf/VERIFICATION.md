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
# Verification details

The reproducible `verify.py` uses only Python's standard library. Execute it as `python3 verify.py`. It checks all nonzero-final-digit inputs of lengths two through five in bases four through fourteen (44 complete finite domains), plus 1,980 constructed instances for larger bases and lengths. It trial-divides the four integers 107, 109, 1787, and 1789 to confirm the base-sixteen illustration. The verifier reports `VERIFIED` on success. The bound on exhaustive testing is explicitly finite; the symbolic carry argument in RESULT.md proves the theorem for arbitrary allowed base and length.

A separate independent audit has not been performed. Claims outside the declared base, digit and prime-factorization subcases are not covered.
