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

# Verification of the finite-field derivation enumerator

The independent executable `verify.py` builds actual derivation matrices using \(D_f(x^j)=j x^{j-1} f\), then tests their squares by matrix multiplication and calculates ranks by field Gaussian elimination. This is independent of the proof's valuation criterion. It enumerates every coefficient vector in the following configurations: \(q=2\), \(2M\in\{2,4,6,8,10,12\}\); \(q=4\), \(2M\in\{2,4,6\}\); and \(q=8\), \(2M\in\{2,4\}\). For each configuration the direct histogram agrees with the exact formula in `RESULT.md`. The executable checks an additional 237 total-count identities for \(1\le M\le79\) and \(q\in\{2,4,8\}\).

To reproduce: place `verify.py` in the same directory and run `python verify.py` with Python 3. No external packages or network access are needed. The final output is `VERIFY_OK: 11 exhaustive matrix cases and 237 symbolic total-count checks`.

The finite tests are not exhaustive over all dimensions or fields. The general claims are established by the written algebraic proof, including the analytic bound on normalized rank; the script does not constitute an independent mathematical audit.
