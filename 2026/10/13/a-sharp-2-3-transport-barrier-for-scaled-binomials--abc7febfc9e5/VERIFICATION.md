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
# Analytic and exact-arithmetic verification

The primary claim follows from the uniqueness of the integer within distance strictly below \(2/3\) of \(2k/3\), the binomial preimage identities for the first four rounded mass coefficients, and the positive factorization of \(a_1a_3-a_2^2\). Ordinary log-concavity is necessary for sums of independent Bernoulli variables. The explicit six-trial coupling proves optimality of the universal constant; a separate quadratic root check proves the first-size exception.

Run `python3 verify.py` from this directory with Python 3 and the standard library. The expected terminal message is `VERIFY_OK parameter_cases=349 coupling_maximum_thirds=2`. The code reproduces exact integer binomial coefficients for all \(2\le n\le350\), verifies the factorization without floating point, tests the \(n=1\) quadratic and computes a 64-unit monotone coupling at \(n=2\).

The all-size validity is proved by algebra, not by the finite checker. The check neither proves priority nor replaces independent validation. The published journal supplement was not accessible for full-text comparison; the source's earlier complete public manuscript and later published main text were examined.
