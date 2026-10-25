---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

Reconstructed exact CDF (1-q^(k+1))^n and p_k differences, n=1 geometric compound-Poisson intensities q^k/k, and n=2 exact G2(z)=(1-q)^2(1+qz)/((1-qz)(1-q^2z)). Its log expansion gives nonnegative summable jump rates [q^(2k)+(1+(-1)^(k-1))q^k]/k. For n>=3, coefficient z^2 of log G_n is -D_n/2 where D_n=(1+q)^(2n)+1-2(1+q+q^2)^n; verified D3=q^2(3+6q+3q^2-q^4)>0 and D_{n+1}=(1+q)^2 D_n+2q(1+q+q^2)^n-(2q+q^2)>0. For a nonnegative integer law with p0>0 any real iid convolution root is nonnegative integer supported, so for large convolution order its second pgf coefficient would be negative, impossible. Additional independent exact rational q,n checks corroborate algebra, not the real-q theorem.

## originality

PASS

DGEII/discrete generalized exponential II and exponentiated geometric are aliases for this same maximum law at integer resilience: they were explicitly checked. The 2016 broader EGG paper presents a non-ID example in different noninteger parameters; the 2023 order-statistic theorem proves log-concavity, not additive infinite divisibility; max-geometric divisibility is a different convolution. No inspected result implies iff n<=2 with explicit n=2 Lévy rates. Original 2013 and 2015 primary full texts inaccessible and remain substantial priority risks; best-of-knowledge PASS, not proof of universal novelty.

## value

PASS

The result gives a complete all-q threshold separating additive infinite divisibility and obstruction for naturally defined order statistics, and an explicit rare n=2 compound-Poisson law. Unlike mere distribution formulas or log-concavity preservation, it determines whether these maxima embed as arbitrary iid convolution sums.

The dated certificate retains the supplied scientific assessment, sources and limitations.
