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

Execute `python verify_pappus_ind2.py` with Python 3.10 or newer. Only the standard library is required. The exact script reconstructs a hardcoded 27-edge Pappus graph independently from the standard eighteen-cycle LCF chord notation, exhaustively tests all 262,144 vertex subsets, computes a complete matching over 20,652 augmented simplices, checks acyclicity over 120,240 directed Hasse incidences and computes the signed integer Morse boundary of its one critical six-cell against its nine five-cells. It then independently computes binary boundary-matrix ranks on the complete original complex. The actual output is `VERIFICATION_OUTPUT.txt` and begins with `PAPPUS_TWO_INDEPENDENCE_MIXED_WEDGE_OK`.

This is an exhaustive finite proof for the named graph, not an extrapolation from experiments. The zero integer differential, not merely the mod-two ranks, is needed to show the six-cell attaching map is nullhomotopic; that implication uses standard Hurewicz theory in the five-sphere wedge. No external audit has been performed.
