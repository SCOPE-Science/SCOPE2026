---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and proof boundary

Run `python verify.py` using the standard Python library. The executable tests all \(845\) admissible ordered pairs of neighbourhood families on a three-outcome domain for two agents. Each constructed action table is checked against its prescribed exact action-outcome set, not just for inclusion. The program separately tests examples with large outcome-to-chromatic-number gaps, singleton-intersection cases, complete-intersection boundaries, and admissible three-agent asymmetric copy factors.

Expected successful output lines are:
```
ALL_TWO_AGENT_THREE_OUTCOME_FRAMES_OK 845
THREE_AGENT_ASYMMETRIC_SAMPLES_OK 4
CHROMATIC_EFFECTIVITY_COMPRESSION_OK
```
The exact sample count is deterministic because the random generator is seeded. Exhaustive enumeration covers only its indicated finite domain. The deductive slice-surjectivity and proper-coloring argument in `RESULT.md` is the proof for arbitrary finite frames; nothing about all-size correctness is inferred from the tests.

The achieved product inequality is sufficient, not necessary for every input. No independent audit was performed.
