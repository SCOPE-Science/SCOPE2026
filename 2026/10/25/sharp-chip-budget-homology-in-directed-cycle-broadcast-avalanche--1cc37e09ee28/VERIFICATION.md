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

# Reproducibility and proof checks

The proof is independent of computation: verify the exact parallel chip-firing recurrence; use the generalized Chinese remainder theorem with pairwise gcd \(g\); identify all maximal faces of the simplicial join; apply the integral join-suspension identity. Nonzero homology of degree \(k-1\) follows directly from all \(m_i\ge2\); no finite calculation is promoted to a universal argument. The universal dimension bound requires positive outdegree and a fixed conserved grain count.

Run `python3 verify.py` (Python 3.9+ standard library). On each selected graph, it constructs directed arcs, simulates a full firing period from exactly \(k\) initial grains at the broadcaster, and compares every observed firing support to all predicted CRT facets. For six finite instances, it enumerates faces and computes boundary ranks over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_5\), and \(\mathbb F_7\); each observed reduced Betti number agrees with the claimed formula. Three additional tuples undergo complete-period facet comparison without full homology reconstruction. The actual run printed `ALL CHECKS PASSED`.

Checked homology examples: \((3,4)\), \((6,10)\), \((9,15)\), \((3,4,5)\), \((4,6,10)\), \((6,10,14)\). Additional exact firing-support checks: \((3,5,7)\), \((6,10,14)\), \((3,5,7,11)\). The checker does not compute integral Smith forms; integral torsion-freeness is proved by the join decomposition. It is not a check on arbitrary unequal pairwise gcd patterns or digraphs with sinks. Independent audit: not performed.
