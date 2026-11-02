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

# Analytic and finite checks
The proof writes every derivative-order term exactly as a positive Laplace integral. The \(4^n\Gamma(n+\sigma)^2/\Gamma(2n+2)\) asymptotic and all three local saddle regimes are calculated directly. The coalescing endpoint uses two explicit rational identities and compact-uniform Gaussian domination. Ordinary power-sum convergence and a local interior cone give the claimed summability thresholds.

The package contains `verify_trace.py`. Running `python3 verify_trace.py` in Python 3 using only the standard library returned:

`CHECK_OK: five fixed-boundary asymptotics and three junction crossover profiles; finite quadrature only`

The five fixed locations include the two open lines, the two junctions, and the circular midpoint. The three moving profiles include a negative, zero, and positive junction displacement. All numerical checks are finite and do not prove asymptotics. No external or independent audit has been performed.
