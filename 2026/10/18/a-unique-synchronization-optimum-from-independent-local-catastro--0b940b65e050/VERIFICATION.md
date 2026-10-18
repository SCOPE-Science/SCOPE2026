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

Run `python verification.py` with Python 3, `sympy`, `numpy`, and `scipy`. The program performs 13 exact symbolic assertions, 20 independent finite-state stationary first/second-moment comparisons, and 35 unique-optimum numerical inequalities: 68 successful checks in total.

The symbolic assertions validate the stationary generator moment equations, rational variance/covariance and injection-independent ratio, derivative signs after factorization, and the stated parameter limits. The independent numerical tests solve the stationary transpose generator for two-site occupation cutoffs of 14 in each coordinate at five parameter choices. Reflecting truncation at those cutoffs is not the original infinite-state chain; their results are corroborative and cannot establish the all-state theorem. The theorem itself is proven by explicit Lyapunov bounds and exact moment balances in `RESULT.md`.

The reset optimum is the unique root of a strictly decreasing cubic; the numerical checks verify sample instances rather than asserting complete root enumeration. All hypotheses require strictly positive arrival, death, hopping and clearing rates; the zero-reset case in the checker is a separate Poisson reference, not a proof that the positive-rate statement extends to negative or zero parameters. Independent audit has not been performed.
