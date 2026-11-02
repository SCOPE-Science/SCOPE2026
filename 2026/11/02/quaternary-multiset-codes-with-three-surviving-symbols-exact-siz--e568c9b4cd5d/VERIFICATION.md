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

# Reproduction and logical limits

Run `python verify.py` in a directory containing the verifier. It requires Python 3.9 or newer, but no third-party packages or external data. The verifier constructs every nonnegative four-part composition of each length from five to eight, compares pairwise multiset-intersection compatibility to disjoint three-symbol deletion shadows, enumerates every size-optimal compatible subset via increasing-index bitmask recursion, and independently recounts the same subsets from exceptional-word selections and four heavy-coordinate categories. It then evaluates fixed-point counts for all 24 permutations of the four-symbol alphabet and recomputes the orbit counts by Burnside averaging. It checks the four-constant construction at further lengths nine through seventeen and ends with `QUATERNARY_THREE_SURVIVOR_VERIFICATION_OK` on success.

The mathematical proof handles all \(n\ge5\), including lengths beyond the finite verification range. The finite programs verify only their stated instances and make no independent publication-priority determination. The optimal-cardinality proof is algebraic-combinatorial; the orbit counts require finite exhaustive enumeration as described in the proof and executable code. The recorded `verification_output.txt` is an ordinary reproducibility log, not an independent audit certificate.
