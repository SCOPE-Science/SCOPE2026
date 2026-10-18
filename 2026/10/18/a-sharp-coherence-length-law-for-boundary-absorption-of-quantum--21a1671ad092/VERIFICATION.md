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

# Verification performed
The standalone Python checker (`code/verify.py`) was run using the dependencies in `code/requirements.txt` and returned `PASS: 279 explicit checks`. It independently reconstructs the Toeplitz absorption compression using Gaussian quadrature for ten packet lengths, verifies the exact two-site chiral eigenvalues and the analytic upper/lower gap inequalities, and checks that changing absorber strength decreases the in-band response for randomized normalized coherent packets. For three initial states it also propagates a finite non-Hermitian chain directly and compares cumulative absorption at time 120 with the exact infinite-time spectral integral.

# Proof boundary
Finite quadrature and time integration do not prove spectral asymptotics. The arbitrary-window theorem follows from the analytic boundary Green function, an exact Parseval identity, pointwise absorption multipliers, and discrete Dirichlet gradient inequalities written in `RESULT.md`. Finite-time, noisy-data and multi-sink extensions are not verified.
