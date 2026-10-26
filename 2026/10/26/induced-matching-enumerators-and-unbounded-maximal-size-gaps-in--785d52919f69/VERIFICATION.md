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

# Reproducibility and verification limits

Run `python3 verify.py` with Python 3 standard library and compare the output with `verification_output.txt`. The checker reconstructs the graph from the original adjacency relation, enumerates candidate subsets of incidence edges, checks inducedness directly, and tests one-edge extensions for maximality. It compares every coefficient, not just the minimum and maximum cardinalities, for nine parameter pairs, covering 2,191,336 tested edge subsets in total.

The upper bound on induced-matching size, \(p+q-2\), is proved in `RESULT.md` and is why the brute-force search need not consider larger candidate subsets. Separate exact-integer tests check support and boundary multiplicity identities for \(2\le p\le20\), \(p\le q\le26\). Those tests do not establish the infinite theorem or bibliographic originality. Independent audit is not performed.
