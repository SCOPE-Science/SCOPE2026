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

# Verification and reproducibility

Run `python3 odd_cycle_wl_verifier.py` using Python 3 with only the standard library. The recorded replay output is embedded in `verification_output.txt`.

The first implementation explicitly builds all vertices and edges of \(C_{2r+1}^{\square d}\), applies simultaneous count-based colour refinement to the entire graph, compares every intermediate round with the predicted distance-layer partition, and checks terminal classes and sizes. It tested 20 graph configurations with 4,006 vertices in total.

The second implementation constructs the weighted transition graph on the weak compositions of \(d\) into \(r+1\) parts. It verifies the degree \(2d\), checks one downward edge per nonzero coordinate and the predecessor-moment reconstruction, and computes colour refinement on the quotient independently; it tested 56 configurations with a combined 2,898 quotient profiles. The two procedures use different adjacency representations.

All finite checks ended in `ALL_TESTS_PASS`. These are corroborating tests only; the universal result is proved by a symbolic induction in `RESULT.md`. No Lean, external certification, or independent audit is asserted. The verifier does not claim to search or verify scientific novelty.
