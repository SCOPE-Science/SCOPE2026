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

Both standalone verifiers were run from the actual included sources. `bch273_exact.cpp` reports 36,856 pair keys, 210 oriented matches, 35 weight-five supports through position zero, seven distinct cyclic orbit representatives, and 1,911 shifts. `bch273_independent.py` independently recomputes the same values, lists every canonical representative, and reports the Frobenius permutation. Exact polynomial-field bit operations are used; no floating-point approximation is involved. The proof covers all five-supported codewords of this length only. Independent audit is not performed.
