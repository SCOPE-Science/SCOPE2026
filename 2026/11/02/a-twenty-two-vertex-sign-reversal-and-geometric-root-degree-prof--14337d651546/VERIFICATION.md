---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Independently reconstructed parent-choice PGF recurrences for ρ_n, µ_n and A_n=Cov(D_n,B_n(z)), including conditional root-selection covariance. Coefficient extraction gives exact unary formula [n/4−(3/2)H_{n−2}−1/(2(n−1))]/(n−1). An independent parent-array enumeration verified finite cases through n=7, and exact rational boundary values are negative at 21 and positive at 22; F(n+1)−F(n)=(n²−7n+2)/(4n(n−1))>0 for n≥7 proves uniqueness. For fixed k, root PGF implies P(D_n=k)→0, µ_k/n→2^{-k-1}, and the Cesàro recurrence proves the covariance limit. No uniformity in k; finite-sum conservation makes the nonuniformity necessary.

## originality

PASS

Best-of-knowledge: exact 22-vertex unary sign threshold and all fixed-k root mixed covariance profile survive; k0 leaf identity acknowledged as known.

## value

PASS

Root branching and global outdegree counts are canonical recursive-tree observables. The unique n=22 sign reversal and geometric fixed-degree cross profile quantify a founder effect invisible in bulk profile CLTs and expose a meaningful nonuniformity constraint.

The dated certificate retains the supplied scientific assessment, sources and limitations.
