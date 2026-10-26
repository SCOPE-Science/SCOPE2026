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

The analytic derivation and quantified assumptions appear in `RESULT.md`. `verify.py` is a standalone Python standard-library reproducer; from this directory execute `python verify.py > recomputed_certificate.json`. With no third-party dependencies, this produces the exact rational vectors, strict leading-sum checks, extrema and mean-abundance comparisons, reciprocal-variance identity, and exhaustive classification of all six binary four-season assignments in four preselected parameter examples. The existing `certificate.json` is the output of that script, and can be compared byte-for-byte.

This finite verification does **not** establish infinite-parameter validity; that conclusion rests on the symbolic contraction and rational inequalities in `RESULT.md`. No code claim addresses stochastic models, empirical data, non-homogeneous growth, or schedules of larger period. Independent mathematical and bibliographic audits have not been performed.
