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

# Reproducibility and limits

Run `python3 verify_incidence.py`. Only the Python 3 standard library is required. Expected output begins with `VERIFY_OK graph_instances=25 induced_matching_recursions=213715 support_checks=51`.

The checker constructs each incidence graph from its original graph, determines conflicts using actual endpoint equality or graph adjacency, enumerates the resulting independent edge subsets, and accepts only those covering every edge of the conflict graph (the definition of inclusion-maximality). It checks 19 complete-bipartite instances with \(1\le a\le b\le6\), \(ab\le25\), and the six complete graphs \(K_n\) for \(2\le n\le7\). It separately checks the algebraic support formula in 51 cases. The graph-level tests do not assume the surjection characterization.

Finite checks are not an all-order proof. The infinite theorem and its boundary cases are established in `RESULT.md` by a separate bijection and a positivity argument. No independent external audit or publication-priority certification is represented by this package.
