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

Direct basis evaluation of weight-zero binary and ternary Rota–Baxter identities for R=[[a,b],[c,d]] gives a²+bc=0, c(a+d)=0, a²(a+d)=0 with no characteristic-specific division. Case a=0 gives either the plane a=c=0 or the square-zero matrices with a=b=d=0 and c≠0. Case a≠0 forces d=−a,bc=−a². Hence precisely plane A={a=c=0} ∪ square-zero cone N={trR=detR=0}; their overlap is line a=c=d=0. For any finite field F_q each component has q² points, intersection q, total 2q²−q and rank profile (1,2q²−q−1,0). The algebra automorphism matrices [[s,t],[0,1]] (s≠0) act by conjugation; orbits have sizes 1, q−1, q repeated q−1 times, q(q−1), total q+2. Counting over extensions gives zeta (1−qT)/(1−q²T)². No assumption of algebraically closed or characteristic-zero field is used.

## originality

PASS

The exact Zhao–Qiao and Sheng–Zhao algebra examples explicitly give the two-parameter family killing e1; neither inspected source claims it exhaustive or describes the square-zero second component, finite-field orbit stratification, or zeta function. Those complete moduli calculations are retained as genuinely new best-of-knowledge content, with the prior plane credited.

## value

PASS

Complete structure of an operator variety on a canonical nonassociative algebra: identifying a missing irreducible component, its point counts and natural automorphism-orbit classification is a useful exact representation-theoretic invariant, not just an isolated pair of matrices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
