---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The positive real Jacobi matrix has simple spectrum and cyclic lossy endpoint, so the non-Hermitian generator is strictly stable and integrated survival solves an exact Lyapunov equation. Its energy-basis diagonal and off-diagonal identities force an exact alpha/gamma+beta*gamma law for real initial vector; reflection symmetry gives alpha=m. A fixed-m rank-one Schur complement reduces beta to an odd alternating chain. Its nonzero sine modes contribute 2(m-1)a^2/b^2 and zero mode contributes (b/a)^(2m-2), giving the stated beta including m=1. Independent actual Gramian checks for 24 parameter combinations m=1,2,3,4,5,7 had max relative deviation 1.7e-13; m=1 separately symbolic. Optimization follows by convexity in gamma.

## originality

PASS

Highly relevant full primary July 2026 Wang-Zhang paper addresses the SAME non-Hermitian one-body SSH defect but studies many-body Liouvillian spectral gaps, local decay modes, exceptional points, and weak/strong-loss exponents; its model uses a single bulk loss; no exact integrated remote-end survival Gramian or all-m gamma optimizer was located in the examined portions or document-wide keyword search. Prior Rudner-Levitov loses an entire sublattice; Varbanov measures at Poisson times. Spectral-gap scaling does not mathematically give a fixed-initial-state integrated norm time or its optimum. The exact finite dimerized formula is novel best-of-knowledge, with possible broader time-delay theory risk.

## value

PASS

Single-endpoint loss and transport across finite SSH chains are natural physical observables. The exact all-m time and unique optimal loss give a substantive geometric zero-mode contribution and exponential-versus-linear optimized scaling; it is not a renaming of the uniform chain or another numerical spectral-gap plot.

The dated certificate retains the supplied scientific assessment, sources and limitations.
