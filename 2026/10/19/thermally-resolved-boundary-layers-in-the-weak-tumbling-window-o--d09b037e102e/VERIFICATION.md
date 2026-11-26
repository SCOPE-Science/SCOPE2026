---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Reflection and the zero total current imply rho even, s odd, and w(ρ_{i+1}−ρ_i)=δ(s_i+s_{i+1}) with w=u+v. Subtracting orientation balances and eliminating ρ gives the stated recurrence, so s=A sinh(ki), ρ=B+AH cosh(ki) and 4uv sinh²(k/2)=δ²+αw. At the right wall the plus-current identity becomes j⁺=δB/2−(Aα/2)cosh(k(L−1/2))/sinh(k/2)=αs_L. The half-angle identity yields B/A=(α/δ)cosh(k(L+1/2))/sinh(k/2), the stated boundary coefficient. Normalization is a geometric sum. In the critical window z→u/v and H→1: the normalized constant term gives the bulk Riemann sum and each of the two geometric terms gives an endpoint atom with uniform summable inward decay. The geometric component has zero rescaled interior density for any sequence bounded macroscopically away from the walls. At a fixed inward index j, s and ρ have the same limiting value, so only the outward orientation contributes. This works also at c=0, when the constant component has zero mass. The log derivative on c>0 is y/(1+y)² with y=2c/δ, with unique maximum 1/4 at y=1; its c=0 value is a continuous extension only.

## originality

PASS

The exact finite model and its transfer matrix, boundary accumulation, and the scale δ/(2L) are covered by Santra. Continuum sticky-wall balance also covers the form of the macroscopic mixture and the corresponding dimensionless response. The distinct claim is the rigorous two-scale stationary match in this thermal lattice: exact normalization and orientation of a fixed-lattice-spacing geometric profile, simultaneously with the interior and atomic limits and no missing mass. The reference's unexpanded matrix powers require extracting the modes, matching their wall coefficient and controlling normalization in a joint size/flip limit; its finite-site numerical slopes and persistence-length estimate do not perform that analysis.

## value

PASS

The distinction between macroscopic wall accumulation and microscopic occupancy of an actual lattice site is motivated by the primary work's finite-site measurements. The exact normalized profile tells how the atom is distributed over sites and which orientation carries it while the size and persistence length compete. Neither the continuum shape nor the crossover scale alone answers how many near-wall sites carry that mass.

The dated certificate retains the supplied scientific assessment, sources and limitations.
