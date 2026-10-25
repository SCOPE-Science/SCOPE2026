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
# Verification notes

The full proof is in `RESULT.md`. The critical checks are (1) the weighted root-mean-square inequality, (2) equality on a Borel cross-section for a finite-period component, (3) countable positive-measure cylinders separating finitely many orbit translates, (4) strict nonattainment through pairwise-disjoint positive-measure shifts, and (5) two-sided estimates on the \(\ell^1\)-to-\(\ell^2\) defect.

The numerical script `verify.py` reproduces cyclic examples and sampled finite-dimensional inequalities. Finite samples do not certify the universal mathematical statements; the analytical proof is the verification of the general result.

Independent audit: not performed.
