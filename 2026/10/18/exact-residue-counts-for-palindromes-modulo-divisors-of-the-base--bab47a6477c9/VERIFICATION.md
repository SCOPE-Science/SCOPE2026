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

# Reproducibility and proof limits

Run `python verify.py` with a standard Python installation. Its independent enumeration of canonical digit palindromes checks all bases from 2 to 14, every modulus greater than one dividing base plus one, and lengths one through seven. It uses rational rather than floating-point comparisons for formula integrality, residue-class sizes, the total count, and the strict discrepancy bound.

The proof of the infinite family is algebraic: evaluate the finite Fourier transform in three disjoint character cases and invert it. The code exercises examples and boundary cases, not all parameters. No external or independent audit is represented.
