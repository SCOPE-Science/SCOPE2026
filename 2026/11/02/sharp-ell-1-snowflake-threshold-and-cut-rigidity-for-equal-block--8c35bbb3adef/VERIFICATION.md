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

# Verification scope
The analytical proof uses an all-cut variance identity with explicit positive square terms, a cut cone characterization of finite real \(\ell_1\) metrics, and finite-support cut constructions for every allowed parameter. All boundary cases \(r,n\ge2\), \(1\le t\le2\) and \(t=n/(n-1)\) are included.

Run the supplied standalone `check_metric.py` with Python 3. It enumerates every cut for seven small parameter pairs and computes all stated mean-distance identities using exact rational arithmetic, including equality cases. For six rational values of \(t\) on each pair it constructs the optimal metrics as nonnegative cut sums and checks all distances. The observed output was `CHECK_OK {'cut_identity_assertions': 15792, 'balanced_cut_equalities': 344, 'exact_embedding_pairs': 1164}`. Independently configured finite cut-cone linear programs reproduced the value in 24 small cases to numerical tolerance; their finite computations were not used for the universal proof.

No proof of additional claims concerning unequal clusters, minimal embedding dimension, or all subcritical cut decompositions is supplied. Literature originality is qualified by the possibility of an unindexed equivalent in older hypermetric/cut-cone literature. Independent audit and independent mathematical validation were not performed.
