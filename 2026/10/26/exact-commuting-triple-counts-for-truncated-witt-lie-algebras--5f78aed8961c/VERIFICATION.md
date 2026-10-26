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

# Verification record

`python3 verify.py` completed with the final line `VERIFY_OK_WITT_COMMUTING_TRIPLES`.

- Exhaustive adjoint-rank checks: \(27\) elements of \(W(\mathbb F_3)\), \(729\) elements of \(W(\mathbb F_9)\), and \(3125\) elements of \(W(\mathbb F_5)\).
- Direct commuting triple enumeration over \(\mathbb F_3\), not using the centralizer formula in the counting loop.
- Direct commuting-pair enumeration for the nonabelian high-order subalgebra over \(\mathbb F_5\).
- Deterministic samples of \(160\) vectors over \(\mathbb F_7\) and \(120\) vectors over \(\mathbb F_{25}\); exact extension-field arithmetic uses irreducible quadratic polynomials.
- Independent verification of the displayed pair count from the exhaustive rank histogram in the listed small fields.

Only the finite configurations above were computed. The all-odd-characteristic result depends on the proof, not an extrapolation from these experiments. This record is not an independent audit.
