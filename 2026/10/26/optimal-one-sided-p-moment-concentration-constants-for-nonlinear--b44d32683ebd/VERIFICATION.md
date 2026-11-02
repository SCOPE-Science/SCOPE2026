---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For 1<p<=2, F(u)=u-1+e^-u and k(u)=u Fprime(u)/F(u) decrease from 2 to1 with kprime=e^-u(u^2+2-2cosh u)/F(u)^2<0. Therefore C_p=sup_{u>0}F(u)/u^p has unique positive maximum u_p for 1<p<2; p=2 gives C_2=1/2 at u down to zero. Apply sharp scalar e^-u<=1-u+C_p u^p conditionally to one-sided deficits D_i=sup_{change Xi} f - f, and published reverse-KL tensorization Proposition 3.4 to derive log E exp(beta(f-Ef))<=C_p V beta^p for independent coordinates and bounded-above integrable f. Chernoff minimization yields c_p=(p-1)/p (p C_p)^(-1/(p-1)). To establish global optimality, additive f=-sum Bernoulli(epsilon) has V=n epsilon and its lower-tail rate d(kappa epsilon||epsilon); as n->infty then epsilon->0, rate tends to epsilon(1-kappa+kappa log kappa). Choosing kappa=e^-u_p produces exactly c_p, p=2 by kappa->1. Thus any larger uniform coefficient fails. Separate rare-event argument yields lim_{p downarrow1}c_p=1. Independent numerical optimization and nonlinear MGF tests corroborate, not prove, full theorem.

## originality

PASS

Compared exact statements and implications with same-object original papers, published related mathematical records, and alternatives. The strictly weaker source theorem does not imply a stronger exponent, still less the matching optimality proof; the cited tensorization is properly attributed. Residual historical priority and access risk explicitly retained.

## value

PASS

Determines the sharp constant for a genuinely nonlinear product-space one-sided heavy-tail inequality, strictly improving the published (p-1)/p for 1<p<2, matching rare Bernoulli obstruction and endpoint behavior; not a mere scalar inequality or unproved generalization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
