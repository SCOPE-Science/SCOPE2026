---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Verified the exact change of coordinates F=t^2(u+v+w)+uvw in characteristic 2 and that projection is a nonsquare quadratic purely inseparable extension. On F=0, multiplication by u+v+w sends the Gauss partials to (vw(v+w),uw(u+w),uv(u+v)); all projective common zeros are the seven F2 points, local linear terms span cotangents, and seven independent cubic conditions leave precisely the three stated cubics. Blowup net -K=3H-Sum E is base-point-free, square two, hence dominant generic degree two. Its ratio Jacobian wedge vanishes identically modulo two, giving purely inseparable degree two; composition degree four. Integral Steiner quartic reduces to the fourth power of the plane equation; this is not the reduced special-fiber dual. Independently rederived polynomial identities, seven F2-point base locus, net rank, and derivative identity with SymPy. The all-algebraic-closure base locus uses the proof, not just finite F2 testing.

## originality

PASS

Classical Cayley/Steiner duality supplies the quartic and four nodes, but the inspected prior Hessian-surfaces work is characteristic-zero lattice geometry and does not give the Fano-seven anticanonical inseparable factorization. Best-of-knowledge original explicit characteristic-two refinement.

## value

PASS

The inseparability and nonreduced-versus-reduced dual distinction illuminate positive-characteristic projective duality; connecting the Gauss map to a complete anticanonical net on the seven-point blowup is an exact geometric structure, independently useful beyond a raw equation substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
