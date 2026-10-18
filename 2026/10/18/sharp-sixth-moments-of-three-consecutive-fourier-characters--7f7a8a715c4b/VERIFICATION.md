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

# Reproducible verification

Run `python3 verify.py` with standard Python 3. The checker constructs the cube coefficients in the polynomial ring \(\mathbb Z[A,B,C]\) using its own sparse-dictionary arithmetic, rather than relying on numerical fitting. It verifies the exact five identities for the sixfold norm at character orders \(3\), \(4\), \(5\), \(6\), and \(\ge7\); the five displayed one-variable numerators; and the factored derivative numerators as integer-polynomial equalities. It also checks rational sign brackets for the fifth-order quintic and uses finite-character evaluations solely as illustrations.

The proof of strict symmetrization and global root uniqueness is given in RESULT.md and is not delegated to this finite checker. The material does not certify independent validation, absence of undiscovered prior results, or broader class coverage.
