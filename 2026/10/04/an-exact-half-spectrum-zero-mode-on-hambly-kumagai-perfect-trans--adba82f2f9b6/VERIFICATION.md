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

The all-level proof is structural. The critical checks are:

1. The Hambly-Kumagai recursion retains every old vertex and replaces each old edge by two new midpoint branches of length two.
2. The Krawtchouk diagonal is zero, so the new Hamiltonian is block off diagonal between old vertices and new midpoints.
3. Proposition 2.15 makes the old-to-new block a layer-weighted unsigned incidence matrix, with two identical columns per old edge. Nonzero layer-wise row and column scalings reduce one column from each pair to the ordinary unsigned incidence matrix of the preceding graph.
4. A connected bipartite graph has unsigned-incidence rank one less than its vertex count.
5. The graph cardinality formula then gives \(\dim\ker H_\ell=(4^\ell+2)/3=|V(HK_\ell)|/2\). The chiral block involution supplies the equal positive/negative split.

The included `verify.py` uses only the Python standard library. It reconstructs the graphs through level \(6\), computes exact rational incidence ranks, checks the all-level formula in those cases, and explicitly checks the published zero multiplicities \(6\), \(22\), and \(86\). It prints `VERIFY_OK` on success.

Limits: finite replay does not prove the theorem; the incidence-rank argument does. The replay does not attempt to reconstruct every weighted Krawtchouk matrix because the proof removes those nonzero weights by exact invertible scalings. No independent audit has been performed.
