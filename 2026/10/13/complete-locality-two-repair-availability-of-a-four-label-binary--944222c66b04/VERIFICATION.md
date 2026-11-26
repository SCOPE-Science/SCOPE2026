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

The nonzero first blocks are distinct so a pair is a repair exactly when its two columns sum to the target column. A helper determines its partner uniquely, so the target's pair count is already the disjoint availability. Two positions in one spread member force all three into it, where the label must vanish; this gives 2^(m-1)-1 internal pairs. Otherwise each two other members are complementary subspaces, giving exactly one decomposition with both summands nonzero, and the label XOR decides if it works. Independent enumeration of the 17 printed labels gives 33 zero-XOR distinct-index triples, t=(4,3,9,6,4,3,8,8,6,6,7,6,9,12,12,12,12), the asserted histogram after multiplying by 15, and 33*15+4*35=635 dual supports. For the distance, the annihilators of the spread members partition the nonzero dual vectors, so a nonzero linear functional vanishes on exactly one member and is balanced on every other member before deleting zero. If u members are selected by the label functional, the mixed weights are 128-u or 144-u; the pure label weights are 15u. The recalculated nonzero u range is 4 to 9, with u=4 for the first two indicator rows summed. Thus rank 12 and distance 60 follow on every realization, not just the test spread. All 17 subspaces of dimension four in dimension eight fill the nonzero vectors since 17*15=255.

## originality

PASS

The code construction is prior work. The distinct supported result is the full alternative two-helper incidence profile and its full-spread counting rule, together with the verified correction to the printed example. None of the confirmed exact or neighboring sources supplies that local incidence result.

## value

PASS

An exact per-coordinate failure-recovery profile for a specified existing code distinguishes coordinates with three disjoint local options from those with twelve, which global distance or the total number of dual triples cannot do. The reusable full-spread count explains why the profile is intrinsic to the labels, and the distance witness materially corrects how the published example can be used.

The dated certificate retains the supplied scientific assessment, sources and limitations.
