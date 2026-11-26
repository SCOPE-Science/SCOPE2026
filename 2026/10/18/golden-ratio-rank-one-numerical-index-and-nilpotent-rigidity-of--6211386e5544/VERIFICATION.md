---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

A unit rank-one map factors as Tz=ℓ(z)u with both factors unit. Along the interior of a primal edge the only norming functional is its support, and the absolute pairing is bounded by endpoint values; at each vertex the norming segment has just the two adjacent supports as extreme points. This gives formula (1) over ten vertex-support pairs of edges. The cosine row (1,1,r,0,−r,−1,−1,−r,0,r) follows from the angle differences, with r²=1−r. Rotate and reflect u onto the first half-edge so 0≤s≤1/2, and change the sign of ℓ to cover the five dual edges. For j=0,1,3,4 the common vertex immediately gives bounds 1, r+r²s, 1−r²s>r, 1, respectively. For j=2 the bounds from v_2,v_4 are positive and vary strictly in opposite directions with t, crossing at t=s with value r+r⁴s(1−s). Equality therefore requires s=0; for j=2 it forces t=0, and for j=1 the v_1 test forces t=1. Both give ℓ=q_2. At (v_0,q_2) the maximum is r by the exact row. Reflection about v_0 sends the perpendicular q_2 to −q_2, so undoing symmetries gives exactly ±T_i modulo the five distinct range lines. q_{i+2}(v_i)=0 gives square-zero, and the cited ordinary-index theorem gives r/2. The supporting checker.py was inspected; its finite sampling is not used to infer the universal bound or rigidity.

## originality

PASS

The exact rank-one value and complete equality set in the regular real decagon are distinct on the compared evidence. The published ordinary numerical index and the octagonal separation analogue are not new claims here.

## value

PASS

The regular decagon is a natural test beyond the inspected hexagonal and octagonal rank-one families. The exact ratio to the known full index isolates the effect of restricting to rank one, and complete square-zero rigidity identifies the actual minimizers rather than merely producing a numerical bound or one candidate. This is a useful exact invariant and structural classification without claiming a general polygon theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
