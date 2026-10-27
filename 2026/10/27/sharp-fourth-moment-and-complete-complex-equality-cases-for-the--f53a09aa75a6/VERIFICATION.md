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

Run `python checker.py` with Python 3 standard library. This reproduces the exact integer Fourier-collision count, a normalized equality witness, and 500 deterministic integer-instance checks of the fourth-moment expansion and inequality.

The analytical proof applies to arbitrary complex coefficients. Exact finite checks do not prove an infinite coefficient statement; the proof uses Parseval for independent torus characters, the matching identity, two-term Cauchy–Schwarz, and complex phase equality. The factorization of equality phases is established algebraically. No external independent audit was performed.
