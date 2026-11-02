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

# Verification

Reproduce the finite checks from the package with `python check_minors.py` (Python 3, standard library only). The code constructs two-atom generalized Hilbert entries as exact fractions, confirms negative order-two principal minors at several rational support points, verifies positive finite Gram determinants at the midpoint, and compares logarithmic rates against the proved value.

The finite checks are **not** the proof of the universal measure claim. The mathematical proof uses a uniform Schur bound, compact-support Laplace principle, binomial entropy maximization and Stirling's formula; its hypotheses include nonzero positive reflection-symmetric measures with compact support strictly inside `(0,1)` and no midpoint. No certification of general positivity when the midpoint is in the support is given. No independent audit has been performed.
