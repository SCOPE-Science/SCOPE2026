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

# Reproducible checks and proven limits

Run `python verify.py` with Python 3.10+ and NumPy installed. The script checks 585 generated generalized eigenvalue pencils against the exact projected Gaussian quotient: dimensions \(m\in\{2,3,4,6\}\), ambient sizes \(n=m+1\) and \(n=m+7\), several trial angles, plus nontrivial complex trial vectors supported in three eigenmodes of a larger ambient space. It checks the exact spectator eigenvalues, compares the complex-Cauchy unit-scale radial tail with its exact value \(1/2\), verifies the three-median second-moment value numerically, and checks the beta-integral constant \(1/2\) algebraically. In one reproducible execution, the script returned `VERIFY_OK: 585 compressed-eigenvalue checks; Cauchy tail and 3-median Monte Carlo; beta integral`.

Proof-critical identities requiring no finite simulation: conditional independence of the orthogonal Gaussian projections; the pencil determinant factorization; the exact complex-Cauchy density; the real-coordinate order-statistic density \(3/[4(1+x^2)^{5/2}]\); the mean-square identity \(\mathbb E|M_3-\lambda|^2=\|(A-\lambda I)w\|_2^2\); and the binomial tail exponent \(k+1\) for odd replication counts. Numerical runs only test finite cases; they neither certify all matrix dimensions nor establish divergent moments. The latter follow solely from the displayed integrations and asymptotics in `RESULT.md`.

No independent audit or independent validation was performed. No result is asserted for non-invariant spectator spaces, correlated sketches, or general nonlinear eigenproblems.
