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

Direct multiplication of the two scalar heavy-ball transition matrices gives trace 1+bc-(2+b+c)z+z^2 and determinant bc. Exact quadratic Schur/Jury inequalities reduce stability for all initial pairs to 0<z<2+b+c and F(z)=z^2-(2+b+c)z+2(1+bc)>0. Its discriminant is v^2(q^2-6q+1), giving sharp q*=3+2sqrt(2) and a forbidden closed band in (0,2) when q>q*. Exact rational recurrence confirms b=0,c=9/10,z=3/2 has x_{2j}=(-11/10)^j x0 from rest; near-unit coefficients give vanishing absolute contrast despite instability.

## originality

PASS

Qualified best-of-knowledge originality: Jin-Huang arXiv:2404.03218 studies an adaptively chosen heavy-ball parameter for inverse problems, not arbitrary prescribed period-two scalar coefficients. Published Resultary SCOPE three-block cyclic minimization results have fixed momentum and alternating block updates, not the same recurrence. Floquet and Jury theory provide tools, not the deficit-ratio theorem itself. Risk: Classical discrete Hill/switched-system literature may contain equivalent period-two Schur inequalities; highly relevant arXiv:2604.14108 full text was not accessible, Oxford attempt returned worker unavailable.

## value

PASS

A sharp stability boundary for alternating individually stable momentum parameters is a motivated optimization/scheduling safety fact, beyond merely stating the classical fixed-coefficient Jury test; it includes a complete parameter classification and exact divergence witnesses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
