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

The standalone `verify.py` implements synchronous Rule 90 directly and then exchanges its first two outputs. It computes matrix powers and ranks by binary Gaussian elimination, checks the exact stabilization point and kernel sizes, and independently enumerates every initial binary state for ring lengths 4, 6, 8, 10, 12 and 16. Further sampled dimensions through 128 include non-dyadic even rings. The local test run terminated with `VERIFY_OK`.

These are finite reproducibility tests only. They are not exhaustive across infinitely many even dimensions and do not independently validate originality. The proof in `RESULT.md` is the support for the universal quantified statement. The 2025 predecessor's full manuscript could not be examined, so historical priority remains provisional.
