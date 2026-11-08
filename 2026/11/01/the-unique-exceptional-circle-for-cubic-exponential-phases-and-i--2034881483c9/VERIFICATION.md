---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For each radius the defect M_r−Re(a r w+b r^2 w^2+c r^3 w^3) is a nonnegative trig polynomial of degree 3. Three distinct angular zeros must each be double, forcing a squared monic cubic with three unit roots. Its constant/sign and Fourier coefficients force B=−2Cr s and A=Cr²(s²+2 conjugate(s)); eliminating s gives d=B²/(4C)−A=r conjugate(B), so B nonzero and candidate r=d/conjugate(B)>0 is unique. Conversely these equations give the exact nonnegative Laurent square C r³|w³−s w²+conjugate(s)w−1|²/2. The self-inversive cubic discriminant Delta=|s|⁴+18|s|²−8Re(s³)−27 is negative iff all three zeros distinct unimodular; zero and positive discriminants yield the claimed boundary/nonexceptional cases. Sympy independently reconstructed Laurent identity, discriminant and the sharp exp(8z−4z²+z³) example. Degree≤2 has at most two distinct angular minima by the double-zero count, completing cubic minimality.

## originality

PASS

Li arXiv:2610.15067v2 establishes general local finiteness of exceptional circles for much broader entire functions; local finiteness does not imply an at-most-one bound for cubics, a coefficient iff criterion or least degree. Rieck arXiv:2307.09219 supplies the known deltoid/unit-circle cubic-root criterion and Fejer–Riesz square methods are classical, not claimed as inventions. The combination forcing the unique radius from an equal-maximizer contact is the assessed original implication. Full Li paper was inaccessible, so a hidden cubic specialization is a recorded risk.

## value

PASS

The exact first-degree threshold and full complex-coefficient criterion resolve a natural boundary of the general maximum-modulus exceptional-circle problem: cubic is minimal and no two exceptional radii exist. The strict deltoid and cusp cases give meaningful geometric classification rather than a gratuitous reparameterized cubic discriminant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
