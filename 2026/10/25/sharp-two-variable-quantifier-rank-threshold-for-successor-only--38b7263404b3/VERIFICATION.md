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

The structural proof checks the four possibilities for two vertices, the two endpoints and central interval, and the rank-depth of each separator \(\Theta_{a,b}\). Its assumption \(n\ge2r+4\) ensures at least four old-center points; one then always remains nonadjacent to any selected vertex. The sharp witnesses cover \(t=1,2\) separately and every \(3\le t\le2q-1\) by \(-1\le a,b\le q-3\) with \(a+b=t-5\).

Run `python3 checker.py` to verify exactly the predicted equivalence partition for each \(1\le q\le6\) and \(1\le n\le22\). The checker computes rank-bounded unary types, not a proof for larger cardinalities. Independently, an exhaustive two-pebble EF minimax implementation matched the same classification on smaller examples through rank four. No external certification is claimed.
