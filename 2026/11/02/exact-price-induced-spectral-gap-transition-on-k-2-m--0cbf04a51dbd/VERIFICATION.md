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

# Reproducibility and scope

Execute `python3 verify_two_hub_gap.py` using Python 3 with no third-party packages. The executed checker reported `PASS: 72390 exact identity, characteristic-polynomial and ratio-sweep checks` after the script was run from its package directory. The exact components use the `fractions` module; floating-point ratio sweeps are independent sanity checks and do not certify global numerical optimization.

The proof of the all-parameter claim is analytic: group averaging, a complete two-hub Laplacian spectral decomposition, necessary and sufficient unit-gap inequalities, and a strictly convex one-variable cost minimization. No step in that proof depends on finite enumeration. The package does not certify the absence of an equivalent historical theorem, does not classify asymmetric optimal allocations, and has no external independent audit.
