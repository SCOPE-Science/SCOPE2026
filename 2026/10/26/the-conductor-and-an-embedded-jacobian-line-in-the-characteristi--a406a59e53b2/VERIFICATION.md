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

The standalone program `check.py` runs in Python 3 with SymPy. Invoke `python check.py` in the directory containing this file.

Observed result: `VERIFY_OK binary_quartic_discriminant_char2; n=0..20 Hilbert checks`.

Checks executed: the integral universal discriminant agrees modulo two with the square of the displayed cubic; every characteristic-two Jacobian generator agrees with its symbolic derivative; the two local normalization coordinate substitutions satisfy the cubic; the Segre parametrization and conductor-ring multiplicative identities hold modulo two; and the displayed Hilbert-function formula is consistent in degrees zero through twenty.

These reproducible finite symbolic checks do not establish the global normalization or the exact conductor on their own. Those are justified by the finite birational incidence morphism, affine normal charts, and the graded module structure proved in `RESULT.md`. The formal assertions have been reviewed for characteristic two; neither independent audit nor external certification has been performed.
