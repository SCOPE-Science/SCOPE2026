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

# Computational checks and limits

Run `python3 verify_hyperbola.py` using a standard Python 3 installation; no third-party libraries are needed. The checker constructs the finite fields of orders 3, 5, 7, 9, and 11, with the order-nine field represented as \(\mathbb F_3[T]/(T^2+1)\), and uses the field trace for additive characters.

It verifies the nonzero sum-fiber uniqueness and the size of the zero fiber; checks 225 deterministic complex-integer coefficient instances against the exact fourth-moment/deficit identity; and independently sums 12,825 Fourier-frequency fourth powers. Five constant-modulus, phase-twisted extremizers are also tested. The executed output was:

`VERIFY_OK finite_fields=5 random_cases=225 direct_Fourier_character_sums=12825 extremizer_checks=5`

All arithmetic in the collision and energy construction is exact in the finite fields and Gaussian-integer input coefficients; direct complex exponentials and deficit comparisons use floating-point tolerance. The unrestricted theorem is justified separately by the algebraic proof in `RESULT.md`. No independent external proof review or validation has been performed.
