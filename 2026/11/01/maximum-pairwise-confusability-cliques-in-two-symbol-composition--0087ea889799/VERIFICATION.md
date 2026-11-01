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

# Finite checks and boundaries

The standalone script `verify_read_cliques.py` enumerates all length-\(n\) words, calculates each two-symbol composition read, adds exactly the edges of read-vector Hamming distance two, and enumerates every inclusion-maximal clique via Bron–Kerbosch recursion with a pivot. Its output compares the *complete labeled set* of maximum cliques to the two asserted constructions, not merely aggregate counts.

Executed successful cases: alphabet size 2 through length 8; size 3 through length 5; size 4 through length 4; size 5 through length 3. In total 20 parameter families, 1,368 vertices across the separate graphs, 8,537 edges, and 213 maximum cliques across those graphs. The run ended with `VERIFY_OK families=20 vertices=1368 edges=8537 maximum_cliques=213`.

The script uses no downloaded input, no random seeds, and no third-party modules. These checks do not prove an all-parameter assertion. The proof in RESULT.md is exact for all stated positive parameters; no claim is made concerning larger read windows or distances other than two.
