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
# Reproducible checks and limits
Run `python3 verify.py` with Python 3 and the NumPy and SymPy packages. The program builds the adjacency graph from its edges and independently computes average mixing from its real symmetric eigenspaces, checking against the theorem. It also uses SymPy exact arithmetic on six small cases and checks multiplicity/rank predictions; the test output is:

`VERIFY_OK independent_graphs=85 exact_entries=494 resonance_tests=4 worst_matrix_error=1.32e-15 min_distinct_gap=5.957e-03 P5_K2_rank=4/10 P6_K3_rank=9/18`

The exact projector, normalized path sine decomposition, root-of-unity sum and algebraic-integer norm proof are in RESULT.md. Numerical tolerance tests are corroborative only and do not constitute an exhaustive test of all integers. Independent external audit has not been performed.
