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

# Reproducible exact checks
Run the included `extremal_f5.py`, `interpolation_check.py`, and `weil_check.py` with Python 3. The first and third require only the Python standard library; the second requires SymPy. The exact outputs are in correspondingly named `.out` files. The exact smoothness checks use polynomial gcd, never bounded geometric sampling. The full arithmetic action and all 240 smooth candidate forms are exhausted. The F25 checker implements the irreducible relation `v*v+v+2=0` independently of the other finite-field implementation. The characteristic polynomial follows from the point counts and Newton identities; all coefficients are displayed in `RESULT.md`. This verification is finite reproducibility evidence, not independent auditing.
