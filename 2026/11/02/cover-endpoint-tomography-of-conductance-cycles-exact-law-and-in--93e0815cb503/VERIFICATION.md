---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For target j, its complement is a path from j+1 to j-1. The event J=j is exactly visiting both endpoint neighbors before hitting j; condition on the first neighbor reached, then apply resistance-linear gambler’s ruin to reach the other neighbor before j. This establishes the two-term law with the correct denominator T_j+r_j or T_j+r_(j-1). For target i+1 and start i the formula reduces to q_i=r_i/(R-r_(i+1)); cyclic recurrence rho_i=q_i(1-rho_(i+1)) and Q=prod q_i<1 prove the signed-product inverse and uniqueness. Positivity and sum one are sufficient for realizability; subtract recurrences to prove sup-norm stability. Uniform q forces uniform rho. All n≥3, including triangle, and strictly positive boundary cases are covered. Independently constructed exact rational absorbing hitting-system calculations matched 204 instances, corroborative rather than a universal proof.

## originality

PASS

Weighted gambler’s ruin and homogeneous-cycle last-vertex laws are classical, explicitly credited. The closest same-observable Idnani–Salem 2026 source describes homogeneous symmetric, biased and time-varying walks in its accessible abstract, but full text is inaccessible; no claim of whole-document noncoverage is made. Directed/unweighted uniformity and graph heat-inverse theorems concern other data. No inspected published statement implies recovery of spatial conductance from n cover-endpoint scalars. Qualified best-of-knowledge PASS, not historical-priority certification.

## value

PASS

Recovering all relative unknown conductances from just one scalar endpoint statistic per starting vertex is a natural inverse problem; the exact feasible-data image, Lipschitz error bound and rigidity distinguish this result from mere elementary hitting-probability evaluation. The scale ambiguity is intrinsic and clearly delimited.

The dated certificate retains the supplied scientific assessment, sources and limitations.
