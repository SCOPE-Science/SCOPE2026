---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

A generic central plane cuts one polygon vertex from each sign-changing original edge. Enumerated the eight position vectors and actual 16 antiprism edges, reduced normals via dihedral symmetry to azimuth phi in [0,pi/4] and c=h U_z/sqrt(U_x^2+U_y^2). Recomputed all ordering chambers for sin(phi), cos(phi+pi/4), and other vertex thresholds; every chamber yields N=6 or 8 with N=8 iff c>max(sin(phi),cos(phi+pi/4)). Conditional upper-hemisphere normal U_z is uniform on [0,1], giving the two integrals and exact arcsine formula. Independent edge-crossing probability arccos(v dot w/|v||w|)/pi gives an independent equivalent formula, confirming normalization. Expansion and equal-edge condition h=2^(-3/4) give sharp asymptotics and regular probability; independently checked all symbolic chambers, numerical quadrature and equality of both formulas. Null orientations explicitly excluded.

## originality

PASS

Grunbaum (2004) describes antiprism geometry, but does not state Haar-random central plane section probabilities; Lonke (1998) treats cube random sections. Related Resultary findings give exact Haar sections of orthotopes and icosahedra or other polyhedral projections, which cannot be substituted for this non-centrally symmetric square antiprism. Broadie (1985) studies polarity, and Aravind (1996) examines other antiprism families; incomplete access is recorded as risk. The all-h two-point law survives best-of-knowledge claim-level comparison.

## value

PASS

The exact distribution for a natural regular solid and its aspect-ratio deformation includes an unexpected two-point section-size support, explicit transition function, monotonicity and asymptotics. It is a useful benchmark for random polytope sections, not a table-only or trivial type calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
