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

The complete proof and definitions are in `RESULT.md`. `checker.py` uses only Python standard-library exact rational arithmetic, with no random input or external downloads. Execute `python checker.py`; the expected output is `TERNARY_HARMONIC_RANK_CHECK_OK 1633`. The checker covers integer dimensions 2 through 10 and degrees 0 through 24, all ternary Fourier supports, and additional closed-form factorial checks. The infinite-parameter conclusion is established by the harmonic monomial construction, Fischer decomposition, and the explicit null-quadric witnesses rather than by checking a finite cutoff.

The equality cases at degrees zero, one, and two are proved by the moment conditions; complete surjectivity starts precisely at degree `max(d,3)`. The literature novelty comparison is bounded, and independent validation remains unperformed.
