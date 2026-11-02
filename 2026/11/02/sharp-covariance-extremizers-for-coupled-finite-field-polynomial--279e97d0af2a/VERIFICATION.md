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

The exact-arithmetic script `verify.py` treats a random degree-below-\(q\) polynomial as a uniform random function, enumerates its value set and the value set after each fixed additive shift, and computes the covariance by independent direct averaging. It separately computes the claimed covariance from the perturbation fiber profile and checks exact equality, strict extremizers, and first nonextremal gaps.

Verified output from `python3 verify.py`:

```
FIELD_OK q=2 functions=4 perturbations=4 unique_profiles=2 min=-1/4 max=1/4
FIELD_OK q=3 functions=27 perturbations=27 unique_profiles=3 min=-10/81 max=26/81
FIELD_OK q=4 functions=256 perturbations=256 unique_profiles=5 min=-417/4096 max=1695/4096
FIELD_OK q=5 functions=3125 perturbations=5 unique_profiles=5 min=-36076/390625 max=198924/390625
VERIFY_OK exact_joint_covariance_and_extremal_profiles=True
```

For \(q\in\{2,3,4\}\), both the random-function inputs and deterministic perturbations were exhaustively enumerated. For \(q=5\), five representative fiber profiles were tested. The field of order four uses its characteristic-two additive structure (exclusive-or). No floating-point arithmetic or external packages are used.

**Proof dependence.** All prime powers are covered by the independent joint-exclusion and discrete-convexity arguments in RESULT.md. Enumeration of four finite fields alone would not justify the general claim. The historical-priority search was incomplete in older specialized correlated-occupancy literature; the numerical checks provide no evidence of novelty. Independent audit and independent validation have not been performed.
