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

`verify.py` performs an independent finite replay of the structural equivalence used in the proof.

It enumerates all tested labeled \((k-1)\)-uniform links, forms their one-point cones, and checks that a cone contains an irreducible configuration of size at least \(n\) exactly when its link contains one of size at least \(n-1\). The tested parameter pairs are \((3,4),(3,5),(4,5),(4,6)\).

For \(k=3\), the script separately computes graph clique number and verifies that cone legality is exactly \(K_{n-1}\)-freeness. It recovers the labeled triangle-free graph counts \(1,1,2,7,41,388,5789\) through six vertices.

A successful run prints `VERIFY_OK 73123 exact assertions`.

The script is a finite consistency check, not an independent proof of the infinite Fraïssé-extension step and not an independent audit. The asymptotic graph-count theorem is cited rather than recomputed.
