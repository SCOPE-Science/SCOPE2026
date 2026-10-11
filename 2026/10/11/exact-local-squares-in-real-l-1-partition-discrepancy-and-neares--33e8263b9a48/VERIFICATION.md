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

Run `python3 verify.py` using only the Python standard library. Expected deterministic exact-rational output:

```
VERIFY_OK profiles=575 arbitrary_signed_pairs=80722 exact_optimal_sign_witnesses=575 nearest_square_witnesses=575 dimensions=2..5 arithmetic=exact
```

The checker exhausts its declared finite sets of rational nonnegative profiles and sign-valued test partners in dimensions two through five, then verifies the exact sign-optimum and closest-square constructions. The test is **not** exhaustive over arbitrary rational \(L_1\) functions or measurable spaces. The analytic proof in `RESULT.md` is required for the general result.

Optional separate optimizer: `python3 stress_lp.py` (requires `numpy` and `scipy`). It solves all sign-orthant linear programs on 50 seeded rational profiles in dimensions two through six, and reports the maximum discrepancy with the sign-partition value below \(10^{-7}\). Its floating-point optimization is corroboration only; it does not certify all infinite-dimensional instances.

The pointwise algebra can be checked independently from the identities
\[
|a+b|+|a-b|=2\max(|a|,|b|),\qquad
|a+b|-|a-b|=2\operatorname{sgn}(ab)\min(|a|,|b|)
\]
for real scalars, with an arbitrary sign at zero. The equal-mass atomic formula uses countable compactness and divisibility of finite atomless measures. The nearest-square construction requires \(\dim L_1\ge2\).

Independent audit: not performed.
