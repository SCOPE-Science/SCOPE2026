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

Run `python3 verify_gamma.py` from a directory containing `gamma_minor.json`. Python 3 standard library is sufficient; no software packages or downloaded datasets are required.

The procedure enumerates the four-label singular cubes in the relevant degrees, discards coordinate-degenerate cubes, checks Gamma hyperedge admissibility on every radius-one star, computes integral cubical faces and their signed boundaries, and confirms a mod-two rank-nine lower bound on the second boundary. It then regenerates the specified \(219\) boundary columns and calculates a determinant of absolute value one on \(219\) distinct rows by fraction-free exact elimination. Together with the homological upper rank bound, this establishes the integral vanishing of \(H_2^{\Gamma}\). The two-section and embedded-homology arguments in `RESULT.md` are symbolic proofs, independent of the enumeration.

This computation does not calculate higher Gamma homology or provide independent validation. No assumptions about uncomputed cases are made.
