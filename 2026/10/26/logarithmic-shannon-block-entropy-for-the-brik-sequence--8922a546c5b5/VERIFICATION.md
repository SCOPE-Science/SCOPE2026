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

# Reproducibility and scope
The mathematical proof is in `RESULT.md`. Run `python check_entropy.py` in the directory containing the packaged files. The expected finite-stage output is preserved in `check_output.txt`. It tests exact recursive word construction, embeddings of later stages into periodic repetitions of an earlier stage, source-window deletion accounting, and inequalities for an explicit scale choice. The finite word experiment runs through stage 15 and checks 3,430 finite conditions. These finite tests cannot establish convergence of factor frequencies or the bound for arbitrarily large block lengths; those claims rely on the analytic proof.

No independent audit or external mathematical validation was carried out. The proof is a self-review and the literature comparisons carry the stated priority risks.
