---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For 0<t<1 developing azimuthal separation delta in [0,pi] gives chord d²=r²+s²−2rs cos(t delta); competitors with angular winding >=pi have length >=r+s by radial angular crossing, and local chords do not exit the rim disk. Maximizing over theta and radial s gives eccentricity max{r,sqrt(r²+L²−2rL cos(pi t))}; elementary constrained minimization has three regimes with sharp t=1/4,1/2. Normalized lateral area has s-density 2s/L² and angular delta uniform [0,pi], giving Fréchet quadratic with minimizer r_F=(2L/3) sin(pi t)/(pi t). Monotone sin2beta/(2beta) and tan(beta)/beta yield exactly two coincidence roots, product radial convexity yields diameter, and branch monotonicity sharp sqrt(3)/2 ratio at t=1/3. Independent calculations checked 99 cone shapes and both root numerical solutions 0.2030336599850761, 0.30793382365126515; finite grids are not continuum proofs.

## originality

PASS

Developing a cone and integrating its distance are classical; claimed new work is their joint global all-shapes center-set classification and exact meeting/metric-ratio transitions. Published planar polygon centers and finite-site terrain facility location do not imply the same whole-cone intrinsic objective.

## value

PASS

Chebyshev and area-Fréchet centers are two canonical intrinsic metric-center functionals on a natural one-parameter compact conical surface. A complete optimizer-set classification, circle-to-apex topology change, exactly two center coincidences and sharp metric radius/diameter law are mathematically motivated global invariants, not just a routine local cone unfolding or one integral.

The dated certificate retains the supplied scientific assessment, sources and limitations.
