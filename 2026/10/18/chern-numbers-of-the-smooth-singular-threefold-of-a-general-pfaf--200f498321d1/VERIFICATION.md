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

# Reproducible numerical verification

Run `python3 verify.py` using only the Python standard library. Its `cnumber_integrals(10,2)` and `cnumber_integrals(10,3)` independently evaluate the same complete localization formula for distinct integer weight assignments, checking all \(3150\) projective-bundle torus fixed points with exact rational arithmetic and verifying all tangent denominators are nonzero.

Expected output:

`VERIFY_OK n10_fixed_points=3150 degree=330 c1H2=-1650 c2H=7920 c3=-31350 K3=41250 chiO=-1650`

For a geometric cross-check, the program also computes the size-eight case on \(\operatorname{Gr}(4,8)\) at two weight choices: it returns \(\int H=84\), \(\int c_1(T)=-336\), and thus genus \(169\). The general rank-stratification, Bertini, adjunction, and fixed-point localization theorems are mathematical arguments, not consequences of a program run. The script does not compute full Hodge numbers, singularities for nongeneral forms, or a universal family beyond the explicitly stated general locus.
