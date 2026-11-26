---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
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

The preceding replay checks the classification and the coefficient formula, not the separately stated scalar minimum. For a direct check of the biclique minimum run `python3 artifacts/check_biclique_minimum.py`. It tests all 28 profiles with \(1\le a\le b\le7\), directly enumerating sets by size until it finds a co-secure dominating set for each profile. It verifies the size-four threshold explicitly at \(K_{5,5}\).
