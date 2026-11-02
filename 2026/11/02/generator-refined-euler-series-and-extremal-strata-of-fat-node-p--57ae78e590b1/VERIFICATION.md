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

Run `python3 verify.py` with Python 3, without external libraries. The program calculates restricted Young diagrams of sizes at most 38 for all 30 pairs of positive parameters up to 5 and 6, obtains their exact quotient-ring generator numbers, and independently expands the claimed rational product expression. It also checks the extremal product and branch symmetry for every parameter pair. Expected output begins with `VERIFY_OK:` and records 4,679 nonzero bivariate coefficients, as well as the leading three extremal coefficients for the (3,6) node.

The proof for all parameters uses torus-localization of Euler characteristic, the complete combinatorial partition identity and a general exact sequence for the generator bound. Neither the computer experiment nor this verification document claims independent proof certification. No independent audit has been performed.
