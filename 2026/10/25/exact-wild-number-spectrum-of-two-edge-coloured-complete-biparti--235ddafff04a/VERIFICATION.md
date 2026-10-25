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

# Verification evidence

The exact theorem and constructive proof appear in `RESULT.md`. `verify_wild.py` exhaustively enumerates every surjective, labelled, two-colour edge assignment for the dimension pairs \((2,2),(2,3),(2,4),(2,5),(2,6),(3,3),(3,4),(3,5),(3,6),(4,4)\). Each monochromatic spanning-subgraph component count is calculated by union-find directly from the adjacency edge lists; the script compares the observed wild-number range against the theorem. The stored transcript `verify_wild_output.txt` ends with `VERIFY_OK`. In particular, the test checks the small exceptional cases and a graph with two independent spanning trees. No reliance on an earlier run's calculations is required.

The infinite conclusion follows from explicit constructions, the cycle-space rank lemma, and one-edge recolouring interpolation, not finite enumeration. The run does not count colourings of each wild number for arbitrary \(a,b\). No independent mathematical audit or priority certification is asserted.
