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

# Exact finite verification

Execute `python3 pappus_independence_checker.py` in Python 3.9+; no packages or files other than the embedded checker are needed. Exact verification was performed on the code embedded in this finding. It enumerates all 2,597 nonempty independent faces, all 1,293 matching pairs and 11,430 directed Hasse incidences and certifies acyclicity by Kahn's algorithm. It checks the 11 critical cells, separately computes the unmodified simplicial boundary ranks over \(\mathbb F_2\), enumerates all 216 graph automorphisms with adjacency/nonadjacency constraints and evaluates their complete signed Lefschetz character.

The character histogram is \(\{-2:21,-1:72,0:54,1:32,2:36,10:1\}\); its average is zero and its squared norm is two. The cyclic shift through six vertex labels has character \(-2\), as required by the known order-three restriction. The general theorem turning an acyclic face-poset matching into a CW model is a mathematical ingredient, not an unverified computational claim.

Limitations: The checker does not independently identify the two irreducible constituents by conventional group-theoretic names, prove originality, or perform any external audit. The quotient rational-homology calculation follows from finite-group transfer and the computed character average; it is not a direct quotient triangulation calculation.
