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

# Direct checks

The file `verify_picard.py` is a standalone exact symbolic and finite-field checker. Execute `python3 verify_picard.py` with Python 3 and no third-party dependencies.

The checker expands the four-term quartic's fourth power with all symbolic parameters over characteristic five, and extracts the nine monomial coefficients that define the Hasse--Witt matrix. It verifies the two nonzero entries, namely \(1\) and \(3b(a^2+b)\). The universal smooth-fibre conclusion then follows from the exact symbolic matrix calculation, semilinear Frobenius, and the squarefreeness condition.

For independent corroboration, the checker also counts points in examples over \(\mathbb F_5\) and \(\mathbb F_{25}\). Those finite enumerations neither enumerate all algebraically closed parameters nor prove the universal claim by themselves.

The geometric Frobenius, Prym isogeny, and Newton-polygon deductions are proved in `RESULT.md`, not outsourced to the checker. Historic sources concerning general Picard Hasse--Witt formulas were not all available in full text. Independent scientific validation is not performed.
