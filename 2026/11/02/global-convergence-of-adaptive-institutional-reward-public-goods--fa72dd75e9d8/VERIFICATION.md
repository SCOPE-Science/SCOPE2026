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

For N≥2 and 0<alpha<a*<beta, S_N(x)=sum_(j=0)^(N-1)(1-x)^j has strictly negative derivative for x in (0,1), and x*=u/(u+1), a*=kappa/(delta S(x*)) is the unique interior equilibrium. Differentiate Bernoulli D(s||t)=(s ln(s/t)+(1-s)ln((1-s)/(1-t))) in x and rescaled a; the cross terms cancel exactly, giving dot V=delta a/epsilon (u-(u+1)x)(S(x*)-S(x))<0 when x≠x*. Independent Sympy differentiation of the original vector field and proposed V gave exact zero residual. The divergence blows up at both boundaries, so each V sublevel is compact and invariant, giving all-time existence. On the invariant subset x=x*, xdot=0 only at a=a*, hence LaSalle yields global convergence and no other compact interior recurrence for every epsilon>0. The Jacobian trace −P/epsilon and determinant Q/epsilon yield sharp focus at epsilon>P²/(4Q), node below and repeated Jordan node at equality. Only interior starts/positive parameters are claimed.

## originality

PASS

Best-of-knowledge original as a global theorem for the exact Hua-Liu Eq. 6. That article introduces the same adaptive institutional reward model and shows local stability plus numerical convergence; those statements do not imply global all-feedback-speed attraction. Zino related adaptive-gain controllers operate with different laws and do not directly dominate.

## value

PASS

A single proper entropy certificate ruling out cycles and attracting all interior initial conditions for an entire parameter/time-scale family is a meaningful dynamical classification, especially in feedback games where local stability and simulations can be misleading. Sharp node-to-focus epsilon identifies a natural local qualitative transition within the globally attracting region.

The dated certificate retains the supplied scientific assessment, sources and limitations.
