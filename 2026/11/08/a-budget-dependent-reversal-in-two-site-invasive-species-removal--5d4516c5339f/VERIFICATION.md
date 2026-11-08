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

# Reproducibility and limits

Run `python3 verify.py` in the extracted directory using Python 3. The script uses only the standard library, deterministic pseudo-random test parameters and a second numerical integration route. It checks the exact integer witness inequalities, cap optima on sample grids, derivative comparisons, and two-term large-deadline asymptotic predictions. The analytical proof in `RESULT.md` is necessary for the statements quantified over every positive deadline, both site rates and occupancy probabilities. No formal proof assistant, external certificate, independent reviewer or ecological-data validation is claimed. Full-text access to one relevant 2009 paper remained unavailable, as noted under limitations.
