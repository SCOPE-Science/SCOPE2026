---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

The affine D_+(z_S) semigroup consists of subset indicator differences. For 2≤|S|≤n−2 all signed basis vectors occur by toggling, giving A^n. For |S|=1, 2(n−1) ratios a_j=t_j/t_1,b_j=t_j generate all monomials; exactly the 2×2 minors are the relations, so the chart is the rank-one Segre cone. Complement gives other extreme charts. Rank-one cone is normal and smooth away from its vertex; its Pic(P¹×P^{n−2})/Z(1,1) local class group is Z and K class (−2,−(n−1)) vanishes rationally iff n=3; Hilbert numerator 1+(n−2)z yields vertex multiplicity n−1. Removing corner simplices from n-cube gives normalized degree n!−2. Independent exact exponent-decomposition checks on n=3..6 (1192 differences) corroborate but do not prove all n.

## originality

PASS

Michałek–Oeding–Zwiernik already define exactly the family P(T_{1,n−1}) and give quadratic ideals in arXiv:1212.1515; construction and normality are not claimed new. Their detailed singular-cone proof in §5 addresses T_{2,n}, not the all-n local affine chart isomorphism for projectivized T_{1,n−1}. The known n=3 six-node complete intersection is credited. No stronger exact source for the uniform higher-n determinantal charts, class groups, Gorenstein border located in inspected primary material.

## value

PASS

The explicit all-chart rank-one description is a structural local classification of a natural classical toric Segre projection; it determines singular support, integral divisor classes, multiplicities and a sharp dimension-dependent Q-Gorenstein boundary. These exact invariants are useful beyond a repeated known monomial presentation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
