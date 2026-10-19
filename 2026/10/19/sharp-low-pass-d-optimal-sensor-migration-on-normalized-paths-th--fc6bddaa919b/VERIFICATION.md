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

Run `python verify_path_sampling.py` with Python 3 and its standard library. The checker evaluates the maximizer lists for all admissible band sizes and path orders through \(N=200\), checks direct normalized-heat observation determinants against the spectral Vandermonde factorization on small paths, and compares exact stationary identities for the polynomial \(p(z)=z(2z-1)(4z-3)\). The universal \(N\)-quantified assertions follow from the proof's analytic monotonicity and finite threshold argument, not from the bounded computations.

Critical proof identities are the weighted discrete cosine eigenbasis, the determinant decomposition, the band-dependent cosine products, the two stationary points \((5\pm\sqrt7)/12\), the strict inequality \((10+7\sqrt7)/108<21/64\), and the six small-path rows. This document records self-review only. No independent audit has been performed.
