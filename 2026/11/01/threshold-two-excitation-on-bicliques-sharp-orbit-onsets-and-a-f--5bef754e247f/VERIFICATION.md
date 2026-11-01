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

# Reproduction

Run `python verify.py` from the directory containing `verify.py` and `certificate.tsv`, using a standard Python 3 interpreter. The checker uses no third-party modules and prints `GHM_THRESHOLD_TWO_BICLIQUE_VERIFY_OK` only if every assertion succeeds. The included `verification_output.txt` is the recorded successful output for this exact package.

The checker recomputes all 676 saturated six-cohort transitions, compares them against the entire tabular certificate, checks the twelve-class first-entry/period histogram, checks the sharp size-threshold matrix for shores 1–6 and the exact stabilization argument in the proof for larger sizes, and verifies the full multinomial census for all 36 size pairs up to 6. It separately evolves 73,449 actual labelled configurations for size pairs 1–4 and 5,5 and compares first-entry time and exact least period with the capped-cohort result.

The all-size mathematical argument requires the exact cohort lumping and six-cohort recurrence specified in `RESULT.md`; a finite list of direct vertex simulations alone cannot prove the claim. No external independent audit or formal machine-checked proof was carried out.
