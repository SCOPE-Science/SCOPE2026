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

# Exact reproducibility

Run `python3 verify.py` with Python 3 standard library. The script builds the eight states, determines every admissible arc directly from the four-bit inequality, discovers all directed simple cycles, and computes the determinant from disjoint cycle families. It enumerates 131064 binary assignments for labelled cycles of lengths 3 through 16 and checks all coefficients against a *separately implemented* transfer trace. It checks the matrix trace polynomial recurrence against explicit transfers through order 36 and exact coefficient symmetry and smallest-weight counts for all even lengths through order 84.

Expected output:

`VERIFY_OK determinant_cycles=3 independent_assignments=131064 n=3..16 transfer_n=1..36 recurrence_n=9..84 extremes_even_n=4..84`

The finite checks are exact corroboration. They do not themselves establish the infinitely many orders. The transfer bijection, determinant cycle expansion, and cyclic-gap extremal classification supply the general proof. No external certification or independent audit is claimed.
