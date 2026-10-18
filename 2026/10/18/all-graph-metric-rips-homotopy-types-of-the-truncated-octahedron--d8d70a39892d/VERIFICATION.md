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

# Reproducibility

Execute `python3 verify_truncated_octahedron_rips.py`. Only the Python 3 standard library is used. The verifier constructs the exact integer-coordinate graph, checks the 24 vertices, 36 edges, degree three, graph diameter six, antipodal distances and complete distance distribution. It independently enumerates every Rips face at scales two through four, constructs deterministic staged vertex matchings, and topologically sorts every oriented codimension-one Hasse incidence to prove the matchings acyclic.

At scales two, three and four the enumerated nonempty face counts are 262, 1758 and 17372. The matchings comprise 126, 878 and 8681 pairs. Their critical-cell degree profiles are respectively `{0: 1, 2: 9}`, `{0: 1, 2: 1}`, and `{0: 1, 4: 6, 5: 3}`. The program evaluates the integral gradient-path signed Morse differential from the three critical five-cells to the six critical four-cells, checks its exact matrix and primitive rank-one image, and separately computes all mod-two simplicial boundary ranks for comparison. The program prints a final `VERIFY_OK` marker only after all assertions pass.

The threshold-five and threshold-six arguments are structural: at threshold five all forbidden pairs form precisely twelve antipodal pairs, while threshold six permits every simplex. Finite calculations exhaust the specified 24-vertex object; they are not being extrapolated to an infinite family. Field homology by itself would not justify the integral homotopy claim, which uses the signed critical-cell boundary and the attaching-map argument.
