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

Run `python verify.py` using Python 3 with NumPy and SciPy installed. This checks the exact Schur-complement spanning-tree polynomial, the symbolic-rational worked examples, budget constraints and complementary-slackness conditions across 320 reproducibly seeded random price and size choices, independent grounded-Laplacian determinant evaluations in 160 cases, 44 successful unrestricted numerical optimization comparisons, and 2,560 asymmetric feasible-budget comparisons.

The checker reported:

```
PASS exact rational determinant cases=28; random KKT/budget cases=320;
PASS spectral determinant cases=160; unrestricted optimizer comparisons=44;
PASS asymmetric feasible allocation comparisons=2560; all four regimes observed
```

The exact rational proof cases include \((m,P,Q,R,B)=(3,2,1,3/2,92)\), with conductances \((x,y,z)=(4,20,16/3)\), and \((3,1,1,1/2,8)\), with \((8/7,8/7,16/7)\). They confirm the stated exact tree-polynomial values.

The unrestricted optimizer comparisons use numerical constrained optimization on the full \(2m+1\) independent edge variables, not a symmetry-restricted problem. One numerical solver instance did not converge and is not counted among the 44 successful comparisons. No numerical search is claimed to exhaust infinitely many parameter choices. The analytical log-determinant strict-concavity and KKT proof supplies that infinite-domain conclusion.
