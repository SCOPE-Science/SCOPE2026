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

Execute `python3 verify.py` from the directory containing the embedded files. The checker uses only Python standard-library integer arithmetic, tests each Hilbert polynomial from n=4 through n=12, and matches published Table 3 for n=4 through n=7. A successful execution prints `VERIFY_OK`. The all-n claim follows from the explicit Segre-cone local proof and Hurwitz factorization, not from finite tests. No independent mathematical audit has been performed.
