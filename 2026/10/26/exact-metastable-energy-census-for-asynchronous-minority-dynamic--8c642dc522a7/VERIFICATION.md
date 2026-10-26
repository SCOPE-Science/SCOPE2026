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

# Reproducibility and verification

Run `python3 verify_prism.py` using the Python standard library. It exhaustively checks every labelled configuration of circular prisms of lengths 3 through 9, computes the full distribution by number of monochromatic undirected edges under the closed-neighborhood minority rule, and asserts equality coefficient-by-coefficient with the analytic polynomial. `verified_output.txt` records the actual complete output and the final assertion message. The uniform-in-size result and quadratic expected absorption bound rely on the self-contained mathematical argument in RESULT.md, not on finite enumeration. No claim is made about basin probabilities, exact expected absorption time, external verification, or publication novelty beyond the documented literature comparison.
