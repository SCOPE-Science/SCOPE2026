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

Reproduce the finite tests with `python3 verify.py` (Python 3 standard library). Expected: `VERIFY_OK n_levels=7 candidate_instances=56`. The script independently enumerates Apéry minima and all pseudo-Frobenius residues for seven small parameter values, while `RESULT.md` supplies the all-parameter proof. Finite checks cannot certify originality or independently audit the theorem.
