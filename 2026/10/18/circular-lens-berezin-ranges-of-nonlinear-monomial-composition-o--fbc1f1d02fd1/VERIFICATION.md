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

Run `python3 check_lens.py` beside this file. The script computes finite samples of normalized-kernel Berezin transforms and confirms the two intersecting-circle inequalities, reconstructs points in the predicted inverse sector, and independently quadratures the lens area. The checker is deterministic and requires only Python standard library.

The actual standalone script was run successfully from the packaged path. No numerical experiment proves the exact infinite family; the proof is the explicit algebraic surjectivity argument and elementary disk geometry in RESULT.md. Inaccessible closely related full-text sources leave a publication-priority risk.
