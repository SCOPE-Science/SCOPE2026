---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

C: For edge BC (length a), the active sector is B−π/2<θ<π/2−C of length A, with W=a cosθ. Three sectors partition unoriented angle space of total π. Taking inverse derivatives on monotone subarcs yields exact density terms 1/√(s²−t²) on their appropriate intervals. For acute, each side contributes two inverse-square-root singularities (total weight 6); right triangle has hypotenuse2 and legs1 (total4); obtuse has only longest side with weight2. In obtuse case the negative density jumps at h_b,h_c cannot cancel, and their positions recover b,c by a h_a=b h_b=c h_c, including repeated altitudes. Thus any triangle side multiset recoverable, leading to SSS congruence. Independent uniform-angle projection grids of 180001 directions tested CDF across acute/right/obtuse examples, without replacing analytic sector proof.

## originality

PASS

O: Read primary general unlabeled projection literature and a complete same-observable parallelogram inverse theorem. Neither supplies or mathematically implies the exact triangle density singularity/jump classification; the all-triangle result is a restricted-family positive theorem compatible with known general nonuniqueness.

## value

PASS

V: Explicit all-triangle identifiability despite directional-label loss is a natural rigorous inverse-geometric result. The signed finite jumps in obtuse case explain why more than extrema or mean width is necessary and give a complete robust-to-angle-type algebraic recovery for ideal laws.

The dated certificate retains the supplied scientific assessment, sources and limitations.
