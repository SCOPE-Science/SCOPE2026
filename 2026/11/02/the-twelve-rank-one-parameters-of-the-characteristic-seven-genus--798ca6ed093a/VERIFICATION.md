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

# Exact arithmetic reproduction

Run `python3 verify_symbolic.py` with Python and SymPy, and `python3 verify_fields.py` with Python standard library only. The first checks polynomial coefficient identities, factorization modulo seven, pairwise-intersection closure over the prime field, and the complete rank-zero/rank-one lists. The second uses unrelated polynomial arithmetic in the prime and quadratic extension fields to reconstruct Hasse matrices and three elliptic-quotient invariants and verify the rank histograms \((2,12,6,0)\) over \(\mathbb F_7\) and \((2,12,384,1764)\) over \(\mathbb F_{49}\). Both scripts completed successfully in this review, producing `HOWE_7_SYMBOLIC_OK` and `HOWE_7_FIELD_OK`. The field counts do not prove all-geometric exhaustiveness: this follows instead from the six explicitly split line-restriction polynomials in the proof. No independent external verification is asserted.
