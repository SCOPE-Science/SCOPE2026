---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

With t_n=S_n/h=u_n/v_n in coprime lowest terms, recurrence u_{n+1}=u_n²+v_n², v_{n+1}=u_n v_n holds. The reduced x_{n+1} gives Q_{n+1}=(u_{n-1}+v_{n-1})²/gcd(h,u_n), so for odd obstruction p, p never divides numerator; for p=2 denominator has valuation one and resulting 2-adic valuation is odd. Thus Q square iff d_n=1. Primes 3 mod 4 never divide u_n; p=2 only can first divide u_1, so only Q_2. For odd p=1 mod4, starting ratio z evolves under T(z)=z+z^-1 until first 0, and sign and inversion preserve first-hit depth. Every hit level nonempty up to k; four-point orbits except possibly two levels involving z²=±1 give at least 4k-4 nonzero field elements, so k<=(p+3)/4 and Q_{k+1}<= (p+7)/4. At h=x_0=5 Q_3=9/5 and deadline 3 is attained. I independently reproduced exact finite-field orbit and rational special case checks.

## originality

PASS

Best-of-knowledge original combined claim, not merely its known premises: Knowing one exceptional index per p does not bound how late that index can occur; a complete functional-graph depth classification might imply the bound, so its unread full detail remains a priority risk rather than being declared noncovering. Broader works and residual risks below qualify priority.

## value

PASS

The original finite-exception theorem does not tell an analyst when all terms must be squares uniformly over starting values. The explicit prime-quarter deadline is a substantive quantitative stopping-time theorem for a natural arithmetic dynamical system; group symmetry explains a nontrivial factor-four bound and has an attained boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
