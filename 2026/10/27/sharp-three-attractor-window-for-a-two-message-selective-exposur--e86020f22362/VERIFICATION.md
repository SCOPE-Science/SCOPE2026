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

The scientific object is the deterministic expected-message update on \([0,1]\), not the random finite-source process. The proof obtains the complete equilibrium census from the strictly increasing quotient \(K(x)\), establishes interval-by-interval monotone convergence, and verifies the critical cubic and the asymptotic collision. The positive-probability perturbation statement follows from continuity and hyperbolic fixed-point persistence, with separate endpoint control.

The bundled `verify.py` was executed in Python 3 with SymPy and mpmath and returned `PASS: 2797 exact-symbolic and high-precision numerical assertions`. The exact symbolic checks verify the rational case, the derivative-ratio identity and the critical Taylor coefficient; high-precision tests corroborate phase regions, separatrix location, source asymmetry and sample orbits. Numerical checks neither constitute a universal proof nor validate the full stochastic finite-source system.

Self-review passed for the stated deterministic theorem. Independent audit is not performed.
