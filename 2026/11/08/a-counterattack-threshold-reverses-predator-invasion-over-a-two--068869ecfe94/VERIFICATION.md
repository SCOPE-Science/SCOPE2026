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

# Verification and reproducibility

The included standalone `verify.py` uses Python's `fractions.Fraction` to compute exactly in \(\mathbb Q(\sqrt{21})\). Run `python3 verify.py`. Its expected final line is:

`VERIFY_OK: exact two-cycle, multiplier, Floquet determinants, counterattack crossover, two opposite invasion witnesses`

It directly checks the two prey-cycle substitutions, symmetric polynomials and multiplier; explicit multiplication of the positive predator matrices; equality of their determinant with the displayed rational polynomial; the exact factorization along the static threshold for three exact parameter values; and both rational strict reversal witnesses.

The analytical proof separately establishes the factorization for all real parameters in the stated interval, the comparison between the determinant sign and the spectral radius under strict positivity and \(P_{22}<1\), and the hyperbolic local stability consequences. The executable checks are finite identities, not a substitute for these quantified deductions. At \(A=2/35\), only a neutral *linear* transverse multiplier is established. No independent external audit or validation is asserted.
