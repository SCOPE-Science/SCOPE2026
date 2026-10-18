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
Run `python3 verify.py` with Python 3 and the standard library. The verifier exhaustively tests all \(3^9=19{,}683\) binary tables on the three-element chain, classifies exactly the semi-Heyting operations, and independently checks the generated row normal forms and all axioms for the 10,400 operations on the five-element chain. It verifies the row cardinalities, finite total counts, reduct fibers and extremal fibers for small sizes. Its expected last line is `VERIFY_OK independent_full_axioms_n_le_3 19683_candidate_tables_n3 generated_axioms_n_le_5 10400_algebras_n5`.

The probabilistic limits are established by the proof in `RESULT.md`: finite enumeration is corroborative only. No independent mathematical or originality audit was performed.
