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

Run `python3 verify.py` using the Python standard library. The successful run prints `VERIFY_OK` and otherwise raises an assertion error.

The script implements exact binary-polynomial finite-field arithmetic and checks:

- all eight smooth \(\mathbb F_2\)-coefficient models against their independently point-counted genus-three \(L\)-polynomials through degree six;
- the complete \(\mathbb F_2\)- and \(\mathbb F_4\)-smoothness counts, the polynomial translation criterion, and all three splitting-type counts for \(q=2,4,8\);
- all four supersingular \(\mathbb F_2\) models by enumerating the four additive roots in \(\mathbb F_{64}\), their Frobenius orbits, their quotient elliptic point counts over the minimal defining subfields, and the resulting \(L\)-polynomial identity.

The finite enumeration validates implementation and small examples only. For all algebraically closed fields and every finite field size, use the derivation of the Cartier action, the additive-kernel quotient, the \(\ell\)-adic character decomposition, and the Frobenius-orbit determinant proof given in `RESULT.md`.

Known limitations: this does not provide a formal proof assistant certificate or an independent scientific audit. The complete geometric moduli theory and split-Jacobian generalities are established prior literature.
