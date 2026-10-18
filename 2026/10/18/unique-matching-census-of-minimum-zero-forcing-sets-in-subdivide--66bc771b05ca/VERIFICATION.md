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

Run `python3 hybrid_forcing_verify.py` with Python 3 and no dependencies. The verifier generates the graph from its definition; independently executes standard zero forcing; enumerates all vertex subsets of the candidate minimum size for \(m=3,4,5,6,7\); tests the unique-perfect-matching criterion; sums the cyclic-run formula; and multiplies the claimed rational generating function as formal series up to order \(15\).

The run examines 379663 subsets in the complete minimum-cardinality layers and recovers counts 24, 76, 225, 649 and 1848 for those five graph orders. It also checks the count formula and generating-function coefficients for \(3\le m\le15\). The rank-nullity proof independently excludes smaller forcing sets for every \(m\), so brute force below the minimum is not needed for the theorem. A finite computer test does not establish the all-parameter classification, which is proved structurally in RESULT.md.

Expected stdout is stored in `hybrid_forcing_verify_output.txt`.
