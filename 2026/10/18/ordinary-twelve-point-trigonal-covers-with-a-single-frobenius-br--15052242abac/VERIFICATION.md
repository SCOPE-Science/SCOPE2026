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

For Q monic irreducible of n≥5 coprime to 6 over F3, (x^3−x)/Q has n distinct simple geometric poles, no rational poles and a unique multiple zero at infinity of order n−3. The Artin–Schreier equation is geometrically connected because a rational coboundary cannot have pole order 1. Wild Riemann–Hurwitz with different exponent 4 per pole gives g=2n−2; Deuring–Shafarevich gives p-rank 2(n−1)=g. The function vanishes at all four rational points of P1(F3), each unramified fiber splitting into three points: exactly 12 points, and degree-three gonality is minimal by the 4d rational-fiber bound. For g>4 Castelnuovo–Severi forces the g1^3 unique modulo PGL2; pole-order comparison in y↦uy+h kills nonconstant h; multiplicity n−3 at infinity forces affine M(x)=ax+b, and Qprime(ax+b)=a^nQ(x) is necessary and sufficient since n odd implies a^{1−n}=1. An affine stabilizer of Q centralizes Frobenius n-cycle, so its order divides gcd(n,6)=1, giving free size-six orbits and precisely (6n)^{-1}∑_{d|n} μ(d)3^{n/d} classes; fixed Q has only three k-deck automorphisms. Independent Sympy irreducibility + affine action found 48 Q / 8 orbits at n=5 and 312 Q /52 orbits at n=7. These bounded checks corroborate, not establish, the all-n formulas.

## originality

PASS

Best-of-knowledge after direct statement/implication comparison with the cited primary mathematical works and targeted Resultary published-record semantic searches; general methods and known special cases are credited. Failure of a search is not proof of priority, and inaccessible plausible sources remain explicit residual risks.

## value

PASS

The explicitly parametrized family simultaneously attains the rational gonality point bound, has ordinary Jacobian and one Frobenius-transitive wild branch divisor, and admits an exact arithmetic isomorphism and automorphism count in every permitted degree. Such rigid concrete families and mass formulas are natural resources for finite-field curve arithmetic, not routine repetitions of the general genus or point-count formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
