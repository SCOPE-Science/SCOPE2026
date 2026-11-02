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

# Reproducibility

Run `python3 verify_band_cross_sections.py` with Python 3 (standard library only). It reports `VERIFY_OK` after checking the explicit root-wise constructions and their full multiplication tables through \(n=5\), independently brute-enumerating all band choices through \(n=4\), and checking the local non-idempotence witness at every root for \(6\le n\le15\).

The checker represents points by zero-based labels and composes maps in right-action order. Its complete finite search does not certify the theorem for arbitrary \(n\); that assertion uses the proof in `RESULT.md`. The journal full text of the related 2025 work was not independently inspected. No independent mathematical audit has been performed.
