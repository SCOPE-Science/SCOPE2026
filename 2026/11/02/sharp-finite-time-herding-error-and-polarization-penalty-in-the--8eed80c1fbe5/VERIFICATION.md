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

Execute `python3 verify.py` using Python 3 and only its standard library. The checker was run against the standalone code embedded in this package and reported:

`PASS 80 exact finite-state configurations, 380 time slices; 117 dispersion-boundary grid profiles; individual/covariance/strict comparisons PASS`

The calculation enumerates the full rational-valued law of the population mean through time \(t=4\) for \(n\le4\) (through \(t=3\) for \(n=5\)), under heterogeneous initial beliefs and rational learning weights. Exact recurrence moments, martingale identities, individual terminal-error formulas and covariance claims match the finite-state computation. Its dispersion grid comparisons and strict heterogeneous-versus-homogeneous cases are additional finite checks.

The checker does **not** establish unbounded-time almost-sure convergence, the maximum-dispersion formula for arbitrary real profiles, or completeness beyond the enumerated small sizes. The written proof establishes those steps. No independent external review or testing has been performed.
