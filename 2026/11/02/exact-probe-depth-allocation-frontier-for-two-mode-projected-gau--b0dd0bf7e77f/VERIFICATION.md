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

# Numerical and analytic verification

The exact result follows from the proof in `RESULT.md`, independently of finite computations. To rerun, execute `python verify.py` with NumPy installed. The program checks deterministic quadrature (65,536 midpoints per integral), 90 independent positive spectral pairs and their strict MSE crossover signs, a three-dimensional example with nonzero resolved/complement coupling, 120 two-step Lanczos reconstructions, and Gaussian moment diagnostics on 260,000 seeded probes. Actual execution output:

`PASS 1694 analytic-identity, quadrature, matrix-Lanczos, and seeded sampling checks`

The symbolic factorization in `RESULT.md` uses only elementary polynomial arithmetic and is reconstructed in the verifier by independent identities across a broad family of eigenvalue pairs. The finite checks cannot establish exactness for all positive eigenvalue pairs; the polar integration and algebraic proof do. The source paper's full P-SLQ procedure also includes boundary coupling, basis setup, and covariance generation, which are outside the tested trace-only statement. Independent mathematical validation has not been performed.
