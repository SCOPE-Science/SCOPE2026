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

The verification package consists of `verify.py`, `cert8.json`, `cert10.json`, and `verification_output.txt`.

`verify.py` uses only the Python standard library. It first verifies the explicit \(K_6\) total 2-labeling. For orders eight and ten it works in the complement, fixes the neighborhood of vertex \(0\) by relabeling, recursively enumerates every completion of the residual regular degree sequence, and checks the expected exact counts \(167\) and \(527481\). Erdős--Gallai is used only as a sound pruning test; leaves are accepted only when every residual degree is zero.

For every completion, the checker intersects the 5-regular graph with the supplied certificate masks. A successful mask must produce a spanning subgraph whose six degree-class sizes are at most \(2\), except for at most one size \(3\). The checker then independently implements the Shan--Zhong interval labeling with edge labels \(1\) and \(3\), recomputes every vertex weight from the graph and labels, and requires all weights to be distinct.

The stored replay result is:

`ALL CHECKS PASSED`

with \(167\) order-eight normalized completions and \(527481\) order-ten normalized completions. These are labeled fixed-neighborhood completions, not isomorphism-type counts. No computation is used to assert anything for order at least twelve.
