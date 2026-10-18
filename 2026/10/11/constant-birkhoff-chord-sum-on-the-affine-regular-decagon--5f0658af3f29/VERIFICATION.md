---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For each unit x, dihedral transitivity reduces to an edge interior x=(a,1-a) or vertex x=(1,0). For an edge, unique norming functional s+t forces y=±(phi,-phi); exact evaluation gives A=2r+r²a and B=phi-r²a. For a vertex, the norming functionals s+t and s+rt force the opposite edge y=(1+r theta,-phi) up to sign, with identical affine A,B expressions. Since A+B=2r+phi=(3sqrt5-1)/2 for every pair, min<=half<=max, and a=1/2 attains both, giving J_perp=g_perp=(3sqrt5-1)/4. Independently evaluated the branches at five non-grid rational parameters including endpoints and checked the active-functional products; actual verify.py uses exact Q(sqrt5) arithmetic on parameter grids, corroborative only.

## originality

PASS

The source Baronti–Papini paper defines orthogonal James/Schäffer constants and computes hexagons and octagon, not the decagonal pointwise chord sum. Related indexed decagonal parameters share values and norm geometry but do not imply that every Birkhoff-admissible pair has the same sum. Known James constant at the same value can imply a bound on J_perp but not the stronger universal identity.

## value

PASS

A pointwise rigidity phenomenon for all Birkhoff-orthogonal chords in a natural regular decagonal norm, rather than merely another isolated numerical norm constant. It simultaneously determines two orthogonality-specific extrema and describes their full feasible chord geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
