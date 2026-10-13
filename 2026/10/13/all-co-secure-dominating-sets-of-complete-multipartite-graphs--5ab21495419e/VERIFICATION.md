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

The analytic proof is the primary evidence.

The script `artifacts/verify.py` enumerates every nondecreasing part-size profile of total order \(2\) through \(10\). For each profile it constructs the graph, checks every vertex subset against the co-secure definition by searching all legal one-vertex swaps, evaluates the structural characterization independently, and compares the exact size distribution with the polynomial formula.

Replay output:

`ALL CHECKS PASSED; profiles=128; subsets_checked=64916; orders=2..10`

The finite search tests small boundaries including \(K_{1,1}\), stars, balanced and unbalanced bicliques, multiple singleton parts, complete graphs represented as all-singleton multipartite graphs, and the transition between two and three partite classes. It is corroborative only and does not replace the arbitrary-order proof.
