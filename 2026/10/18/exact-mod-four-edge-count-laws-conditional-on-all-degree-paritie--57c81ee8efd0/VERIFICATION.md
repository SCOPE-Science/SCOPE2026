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

# Reproducible verification

Run `python3 verify.py` in the same directory as this document. No nonstandard Python packages, external data, or network are needed.

The checker separately evaluates the conditioned Gaussian-integer expectation from a Krawtchouk expansion and evaluates the parity-case closed forms for each even feasible Hamming weight through order twelve (45 comparisons). It also enumerates all labeled graphs on three through six vertices, reconstructs the full four-residue count distribution within each degree-parity fiber, and checks its transform, normalization, conditional edge-parity balance, and asserted uniformity (60 fiber comparisons covering 33,864 graphs).

Expected stdout: `OK: 105 independent exact analytic/finite-graph instances; n=3..12 analytic, n=3..6 exhaustive.`

All calculations are exact integers. The finite tests are consistency evidence, not exhaustive verification for arbitrary order. The universal proof is in `RESULT.md`, Steps 1–5. No independent audit or external proof certification has been performed.
