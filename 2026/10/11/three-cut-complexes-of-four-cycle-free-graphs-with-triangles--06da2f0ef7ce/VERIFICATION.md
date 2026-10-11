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

Run `python3 verify_squarefree_threecut.py` with Python 3. The checker reconstructs the connected-triple dual, tests four-cycle exclusion, verifies that every removed edge is a genuine free face at the moment of deletion, proves connectedness of the resulting graph for the tested instances, and checks the degree/triangle rank count. It checks four infinite-family instances (three through six linked triangles) and the truncated tetrahedral graph. In addition, it directly reconstructs the original cut complex for the twelve-vertex truncated tetrahedral graph and computes every reduced mod-two Betti number. The expected nonzero list is `[(8, 27)]`, followed by `VERIFY_OK`.

The finite computations are illustrative, not exhaustive over all graphs. The uniform proof uses unique common neighbors for nonadjacent endpoints in a four-cycle-free graph, uniqueness of edges among graph triangles, elementary simplicial collapses, integral Alexander duality, and Hurewicz–Whitehead. In particular, the checker does not independently establish the unrestricted theorem. No independent audit has been performed.
