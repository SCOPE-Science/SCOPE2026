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

# Reproducibility checks

Execute `python verify.py` with Python 3 and its standard library. The program checks the exact half-crossing velocity contraction against direct fourth-order Runge–Kutta integrations, compares the physical flight-time integral against the integrated crossing times, verifies the logarithmic-period identity numerically, and compares the known \(n=2\), \(\eta=1\) period and multiplier with their published numerical values. It passes 18 individual finite checks on five test parameter pairs. The program does not perform interval certification; tolerances are reported directly in the code.

The proof of the theorem is symbolic: exact reduction to a Riccati angular equation, integration of a positive quadratic denominator, an integrable physical-time quadrature, elementary invariant-ray geometry, and quasi-homogeneous scaling. None of the assertions about all degrees, all parameters, or infinite-time rotation follows from enumerating the test cases. The domain and the excluded critical-regime claims are stated in `RESULT.md`.
