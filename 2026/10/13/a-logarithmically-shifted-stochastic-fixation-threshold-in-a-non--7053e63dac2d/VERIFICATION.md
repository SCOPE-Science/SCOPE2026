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

# Reproduction and scope

Execute `python verify.py` with Python 3 and no third-party dependencies. The program checks the rational polynomial factorization for three distinct benefit parameters, corresponding to a negative, zero and positive barrier \(D\); checks that the exact rational barrier values match \(-1/4860\), \(0\) and \(9/25880\); uses exact quadratic lattice-sum formulas and numerically stable log-domain summation for populations of sizes \(1000\), \(3000\) and \(6000\); and verifies the moving critical crossover at sizes \(3000\), \(10000\) and \(30000\).

The full theorem does not depend on those finite checks. Its unrestricted basis is the exact birth–death harmonic recurrence, the closed quadratic lattice sum, a uniform Euler–Maclaurin identity and a two-location lattice-Laplace comparison with a geometric boundary contribution. The convergence statements require fixed positive selection strength; the moving-parameter crossover keeps that strength fixed.

The claim concerns a specifically defined expected-payoff Fermi closure, not the original hypergraph stochastic process. No independent audit, formal proof-assistant certification, or empirical validation is claimed.
