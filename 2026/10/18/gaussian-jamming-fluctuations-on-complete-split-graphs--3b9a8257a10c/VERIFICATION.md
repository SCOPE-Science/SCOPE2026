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

Run `python split_graph_verify.py` using Python 3 and only the standard library. The program exhaustively checks the physical random edge-order model on three small graphs (including 362,880 edge orders for the case with two independent vertices and three clique vertices), compares all first and second exact-rational moments against an independent two-dimensional chain recurrence, evaluates the recurrence for populations up to 1,200 with four independent-class proportions, and independently checks the one-dimensional variance integral by midpoint quadrature.

The computed values approach the analytic constants as the number of vertices increases; they do not certify a central limit theorem. The proof relies on the explicit generator, the invariant of the fluid ODE, late-time separation of vacant populations, martingale bounds, and limiting predictable quadratic variation. The simulation checks do not establish absence of equivalent results elsewhere in the literature. Independent validation has not been performed.
