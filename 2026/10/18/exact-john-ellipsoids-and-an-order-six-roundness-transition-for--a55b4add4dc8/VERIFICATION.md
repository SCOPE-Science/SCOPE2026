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

Run `python verify.py` in an extracted package containing the accompanying script. The program uses only the Python standard library and exact `fractions.Fraction` arithmetic. It checks the two projector ranks and idempotence and independently calculates \(\Pi_U\)- and \(\Pi_W\)-energies of cut normals in the actual edge coordinates for complete graphs of orders \(4\) through \(8\).

Across \(4\le n\le299\), it verifies every indexed facet orbit inequality, including equality exactly at the claimed contact sizes; it also checks positivity, the analytic squared-semiaxis values, and the John weights on all \(296\) orders. Its successful marker is `EXACT_VERIFICATION_OK` with `facet_orbits= 44252 john_kkt_orders= 296 projection_orders= 5`.

These are **finite exact checks**; they neither enumerate all convex bodies nor prove the theorem for unbounded orders. The proof for all orders is the analytical symmetry reduction, universal cut-inequality computation, unimodal distance comparison, and exact full John contact decomposition given in `RESULT.md`. An independent human or external mathematical validation has not been performed.
