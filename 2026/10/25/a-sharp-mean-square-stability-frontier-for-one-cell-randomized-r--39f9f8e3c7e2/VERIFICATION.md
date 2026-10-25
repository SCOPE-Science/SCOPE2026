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

# Verification details

The exact proof establishes the source-stage recurrence, the six-variable symmetric covariance map, the cubic Jury boundary, the discrete Lyapunov transfer, the factorization into a degree-seven polynomial, and positive-definite eigenfunctionals guaranteeing mean-square nondecay/growth. These are infinite algebraic arguments, not inferred from finite experiments.

Run `python3 verify.py` with Python 3 standard library from the containing directory. The script independently builds the matrix \(\mathcal T_z\) using exact rational stage moments, reconstructs the six Lyapunov equations, checks the closed rational gain and crossing identity for six rational parameters, checks the deterministic-versus-mean-square stability gap at \(z=7/6\), and reconstructs four successive source-stage updates. It reports `PASS: 239 exact-rational identities and independently reconstructed matrices`.

Scope limits: the verifier checks finite rational instances of universal identities. It does not independently certify all real parameters or the literature priority assessment; those are supported respectively by the mathematical proof and the documented source comparisons. Independent scientific audit has not been performed.
