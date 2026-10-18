---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For fixed d>=6, d(mu_m±s_m)=d±sqrt(2d)+[2d±(d+6)sqrt(2d)/2]/m+O_d(m^-2). Conditioning on W=chi_m^2/m yields E H_d(tW)=H_d(t)+t^2 f_d'(t)/m+O_d(m^-2) using EW−1=0, E(W−1)^2=2/m and fourth-moment/tail control. In each moving endpoint the exact first coefficient b_±+(d/2−1)t_±−t_±^2/2=±2sqrt(2d). Subtraction gives 2sqrt(2d)[f_d(t_+)+f_d(t_-)]/m>0; t_->0 for d>=6. Consequently C_{d,m} exceeds the chi-square limit for all sufficiently large m, pointwise in d. Independently rederived both symbolic identities using SymPy (R1_F_ENDPOINT_IDENTITY_OK); finite F distribution regression in source is not used as infinite proof.

## originality

PASS

Sun–Hu–Sun prove all-m F/chi-square variation for d=1..4, and their section 5 discusses unresolved d>=5, rather than the fixed-d large-m first-order coefficient. The separately published d=5 result leaves fixed d>=6 open. A general CDF expansion could entail a derivative term, but no inspected result establishes the moving one-standard-deviation margin and positive endpoint sum; the result is a best-of-knowledge targeted gap rather than an assertion of absolute priority.

## value

PASS

The one-standard-deviation probability conjecture is a stated nontrivial distribution-comparison problem. A positive sign in the leading finite-m correction proves the previously untreated high-denominator tail for every fixed numerator degree >=6, not merely a numerical fit. Exact density endpoint coefficient quantifies the approach and could be used in future uniformity/monotonicity work. The result explicitly does not claim all finite m or a uniform d threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
