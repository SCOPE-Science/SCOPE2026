---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Regular simplex vertices v_i=(e_i−1/(d+1))/sqrt2 yield oriented roots (e_i−e_j)/sqrt2. Width is their maximum projection; root pairs have inner product <=1/2, with 2(d−1) half-angle neighbors per root, so only π/3-separated cap pairs overlap before t0=sqrt(2/3). For three distinct roots ||a+b+c||²<=6, implying common cap t<=sqrt(2/3), so inclusion-exclusion is exact through second order. Conditional spherical coordinates along normalized sum/difference of pair centers produce Q and J beta integrals; d=2 circle expression and d=3 Gauss–Bonnet lens. Tangency coordinates scale x=δ, y=sqrt(δ), yielding lens volume 8 κ_{d−2}/d*(4/sqrt3)^((d−2)/2)δ^(d/2), and normalized H pairs give claimed coefficient. Independent root enumeration d2..8 checked 1260 half-angle pairs and 5 d3 lens analytic-versus-integration values.

## originality

PASS

Finch derives regular-polytope width moment data and specifically identifies tetrahedral width density as a missing problem in a related paper; Finch regular-simplex paper studies mean and moments, while Kabluchko–Litvak–Zaporozhets give Gaussian-range mean/asymptotic relations. A published Resultary result for *simplex vertex centred* cap unions concerns different centers than oriented A_d roots, and cannot supply the root multiplicity/first overlap coefficient directly. No inspected full distribution tail overlaps these claims.

## value

PASS

The random width distribution is a natural geometric probability statistic of regular simplices. A sharp first cap-overlap transition, exact upper-tail interval, and dimension-dependent nonanalytic exponent are useful exact data even without a complete lower tail, and the oriented-edge root combinatorics distinguish it from routine moment computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
