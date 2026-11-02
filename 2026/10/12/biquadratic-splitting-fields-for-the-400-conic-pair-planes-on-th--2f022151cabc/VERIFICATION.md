---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

Reconstructed the projective row action from four explicit matrices and H1=(1,1,1,0), H3=(0,0,1,i(1+sqrt5)/2). Exact computation over the Q-basis (1,i,sqrt5,i sqrt5), using field norm inverses, independently found disjoint normalized plane orbits of 160 and 240 elements and closed Galois action. For sigma_i, sigma_sqrt5, sigma_i*sigma_sqrt5 the 400-element fixed counts are 64,160,16. Their simultaneous fixed intersection is 16 Q-rational planes, giving 144 Q(i)-minimal, 48 Q(sqrt5)-minimal, zero Q(sqrt(-5))-minimal, and 192 full biquadratic fields. Orbit-stabilizer yields 16 one-, 96 two-, and 48 four-element Galois orbits. Four sample plane equations were independently verified to belong to the corresponding orbit and have the stated field. Exhaustiveness uses Naskręcki Theorem 1.1 and Corollary 3.1, not an unsupported extrapolation from 400 tests.

## originality

PASS

Best-of-knowledge PASS, qualified. Naskręcki's Theorem 1.1 and Appendix A already supply the quartic, group, conic seeds and geometric orbits, and Corollary 3.1 already counts the 400 planes. They do not state the exact Galois projective fixed-point counts (64,160,16), minimal supporting-plane fields (16 Q,144 Q(i),48 Q(sqrt5),192 Q(i,sqrt5)) or 16+96+48 orbit profile. The independently checked finite Galois computation is a new arithmetic extraction rather than a new geometric conic census. Those inputs make the refinement short and potentially implicit in older calculations, so priority is qualified, not absolute.

## value

PASS

The whole geometrically reducible hyperplane set is a natural complete finite arithmetic configuration attached to the distinguished 800-conic K3 quartic. Minimal fields of projective plane equations and their actual Galois orbit lengths are intrinsic to the fixed Q-embedding and not determined by the geometric count 400 or by the conic component coefficient field. The full exact 16/144/48/192 classification clarifies which plane sections descend over Q and the two quadratic subfields versus requiring the biquadratic compositum. Such precise incidence/descent data are reusable without new general theory; the claim is narrow and computation-heavy, but not an arbitrary slice or isolated arithmetic curiosity. Its value is modest and relies on original arithmetic information rather than a new conic construction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
