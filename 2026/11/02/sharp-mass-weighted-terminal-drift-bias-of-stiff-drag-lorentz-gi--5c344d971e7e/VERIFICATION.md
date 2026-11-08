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

The physical mass metric Q=diag(eps)-eps eps^T/(1+sum eps) is positive definite and Q M_rel has strictly negative Hermitian part -diag(eps_i alpha_i), since Q(I+1 eps^T)=diag eps. With Z=dt M/2, exact source stability function R=(1-z)/(1-2z+2z^2) gives f(z)=-z/[(2z-1)(2z^2-3z+2)]. Both quadratic denominator modulus factors increase on moving left from imaginary axis, giving |f(z)|^2<=G(|z|²)=s/[(1+4s)(4s²+s+4)]. Its derivative is proportional to 1-2s²-8s³, with unique positive root s*=0.42904716474868 and maximum C*=0.17487257559622. The Cayley transform of Q^{1/2}ZQ^{-1/2} is contractive; von Neumann inequality yields ||f(Z)||_Q<=C* despite nonnormality. The alpha->0 one-species normal case with legitimate stiff step approaches the boundary. Independent SymPy derivative check and 80 independently assembled multi-species physical-matrix examples corroborated algebra and bound. Does not cover resolved branch, nonlinear forcing or transient errors.

## originality

PASS

The 2026 source specifies the GIRK fixed-point function and gives a large-step bias order; the additional sharp universal kinetic-metric rational functional-calculus constant and stiff-branch extremizer were not established by accessible primary summaries. Generic von Neumann theory is known and explicitly credited, but its application to this exact physical metric plus scalar maximization is nontrivial. Full text of the primary charged-dust paper was unavailable, leaving overlap risk.

## value

PASS

Provides a dimension- and nonnormality-independent sharp engineering-relevant terminal-drift error tolerance for the physical stiff integrator, including a physically realizable sharpness construction. Unlike merely checking a stable eigenvalue, it controls arbitrary coupled-species kinetic-norm amplification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
