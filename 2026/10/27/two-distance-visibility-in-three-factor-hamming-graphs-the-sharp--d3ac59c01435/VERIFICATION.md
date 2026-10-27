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

# Reproducibility and verification

The mathematical proof is in `RESULT.md`. The finite verification programs do not certify the infinite statement and are not independent audit.

Run `python3 check_visibility.py`. This pure-standard-library program obtains all maximal cliques of the distance-at-most-two graph by a pivoted Bron–Kerbosch search, enumerates every subset of each maximal clique, and compares the direct geodesic obstruction test to the geometric three-carrier classification. It checks six factor triples: \((2,2,2),(2,2,3),(2,3,3),(3,3,3),(2,3,4),(3,3,4)\). Its final status is `ALL_FINITE_CHECKS_OK`. The largest case examines 30,992 diameter-two candidate subsets and returns optimum \(8\) with \(36\) maximizers.

Run `python3 check_zarankiewicz.py`. It tests five explicitly listed rectangle-free square matrices of orders two through six, checks the strict row-pair counting obstruction to one more occupied cell, and verifies the circulant construction for all orders seven through thirty. Its final status is `C4_FREE_CONSTRUCTIONS_OK`. For arbitrary orders at least seven, rectangle-freeness follows from the six distinct modular differences in the written proof, not the finite script.

No stochastic tests, downloaded third-party papers, hidden artifacts, or auxiliary generated inputs are required. Verification does not supply new values of the open Zarankiewicz function above order six, and no independent review or validation has been performed.
