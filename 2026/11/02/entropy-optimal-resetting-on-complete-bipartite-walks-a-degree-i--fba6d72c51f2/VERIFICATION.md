---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and limits

The unchanged companion `check_entropy.py` is a standard-library finite diagnostic. It compares explicit transition matrices with the entropy formula and checks rates, gains and comparison rates for the fixed opposite part at n=1,2,5,10. Its star and proportional-part diagnostics are contextual, not assertions of the fixed-n≥2 finding. The proof in `RESULT.md` proves the infinite limits by an entropy envelope and global localization; no finite calculation or finite-size optimizer uniqueness is required.
