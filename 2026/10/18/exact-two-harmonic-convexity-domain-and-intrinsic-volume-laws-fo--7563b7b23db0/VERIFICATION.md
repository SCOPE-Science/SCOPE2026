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

# Verification record

The standalone script `check.py` was executed with Python 3 and SymPy/mpmath. It passed exact differentiation identities for the two curvature-radius eigenvalues, the parallel-radius integrating-factor identity, the rational endpoints and tangency parameter identities, the interior quadratic stationary-value factorization, and exact surface-area and enclosed-volume polynomial integrations. It also passed 50,000 deterministic coefficient tests against independent global quadratic minimization and high-precision numerical integrations at four parameter pairs.

The all-direction and all-parameter assertions rely on the analytic proof in `RESULT.md`, specifically polynomial minimization on the closed interval and the support-extension Hessian equivalence. Finite numerical tests do not prove universal convexity or novelty. The script does not establish historical priority or any independent expert assessment. One relevant particle-shape source was examined only through a publicly available abstract; this is explicitly retained as a literature-access limitation, not a claim that the full document was checked.
