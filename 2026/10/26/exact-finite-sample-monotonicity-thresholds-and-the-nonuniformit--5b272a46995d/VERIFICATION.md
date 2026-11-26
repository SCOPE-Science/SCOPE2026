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

Run `python3 verify.py` with Python 3. It uses exact rational Gaussian elimination to check finite matrices at sample parameters, including the four-point corner value and defect. Optional long-grid calculations require NumPy. The expected terminal marker is `VERIFY_OK`.

The exact sign regions follow from symbolic factorization of the slope-coordinate inverse in `RESULT.md`, not from sampled parameters. The large-length negative slope is given as a comparison and follows from known asymptotic HP filter weights and boundary bounds; a direct residual estimate is included. The source's journal version was not used as full text in this comparison; the corresponding joint-work author exposition in Sakarya's dissertation provides the decisive finite-weight and limit statements. Exact historical overlap of the first finite cutoffs outside the inspected work remains possible.
