---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For real r>0 and N>=1, increment Δ_N=a_r(N)-a_r(N-1)=P_{r,N}(1-int_0^1 R_{r,N}(t)dt), with P=Gamma(N+r+1)/(Gamma(r)Gamma(N+1)) r^r N^N/(N+r)^(N+r+1), R=(1+t/N)^N/(1+t/(N+r))^(N+r+1). Beta integral and source Lemma 2.2 yield identity. Ratio P_{N+1}/P_N=(1+1/N)^N((N+r)/(N+r+1))^(N+r+1)<1. R(t) in (0,1) and strictly increases in N because x log(1+t/x) has strictly negative second derivative and the additional logarithm derivative is positive. Thus positive H=1-int R strictly decreases, and Δ_{N+1}<Δ_N. This establishes strict ordinary discrete concavity for every integer n>=0, without extending to arbitrary cutoff or continuous index.

## originality

PASS

Guo–Tao–Hu establish Δ_N>0 via the same integral and a monotonicity lemma, but not Δ_{N+1}<Δ_N. Finner–Roters and Karp results for log-concavity in beta/F parameters usually fix the CDF argument, unlike moving cutoff r/(n+r+1); log-concavity is not equivalent to ordinary concavity. No direct covering Resultary record found.

## value

PASS

Diminishing increment is a meaningful strengthening of the exact sequence governing Chvátal-inspired negative-binomial mean-tail lower bounds; curvature is useful for interpolation and finite truncation estimates and is not forced merely by positivity of increments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
