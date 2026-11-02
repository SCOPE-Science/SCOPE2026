---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

At stationary exponential observation times the perpetuity X=Z+UX' with Z a Brownian displacement over Exp(lambda), gives (1+kappa||t||²)phi(t)=E phi(Ut) for kappa=D/lambda. Substitution phi=(1+beta||t||²)^(-q) and coefficient comparison gives E U^(2n)=1-hn/(q+n-1), h=kappa/beta. For q<1 this violates E U4<=E U2, and as n tends to infinity it gives P(U=1)=1-h>=0. Hausdorff moment uniqueness identifies only the asserted two-atom law for q=1 or (1-h)delta1+h Beta(2q-2,1) for q>1, with q>=1, beta>=kappa. The beta integral exactly verifies the identity for all z>=0. E U²<1 ensures L² perpetuity convergence and synchronous-coupling contraction, proving unique invariant law for any finite d. Independently checked 228 exact rational moment identities plus boundaries. This depends on common scalar iid [0,1] resets, not general affine resetting.

## originality

PASS

The exact inverse feasible region and uniqueness of multiplier law are not given by the inspected fixed-multiplier Brownian-resetting source. General polynomial-process moment methods from Assefa et al. and partially stochastic Levy resetting work may contain broader stationary identities; the most closely relevant 2026 moment paper full text could not be accessed, so originality is best-knowledge with a material priority risk. The beta integral is classical and not claimed independently new.

## value

PASS

The theorem solves a complete inverse stationary-law design problem: every dimension, precise achievable parameter region, uniqueness of admissible reset distribution, and a sharp effective-reset boundary. These are meaningful stochastic-process structural facts, not a numerical isolated case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
