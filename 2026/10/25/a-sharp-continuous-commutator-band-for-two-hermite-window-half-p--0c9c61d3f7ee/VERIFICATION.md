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

The proof is analytic and treats the complete Hilbert space. To reproduce finite sanity checks, run `python check.py` with Python 3.10 or newer. It uses no third-party dependencies and prints the recorded 714-pass summary.

Checks performed: independent Simpson quadrature for all four Hermite Gram entries at seven cut locations; direct multiplication of the two compression fibers for 120 distinct threshold/location triples; Gaussian spectral-edge and optimal-separation identities at additional sample points. Finite quadrature cannot prove an exact global supremum, spectral type, or equality classification. Those statements are established by the explicit matrix formula, multiplication-operator spectral theorem, and elementary derivative signs in RESULT.md.
