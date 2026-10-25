---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

The 12 nearest-site Voronoi pentagons have five equal great-circle sides at angular inradius ρ=½ arccos(1/√5), corner radius R=arccos √((1+2/√5)/3) and side length ℓ=arccos(√5/3). Integrating a polar cap over one pentagon, its clipped segment has S′(t)=2 sin(t) α(t), α=arccos(tanρ/tan t). Twelve normalized cells yield F(t)=6(1−cos t)−15S(t)/π between ρ,R, with cap CDF below and total coverage above. Expanding α at ρ proves the 3/2 threshold, and F′(R−)=0,F″(R−)<0 the quadratic uncovered tail; the spherical Laplacian identity Δ(u·v)=−2(u·v) with constant outward edge derivative −sinρ gives the exact chord moment 2−15ℓsinρ/π. Independently evaluated scalar moment 0.1682513876492615 and endpoints rho=0.5535743588970452,R=0.6523581397843682. Inspected check.py, whose radial quadrature/Monte Carlo are finite corroboration, not continuum proof.

## originality

PASS

Best-of-knowledge: targeted semantic published search, direct mathematical implication checks and primary full-text comparisons identify relevant component machinery or partial results but not a dominating exact statement, with the listed residual risks.

## value

PASS

The exact nearest-angle distribution, both different onset exponents and an exact nearest-chord quantization moment for the canonical 12-vertex icosahedral code are mathematically natural geometric-probability invariants; covering-radius tables and packing optimality do not supply this full function. Researchers in spherical quantization and coding can use these precise endpoint laws.

The dated certificate retains the supplied scientific assessment, sources and limitations.
