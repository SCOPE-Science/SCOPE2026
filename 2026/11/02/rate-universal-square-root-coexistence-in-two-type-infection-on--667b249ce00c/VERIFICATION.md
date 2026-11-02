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

The finite-source formulas follow from an exponential first-hub race, a two-step Erlang survival function, and exact integration. For any fixed positive rate pair, the asymptotic expansion is obtained analytically from the rescaled integral by Taylor expansion with a dominated tail bound. Conditional late infections are independent competing exponential races; binomial concentration gives the claimed minority moment law. No finite experiment is used as an infinite proof.

Run `python3 checker.py` with Python 3 from the directory containing this file. The program requires no third-party package. It reconstructs the complete terminal type-1 population distribution on small \(K_{2,n}\) graphs in two different ways: (i) a direct, acyclic four-count Markov-chain recursion using only rational rates and (ii) the first-hub/second-hub conditional race. It also checks exact coexistence probabilities, strict monotonicity as peripheral count grows, rate-swap symmetry and numerical convergence to the two-term Laplace expansion. Its recorded result is `PASS: 687 exact-rational assertions and asymptotic diagnostics`.

All finite-state arithmetic uses exact `fractions.Fraction` values. The asymptotic diagnostics use floating-point conversions of exact rational formulas and are explicitly non-certifying. No external validation, human expert review, or formal proof certification was performed. No claim is made for recovery, non-exponential contact times, graph randomness, or growing numbers of hubs.
