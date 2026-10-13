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
The embedded `verify_degree_coreness_boundary.py` performs an exact finite replay using only the Python standard library.

It enumerates every labeled simple graph on \(2\) through \(7\) vertices and retains the connected graphs. The connected counts are checked against
\[
1,\ 4,\ 38,\ 728,\ 26704,\ 1{,}866{,}256.
\]

Core numbers are computed on the complete enumeration by minimum-degree peeling. Every seven-vertex failure is independently rechecked by direct \(k\)-core pruning, and connectivity is independently rechecked by transitive closure.

The replay verifies:
- failure counts \(0,0,0,0,0,420\) for orders \(2,\ldots,7\);
- degree sequence \((4,3,2,2,1,1,1)\) for every failure;
- core-number multiset \((2,2,2,1,1,1,1)\) for every failure;
- exactly one failure isomorphism class;
- representative edges \(\{01,04,05,06,12,13,23\}\);
- representative core-number vector \((1,2,2,2,1,1,1)\);
- orbit size \(420\);
- automorphism-group order \(12\).

Run:

`python3 verify_degree_coreness_boundary.py`

The first output line must be:

`VERIFY_OK`

The structural proof in `RESULT.md` is independent of the exhaustive census.
