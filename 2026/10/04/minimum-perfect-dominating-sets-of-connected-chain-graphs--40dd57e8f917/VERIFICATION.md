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

The proof was reconstructed from the chain-graph neighborhood definition rather than inferred from finite data. The critical equalities are that an unselected vertex in \(A_i\) has exactly \(Y_i\) selected neighbors and an unselected vertex in \(B_j\) has exactly \(X_j\) selected neighbors. They yield the stated profile criterion directly.

The standalone `verify.py` independently builds every canonical connected chain graph of order at most \(10\), enumerates every vertex subset, and checks the outside-only perfect-domination definition against both the profile criterion and the closed minimum-size/count formula. Replay output:

`VERIFY_OK profiles=511 subset_checks=349524 perfect_sets=13825 criterion_checks=349524 minimum_checks=511 exception_profiles=28 max_order=10`

The finite replay is not an infinite proof and is used only as a stress test. No assertion is made about disconnected chain graphs, efficient domination, perfect \(k\)-domination, or inclusion-minimal perfect dominating sets of nonminimum cardinality.
