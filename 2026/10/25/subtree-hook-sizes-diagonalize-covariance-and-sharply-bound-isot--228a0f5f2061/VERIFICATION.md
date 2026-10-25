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
Run `python checker.py` with Python 3 from the same directory as the text files. It uses only the Python standard library and reconstructs first and second coordinate moments exactly from the standard linear-extension triangulation. It tests all increasing-parent rooted trees up to six vertices plus three independent seven-vertex examples, cross-checks the beta-spacing moments, diagonalized covariance and sharp tree bounds.

Observed local output: `VERIFY_OK exact_rooted_trees= 157 rational_equalities= 7602`.

Finite exact tests do not establish a result for all tree sizes; the arbitrary-dimensional proof is given in RESULT.md. Bibliographic uniqueness and independent validation have not been established.
