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

Execute `python3 verify_uniform_pairs.py` with standard Python 3. The program enumerates derangements up to 8 labels, computes cycle-partition types of 2-regular complements and explicit incidence matrices, and checks class sizes, connectivity, and the uniform two-atomic-type counting data. It separately enumerates all labeled regular incidence matrices in the small parameter ranges described in RESULT.md. Expected exact text is in `verification_output.txt` and ends in `VERIFICATION_OK`. It is a finite cross-check, not an infinite proof and not independent scientific validation. The infinite claims follow from the proof in RESULT.md.
