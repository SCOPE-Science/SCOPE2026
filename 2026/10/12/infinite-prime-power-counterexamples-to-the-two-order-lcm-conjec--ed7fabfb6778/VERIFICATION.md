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

For T=[[a,-1],[1,0]], det=1, T^r scalar iff U_r=0 mod t; first scalar exponent is alpha and matrix period pi, and its scalar value squares to 1. Rank and period obey lcm under modulus lcm. With a≡4 mod6, e=v2(a), m=2^(e+1), U4=a(a²-2) has v2=e+1 and U5≡1 mod m, giving alpha(m)=pi(m)=4. Modulo 3^j the tripling identity U_(3r)=U_r(3+(a²-4)U_r²) yields an odd zero exponent 3^j, while pi(3^j) is even by reduction to 3, forcing pi=2alpha. Combining odd rank R with alpha(m)=4 yields pi(m3^j)=alpha(m3^j)=4R. Independently checked a=4,10,16 and j=1,2,3 by modular recurrence-state traversal, not substituted for universal argument.

## originality

PASS

Benfield–Lippard Conjecture 5.2 mixed (1,2) table entry predicts output 2; the explicit a≡4 mod6, moduli 2^(e+1),3^j give output 1 infinitely often. Renault already proves general rank and period lcm laws; the new simultaneous rank/parity realization is not contained in merely stating those laws. Resultary nearby Lucas records discuss other invariants. Best-of-knowledge directly new counterexample family to explicit conjecture.

## value

PASS

Refutes a mathematically specific published multiplication-table conjecture, not just a small modular exception: infinitely many recurrence coefficients and infinitely many moduli per coefficient are covered by an exact structural argument. It motivates correction of one identified table entry without claiming a full classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
