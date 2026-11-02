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

# Reproduction of the finite certificate

Run `python3 verify_nos.py` (Python standard library only). The verifier independently regenerates all four-symbol length-three words and quotient graph edges, finds all six odd-degree quotient vertices, enumerates every three-edge perfect matching, evaluates the two chosen telescoping-flux obstructions (nonzero remaining sums \(-2\) and \(+2\)), and checks all \(24\) cyclic windows of the explicit witness. `verification_output.txt` is the captured stdout from an actual successful execution.

The universal upper bound is the mathematical reduction from any longer negative orientable word to an Eulerian distinct-edge quotient subgraph; the finite checker checks the complete small graph, not an open-ended collection of test words. This is a reproducible self-review, not an independently audited or certified proof. Literature priority is not independently certified.
