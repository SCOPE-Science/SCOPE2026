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

# Verification

The self-contained script `verify.py` performs independent elementary Smith elimination and enumerates all ordered \((E,F)\) for nine small finite-ring/size cases. Each histogram is compared with a separate implementation of the three-valuation distribution. The script prints `PASS` for each enumerated case and raises an assertion on disagreement.

The conceptual general proof does not rely on sample statistics: it is the bordered-matrix equivalence, the two-by-two valuation pivot, and the primitive-vector probability calculation given in `RESULT.md`. Enumeration covers only listed finite rings and sizes, not all finite chain rings. No external validation or independent audit was performed.
