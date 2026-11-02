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

# Verification of the stationary mode classification

The accompanying file `verify.py` is a standalone SymPy/mpmath program. Execute `python verify.py` with Python 3, SymPy and mpmath installed. In the reviewed computation, it returned:

```
PASS: 115 symbolic and numerical checks
Exact witness interior stationary points:
  x_min = 0.0409312687796573054 ; p(x_min)/p(0) = 0.99952540321869197
  x_max = 0.0823098685578010443 ; p(x_max)/p(0) = 1.00008878159333551
```

The symbolic checks reconstruct the derivative of the published stationary-density formula and verify its quadratic numerator, endpoint sign, discriminant, central boundary polynomial, exact witness factorization and sixth-order critical polynomial. Independent numerical quadratures compute the unnormalized density ratios and verify the derivative at positive positions. One hundred deterministic parameter substitutions corroborate the classification, but the uncountably many positive parameter values and positions are covered by the analytic proof in `RESULT.md`, not finite testing.

The proof assumes the positive, normalizable stationary density established by the cited source; it does not independently prove uniqueness of the Markov invariant distribution. It does not establish a global count for noncommensurate rate gradients. No independent mathematical audit has been performed.
