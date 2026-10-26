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

The bundled `verify.py` was executed successfully with Python 3 and SymPy. It checked eight symbolic identities, including all rational reductions, the derivative factorization, the critical-value resultant and endpoint values. Four high-precision critical-value assertions and the explicit optimizer equality were confirmed numerically, and 2,500 seeded complex triples satisfied the claimed inequality in finite checks.

The analytical argument is in `RESULT.md`: the global maximum is justified by a unique-in-parameter rational optimization, exact derivative signs and boundary exhaustion, rather than finite enumeration. Numeric approximations are display aids only. The general-degree and alternate-weight cases remain unproved. Historical originality cannot be certified by failed searches; the closest sources, implication comparisons, material read and remaining risks are given in `AUDIT.json` and `REVIEW.md`.
