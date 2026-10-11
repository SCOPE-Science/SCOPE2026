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

# Reproducibility and evidence

Run `python3 verify_morse.py` and `python3 verify_independent.py` with standard Python 3. Both commands completed with all assertions passing. The programs are standalone and reconstruct every datum; neither program reads cached output or external datasets.

The first program recomputes 24 vertices, 36 edges, 26,440 nonempty simplices, 13,211 discrete-Morse pairs, one critical 0-cell, five critical 5-cells and twelve critical 6-cells. It constructs all 143,760 oriented Hasse incidences and confirms that the topological sort visits all 26,440 simplices. The signed integral 5-by-12 Morse boundary is recalculated, with its only nonzero rows identical and containing -1, -1 and +1 in columns 5, 6 and 9 (1-based). Consequently the Smith form has one unit invariant factor and the integral CW cancellation is valid.

The second program uses Euclidean coordinates in the quadratic integer ring to reconstruct all 36 edges, separately enumerates the 26,440 nonempty simplices, and computes simplicial boundary ranks over \(\mathbb F_2\). It finds reduced Betti ranks 4 in dimension 5 and 11 in dimension 6, with zero in all other degrees. This confirms the field-homology consequences but cannot by itself establish the integral homotopy result; that relies on the first program's signed Morse matrix and the homotopy-theoretic attaching-map argument.

The resulting theorem is restricted to the ordinary independence complex of the truncated-cube graph. Literature searches cannot exclude every unindexed equivalent computation. Independent scientific review has not been performed.
