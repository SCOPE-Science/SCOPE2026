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

# Verification of the integral equivariant formula

Run `python verify.py` with Python 3 and no third-party packages. The program exhaustively constructs simplices using the actual higher-independence definition for test part vectors and permitted values of the parameter. It calculates augmented simplicial boundary ranks modulo two and compares the resulting Betti vectors with the closed integral theorem. It independently computes signed Lefschetz traces from each stabilized simplex and the predicted character from permutation-cycle determinants. It averages traces over the complete within-part groups and the complete wreath groups when all part sizes are equal. Eight configurations, including group orders 384, pass and the program finishes with `HIGHER_INDEPENDENCE_EQUIVARIANT_CHECKS_PASSED`.

This verifies finite cases and character normalizations, not the infinite theorem by enumeration. The written augmentation-kernel and relative-homology argument proves the all-parameter result. Rational quotient acyclicity is weaker than integral acyclicity or contractibility.
