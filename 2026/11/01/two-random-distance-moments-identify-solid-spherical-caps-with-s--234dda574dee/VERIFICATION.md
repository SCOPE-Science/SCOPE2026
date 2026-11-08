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

For the solid cap R>0, 0<t<=2, u=2−t, axial density proportional to 1−z² and conditional transverse uniform disks yield Z_j=∫z^j(1−z²)dz/∫(1−z²)dz. Independent expansion of ||X−Y||² and ||X−Y||⁴ gives M1=R²*3(2−u)A/[40(1+u)²], M2=R⁴*(2−u)²B/[70(1+u)²], A=7u³+14u²+20u+8, B=41u⁴+82u³+99u²+108u+36. Q=160(1+u)²B/(63A²); exact differentiation gives Q'=3200(1+u)u²(66u³+117u²+56u+12)/(63A³)>0 for 0<u<2, with Q(0)=10/7, Q(2−)=7/4 and Q−10/7=(25/63)u³+O(u⁴). Thus Q determines shape, M1 fixes R, inverse has sharp 1/3 Hölder at the full ball. Independently recomputed polynomial integrals/derivative/cubic coefficient symbolically, not relying on Monte Carlo. No noisy statistical assertion.

## originality

PASS

Best-of-knowledge new part is GLOBAL TWO-EVEN-MOMENT INVERSION and sharp cubic-root endpoint, not forward integration alone. Tu–Fischbach arXiv:math-ph/0201046 develops general full spherical-object pair-distance densities (different geometry); Bonnet et al. arXiv:2010.03351 studies first ordinary-distance moment / intrinsic width inequalities; Moseeva et al. arXiv:2007.07297 addresses surface points/spherical angular distance. García-Pelayo 2011 general even-moment methods may reproduce forward formulas but full text inaccessible; no inspected implication produces strict cap-shape inverse with optimal exponent.

## value

PASS

Solid spherical caps form a canonical two-parameter convex-body model, and two independent-point Euclidean even distance moments are natural stereological observations. The exact feasible ratio interval, unique global inverse and optimal cubic ill-conditioning at the full ball are precise, nonmechanical, potentially useful shape-identification results; not simply a known inertia table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
