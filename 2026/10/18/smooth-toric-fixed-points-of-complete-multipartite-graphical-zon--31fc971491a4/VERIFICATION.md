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

# Mathematical verification

The all-parameter argument proves the colored-block bijection, Hasse-edge tree criterion, integral tree-root lattice basis, and formal transfer-matrix enumeration; its validity does not depend on finite data.

The standalone `verify.py` requires only Python's standard library. Run `python3 verify.py`. It compares orientation deduplication over all vertex orders with a separate exact labeled-block enumeration for five parameter tuples: \((1,1,1)\), \((1,2,2)\), \((2,2,2)\), \((2,2,3)\), and \((1,2,3)\). The two methods yield identical totals and smooth counts, and the program reports `VERIFY_OK`.

Finite enumeration does not certify the infinite statement or any assertions about positive-dimensional singular strata. No independent external audit has been performed.
