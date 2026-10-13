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

# Reproducible finite checks

Run `python3 artifacts/verify.py` with Python 3 (standard library only).

Observed output:
```
VERIFY_OK
formula_checks 108800 nonvalid_projections 36841 maximum_selected_atoms 3
all_BALFIs_q1 6 all_BALFIs_q2 1296 random_BALFIs_q3 1000 sharp_trace_r_2_to_9 True
```

The script enumerates every admissible pair of unary operators on Boolean algebras having one and two atoms, every two-variable valuation, and five nested formulas. For non-top formula values it constructs the projected operation tables, checks every BALFI equation on the smaller algebra, compares all subformula values, and separately checks the corresponding atom-vector certificate. One thousand seeded random operator tables on a three-atom Boolean algebra further stress nested behavior. Exhaustive coordinate-deletion checks for the top-and-coatoms sharpness trace range from two to nine trace elements.

The infinite-quantified claim is **not** verified solely by testing. Its general proof uses local finiteness of finitely generated Boolean algebras, greedy refinement of finite trace partitions, and a structural induction. The checker does not test all arbitrary infinite Boolean algebras, extensions of RmbC, or minimum formula countermodel cardinalities.
