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

# Verification
Run `python3 verify_osome.py` with Python 3 (standard library only). The program separately computes the overpartition marked-part statistic and the theta generating-function identity through index 420, evaluates all-index divisor-character residues, independently enumerates two binary quadratic norm representations on odd indices, and checks the squarefree prime corollary. See `verify_output.txt` for the actual captured replay. These checks are finite and do not establish the infinite claims; the all-index proof is provided in `RESULT.md`.
