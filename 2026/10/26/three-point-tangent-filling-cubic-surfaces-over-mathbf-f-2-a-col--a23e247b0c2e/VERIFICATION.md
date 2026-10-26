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

Run `python3 check_normal_forms.py` for the 64 normal forms, 44 rationally regular forms, 576-element stabilizer, two exact coefficient orbits, representative Jacobian rank and final 1,540 count. Run `g++ -O3 -std=c++17 crosscheck_full_scan.cpp -o crosscheck_full_scan && ./crosscheck_full_scan` for an independent exhaustive bit-parity verification across all 1,048,575 cubic forms. Both programs use only ordinary source files in this package; the first requires Python 3 and the second a C++17 compiler.

The first program establishes geometric smoothness through derivative systems that are invertible linear forms in coordinate squares for one representative of each exhaustive group orbit. The second directly checks only rational regularity and tangent-plane coverage; it is not a standalone geometric-smoothness test. Group action and symbolic derivative identities in RESULT.md finish the infinite-field argument.
