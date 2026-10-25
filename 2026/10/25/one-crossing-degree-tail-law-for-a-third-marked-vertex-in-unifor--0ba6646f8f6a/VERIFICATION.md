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

Use Python 3.10 or later and run `python3 verify_threepoint_degree_tails.py`. The checker reads no external files and uses the Python standard library. It reconstructs the conditional laws from every Prüfer sequence on three through seven vertices, verifies exact degree-tail differences on all distance levels up to thirty vertices, and checks the explicit coefficient identity and conditional mean ordering. Expected final line: `VERIFY_OK`. These are exact finite confirmations only; the theorem for arbitrary size is established in `RESULT.md` by the weighted Cayley formula and the coefficient single-crossing argument.

Independent audit has not been performed. No external verification channel is represented as completed.
