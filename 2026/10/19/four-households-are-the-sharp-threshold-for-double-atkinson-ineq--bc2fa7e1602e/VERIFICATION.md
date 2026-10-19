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

From the same directory as the accompanying program, run `python3 verify.py`. The script requires only Python 3's standard library and checks the exact rational signatures, product ratio, coefficient sign count, and three-plus-three alternation patterns. It also computes high-precision decimal approximations of the two crossing values. Its decimal output is illustrative, not an infinite-domain proof. The universal three-household claim and the uniqueness of the four-household crossings follow from the generalized Descartes argument and the analytic sign tests in `RESULT.md`; they cannot be established by finite sampling.
