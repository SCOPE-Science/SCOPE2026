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

# Reproducibility and proof limits

Run `python3 graph_preconditional_check.py` after extracting the complete embedded files. It enumerates all graphs on one to four labelled vertices, verifies the original five axioms and all additional claims for each graph and every tuple of subset arguments, and reports `GRAPH_PRECONDITIONAL_OK 266376`. The proof in `RESULT.md` is uniform for all finite nonempty vertex sets. The finite exhaustive checks by themselves do not prove the infinite family.

Scientific overlap review compared the conditional semantics in Chen's arXiv:2607.20221 §§3–4, Holliday's arXiv:2402.02296 Proposition 4, and the relational methods of arXiv:2207.06993 §6, plus the published chain normal form. The unary graph-polarity description is standard in substance; only the stated same-carrier conditional lifting and its strengthening/boundary are assessed as original. Independent audit has not been performed.
