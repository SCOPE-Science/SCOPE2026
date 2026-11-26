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

Choosing the original pair of positions is in bijection with gap-based insertion vectors producing a given output, including repetitions. An output with at least two positions outside the joint center alphabet can have at most two usable positions, which cannot realize both distinct centers, so an alphabet of size q contributes exactly C_p+(q-s)E_p. Of the 15 partitions of four positions, two give identical centers, leaving 13 patterns, independently recomputed. Four patterns have (s,C,E)=(2,11,8) and all other admissible expressions are 8q-6, 4q or 6, strictly smaller than 8q-5. The four patterns are precisely one constant word and one mixed word with one letter in common, in either order, hence 2q(q-1) unordered labeled pairs. Any shared output multiset can be realized with distinct vectors up to each minimum multiplicity, so the maximum plus one is the exact threshold. Independent replay: /workspace/branches/fe1c6237-5bbe-4323-a9b5-63c887d34d3c/record4_coeff_check.py and record4_coeff_check.log, all 13 coefficients, 44 finite pattern/alphabet cases, and full maximizer checks for q=2 through 8. The original verifier was inspected, not executed; the all-q proof is the support argument plus the exhaustive finite table.

## originality

PASS

The repair expressly credits both binary maximum and consequent threshold to prior work. The remaining claim is the exact all-alphabet size and full equality classification, not the binary scalar or established multiset model.

## value

PASS

The motivating unique-error reconstruction model needs a sharp multiset overlap bound. The all-alphabet formula gives the exact worst-case observation requirement and the equality classification identifies every ambiguous extremal pair. This is a complete base regime for the model's recursive bounds, not merely recomputation of the published binary number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
