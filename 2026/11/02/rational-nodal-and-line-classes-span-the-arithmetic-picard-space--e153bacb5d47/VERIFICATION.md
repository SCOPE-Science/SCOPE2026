---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For F=e1 e3−e4 each gradient entry in characteristic three is P(x_i), with P(X)=X³+(e2−e1²)X+e1 e2. This also gives a geometric completeness check independent of the finite-point search: for three distinct coordinate values the three roots sum to zero. If a is repeated, then e1=a and the pairwise sum of the roots is e2, forcing a=0 from P, hence the remaining coordinates are opposite. For two distinct values of multiplicity 2+2 the root equations give a²+b²=0 and a²(b−a)=0, a contradiction. For multiplicities 3+1, P(X)=X(X²−b²) where b is the single value, so the repeated value is 0 or −b. The all-equal case is one point. These classes all satisfy F=0 and give exactly the four rational orbits. Their nonsingular quadratic terms were verified, agreeing with the reported chart quotient lengths and showing ordinary double points. Finiteness of the geometric singular locus implies geometric integrality; adjunction and the crepant nodal resolution give the K3. The independently enumerated projective planes give all 20 rational lines by testing the restriction polynomial, not just rational point evaluations. On the resolution, adjunction gives self-intersection −2, a line through a node meets the exceptional conic transversely once, distinct lines through one node separate by their distinct tangent directions, and smooth line intersections are transverse. The independent incidence matrix has rational rank 21 and reproduces the indexed principal determinant 1536. The same replay gets quartic counts (25,145) and resolution counts (70,280), adding q points per rational node over each field. Purity and equality in the F_9 bound force squared eigenvalues 9, and the F_3 trace 60 gives multiplicities 21 and 1 for +3 and −3. Injectivity of the étale divisor class map bounds the fixed rational space by 21; the minor and rationality give the opposite inequality and spanning. No Tate assumption is needed for spanning, while the geometric complementary direction uses the established K3 Tate theorem over F_9.

## originality

PASS

The supported distinct claim is generation by this explicit list of 35 geometric classes defined over F_3, certified by their rank-21 intersection pairing. The characteristic-three model, singularities, zeta function, and the arithmetic dimension 21 already have material same-model coverage; none of those, on its own, is credited here as new.

## value

PASS

The arithmetic rank alone or a Tate-theoretic existence result leaves arithmetic divisors abstract. Exhibiting a geometrically motivated complete rational spanning set on this special fibre, together with an explicit nonsingular intersection minor, makes divisor classes and intersections available for further work. It answers a natural generation question rather than merely recomputing the known point counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
