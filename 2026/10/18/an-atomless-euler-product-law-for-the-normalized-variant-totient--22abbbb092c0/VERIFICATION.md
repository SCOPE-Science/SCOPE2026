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

# Finite reproducibility checks

The standalone `verify.py` uses Python 3 standard-library exact fractions and integer gcd. It computes the defining count directly for every integer from 1 through 1200 and compares it to the separately factored multiplicative surrogate exactly. It verifies the exact formula at multiples of four and confirms 512 distinct rational finite Euler factors from the first nine primes through 23. It also approximates the absolutely convergent mean constant from primes up to 200000 and compares four finite sums. The exact output is in `verification_output.txt`.

# Proof obligations and limitations

The infinite claims are proved by the uniform arithmetic approximation, fixed-prime CRT independence, the summable large-prime probability tail, nonzero expected logarithmic product, prime-valuation injectivity, and Dirichlet-convolution summation in `RESULT.md`. Finite checks cannot establish these claims by extrapolation. This verification is not independent validation.
