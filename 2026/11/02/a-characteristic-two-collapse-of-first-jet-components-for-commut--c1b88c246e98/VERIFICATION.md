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

# Reproducibility and verification

Execute `python3 checker.py` using a standard Python 3 installation. It uses no third-party modules, data files, solver packages or network services. `checker_output.txt` records a completed run.

The checker constructs ordinary \(2\times2\) matrix products over prime fields and the actual four-element extension field, rather than assuming the theoretical lifting normal form. For each chosen base tuple it creates the homogeneous coefficient equations \(A_iB_i+B_iA_i=0\) and \([A_i,B_j]+[B_i,A_j]=0\) on the \(4m\) first-order entries, and computes their finite-field rank. It exhausts 15 parameter combinations, verifies every nonzero constant-term tuple and exact fiber cardinality, and separately exhausts the complete dual-number matrix space for two small cases.

Expected terminal marker:

`DUAL_JETS_COMMUTING_SQUARE_ZERO_OK 15 RANK_CASES 2 BRUTE_CASES`

These computations verify finite instances only. The proof of the formula over all fields and all arities is the algebraic normal-form and irreducible-stratification argument in `RESULT.md`. No computation constitutes an independent mathematical audit, and the unreduced jet-scheme structure is not asserted.
