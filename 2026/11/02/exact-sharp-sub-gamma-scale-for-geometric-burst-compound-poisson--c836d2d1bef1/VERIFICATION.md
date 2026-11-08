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

For centered compound Poisson X of intensity lambda>0 and positive geometric jumps J with Pr(J=k)=(1-q)q^(k-1), the variance is V=lambda*(1+q)/(1-q)^2. The canonical second-order equilibrium factorization log Ee^(tX)=V*t²/2*E e^(tR) has R=M+U with M geometric on nonnegative integers, U independent density 2*(1-(1-q)u)/(1+q) for 0<u<1. Mean c=E R=(1+4q+q²)/(3(1-q²)). Direct stop-loss calculation gives cS(u)-F(u)=(1-q)² u(u-1)((1+q)u-1)/(3(1+q)²) on 0<=u<=1, so log(F(u)/c)+u/c has maximum at cell endpoint; F(0)=c and F(1)=q*c<c*exp(-1/c) using -log q>1/c. By geometric memorylessness F(m+u)=q^m F(u), proving R<=cx Exp(mean c) at every threshold. Thus Eexp(tR)<=(1-c t)^-1 for 0<=t<1/c, yielding the sub-gamma bound; comparing cubic Taylor coefficients with exact variance proxy enforces c>=kappa3/(3V)=given c. Formula is sharp for every q in (0,1), lambda>0. NBUE fails on part of (0,1) since F/S>c. Audited symbolic verifier and independently checked key polynomial and moment expressions; finite numerical grids alone do not establish convex order.

## originality

PASS

Chen 2026 establishes the general canonical remainder factorization, optimal sub-gamma variational method and M-class sufficient criterion; those are prior and explicitly credited. The inspected full Chen HTML material discusses gamma and bounded-jump examples, not the geometric jump closed formula, global stop-loss inequality or NBUE counterexample. Willmot 2002 treats compound geometric distribution residual lifetimes, a different summation model; only bibliography and abstract available, so cannot claim full noncoverage. The assessed geometric-jump specialization provides a new exact convex-order certificate best-of-knowledge.

## value

PASS

Sharp sub-gamma scales with fixed variance proxy are natural concentration constants for clustered arrivals; this formula is explicit in q and lambda-independent and its convex-order proof works even though a tempting stronger NBUE condition fails, providing a useful structural boundary for general bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
