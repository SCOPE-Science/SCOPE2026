---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

For multiplicities m_j, removing required copies yields P(m_{j_i}>=r_i all)=p(n-s)/p(n) exactly. Hardy–Ramanujan ratios with r_i~x_i sqrt(n) give independent rate-c j exponential limits. The uniform bound p(n-s)/p(n)<=C exp(-delta s/sqrt(n)), obtained by splitting s<=n/2 from s>n/2, yields uniform L1 control <=C/[delta(J+1)] for the weighted tail. This justifies convergence of the infinite numerator; Erdos–Lehner gives L_n/(sqrt(n)log n)->1/(2c), so Slutsky yields Z. Telescoping 1/[j(j+1)], square-sum 2zeta(2)-3, and gamma ratios give all constants. Independently checked 432 exact joint-tail identities for n=1..16 and the three smallest part sizes, and numerical Gamma/product comparisons at four t values. These finite checks do not prove classical partition inputs or the weak limit.

## originality

PASS

Dawsey–Russell–Urban 2022 introduce exactly these normalized polynomial integrals, prove density, and discuss fixed-length average monotonicity. They do not establish the random fixed-size, logarithmically rescaled integral weak limit in the inspected full-text sections. Hardy–Ramanujan, Erdős–Lehner, and Fristedt multiplicity laws are credited, not repackaged as discoveries; their combination requires an explicit uniform weighted-tail bound and normalization.

## value

PASS

A natural statistic specifically introduced in the partition-polynomial literature has a previously uncomputed nondegenerate limit law, explicit infinite exponential-series and Gamma transform, and sharp decay scale. This provides a meaningful probability distribution theorem independent of the unrelated fixed-length average conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
