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

# Reproducible verification

The standalone script `verify.py` runs with Python 3 and the standard library only. From the extracted scientific package, execute:

```sh
python3 verify.py
```

Observed result:

```text
VERIFY_OK checks= 1165
q=0.4 first-moment growth: 0.889897948557
q=0.4 second-moment growth: 1.113507624413
q=1/2 second-moment growth: 1.260689853402
```

The script performs exact integer and rational checks of the nilpotent/Jordan matrix products, of the critical positive-definite quadratic invariant, and of all binary transmission histories of length at most seven for selected rational initial states. It also evaluates the infinite-series homogeneous eigen-energy numerically, including fractional moment orders, at several probabilities and coupling strengths; verifies the resulting single-step expectation equation; and checks enumerated finite-horizon expectations. The unique positive rates for moments one and two are independently compared with the explicit polynomial formulas.

No finite numerical computation proves the uniqueness of the real-order root for all parameters or establishes an infinite-time limit. Those statements are justified by the proof in `RESULT.md`: monotone convergent series, rank-one factorization, a positive homogeneous eigen-energy uniformly comparable to the Euclidean norm power, and stochastic-order monotonicity of a geometric count. The claim is not independently audited or formally certified.
