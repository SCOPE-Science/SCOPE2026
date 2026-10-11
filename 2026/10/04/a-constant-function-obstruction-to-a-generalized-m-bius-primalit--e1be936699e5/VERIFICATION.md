---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

For the admissible constant function f(m)=1, the recurrence becomes star_f(n)=1-n-sum_{d=2}^{n-1}star_f(d). The base case n=2 is -1, and if all earlier values are -1 then the sum is -(n-2), so star_f(n)=-1. Thus every n>=2, including composite n=4, has value -1. A fresh bounded replay through n=100 independently matched the induction; the infinite conclusion rests on the induction, not the finite check.

## originality

PASS

The current primary abstract still advertises the literal fixed-form equivalence star(p)=-1 iff p is prime. The constant-one specialization directly contradicts that formulation, and current Resultary search returned no earlier correction or same counterexample other than the assigned record. The source PDF route was unavailable in this audit, so a body-level clarification in a later version remains a residual risk, but inaccessible full text alone does not defeat best-of-knowledge originality when the current primary abstract itself retains the contradicted statement.

## value

PASS

An explicit all-n counterexample that exposes a quantifier error in a current published primality characterization is mathematically worthwhile even though the induction is elementary. It identifies the first composite failure and sharply separates the literal theorem from a potentially repairable universal-over-f statement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
