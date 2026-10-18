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

The standalone standard-library `check.py` executes an exhaustive enumeration of the entire ternary word space at each length through 11. It generates the 147 s-primitive candidate words (lengths at most eight), checks no primitive at length nine, and uses endpoint filtering plus the exact greedy-prefix/greedy-suffix occurrence characterization to enumerate all shortest covers. It checks 127530 pattern/text cases independently via direct positional embedding enumeration, then independently certifies the six exceptional witnesses and exclusion of all covers of length at most five. The expected captured output is included as `check_output.txt`.

The mathematical argument that enumeration suffices is in RESULT.md: shortest covers are s-primitive, adjacent repetitions cannot be primitive, and an embedded nonprimitive factor makes the full word nonprimitive. No unexamined words longer than eight can be shortest-cover candidates. Computations provide a finite exhaustive proof of the sharp cutoff, not a purported proof of a theorem about arbitrary longer input lengths. No external audit or validation has taken place.
