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

For the EXACT displayed integral projective ideal (F,G), F degree 4 and G degree 12 meet properly in all characteristics, so every geometric fiber has intersection length 48. Outside primes 2 and 3, F is smooth, G splits into three disjoint quartic pencils each with four distinct lines and four transverse F-intersections, giving 48 reduced points. Mod 3, G-(X^4-Y^4)^3 is divisible by F; the reduced D=V(F,X^4-Y^4) has precisely 16 simple F9 points and G cuts 3D, with completed local ring k[[t]]/(t^3). The degree-4 norm on F9 yields 28 Hermitian points partitioned 16 noncoordinate plus 12 on coordinate axes. Mod 2, F=L^4 and G=H^4; three transverse reduced intersections of L,H give k[[u,v]]/(u^4,v^4), each length 16 and Hilbert function 1,2,3,4,3,2,1. Proper finite morphism with constant fiber length 48 over DVRs is torsion free, hence flat of rank 48 over Z. Independently checked the mod-3 polynomial identity with SymPy, reviewed supplied exact F9 enumeration; characteristic-independent proof is geometric, not finite enumeration.

## originality

PASS

Best-of-knowledge originality qualified by primary literature, prior methods and named residual priority risks; the final evaluated theorem is not established or logically implied by the cited comparator statements.

## value

PASS

This classifies all bad-reduction characteristics and the *schemes*, not just their support cardinalities, for the canonical published integral equation of a distinguished 48-point configuration. Curvilinear 16-times-3 degeneration in characteristic 3 and transverse fourth-power 3-times-16 degeneration in characteristic 2 are different natural local invariants; the Hermitian rational-point and triple-pencil coincidence is geometrically motivated. No claim of novelty for the known complex 48-point ideal or classical Hermitian count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
