---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Swapping the consecutive values j,j+1 flips D_j and preserves the window pattern whenever at most one is in the window. Otherwise their window ranks are consecutive and the two binomial factors count exactly the sets realizing those ranks; conditional ordering contributes 1/k!. This proves the signs, normalization and window-start invariance, including k=n and j=1,n-1. The first k-1 columns of the kernel are triangular with positive diagonal, and the identity signature and its single adjacent-value reversals span the signature space. Every signature occurs (orient the chain on ranks and take a linear extension). The binomial leading terms give the Bernstein scaling; the two three-letter peak signatures are opposite. The scope's caveat on independence must be read as concerning the full vector: the peak indicator and each single D_j are in fact independent because both are Bernoulli, whereas the all-zero D vector forces the identity and hence no peak.

## originality

PASS

The inspected matches cover two-sided aggregate descent or peak statistics, or organize local covariances with different partner statistics. None establishes the all-k fixed-window, fixed-value covariance factorization and signature classification. The judgment is for that structural statement, not the general idea of two-sided statistics or the adjacent-transposition argument.

## value

PASS

The mixed covariance matrix couples two naturally different coordinates, local positional order and adjacent numerical labels. Its exact rank and its equivalence classes give information not supplied by aggregate correlations: they identify every pattern contrast that disappears from these measurements, and show that moving the window cannot change those measurements. The finite boundaries and the explicit scaling are useful for treating fixed pattern length across n.

The dated certificate retains the supplied scientific assessment, sources and limitations.
