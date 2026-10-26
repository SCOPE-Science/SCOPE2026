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

# Exact verification

Execute `python3 verify.py` with Python 3.9 or later; no third-party modules are required. The checked marker is `VERIFICATION_OK`. The program counts all acyclic subsets independently via union-find for \(2\le n\le6\), checking the total, one marked edge, and all three marked-pair counts. It checks coefficient identities by integer polynomial arithmetic and evaluates all covariance formulas and their strict negativity for \(2\le n\le2000\), giving 8,059 counted assertions/comparisons.

The proof for arbitrary \(n\) uses the three-state completion recurrence and exact polynomial factorization in RESULT.md, not finite enumeration. Counts from enumeration alone would not establish the unrestricted theorem. Publication priority has not been independently audited.
