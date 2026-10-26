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

Run `python VERIFY.py` after installing NumPy as listed in `requirements.txt`. The program enumerates dimensions from two through thirty and all nonzero row offsets, checking the Gram least-singular-value identity for 8,990 deterministic nonzero test vectors, all predicted cyclic zero eigenvalue counts and the Fourier eigenvalue product. The result was `VERIFY_OK spectral zero counts, pseudodeterminant product, Gram identity and coefficient; 8990 vectors`.

The asymptotic probability law is derived analytically from the Gaussian small-ellipsoid expansion and inclusion–exclusion; a finite matrix enumeration cannot certify an asymptotic theorem. Independent scientific audit has not been performed. All calculations use the real, unnormalized model in RESULT.md; no random seed is needed for the deterministic checks.
