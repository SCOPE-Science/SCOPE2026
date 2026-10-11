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

For three distinct selected columns, division by the first column reduces the determinant to \(-(u-1)(v-1)(S_m(u)-S_m(v))\). If the common value of \(S_m(u)\) and \(S_m(v)\) is zero, three distinct common \(N\)-th and \(m\)-th roots force \(\gcd(N,m)\ge3\). If it is nonzero, unit-circle conjugation gives \(u^{m-1}=v^{m-1}=a\); the geometric-sum formula then yields \((1-a)(u-v)=0\), so \(a=1\) and \(\gcd(N,m-1)\ge3\). The converse subgroup witnesses are immediate. For a three-element row set, divisor-uniformity at every divisor \(d\ge3\) is exactly pairwise distinctness modulo \(d\), equivalent to the two gcd conditions. Independent exact regression reproduced the divisor-uniformity equivalence for all 44,551 pairs with \(3\le N\le300\).

## originality

PASS

The foundational full-spark paper supplies divisor-uniformity as a necessary condition in general and an iff criterion only at prime-power order. The complete Achanta et al. conference paper treats arithmetic-progression row sets and row sets obtained by deleting one row from a consecutive block; it explicitly says its general deleted-row results do not give a necessary-and-sufficient condition for all parameters. Except for small boundary cases, \(\{0,1,m\}\) is neither family. Targeted Resultary and web searches located related three-point uncertainty and prime-square-minor results, but those cover different quantifiers or only special orders and do not imply the submitted all-\(N,m\) criterion.

## value

PASS

The result gives a sharp, constant-time arithmetic test for a natural infinite family of nonconsecutive Fourier sampling patterns and identifies a family in which the standard divisor-uniformity necessary condition is sufficient at every composite order. That is a structural classification rather than a finite parameter check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
