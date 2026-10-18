---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Reconstructed per-index V_i: fixed η(i) contributes Cov(F,V_i)=(n−f)/[n(n−1)]; moved η(i) contributes 2f/[n(n−1)(n−2)], using Σ_b |{i,η(i)} ∩ {b,η(b)}|=4. Sum over f fixed and n−f moved indices gives f(n−f)/[(n−1)(n−2)]. Independent complete enumeration for every η,Π∈S_n for n=3,4,5 matches rational covariance. Boundary f=0/ n gives zero; n−1 is impossible, and n=2 excluded. F=n implies Π=id and Cη=n; for η fixed-point-free nonidentity Cη variable hence uncorrelated not independent. Full proof is counting, not finite extrapolation.

## originality

PASS

Direct Section6 primary paper compares exactly Cη and known marginal mean, and independent conditioning adds novel mixed moment with F(Π); known marginal moment theorems do not automatically determine cross covariance.

## value

PASS

Exact support-only universality of a joint random-permutation statistic and uncorrelated-yet-dependent boundary provide reusable structural information beyond known marginal commutator moments; natural mixed invariant of same random permutation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
