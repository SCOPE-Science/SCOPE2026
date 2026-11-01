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

# Reproducibility and verification limits

Run `python3 verify_prism.py` from the directory containing this file and the script. Python 3 standard library is sufficient. A successful execution prints `VERIFY_OK` and the maximizing half-height with sample probabilities.

The exact part checks all \(\binom63=20\) nonzero triple determinants, all \(2^6=64\) possible sign vectors, feasible pair-intersection rays, and the four symbolic angular-area formulas with multiplicities \(2,12,6,12\). It also checks the coefficient identity that their total spherical area is \(4\pi\). Since every determinant is a nonzero rational multiple of \(h\sqrt3\), this is an exhaustive proof certificate for the chamber combinatorics at **all** positive aspect ratios, not just at sampled values.

The numerical part uses deterministic Gaussian normals to sample 80,000 directions at each of five prescribed aspect ratios; 400,000 samples altogether. The checks are supplementary, not an exact proof of the limiting probabilities. Root finding provides a decimal approximation to the unique maximizer; strict uniqueness follows from the derivative sign argument in RESULT.md.

This check does not certify historical publication priority, does not inspect inaccessible whole papers, and is not independent mathematical validation.
