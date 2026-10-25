---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

Condition on specified k spacings exceeding x; normalized shifted vector is Dirichlet(1)^n and event probability (1−kx)_+^{n−1}. Expanding quadratic score using EΣT_i²=2/(n+1), inclusion–exclusion yields full displayed mixed tail law, including boundaries 0≤x≤1; conditional formula restricted x>1/n. Integrating three beta terms and alternating binomial/harmonic identities gives Cov(M,G)=[H_n²+H_n^(2)−2H_n]/[n(n+1)(n+2)] >0 via harmonic recurrence. Independent rational beta/harmonic sums for n=2..39 agree. Dirichlet fourth moments and maximal spacing variance yield Corr~√6/(2π)(log n)²/√n; zero asymptotic correlation does not imply independence.

## originality

PASS

Shtembari/Caldwell full ordered-spacings text yields maximum-gap marginal laws, while Greenwood quadratic-score tests are known separately. Neither alone determines the threshold-dependent mixed tail expectation or harmonic positive covariance. Resultary searches for Dirichlet maximum/Greenwood co-moment found no clear covering claim; an earlier general Dirichlet ordered-statistic mixed theorem may exist. Best-of-knowledge PASS.

## value

PASS

Largest gap and Greenwood's sum of squared gaps are standard goodness-of-fit spacing scores. Full mixed tail moment and sharp positive-to-asymptotically-zero correlation describe concrete joint behavior needed when using both scores, not an arbitrary moment or one-off table entry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
