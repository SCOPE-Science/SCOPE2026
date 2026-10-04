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

The verifier `artifacts/verify_rank4_f2.py` uses only the Python standard library. It checks the explicit order-11 witness by exact arithmetic over \(\mathbb F_2\), reconstructs all 120 admissible factor-pair types, builds the compatibility graph, and runs deterministic exact maximum-clique branch-and-bound with greedy proper-color bounds. The recorded output is in `artifacts/verification_output.txt` and ends with exact maximum clique size 11 and witness rank four.

The computation proves only the stated binary rank-four extremal claim. It does not classify all maximum cliques or extend the value to other fields.
