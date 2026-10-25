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

# Reproduction and limits

Execute `python certify.py` with SymPy and mpmath. This code reconstructs the precise scattering numerator jet equations, computes symbolic derivatives, and uses directed-rounded interval enclosures of their Jacobian and the fourth numerator derivative. The certified infinity-norm upper bounds on the Newton-map defect and center residual give a contraction into a closed rational box; Banach's fixed-point theorem supplies an actual positive solution. The nonzero fourth-derivative interval supplies exact multiplicity. The reproduced checks do not establish global optimality, uniqueness outside the displayed box, stability under parameter drift, or independence from existing literature. Independent validation has not been performed.
