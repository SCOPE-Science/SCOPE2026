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

# Finite and structural checks

The exact Python program `verify.py` takes no external input and uses only the standard library. It constructs the two-subset Kneser graph from disjointness, enumerates every vertex subset of cardinalities one through four for each of the six values \(5\le n\le10\), tests ordinary and skew forts directly from neighborhoods, and compares every accepted four-set with a separate graph-shape classifier. It also runs two distinct forcing-closure processes for candidate white sets at \(5\le n\le8\), testing both static/dynamic equivalences. The corresponding output is `verify_output.txt`.

The run covered 264,959 static candidates and 34,028 directly simulated initial configurations. Counts of minimum ordinary and skew forts for \(n=5,6,7,8,9,10\) were respectively \((20,5),(135,30),(210,105),(595,385),(1953,1575),(6615,5985)\). The proof establishes the classification at every larger order; there is no extrapolation from the finite run to the theorem.

No independent verification, computer proof assistant, or external certificate is asserted.
