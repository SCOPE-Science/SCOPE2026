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
# Reproducible checks

Run `python3 verify.py` from the directory containing the standalone script. It uses the standard library only, creates connected block graphs by explicitly gluing cliques along vertices, computes the exact coefficient vector by the recursive clique-incidence transfer, and independently iterates through every vertex subset testing whether each excluded vertex has at most one included neighbour.

The script checks 1,816 test instances of order up to twelve, consisting of clique chains, deterministically seeded arbitrary gluings, and complete graphs. Duplicate isomorphic instances are not identified. It asserts exact equality of every polynomial coefficient for every instance. The observed output begins with `PASS: 1816 connected clique-block-tree cases; maximum n = 12`.

Sample vectors in increasing degree: one triangle `[1, 3, 0, 1]`, two triangles sharing a vertex `[1, 5, 0, 2, 0, 1]`, three triangles in a chain `[1, 7, 4, 3, 0, 2, 0, 1]`, and a four-clique with three distinct pendant edges `[1, 7, 6, 1, 1, 3, 3, 1]`.

These are finite checks and cannot certify a theorem for arbitrarily large block graphs. The proof uses a disjoint, exhaustive recurrence over the block incidence tree. No independent audit has been performed.
