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

# Reproduction and proof checks

Run `python3 verify_two_threshold.py` in the directory containing this file. The program relies only on the Python standard library. It computes \(g(z+h)+g(z-h)\) directly from logistic derivatives, locates the zeros using an independent direct-benefit grid and bisection method, and cross-checks the explicit quadratic root formula. It verifies left/right flow signs at all zeros for 141 parameter configurations, including the exact rational/algebraic witness with \(n=10\), \(H=3\), and \(\theta=17/64\). The 140 additional parameter triples are deterministic from the embedded seed.

The program prints four approximate roots \(0.29422383882416\), \(0.42245482677022\), \(0.57754517322978\), and \(0.70577616117584\) and reports all parameter checks passed.

Analytic proof requirements are separately specified in `RESULT.md`: the two-sigmoid hyperbolic identity, the exact derivative and maximum of \(F_H\), the strict endpoint inequalities, the quadratic roots, and the signs establishing attraction and repulsion. The published gradient and fitness-curvature equations are hypotheses about the particular weak-selection pair approximation, not newly proved stochastic-process convergence claims. Numerical checks alone cannot establish four-root maximality on an infinite parameter domain. Independent scientific audit has not been performed.
