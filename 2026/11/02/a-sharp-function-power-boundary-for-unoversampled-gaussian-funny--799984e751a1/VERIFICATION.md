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
# Verification and reproducibility

Run `python verify.py` after installing `requirements.txt`. The program constructs explicit randomized rank-one Nyström matrices, compares their true eigenvalues to the scalar formula, tests two exact closed-form expectation identities (for \(m=1\) and \(m=3\), \(\beta=1\)) using numerical quadrature, and compares further finite-\(L\) normalized integrals to the asymptotic gamma-function coefficient. Its deterministic checks use an explicitly fixed random seed. Expected message:

`VERIFY_OK 462 independent matrix, exact-integral and asymptotic-constant checks`

The exact formulas checked are derived in RESULT.md. Computational checks are finite tests and do not imply the infinite-\(L\) equivalent, whose proof is analytic via beta-prime densities and dominated convergence. Results do not address finite-precision breakdown. Independent scientific audit has not been performed.
