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

# Verification of the exact even-helm zero-forcing census

Both embedded programs were run on the same even-helm convention described in RESULT.md. `check_python.py` independently implements graph closure from neighborhood bitmasks and a cyclic-defect parser. `check_cpp.cpp` is a separate C++17 implementation of the same two mathematical tests, with different subset enumeration and graph construction. Both confirmed all size-\(k\) pendant candidates and the formula for rim orders 6 through 20 in increments of two. The Python implementation also exhaustively excludes smaller zero forcing sets for orders 6, 8, and 10. A successful finite check is not an infinite proof; the written forcing-chain, component and defect-count arguments establish the general theorem.

No independent external audit was performed.
