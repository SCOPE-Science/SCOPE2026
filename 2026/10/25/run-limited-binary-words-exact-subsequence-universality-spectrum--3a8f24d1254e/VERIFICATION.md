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

Greedy arch decomposition counts scattered subsequence-universality index. Tracking completed arches and current run length yields S_j=1+uzE+zS_(j+1), E=1+z(S_1+S_2). Solving gives F=1+2z A_R(1+uz)/(1−uz²(A_R+A_(R−1))); its coefficient polynomial has gapless support [2k,(R+1)k+R] and leading coefficient 2, proving all R,k and forcing thresholds. Independent direct target-subsequence exhaustive check of 5,235 admissible short binary strings plus exact support checks passed.

## originality

PASS

Known greedy arches, unrestricted binary universality enumerator and constrained run enumeration do not individually or jointly state the exact two-sided run-constrained bivariate index law; original mathematical synthesis is qualified by an unindexed joint-enumerator risk.

## value

PASS

The exact all-length all-cap index spectrum and two sharp forcing-boundary words connect natural homopolymer constraints with subsequence pattern completeness, a useful finite-language invariant beyond the known arch test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
