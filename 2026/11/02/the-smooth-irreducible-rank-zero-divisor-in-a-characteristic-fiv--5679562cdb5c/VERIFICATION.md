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

The accompanying `verify.py` is a symbolic computation over \(\mathbb F_5\). It checks the two coefficients in \(f^3\), the Cartier Hasse cycle polynomial, the exact Gröbner basis for singularities, boundary exclusion, polynomial-root contradictions, and a nonempty smooth-parameter example. Reproduce with `python verify.py` and SymPy (tested with installed 1.14). The generic-field pole argument at infinity, the Cartier-to-rank inference, and absence of complete Newton classification are explicit in RESULT.md. This is a reproducibility artifact and self-review, not independent validation.
