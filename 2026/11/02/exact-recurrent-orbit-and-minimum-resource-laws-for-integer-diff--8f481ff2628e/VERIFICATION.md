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

The exact claims are reproduced using `python3 verify_bistar.py` in Python 3 with the standard library. The checker computes synchronous edge transfers from the original state, not from the proposed phase formulas; enumerates all normalized candidates inside degree-implied necessary bounds; and tests the two-step return and non-fixed condition. It compares complete canonical-state dictionaries and minimum nonnegative conserved totals against the independently implemented constructive parameter enumeration. It checks eight labelled bistars and 9,044 primitive two-cycles, including conserved-sum residue vectors, without relying on random samples. The saved `verify_bistar_output.txt` records the passing run.

Finite exhaustive cases support the algebraic derivation but cannot prove the infinite-parametric statement. The written proof derives the all-parameter leaf synchronization and strict/tied bridge split. No independent mathematical audit or machine-formal proof has been performed. The cited literature comparison is limited to the stated material and indexed searches.
