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

# Reproducibility and scope

The standalone `verify_lifts_length3.py` directly enumerates all residue-field block-lifts for \((n,q)=(1,2),(2,2),(2,3)\) by powering the corresponding \(3n\)-dimensional matrices over prime fields, and separately exhausts independent pairs \((g,h)\) of companion polynomial coefficients at \((2,5),(3,2),(3,3),(4,2),(5,2)\), plus \(\mathbb F_4\) with \(n=2,3\). Expected frequencies are computed from the theorem, then compared with observed frequencies; discrepancies raise assertions. Replaying with Python's standard library prints `VERIFY_OK` and `VERIFY_GF4_OK`.

In the binary dimension-two lift, the observed frequencies are \(\kappa=2:16\), \(\kappa=3:48\), \(\kappa=4:64\), \(\kappa=6:128\); \(\kappa=5\) is absent. The companion checks cover larger dimensions and characteristic four, but are finite. The proof's cyclic reduction, determinant surjectivity, and valuation arguments are the reasons the formula holds for all \(n\) and finite fields. No independent audit has been performed.
