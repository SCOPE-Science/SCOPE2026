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

# Exact verification

Execute `python3 verify_euler.py` alongside these files. The program is self-contained and uses only the Python 3 standard library; it makes no network requests. The locally executed program returned `EXACT_VERIFICATION_OK: companion Smith divisors n=3..128, Hessian identity n=3..40`.

The checker verifies the exact minors of \(C^n-I\) for each \(3\leq n\leq128\) and independent integer quadratic/polar identities for \(3\leq n\leq40\). It does not purport to verify infinitely many instances computationally, the published source's global theorem, or literature priority. Those require the explicit proof and scientific comparison recorded in `RESULT.md` and `REVIEW.md`.
