---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility

Execute `python3 pentagon_verify.py`. It needs no third-party libraries. The program exhausts 125 labeled trees and all 16 signed tight-edge assignments per tree, producing 310 distinct affine potentials partitioned by their exact feasible parameter intervals. It verifies the 70 interior vertices, all five signed dihedral orbit sizes, both 30-vertex endpoint lists and their squared-normal histograms, and the absence of interior collisions. It uses polynomial integer arithmetic for the contacting-normal determinant and exact rational arithmetic in \(\mathbb Q(\sqrt5)\) for the Fourier projection, projected orbit count and strict bounding inequalities.

The success marker is `ALL EXACT CHECKS PASSED`. Numerical optimization and sampled parameters play no role in the asserted infinite-parametric conclusions. The center locus and golden-ratio transition follow from the exact analytic inequalities in `RESULT.md` combined with this exhaustive finite certificate. No formal proof-assistant verification is asserted.
