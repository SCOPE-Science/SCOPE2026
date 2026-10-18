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

# Reproduction and verification

Run `python3 VERIFY.py` with Python 3.9 or newer; no third-party modules or external data are required. The program constructs Sylvester Hadamard matrices, independently evaluates every term in the sketched one-variable ridge normal equations, verifies binomial and hypergeometric probabilities using exact rational arithmetic, compares exact Gaussian-angle CDFs with deterministic angular grids, checks the exact Cauchy-only tail beyond the nonsingular support bound, and approaches the Gaussian singular-sector coefficient by numerical quadrature.

Actual execution of the submitted `VERIFY.py` completed with:

`PASS: 2292 deterministic identity, geometric probability, and asymptotic checks`

The check count includes 2,292 executable assertions under a fixed random seed. Finite checks do not establish existence of moments at every sample count or any asymptotic limit. Those statements follow from the analytic derivations in `RESULT.md`, particularly the normal-variable reduction, exact mixing probabilities, Gaussian singular integral, and concentration estimate. A separately conducted independent scientific audit has not been performed.
