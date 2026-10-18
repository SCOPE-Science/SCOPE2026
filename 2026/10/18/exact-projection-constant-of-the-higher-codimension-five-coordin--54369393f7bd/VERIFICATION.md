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

# Verification

The exact checker `check_exact.py` uses only `fractions.Fraction` from the Python standard library. It checks (i) the four required biorthogonality relations, (ii) every one of the five absolute row sums, (iii) the probability-vector and bounded-sign hypotheses for the dual inequality, (iv) all ten rational component equalities for the two dual vectors, (v) primal–dual equality, and (vi) the strict improvement over the previously constructed projection norm.

The infinite family is established by direct-sum decomposition and projection compression in the paper; the checker only evaluates the finite rational core. No claim of independent auditing, publication priority certification, computational exhaustiveness over arbitrary projections, or a complex-scalar analogue is made.
