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

# Verification and reproducibility

Run `python3 verify.py` with Python 3.9 or newer. No third-party library is required.

The exact-arithmetic component represents elements of \(\mathbb Q(\sqrt3)\) as pairs of rational numbers. It verifies the proposed conductance budget, two eigenvalue factors, and the vanishing of the three-block characteristic polynomial at one. The finite matrix component diagonalizes all uniform-base graphs with \(2\le p,q\le16\), omitting the exceptional size, and the exceptional five-vertex Laplacian. It also checks the five-vertex embedding's seven edge distances and centered variance.

The program reports 224 nonexceptional full-spectrum cases and the exceptional case. The infinite classification does not follow from this enumeration; it follows from the unit-edge embedding bound and explicit constructions for every pair of positive integer part sizes in the stated ranges. Any further independent assessment remains unperformed.
