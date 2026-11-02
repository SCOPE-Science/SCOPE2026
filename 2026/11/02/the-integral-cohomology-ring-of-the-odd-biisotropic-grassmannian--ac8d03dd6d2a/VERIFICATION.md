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

# Verification record

The universal proof is contained in `RESULT.md`. It uses the Schubert–Pieri pairing for a smooth codimension-two linear section, integral weak Lefschetz, a weighted homogeneous regular-sequence argument valid after base change to every field, a primitive top integral class, and unimodularity of Poincaré pairings. These are mathematical deductions, not numerical extrapolations.

The standalone standard-library script `verify.py` can be run by `python3 verify.py`. It checks polynomial identities, Schubert pairings, middle integral intersection determinants and Hilbert-series ranks for every integer \(2\le n\le12\). Actual run result: `VERIFY_OK`.

The diagnostic script does not enumerate or certify all integers. The all-integers claim depends on the full proof and the motivating paper's additive cohomology theorem. Independent mathematical validation has not been performed; prior-work priority remains subject to the literature risk documented in `REVIEW.md`.
