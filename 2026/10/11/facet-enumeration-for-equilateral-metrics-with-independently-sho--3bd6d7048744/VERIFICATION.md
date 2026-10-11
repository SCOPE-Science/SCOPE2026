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

The proof reduces vertexhood to the rank of incidence normals in the active tight-edge graph; every disconnected tight graph admits a feasible small perturbation. The fact that the short edges form a matching forces a cross-edge, global range one, and exactly the six paired states. The connected complete-bipartite anchor core proves sufficiency. The resulting count follows from disjoint exclusions of all-lower and all-upper assignments and standard polar duality.

The standalone `matching_facet_checker.py` gives a separate finite check. It enumerates all labeled spanning trees using Prüfer sequences, imposes every signed set of tight metric equalities, solves their potentials over integers, and retains the feasible ones. For \(3\le n\le6\) and every admissible \(k\), three independent rational length settings were tested: \(36\) test cases in total (some repeated when \(k=0\)), all matching the analytic classification. Run with `python matching_facet_checker.py` using Python's standard library. This enumeration is exact within its checked sizes, not a certificate for arbitrary dimensions or all real parameters.

The duality statement requires real scalar fields and finite-dimensional polyhedral polarity. The claim is restricted to disjoint short pairs with lengths strictly between zero and one. No independent audit has been performed.
