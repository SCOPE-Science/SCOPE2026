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

# Exact reproducibility and limits

Execute `python3 verify.py` with `collapse_n5.json` beside it. The script builds the graph from the defining edges and enumerates every clique of the square graph, verifies each of 48 elementary free-face collapse steps and the octahedral remainder at size ten, and computes all twenty signed simplicial Lefschetz values. It also checks the two diameter-two cases and finite good-cover/nerve-collapse examples for \(6\le n\le13\). The stdout in `verify_output.txt` was obtained from this package.

The proof of the infinite family rests on an explicit cyclic good cover, its nonempty-intersection structure, the nonliftability of two exceptional projected cliques at \(n=6\), and a uniform nerve collapse. Finite runs do not independently certify any unbounded quantifier. An independent audit has not been performed.
