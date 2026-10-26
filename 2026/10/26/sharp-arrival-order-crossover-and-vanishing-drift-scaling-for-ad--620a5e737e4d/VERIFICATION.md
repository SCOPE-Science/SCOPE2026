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

The first-passage density, CDF, likelihood-ratio sign pattern, and scaled survival limit are derived analytically in `RESULT.md` under the specified positive-parameter hypotheses. `check_first_passage.py` uses only Python 3 standard-library functions and repeats 300 finite-difference CDF derivative checks, 300 density-ratio identities, four positive-drift scaling comparisons, and two explicit arrival-order reversal examples. Execute `python check_first_passage.py` from a directory containing that file. The checks passed in the packaged form. Floating-point experiments do not prove uniqueness, absence of additional roots, or any all-parameter statement; these are justified by the ratio and derivative arguments. External independent audit has not been performed.
