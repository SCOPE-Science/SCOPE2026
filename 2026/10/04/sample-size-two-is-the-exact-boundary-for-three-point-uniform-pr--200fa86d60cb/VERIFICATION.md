---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The exact event partition gives the displayed means, variance and covariance. Differentiating at s=1/3 reduces the sign to -D_k with k=n-1. D_2=6 and D_3=248/9; for k>=4 the leading difference E_k=4(8/3)^k-9*2^k exceeds 27 at k=4 and satisfies E_{k+1}>2E_k, while every remaining term in D_k is positive. Hence rho_n'(1/3)<0 for every n>=3. Exact-rational finite enumeration checks the moment identities but is not the infinite proof.

## originality

PASS

Originality passes. Papadatos and the prior Resultary finding establish the sample-size-two uniform extremality baseline. The audited derivative formula proves the opposite local behavior simultaneously for every n at least three; targeted Resultary search found no prior all-n obstruction.

## value

PASS

This gives the exact first sample-size boundary for a published probability-vector extremality direction on the smallest nontrivial lattice: uniform is uniquely optimal for two observations but already has a strict escape direction for every larger sample size.

The dated certificate retains the supplied scientific assessment, sources and limitations.
