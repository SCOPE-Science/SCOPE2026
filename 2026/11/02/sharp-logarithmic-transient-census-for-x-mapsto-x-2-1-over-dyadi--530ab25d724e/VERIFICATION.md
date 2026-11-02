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

# Computational and symbolic reproducibility

The independent standard-library script `verify_minus_one.py` enumerates all vertices, outgoing edges, cycles and exact depth counts for every \(2\le n\le16\). It independently checks the piecewise cumulative formulas and the sharp maximum.

The actual completed replay produced: `VERIFY_OK n_levels=15 total_graph_vertices=131068 sharp_tail_formulas=15`.

The infinite proof instead uses the identity \(f^2(x)=x^2(x^2-2)\), elementary induction on the valuation, and the four solutions of \(z^2\equiv1\pmod{2^k}\) for \(k\ge3\). No finite enumeration proves the all-\(n\) theorem. No independent external audit is claimed.
