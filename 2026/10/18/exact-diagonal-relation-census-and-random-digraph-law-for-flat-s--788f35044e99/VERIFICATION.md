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

Run `python3 star_semilattice_checker.py` using Python 3.9 or later; it uses only the Python standard library. The checker was run from its actual standalone file and returned `VERIFY_OK`. It independently tests coordinatewise meet compatibility for every reflexive binary relation on the flat semilattices with one, two, and three atoms. Actual results (all diagonal, symmetric, congruence) were `(4, 2, 2)`, `(25, 5, 4)`, and `(322, 18, 8)` respectively. It compares two independently organized exact arithmetic sums through eleven atoms and prints the asymptotic dominant-term ratios through forty atoms.

These are exhaustive only over the specified small finite semilattices. The enumerator at arbitrary size and the limit law follow from the mathematical derivation in `RESULT.md`, not empirical extrapolation. An independent mathematical audit has not been performed.
