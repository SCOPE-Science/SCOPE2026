---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Rebuilt the independent smallest-letter insertion process: B_j are independent Bernoulli(1/j) indicators of a new initial record, and D_j=D_{j-1}+(1-B_j)1{U_j>D_{j-1}/(j-1)}. Conditioning the B-vector on its total admits a coordinatewise monotone coupling by induction and Newton log-concavity; the update is antitone in B and monotone in integer D, proving every tail inequality. Strictness follows from positive probability of the final B_n changing and a positive last descent increment. Independent covariance recursion gives C_j=(1-1/j)C_{j-1}-1/(2j), hence the asserted value. Independent exact joint recurrence and tail checks through n=9, direct permutation enumeration through n=7 corroborate but do not prove the infinite statement.

## originality

PASS

Classical bivariate Eulerian–Stirling enumerators give exact joint distributions but their inspected main theorems do not state the all-r conditional stochastic order or a monotone Bernoulli coupling; an implication from older total-positivity theory remains a real priority risk.

## value

PASS

A complete stochastic regression order between two fundamental permutation statistics is materially stronger than a single negative covariance, applies to every increasing function of total descent count, and has an explicit explanatory coupling; it is a natural all-n structural dependence theorem, not a restated joint enumerator.

The dated certificate retains the supplied scientific assessment, sources and limitations.
