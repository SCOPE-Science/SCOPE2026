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

# Reproduction and checks

Run each standalone program with Python 3 and locally installed `sympy`, `numpy`, `mpmath`:

```
python checks/ambiguity_1d_checker.py
python checks/ambiguity_nd_checker.py
```

The checked outputs are recorded in `checks/check_output.txt`. The first program verifies algebraic one-dimensional parameterization, the sharp delay maximum, fold identities, high-precision direct quadratures and 25 zero points. The second verifies the all-dimensional completed-square identity, the frequency-boundary formula, five tensor Gauss-Hermite quadrature instances and 80 orthogonal zeros. All computations use the definitions and Fourier normalization stated in the proof. The infinite-dimensional range of the assertion is established analytically; the finite checks are sanity tests, not exhaustive certification. Publication priority and independent expert validation have not been performed.
