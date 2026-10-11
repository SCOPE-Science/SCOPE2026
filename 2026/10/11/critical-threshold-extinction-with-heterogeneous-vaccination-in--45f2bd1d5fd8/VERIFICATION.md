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

# Proof and arithmetic verification

The all-dimensional statement is supported by the analytic argument in `RESULT.md`: the eigenvector cancellation; the exact Dini inequality for the positive-part correction; the invariant-set exclusion at a susceptible threshold crossing; the asymptotically forced stable susceptible equation; and the uniform small-data bound for Lyapunov stability.

The accompanying `check_threshold.py` uses only the Python standard library `fractions.Fraction`. Running `python3 check_threshold.py` reproduces the two-group critical next-generation matrix, checks the Perron identities, computes the exact infection derivative and the two positive-part derivative branches, and prints `CHECK_OK`. This isolated finite arithmetic test is neither an exhaustive exploration nor an independent mathematical certification.

The first public source date is the dated first arXiv submission (2022-02-07), not the 2023 journal publication or subsequent arXiv revision. Source and novelty comparisons, including the inaccessible potential comparator, are described in `REVIEW.md` and `AUDIT.json`.

Limits: no numerical test proves the continuum of parameter choices or all group counts. Independent external validation remains not performed.
