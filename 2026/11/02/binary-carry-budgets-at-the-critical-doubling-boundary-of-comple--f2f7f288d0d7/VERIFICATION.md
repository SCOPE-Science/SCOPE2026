---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For positive strictly increasing sequence S with exact doubling after N and b_n=floor(alpha s_n), verified Brown complete-subset-sum criterion b_j<=1+sum_{i<j}b_i, including duplicate indexed summands and zero values. Put H_j=1+sum_{i<j}b_i-b_j. For n>=N, floor(2 alpha s_n)=2 floor(alpha s_n)+epsilon_n with epsilon_n the successive binary digits of frac(alpha s_N), giving H_{N+r}=H_N-sum_{j<r}epsilon_{N+j}. Nonnegative deficits for all indices thus require and suffice for dyadic fractional part with popcount<=H_N, plus finite prefix inequalities. Upper bound on H_N for alpha in [0,B] gives O((log 1/delta)^K) dyadic covers and zero local upper box dimension. For S^(m)=(2,..,2m,4m,..) and alpha in [1/2,1/2+1/(8m)), checked prefix floor k/2, H_N=(m-1)^2, first two fractional digits zero, and exact count sum_{j<=min((m-1)^2,L-2)} C(L-2,j), asymptotic L^{(m-1)^2}/((m-1)^2)!. Pure geometric s_n=m 2^{n-1} case is alpha=1/(m2^j). Independently tested exact dyadic and Brown examples; finite tests not used to prove infinite classification.

## originality

PASS

No inspected current-priority source states or unambiguously implies the precise new theorem; methods and covered neighbors are credited explicitly, and residual inaccessibility/overlap risks remain. Best-of-knowledge originality, not world-priority certification.

## value

PASS

Addresses the meaningful critical base-two boundary where a finite prefix slack exactly budgets all future binary carries; establishes full scale classification, countability/zero dimension, and explicit families with arbitrarily high polynomial degrees in binary resolution. The quantified finite-prefix complexity distinguishes it from routine base-two geometric completeness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
