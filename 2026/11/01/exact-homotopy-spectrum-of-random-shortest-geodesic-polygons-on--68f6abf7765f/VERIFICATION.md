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

# Reproducible checks and limits

Run `python3 check.py` with Python's standard library. The checked standalone source is supplied in the same package. It recomputes the first eight odd Legendre integrals numerically without using the Catalan recurrence for integration, confirms the exact \(n=3,4\) integral benchmarks against separately summed spectral traces, tests 13 consecutive finite-length values and their explicit two-mode inequalities, and simulates independent spherical lifts for five loop lengths (25,000 trials each). It prints `ALL_CHECKS_PASSED` on success.

The universal correctness claims require the analytic steps in RESULT.md: antipodal geodesic lift parity, trace representation, Legendre eigenvalue computation, and Hilbert–Schmidt tail estimates. Neither Monte Carlo sampling nor finitely many trace sums prove an infinite-length statement. The supplied checker is corroborating evidence only.

No independent audit has been performed.
