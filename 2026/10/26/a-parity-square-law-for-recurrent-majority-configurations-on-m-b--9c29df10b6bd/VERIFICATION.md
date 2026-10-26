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

# Reproducibility and proof boundaries

Run `python mobius_majority_verify.py` with Python 3 and the NumPy, NetworkX and SymPy libraries. The script checks all \(256\) transfer states and their allowed arrows, identifies the recurrent strong components and row-swap action, proves the four stated characteristic-polynomial identities by exact symbolic determinant calculations, and checks the resulting traces against the closed expressions for widths \(1\) through \(24\). The characteristic polynomial identities themselves prove the expression for all widths, not only the tested values.

A separate direct vertexwise application of the majority rule exhaustively enumerates each binary configuration for width \(3\) through \(11\). The output in `mobius_majority_verify.log` records each observed fixed-state count, period-dividing-two count, and number of primitive two-cycles. No certificate is claimed for general graphs, arbitrary local rules, attraction basins, or independent review.
