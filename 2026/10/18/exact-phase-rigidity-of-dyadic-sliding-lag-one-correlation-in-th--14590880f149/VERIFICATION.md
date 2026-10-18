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

The standalone `verify_phase.py` requires Python 3 only; run `python verify_phase.py`. The script has independent digit-pattern and recurrence definitions of the binary Rudin–Shapiro sequence, then computes each relevant sum directly and by its claimed phase expression. It tests 1,175,569 sliding windows across selected dyadic lengths; exact three-value frequency histograms at twelve scales; and eighty large arbitrary starting indices (including indices much larger than the generated prefixes). Successful output:

`VERIFY_OK independent_generators=131074 sliding_windows=1175569 dyadic_histograms_m2_to13=12 large_offset_checks=80`

The theorem is independently justified by the exact parity recurrence and two finite-sum transfer identities in `RESULT.md`; test coverage is finite corroboration, not a claim of exhaustive computational verification for infinitely many indices. The scientific literature comparison is not an independent audit or priority guarantee.
