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
# Verification record

The proof in `RESULT.md` is the evidence for all positive exponents; no finite computation establishes infinitely many cases on its own. Reproduce the finite checks with `python3 verify.py`.

The verifier computes integer matrix powers, verifies the explicit matrices at exponents seven and fourteen and their determinant conditions, checks row-valuation strata and the exact sum of pair-incidence counts for exponents one through nine, then enumerates all primitive cycles for exponents one through five and recomputes the first and second moments independently of the lag formula. It reports `VERIFY_OK` only if all assertions hold. The checked outputs were generated from the packaged script before insertion in the ledger.

The original source provides the companion matrix and classical period-lifting context. The independent derivation of the exact second moment is mathematical, and the strongest residual limitation is priority/implication comparison with inaccessible complete general-frequency papers.
