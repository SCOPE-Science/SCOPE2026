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

# Verification of first-round graded-modal type spectrum

`verify.py` is a standalone Python 3 standard-library verifier. Run `python3 verify.py` in the extracted artifact directory. The actual completed run returned:

```text
EXHAUSTIVE_OK 9418 binary matrices, literal graded formulas versus profile count
CRITICAL_OCCUPANCY_OK 0.2 integral 0.725624 samples [0.733726, 0.729645, 0.727627]
CRITICAL_OCCUPANCY_OK 0.5 integral 0.769926 samples [0.777549, 0.773695, 0.771801]
CRITICAL_OCCUPANCY_OK 0.8 integral 0.725624 samples [0.733726, 0.729645, 0.727627]
RECTANGULAR_RANDOM_OK 32 draws; eight aspect-exponent groups
VERIFY_OK exhaustive_matrices 9418 critical_PMF_cases 9 random_rectangular_cases 32
```

The exhaustive portion enumerates all binary rectangles with dimensions at most four and cell count at most twelve, and independently evaluates depth-one graded counting formulas and the proposed degree-color signatures. The critical-occupancy portion evaluates exact finite binomial probability mass functions against a deterministic quadrature for the Gaussian limit at three fixed marking densities and three lengths. The random portion samples 32 rectangles covering the exponent regimes on both sides of both critical values, and compares direct observed types against the degree-alphabet product.

Finite exhaustive and numerical checks do **not** certify any infinite-size asymptotic theorem. The proofs of the occupancy limits and uniform degree-pair saturation are analytic and reproduced in `RESULT.md`. Independent mathematical and originality audits have not been performed.
