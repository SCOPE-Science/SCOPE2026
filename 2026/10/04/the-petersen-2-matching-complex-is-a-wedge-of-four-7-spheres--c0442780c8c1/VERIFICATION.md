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

The verifier is self-contained and uses only the Python standard library.

It reconstructs the Petersen graph from the fixed fifteen-edge list, enumerates every nonempty face of the \(2\)-matching complex from the degree-at-most-\(2\) condition, and checks the exact face vector
\[
(15,105,445,1245,2358,2985,2400,1095,215,6).
\]

It then rebuilds the repeated-toggle matching in the fixed edge order. The expected result is \(5432\) matched cover pairs and five critical cells: one in dimension \(0\) and four in dimension \(7\). The script constructs every cover relation in the nonempty face poset, reverses exactly the matched covers, and checks acyclicity by topological sorting all \(10869\) faces across all \(63780\) Hasse edges.

As a separate check, the script computes boundary ranks over \(\mathbf F_2\) and confirms reduced Betti number \(4\) in degree \(7\), with all other reduced Betti numbers zero.

The computation is finite and exhaustive for this graph. It does not verify any family-level generalization or bibliographic novelty.
