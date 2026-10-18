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
Run `python3 verify.py` from the extracted package. It uses only the Python standard library and executes exact rational Stirling/moment/dispersion checks over 150 parameter cases and independently approximates total-variation distances for four fixed parameter choices at three sample sizes. The checker was executed after extraction from the generated record. These are finite sanity checks; the proof of the infinite asymptotic limit is in `RESULT.md`. Independent validation has not been performed.
