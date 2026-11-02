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

Run `python3 verify.py` with Python 3 and only the standard library. The script checks all labeled nonempty simple regular graphs on two, four, and six vertices (respectively \(1\), \(7\), \(171\) cases) against direct enumeration of all balanced committees; independently checks bipartiteness; and checks every subset of voters and every admissible committee for seven named representative graphs, including the complete four-vertex and six-vertex graphs. The expected final marker is `VERIFICATION_OK`.

The grand-coalition score and all-voter subsidy formulas are verified with exact integer or half-integer arithmetic. No floating point is used. The general theorem's soundness depends on the proof in `RESULT.md`: the computational run cannot cover arbitrary graph order. The included source file is the whole checker and has no dependencies on private files, external datasets, or network access.

No independent validation has been performed.
