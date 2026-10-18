---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For p finite, reconstruction x=theta_tau(theta_f(S^{-1}x)) gives M subset Ran(theta_tau), and linearity gives span(M) subset Ran. Every coefficient vector is the l^p norm-limit of coordinate truncations; bounded synthesis carries it to the norm-limit of finite combinations of tau_n in M, so Ran subset closure(span M). Both sides yield closure(Ran)=closure(span M). Independently checked singleton M={u}, p=1, tau_n=u, f_1(u)=1, f_n(u)=0 for n>=2: bounded theta_tau(a)=(sum a_n)u, S(u)=u, proper one-dimensional range for dim X>1. No closed-range assertion follows.

## originality

PASS

The directly inspected arXiv 2211.10652 v1 and 2026 journal theorem assert full ambient surjectivity, which is contradicted by the qualifying singleton frame. No equivalent erratum or range sandwich was identified. This is a sharp correction, not a corollary of the printed (false) theorem; an unindexed correction remains a risk.

## value

PASS

A foundational frame definition admits proper M subsets; correctly separating algebraic span, synthesis range and closure prevents invalid surjectivity uses and gives the sharp general replacement. The tiny singleton example is chosen for decisive hypothesis diagnosis, not mere renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
