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

The proof was reconstructed from the definitions rather than inferred from a search result.

For an arbitrary singular \(\kappa\), set \(\mu=\operatorname{cf}(\kappa)\) and choose a strictly increasing cofinal sequence \(\langle\kappa_i:i<\mu\rangle\). The proposed subsystem uses, on level \(\kappa_j\), all later branches \(B_{\kappa_i}\) with \(i>j\).

The following checks were carried out explicitly:

1. Every chosen node exists because \(\kappa_j<\kappa_i\) whenever \(j<i\).
2. Every subsystem level has cardinality exactly \(\mu\), since a tail of the infinite regular cardinal \(\mu\) has cardinality \(\mu\).
3. For any two subsystem levels, choosing a still later branch gives comparable nodes on both levels; the predecessor-comparability axiom follows from the ambient tree order.
4. Since \(\kappa\) is singular, \(\mu^+<\kappa\); hence the subsystem is narrow in the source's width sense.
5. Every positive-level node belongs to a branch of height below \(\kappa\), so its cone is bounded. Therefore no subtree of height \(\kappa\) containing such a node can be well-pruned, and every height-\(\kappa\) subtree must contain such nodes.

No finite experiment, enumeration, or external certificate is used. The result does not assert anything about two-cardinal trees or about regular-height trees.
