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

# Exact finite checks and limits

Execute `python3 verify.py` using Python 3 and its standard library. `verification_output.json` is the exact compact JSON output from the stored executable run. The verifier constructs the Fano matroid directly from the seven XOR triples; constructs the non-Fano relaxation from the single restored line; enumerates every clique and each Hasse incidence; constructs and verifies acyclic Forman matchings by complete topological sorting. It checks the combinatorial rank-three, corank-four rook link at the newly relaxed basis.

Observed Fano values: 28 bases, f-vector [28,126,140,28], 322 nonempty faces, 784 Hasse incidences, 154 matching pairs, 1 critical vertex and 13 critical triangles. Observed non-Fano values: 29 bases, f-vector [29,138,170,44,3], 384 faces, 977 incidences, 182 matching pairs, 1 critical vertex and 19 critical triangles. The checker exhaustively verifies the incidence digraph is acyclic, so the Morse theorem supplies the integral sphere-bouquet homotopy classifications.

The generic relaxation theorem uses a separately written combinatorial/topological proof, not the finite check as an empirical extrapolation. No historical full-text audit of every published basis-graph paper, independent scientific review, or general computational census is claimed.
