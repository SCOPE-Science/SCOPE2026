---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Direct algebra gives the required difference D=-pq+3p+3q+3. For p at least 11, setting E=-D excludes two non-q divisors by size and two q-multiples modulo q; the only remaining mixed case gives incompatible lower and upper bounds. Thus p is 3,5,7, where the divisor sets are finite and yield exactly the eight values. A fresh independent prime sweep below 150 reproduced exactly those eight values and explicit witness pairs; the proof supplies the unbounded exclusion.

## originality

PASS

The primary 2024 2-near-perfect paper explicitly proposes changing the signs and singles out the mixed-sign relation as a future direction; the later two-prime classification again lists hybrid forms as future work and reports only computational exploration. Neither source classifies the squarefree three-prime slice 2pq. Resultary returned the audited record as the exact hit and no distinct prior theorem that implies the eight-value classification.

## value

PASS

The mixed-sign equation is explicitly proposed by the source literature, and 2pq is its first natural squarefree three-prime support slice. A complete infinite-family classification with an analytic large-prime obstruction is a motivated arithmetic result rather than an arbitrary finite search.

The dated certificate retains the supplied scientific assessment, sources and limitations.
