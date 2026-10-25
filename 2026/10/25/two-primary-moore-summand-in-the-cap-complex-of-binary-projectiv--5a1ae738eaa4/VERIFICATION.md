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

# Exact verification procedure

Run `python3 verify_pg32.py` with Python 3.9 or newer. No third-party modules or downloaded data are required. The verifier enumerates every nonempty subset of the fifteen nonzero binary four-vectors, reconstructs all 35 forbidden line triples and 3,048 faces, builds an acyclic matching and checks every oriented incidence in the face poset. It then computes the exact signed Morse boundary coefficients and their integer gcd. The residual CW complex has one vertex, one three-cell, and 78 four-cells, with attaching-degree ideal \(2\mathbb Z\); the resulting homotopy type is \(M(\mathbb Z/2\mathbb Z,3)\vee\bigvee^{77}S^4\).

The separate direct simplicial boundary-rank calculations over \(\mathbb F_2\) and \(\mathbb F_3\) provide consistency checks, but are not substituted for the integral degree calculation. The complete expected stdout is included as `verification_output.txt`. Every size or count in the proof is finite and exhaustively checked; no extrapolation to other projective spaces is asserted.

Limitations: Computational verification is replayable but has not received independent scientific audit. Source-search coverage is not a guarantee of priority.
