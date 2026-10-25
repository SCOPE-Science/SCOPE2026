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

# Verification of the forest-collision theorem

Run `python checker.py` with Python 3 (no third-party dependencies). The checked source file enumerates all set partitions for \(1\le n\le7\), compares \(75\) exact edge-collision histograms for path, star and matching forests against the finite Bell-transform formula, and checks one triangle boundary. The observed output was `FINITE_CHECKS_OK 75 forest histograms and triangle boundary`; `BELL_7 877 SPANNING_TREE_AVOIDANCE_7 203`.

The analytic claim is established by four independently inspectable arguments in `RESULT.md`: exact conditional forest factorization, a moderate-deviation inequality derived from successive box-count weights, Le Cam total-variation coupling to a moving Poisson parameter, and a relative-error decomposition in which the excluded tail is smaller than the minimal main term \(W(n)/n\). Explicit scope limits are fixed \(r\), all labelled simple forests with up to \(n-1\) edges, and uniform equivalence-relation sampling. No finite enumeration certifies the asymptotic or priority claim. Independent audit has not been performed.
