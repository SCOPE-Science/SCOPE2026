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

# Reproducibility

Run `python3 verify.py` with a standard Python 3 installation. The program needs no external packages or downloaded data. It reports:

`VERIFY_OK graphs= 84 independent_pairs= 2490828 adjunction_graphs= 11 tree_recursions= 11 path_recurrence_to=15`

`PATH_EXAMPLES [(2, Fraction(23, 25)), (3, Fraction(147, 169)), (4, Fraction(14, 17)), (5, Fraction(6177, 7921))]`

The program builds all upward-closed subsets of every graph incidence frame on at most four graph vertices, plus nine selected five- or six-vertex frames. It independently evaluates the implication condition by principal upsets, compares the resulting counts with a state-weight enumeration, and verifies the direct adjunction characterization on all graph instances through three vertices. It also tests forest message passing and the Fibonacci/cubic path recurrence over a finite range. These tests are finite; the derivation of the formulas for arbitrary graphs and the infinite path asymptotic appear in `RESULT.md`.
