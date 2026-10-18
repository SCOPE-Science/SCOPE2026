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

# Verification and scope

Run `python3 artifacts/verify.py` using Python 3 standard library. The program independently reconstructs the Fano-plane incidence graph, checks all graph degrees, enumerates every four-subset and its connectivity, and rebuilds the full face poset. It verifies exactly 903 top-dimensional facets and 15,816 faces, including the empty face. Every one of the 108,416 Hasse covers is oriented under the specified vertex-toggle matching and every directed vertex is consumed by a topological sort, proving no gradient cycle exists. Exactly 188 critical nine-cells survive, with no other critical cells. The expected terminal line is `VERIFY_OK`.

Run `python3 artifacts/verify_mod2.py` for an independently assembled augmented simplicial boundary complex, with no use of the Morse matching. Its complete mod-two boundary ranks, in increasing positive chain-size order, are `(1,13,78,286,715,1287,1716,1716,1287,715)`. Thus the sole nonzero reduced mod-two Betti number is 188 in degree nine. The expected terminal line is `MOD2_VERIFY_OK`.

These computations constitute a complete finite exact certificate for the stated graph and cut parameter. The independent boundary check confirms the homology in characteristic two; the separately proved acyclic integral discrete-Morse model is needed for the integral homotopy conclusion. They do not establish results for larger graphs or different cut parameters, and independent validation has not occurred.
