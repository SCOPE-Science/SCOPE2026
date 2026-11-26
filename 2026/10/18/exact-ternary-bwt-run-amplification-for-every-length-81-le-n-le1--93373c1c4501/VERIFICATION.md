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

The cyclic-to-linear factor-two bound applies on this nonconstant primitive interval. Independently, among sorted rotations starting with a letter a, first come those whose first non-a letter is below a, then those for which it is above a. In the former group the last rotation has maximal initial a-streak in that group, and in the latter the first rotation has maximal streak. These terminal/initial rotations cannot have predecessor a, as prepending that a would give a longer streak in the same group. Since consecutive L entries differ, pair each L=F rotation in the below group with its successor and in the above group with its predecessor. This injects matches into mismatches, which count input cyclic boundaries. For the upper bound, independently reconstructed 80 inverse words by stable inverse-permutation traversal, sorted their rotations from scratch and checked primitivity, all last columns, linear runs n, and cyclic runs (n+1)//2. A ternary witness keeps all lexicographic comparisons in every larger stated ordered alphabet. Constant-necklace conventions and sentinel variants are outside the claim. Replay: /workspace/branches/independent_replays/replay3.py with the frozen BWT_WITNESSES.tsv, output replay3.out (ALL_80_ROTATION_CENSUSES_OK). This is a finite certificate, not extrapolation.

## originality

PASS

The factor-two inequality, cycle criterion, Hamming identity and already constructed special lengths are not original here. The supported distinct contribution is contiguous attainment on the entire 81–160 interval, specifically the lengths not covered by the inspected prime families or other interval results. Real overlaps at named lengths are credited; no inspected source yields the whole interval, and the residual risk is not a priority conclusion.

## value

PASS

This certifies a substantial contiguous block of exact cases of a stated extremal conjecture, rather than isolated rechecks or ordinary unclustered feasibility; it includes lengths outside the arithmetic families. Explicit extremal inputs across both parities can be used to test candidate structure theorems about sharp necklaces. It does not resolve the general conjecture or characterize all minimizers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
