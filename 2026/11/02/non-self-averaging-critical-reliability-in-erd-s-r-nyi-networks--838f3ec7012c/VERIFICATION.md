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

# Reproducibility and verification

Run `python3 verify_critical_reliability.py` with Python 3.9 or newer. It has no third-party dependencies and requires no data downloads. The verification file exercises 226 exact or numerical assertions, comparing two independent finite expressions for mean reliability, the conditional two-thinning second moment, exact isolated-vertex means, and the exponential-integral normalization.

The main proof is analytic. The finite enumerations are not used to claim asymptotic or infinite certification. The critical scientific checks are the marked-isolate factorial-moment argument, the connectivity-without-isolates union bound, the conditional second moment, and the integrated \(L^2\) tail bound in RESULT.md. These were separately reconstructed by direct mathematical inspection. No independent audit has been performed.
