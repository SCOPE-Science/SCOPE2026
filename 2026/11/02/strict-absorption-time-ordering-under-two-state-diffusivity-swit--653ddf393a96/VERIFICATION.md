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

The two-state Feynman–Kac clock transform has factor f_gamma solving f''+2 gamma f'-(lambda h)^2 f=0 with f(0)=1,f'(0)=0. Its time derivative is positive for t>0; differentiation in gamma gives a forced ODE with strictly negative source -2f' and positive Green kernel, hence partial_gamma f<0. For uniform initial spatial position, Dirichlet–Neumann heat content is the positive-weight sum |integral phi_j|^2/|Omega| times positive clock modes, with positive ground-state weight; this gives strict first-order absorption-time stochastic ordering for each t>0 and bounded connected regular domain. On a fully absorbing interval, subtracting state-averaged coupled backward equations gives the scalar positive Dirichlet resolvent and the exact hyperbolic-cosine mean formula, strictly decreasing at fixed interior x. Frozen gamma=0 and homogenized gamma->infinity limits match; no claim of full stochastic order from a fixed nonuniform start. Source checks use direct formula algebra, not finite-difference tests as universal proof.

## originality

PASS

Grebenkov's general switching-diffusion clock transform and arbitrary-domain spectral machinery are prior, but their mere formula is not yet the quantified strict switching-rate ordering proved here. Jain–Sebastian 2016 is a highly relevant bounded rearranging-environment survival paper, but only abstract was obtainable; authorized institutional full-text retrieval returned vpn_disconnected. This is a substantial residual priority risk, not a discovered coverage theorem.

## value

PASS

Uniform-in-time first-order stochastic order simultaneously for broad absorbing/reflection geometries, plus fixed-location mean monotonicity with exact interval formula, provides a testable sharp physical rate comparison not implied by knowing isolated mean coefficients.

The dated certificate retains the supplied scientific assessment, sources and limitations.
