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

# Verification of the central-section vertex formula

The proof is analytic and covers all integer dimensions at least four and every positive half-width vector. The finite program below supplements but does not prove the universal assertions.

Run `python3 verify.py` with any recent Python 3 standard library. The observed output from the bundled source is:

```
VERIFY_OK
counted_example_means [(3, 4.696, 4.701919), (3, 4.426222, 4.412228), (4, 10.685778, 10.666667), (4, 9.585778, 9.563942), (5, 23.595111, 23.613379), (5, 21.749111, 21.740045)]
transfer_trials 72000
local_Hessian_checks (4, 5, 9)
```

The first number of each pair is an empirical average computed by independently testing all coordinate edges for transversal crossings, not by evaluating the claimed formula. The second is the analytic expectation. The two exact identities used as deterministic anchors are the dimension-two constant of two vertices and the four-dimensional cube mean of \(32/3\). Numerical transfers are sampled only; the strict inequalities follow in the proof from the explicit derivative identity with positive factor \((x-y)(1-x-y)\). The strict lower infimum and its nonattainment are likewise analytic, not a numerical extrapolation.

The evidence does not amount to exhaustive dimension sampling or independent verification. The historical comparison is limited to sources actually read and queried.
