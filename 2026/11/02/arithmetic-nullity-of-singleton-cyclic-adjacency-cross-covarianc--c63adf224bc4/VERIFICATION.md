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

# Analytic and finite verification

The proof in RESULT.md covers all integers \(n\ge3\) and \(1\le d<n\); neither \(n\) nor \(d\) is bounded in the mathematical argument. It separately checks the two overlap cases, the rank-one constant mode, Bell log-convexity, a published normalized Bell ratio bound, the full Fourier spectrum and the modular arithmetic for zero modes. The all-order Bell inequality is a published premise, not a conclusion inferred from the finite experiment.

The adjacent standalone `check.py` uses only the Python 3 standard library. It exhaustively iterates all set partitions via restricted-growth words for each \(3\le n\le9\), compares all one- and two-indicator counts with Bell-number contractions, calculates rational ranks for every displacement and checks the aggregate covariance sign. It separately checks the Bell ratio inequalities for \(3\le n\le99\). Execution of the actual package checker reported `PASS: 4358 exact assertions`, with the \(n=6\) ranks `5,6,3` for displacements \(1,2,3\).

Finite testing cannot establish a general identity or an impossibility statement. The result makes no claim about independence, higher moments, noncrossing or weighted partitions, and has not undergone independent audit.
