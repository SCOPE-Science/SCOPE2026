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

# Reproducibility checks

The standalone `verify_weighted_wheel.py` independently constructs the weighted wheel and computes shortest paths with NetworkX weighted Dijkstra. SymPy rational arithmetic checks 600 quadratic identities for rim orders 4 through 13 at rational spoke lengths and positive integral exponents. The code also uses NumPy and SciPy to inspect the critical eigenvalue signs and centered Gram ranks for orders 4 through 39.

Observed output from running that standalone checker:

```text
EXACT_WEIGHTED_SHORTEST_PATH_DECOMPOSITION_OK 600
CRITICAL_TRANSITIONS_OK 36 n=4..39 nullities even=2 odd=3
TRANSITION 4 t= 0.707106781187 p= 2.0
TRANSITION 5 t= 0.839979313649 p= 1.855205961074
TRANSITION 6 t= 0.774281326315 p= 1.584962500721
TRANSITION 7 t= 0.852446141977 p= 1.517495752539
TRANSITION 10 t= 0.844676487308 p= 1.321928094887
TRANSITION 11 t= 0.882359312101 p= 1.296289919657
TRANSITION 20 t= 0.912599155962 p= 1.152003093445
TRANSITION 21 t= 0.924973161004 p= 1.14524783392
ALL_WEIGHTED_WHEEL_CHECKS_OK
```

The infinite-family proof follows from an exact zero-sum decomposition, Fourier eigenvalue bounds and monotonicity; finite computations are not a substitute. Published-source priority remains potentially incomplete. Independent mathematical audit has not been performed.
