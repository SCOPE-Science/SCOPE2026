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

# Reproduction and limits

Run `python verify.py` with Python 3 and the `networkx` package. The program implements a shortest-path test for the original all-endpoint definition independently of the distance-two compatibility condition, and exhaustively compares both conditions for every vertex subset on the two smallest instances. It then builds a distance-two compatibility graph and checks all maximal cliques and all cliques for the doubly binary family at \(2\le m\le8\). It also independently checks every candidate two-vertex maximal total-visibility set for \(2\le a,b\le6\).

The recorded output appears in `verify_output.txt`. The finite checks cover \(4352\) full geodesic subset comparisons, \(1156\) enumerated facets, \(19807\) enumerated faces including empty sets, and \(484\) maximal pairs across \(25\) broader parameter cases. Their success does not prove the unrestricted infinite theorem; the combinatorial argument in `RESULT.md` does. No external/independent audit has been conducted.
