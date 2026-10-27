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
# Reproducible checks

Run `python verify.py > certificate.json` with Python 3 standard library. The code enumerates every latent binary triple and observed binary triple in its selected rational parameter models, computes exact means, covariances, and inversion, and compares the concrete limiting examples. Three valid memory/detection parameter examples include \(\lambda=-1/4\). It checks complete two-season cell probabilities, the complete three-season zero-memory joint distribution and equal pairwise moments but unequal joint three-way event under false positives. The embedded `certificate.json` is the byte-for-byte deterministic expected output; all fractions are exact.

The proof of the general three-season statement is algebraic and is presented in RESULT.md. Enumeration does not establish universal statements by sampling. The false-positive example only establishes ambiguity given first and second moments, not given the complete triple joint law. This verification is not an independent scientific audit.
