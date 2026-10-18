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

The standalone `verify.py` uses only Python's standard library and exact rational arithmetic. It exhaustively generates all uniform-attachment recursive trees through eight vertices, builds an independently derived scalar-leaf-count Markov distribution, and constructs the exact full two-tree leaf-count joint distributions for all integer parameters \(2\le t\le n\le16\). It checks means, variances, covariance identities, correlation where defined, strict positivity, independence through shared size three, upper-quadrant covariance inequalities for all thresholds, and large-parameter deterministic correlation scaling.

Execution from the packaged script: `python3 verify.py` — **PASS: 16932 exact assertions; recursive trees exhaustively listed to n=8; all bivariate leaf-count distributions checked through n=16**.

The induction, conditional independence, monotone coupling and martingale bracket proof are recorded in `RESULT.md`. Exhaustive finite tests are not proofs of infinite quantifiers or weak convergence. Neither independent scientific auditing nor independent historical-priority confirmation has been performed.
