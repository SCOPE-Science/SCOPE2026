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

# Reproducibility and limitations

Run `python verify.py` with the dependencies from `requirements.txt`. It constructs the full \(n^2\)-dimensional Hamiltonian, groups equal energies, and uses detector-restricted singular vectors to build the absorbing projector. It then verifies every ordered localized pair and every exchange pair for each \(n=4,5,6,7,8,9\) at hopping parameters \((1,1)\), \((1,1.5)\), \((0.75,1.25)\), and \((2.3,2.3)\). It checks the rank and projector idempotence, plus random unequal positive loss rates for sizes at most six and actual matrix-exponential capture for size four. The expected success line is `VERIFY_OK spectral_ranks=24 sitewise=1084 exchange=928 lossy_spectrum=12 long_time=4`.

All tests are finite. General coverage over arbitrary \(n\), all positive hopping strengths, and all strictly positive absorber strengths is provided by the analytic spectral decomposition and the strictly positive detector Gram matrix. Numerical eigenvalue thresholds are used only in the standalone test; no universal numerical certificates or independent reviews are claimed.
