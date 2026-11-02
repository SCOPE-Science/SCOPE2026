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

Run `python3 verify.py` with a Python 3 standard-library interpreter. The script computes the exact primitive cyclic-word table at lengths one through nine for every lag residue; its expected table includes only a zero fixed point, four primitive period-four words for each of residues two and three modulo four, and nine primitive period-nine words for each of residues four and six modulo nine. It separately enumerates 21 and 56 positive six-run length compositions and checks the full six-row finite certificate table after grouping the two periodic eight-word cases. The checks compare exact residue equalities, no floating-point arithmetic, statistical inference, timeouts, or external files. The structural argument in RESULT.md reduces all arbitrarily large lag values to these finite checks. This is computationally reproducible self-review and is not independent mathematical auditing.
