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

# Direct finite verification

Run `python3 verify.py` using the Python standard library only. The program independently constructs the edges of the complete bipartite graph subdivision, computes the conflicting edge pairs by examining **actual distinct third edges**, and tests inclusion-maximality by attempting single-edge additions.

For each \(2\le b\le5\), it inspects all \(2^{4b}\) edge subsets and compares the complete cardinality distribution to the proposed formula. Their total is **1,118,464 candidate edge subsets**. It independently checks edge-conflict incidence identities through \(b=9\) (176 graph edges across eight parameter values) and enumerates the closed pairs \(A=N(B),B=N(A)\) for each \(2\le b\le9\), comparing all coefficients and totals. A separate small direct invocation at \(b=1\) confirms four size-two sets. Expected main verifier output:

`VERIFY_OK direct_edge_subsets=1118464 incidence_edges=176 closure_parameters=8`

These experiments do not establish a theorem for unbounded \(b\). The proof of the complete four-type classification and the exhaustive fixed-point correspondence is the mathematical certificate for that range. Source-priority review is provisional; independent mathematical audit was not performed.
