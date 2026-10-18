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

The finite claim is verified by `python verify_gp.py` and `python verify_lcf.py` in the same directory as `CERTIFICATE.json`. Both require only Python 3.10+ standard library. The programs reconstruct graph edges rather than importing the certificate as an unverified graph.

The first verifier enumerates all 55,455 supports of size at most five, proves no support of size at least six can give weight below twelve, checks the 72 canonical states, 96 transition edges, and the complete branch-to-line-graph incidence bijection, then performs all-source breadth-first search.

The second verifier independently constructs the LCF representation of the graph, verifies the supplied isomorphism to the generalized-Petersen model, recursively enumerates the same bounded support domain by an endpoint-coverage formula, independently rebuilds all 96 transitions and calculates every eccentricity. It also cross-checks the finite incidence certificate. Both verified outputs were recorded from executing the actual included scripts.

The proof is exhaustive for this graph because there are only 24 edges and every label-2 support of size at least six already has weight at least twelve. The approach makes no assertion about the parameter on other cubic graphs, about unconstrained relabeling models, or about independent external validation.
