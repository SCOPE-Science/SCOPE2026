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

The mathematical argument in `RESULT.md` supplies the proof for arbitrary finite legal path profiles and all fixed minimum path lengths. The principal critical steps are the equal-path-sum characterization of graph gradients, the weighted averaging that computes the Hilbert projection, the explicit signed matrix coefficients, and a matching Cauchy–Schwarz upper bound and balanced-path lower bound.

Run `python3 verify_theta.py` with Python 3 and only the standard library. The script constructs independent exact incidence-based orthogonal projections, compares their matrices with the derived formula, compares induced maximum norms, checks symmetry and representative idempotence, and checks exact witnesses for eight minimum path lengths and 43 scaling parameters each. The recorded execution passed 21,580 exact-rational comparisons on 127 finite network profiles and 344 large scaling witnesses.

The script deliberately does not attempt exhaustive enumeration of arbitrary network sizes or prove the infinite asymptotic assertion computationally. Universal quantifiers and limiting statements rest on the explicit proof. Source comparisons show that the square-root construction and its growth order are not original, while the exact all-profile formula and the minimum-path-length hierarchy are the stated claims requiring any future independent scientific assessment.
