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

# Reproducibility and limitations
The attached `verify.py` is a standalone Python 3 script using the standard library only. In the directory containing the file, run `python3 verify.py` (no downloads or external files). It prints `VERIFY_OK coefficient_profiles= 850 direct_determinants= 29250 exact_tuned= 15` when all assertions pass.

The program derives the determinant as a six-term permutation expansion, independently of the claimed three Laurent coefficients. It tests 450 general asymmetric/symmetric parameter configurations at 13 Bloch phases each, 200 analytically tuned cases with unequal side potentials at 13 phases each, and 200 balanced-product cases at 13 phases for each of three caging energies plus 13 phases for each of five flux choices in the protected flat band. It also verifies 15 parameter identities with exact rational arithmetic. The pseudorandom seed is fixed for reproducibility.

These checks are finite corroboration only. The infinite-chain claims rely on the exact Laurent identity, exhaustive case distinction and explicit polynomial eigenvectors in `RESULT.md`; no exhaustive computer census or independent certification is asserted. The code uses floating-point tolerances solely in sampled complex determinant evaluations; exact rational identities are separate.
