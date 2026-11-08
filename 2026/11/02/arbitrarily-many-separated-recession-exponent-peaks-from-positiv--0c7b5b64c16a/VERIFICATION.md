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

Log amplitudes L_j(t)=E_j logR-2^j t meet adjacently at T_i=(n-i)logR, separated by logR. Around T_i, scaled v=2^{i-1}(t-T_i), ratio of neighboring terms is s=e^{-v}; all nonadjacent components and their first two derivatives are O_n(R^-1) compared to dominant pair uniformly on compact v. For adjacent rates λ and 2λ, β=B(v)=(1+s)(1+4s)/(1+2s)²=1+s/(1+2s)², whose unique nondegenerate maximum is 9/8 at s=1/2, v=log2. C² convergence plus negative curvature yields nearby unique strict peak with claimed timing and height O_n(R^-1). Fixed separated transition times yield separate peak windows; midpoint between adjacent transition times is dominated by a single term, hence β→1. Independent exact rational n=3 R=100 verified two disjoint strict three-time peak brackets. The asymptotic theorem uses fixed n and R→∞, not simulation or any uniform-in-n bound.

## originality

PASS

Published heterogeneous linear-reservoir literature establishes apparent nonlinear recession slopes from positive linear drainage, and Gao 2017 treats two parallel reservoirs; Roques 2022 studies two-component recession exponents (including a two-rate peak), not arbitrary all-n hierarchy with n-1 separated equal-height peaks and troughs in the inspected text. The contribution is the explicit many-component asymptotic constructive pattern.

## value

PASS

Distinguishes qualitative nonlinear-looking hydrological recession profiles from actually nonlinear component dynamics by showing arbitrarily many pronounced, well-separated exponent peaks from strictly linear positive reservoirs. The fixed-n construction and universal 9/8 two-rate envelope are natural motivated exact stress-test facts, not an empirical prevalence claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
