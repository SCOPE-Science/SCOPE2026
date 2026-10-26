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

The exact verifier `verify.py` was run with Python's standard library from its package path. It enumerated every triple intersection of 52 half-integer discontinuity planes and four box-boundary planes within the bounded prism using exact integer determinants, obtaining precisely the candidate knot set `0,1/6,1/4`. It then evaluated the two-dimensional Haar integral by exact rational slicing at six parameter values interior to the two intervals and at each endpoint. Because the signed cell areas are quadratic functions on the knot-free parameter intervals, these checks prove the full real-parameter identity.

The lower-order Walsh independence identities are proved separately from Fourier parity and Haar orthogonality. They do not rely on finite enumeration. The entropy-zero statement is proved by polynomial growth of orbit-covering numbers. The certificate makes no claims about arbitrary fourth-order time patterns, longer blocks, or external independent auditing.
