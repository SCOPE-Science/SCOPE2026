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

# Verification scope

The proof in `RESULT.md` gives a closed derivation for every dimension \(d\ge3\); no external theorem prover or independent validation is claimed. The root and coefficient formulas are exact mathematical identities. The cap remainder is obtained by a uniform \(O_K(\sqrt\varepsilon)\) control over the transverse-coordinate factors, and disjointness of shortest-coordinate caps below radius \(\sqrt2 a_*\).

## Reproducible computation

Run `python check.py` using Python 3 with standard `math`, `itertools`, `random`, and the installed NumPy and SciPy libraries. A successful extraction and execution of the packaged checker produced:

```
ORTHOTOPE_LOCAL_DISTANCE_OK root_cases=6 quadrature_cases=16 cusp_2d_cases=12 cusp_3d_cases=8 cusp_nd_cases=12 simulations=3
```

The suite verifies exact-to-roundoff recovery on explicit orthotopes of dimensions two to five, independently integrates the two-dimensional difference density numerically on 16 examples, examines the first-break coefficient for 32 dimension/parameter combinations (including repeated shortest sides), and compares simulated independent-point distances in three examples. Checks are finite experiments, not proofs of the general statement. Neither independent mathematical review nor certified interval computation was performed.

## Limits of verification

The closed-form theorem applies to exact population probabilities, dimensions at least three, and axis-orthogonal boxes. It makes no claim about arbitrary convex bodies, finite-sample stability, or the full historical uniqueness of these formulas.
