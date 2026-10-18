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

The publisher source actually prints psi=u*g(psi) and P(X=0)=psi(0)=g(0). Evaluating u=0 forces psi(0)=0; Lagrange inversion gives p_n=1/n [z^(n-1)]g(z)^n for n>=1. g is a nondegenerate offspring PGF with mean m=(1-c)*gamma*theta/(1-theta). The sum of p_n is the smallest fixed point q=g(q), hence one for m<=1 and q<1 for m>1; the latter has missing mass at infinity and a conditioned finite-progeny law p_n/q. At paper simulation gamma=1.5, theta=.4, c=.3, m=.7 and g(0)=.625330601..., so adding the asserted zero mass yields 1.625330601..., whereas positive coefficients already have total one. This does not determine the simulations implementation.

## originality

PASS

A general Lagrange/branching identity is of course classical, and the simple psi(0)=0 step is not claimed as a newly discovered universal theorem. The specific published RPSL model asserts a mutually inconsistent zero atom and normality in its own Theorem 1/Section 2, and this audit did not find an earlier RPSL-specific published correction. The model-specific inconsistency and sharp normalization phase are the novel corrective findings, without relabeling classical inversion as novel.

## value

PASS

Although evaluating u=0 is elementary, it detects a consequential error in a currently published count-data model: support, total mass, zero inflation, finite-mean regime, and likely likelihood/fit interpretation change. The specific m=.7 example demonstrates mass 1.6253 if the asserted atom is included. This is not a cosmetic sign check; the exact corrected normalization and extinction phase have direct mathematical/statistical importance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
