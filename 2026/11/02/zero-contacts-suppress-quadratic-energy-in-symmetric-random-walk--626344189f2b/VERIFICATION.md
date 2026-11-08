---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For balanced simple symmetric walk bridges S0=S2n=0 with n>=2, R=sum over interior even-time zeroes and Q=sum over t=1..2n-1 S_t². Exchangeable balanced signs give E S_t²=t(2n-t)/(2n-1) and EQ=n(2n+1)/3. Conditioning on any prescribed q≥1 interior zeroes decomposes into independent bridges, each length 2ell_j with energy ell_j(2ell_j+1)/3, yielding deficit (4/3) sum_{i<j}ell_i ell_j. One-contact probability c_k c_{n-k}/c_n, and [z^n](zB’(z))² for B=(1−4z)^(-1/2) yields Cov(R,Q)=−n(n−1)b_n/6, b_n=4^n/c_n. Three-segment renewal GF gives ER=b_n−2 and VarR=4n+2−b_n−b_n². Balanced signs m2=−1/(2n−1), m4=3/((2n−1)(2n−3)), and edge-weight equal/incident/disjoint sums give VarQ=8n²(n−1)(2n+1)/45. Stirling then gives limiting corr −sqrt(5pi)/(8sqrt(4−pi)). Independently enumerated all bridges n=2..7 and exact covariance; read original checker which enumerates to n=9, but bound not used as infinite proof.

## originality

PASS

Direct statement-level primary comparisons and Resultary semantic searches support best-of-knowledge originality: Knight 2000 full paper not completely read; its observable is integral |B(t)| rather than integral B(t)² and discrete energy, but indirect integral-transform consequences cannot be excluded. Other joint Brownian local-time/quadratic functional papers may have equivalent limit; exact finite-n bridge joint formulas appear not covered by accessible sources.

## value

PASS

A full exact joint-moment and conditional pinning-deficit theorem for a canonical discrete bridge observable. The negative covariance has an exact size-dependent coefficient and nonzero universal correlation limit; useful for random-walk contacts versus squared-height energy, not just known Rayleigh marginal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
