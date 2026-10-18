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

# Verification of the fifth-power graph pair-sum census

Run `python3 verify_quintic.py` with Python 3 and no third-party packages. The program directly constructs \(\mathbb F_p\) for prime orders \(7,11,13,17,19,23,29,31,37\), as well as \(\mathbb F_{49}=\mathbb F_7[\alpha]/(\alpha^2-3)\) and \(\mathbb F_{121}=\mathbb F_{11}[\alpha]/(\alpha^2-2)\). Both quadratic moduli are nonsquares in their prime fields.

For all 11 fields, the checker enumerates every ordered pair on the fifth-power graph, computes every two-dimensional sum and its exact integer multiplicity, and verifies all five multiplicity-frequency formulas on every row with nonzero first coordinate. It also checks the exceptional zero row, exact energy, and the equality of the two energy expressions. For prime orders \(7,11,13\), it additionally evaluates the complete normalized complex character sum and confirms the fourth-moment normalization.

Observed completion: `VERIFY_OK fields=11 nonzero_rows=346 ordered_pairs=21731 all_histograms=PASS all_energies=PASS extension_fields=2`.

The exhaustive statements above refer only to the listed finite fields. The unrestricted theorem for all prime powers in characteristic greater than five follows from the self-contained discriminant and quadratic-character proof in `RESULT.md`, not from extrapolation of these tests. Independent mathematical audit has not been performed.
