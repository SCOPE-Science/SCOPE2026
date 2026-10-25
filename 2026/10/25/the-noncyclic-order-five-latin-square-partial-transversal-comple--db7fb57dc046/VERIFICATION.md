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

# Reproduction
Execute `python3 verify.py` with Python 3 standard library. The complete stdout must match `verify_output.txt` and end with `VERIFY_OK`.

# Evidence and boundaries
The verifier enumerates all 56 reduced squares, separating the cyclic (6 reduced) and noncyclic (50 reduced) isotopy classes. For the **new noncyclic claim**, it exhaustively enumerates 507 nonempty faces and 1,406 signed incidences, verifies all 226 matching pairs and acyclicity by a complete gradient topological sort, computes the signed 52-by-4 Morse boundary and its determinant-minus-one four-by-four full-rank minor, and explicitly eliminates all 126 fundamental-group generators using Tietze moves. The resulting 48 sphere summands follow by Hurewicz and Whitehead. The checker also reports the **previously addressed cyclic case** as reference, not as a new finding. Computations are exhaustive for the stated finite order-five domain, not a proof for other orders. No independent audit was performed.
