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

# Reproduction and boundaries

Extract `verify.py` from the same package and run with Python 3:

```sh
python3 verify.py
```

The script uses the standard library only and reports `PASS: 5100 grouped reproducible assertions`. It performs separate direct complex Fourier moment solves and compares their weights to the rank-one and rank-two Dirichlet-kernel formulas for odd sizes between five and twenty-one, with larger finite grid sizes used for sign and frontier checks. It also checks mass preservation, symmetry, positivity outside the center, numerical threshold crossings, monotonicity samples, and the absolute-weight identity.

Mathematical verification is analytic: (i) the trigonometric Vandermonde is nonsingular for distinct nodes, (ii) exactness on original cardinals determines each updated weight, (iii) trigonometric inequalities show positivity of all noncentral weights, (iv) the central weight is strictly decreasing in displacement, (v) the inverse-sine function is strictly convex on the necessary domain, and (vi) a fixed-displacement expansion yields the stated norm scaling. These steps are fully supplied in `RESULT.md`.

Finite floating-point checks are not an exhaustive or certified proof for all odd orders; they do not establish literature novelty or independent validation.
