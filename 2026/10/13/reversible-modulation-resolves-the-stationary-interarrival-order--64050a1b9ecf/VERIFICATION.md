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

A=-Q+D is positive self-adjoint in L²(pi) under detailed balance and positive mean event rate: <f,Af>=1/2 sum pi_i q_ij(f_i-f_j)^2+sum pi_i lambda_i f_i². Spectral weights at 1 are nonnegative and sum to one, giving hyperexponential S_pi(t). Its hazard derivative is minus a positive tilted variance, and h_pi(0)=lambda_*. Palm initialization gives S_alpha(t)=-S_pi_prime(t)/lambda_*=(h_pi(t)/lambda_*) S_pi(t), hence S_pi>=S_alpha, strict for all t>0 unless all lambda_i equal. Handles rates lambda_i=0 and nonuniform pi; independent reconstruction, not finite extrapolation.

## originality

PASS

Best-of-knowledge same-object comparison finds no prior complete final classification; exact source implications, aliases, and residual risks explicitly recorded. No failed search is offered as proof of novelty.

## value

PASS

A complete natural reversible class (including all finite birth-death modulators) of an explicitly conjectured stationary/event-stationary MMPP order, plus equality and positive spectral structure; significantly extends proven two-state and ordinary symmetric-C cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
