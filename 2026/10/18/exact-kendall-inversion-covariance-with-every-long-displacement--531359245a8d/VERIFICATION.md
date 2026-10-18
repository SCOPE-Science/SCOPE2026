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

# Reproducibility and proof limits

Run `python3 check.py` from the extracted package directory with a standard Python 3 installation. The verifier enumerates the 46,232 permutations in orders two through eight and compares each covariance with an independently computed rational expectation. It additionally checks the first-difference and maximum laws through order 500. A completed run reported `PASS: 124865 exact checks; 46232 exhaustively enumerated permutations; n up to 500 for peak/difference identities.` The exact proof for all orders is the finite-sum conditional expectation argument in RESULT.md, not a computational extrapolation.

The primary literature searches inspected HTML for the exact threshold-specific result and stronger coverage. Complete historical uniqueness and any external independent audit remain unestablished. No computational timeout is interpreted as a proof.
