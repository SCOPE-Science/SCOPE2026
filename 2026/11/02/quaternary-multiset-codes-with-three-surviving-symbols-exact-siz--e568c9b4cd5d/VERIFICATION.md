---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and logical limits

Run `python verify.py` using Python 3.10 or newer. No third-party packages or external data are needed. For lengths five through eight, the verifier lists every nonnegative four-part composition and verifies that disjoint three-symbol deletion shadows agree with the pairwise intersection test. It enumerates all codebooks of the known optimal sizes by increasing-index recursion, recounts them using exceptional words and heavy-coordinate pools, and checks fixed-point counts under the 24 alphabet permutations. The corresponding Burnside averages give the orbit counts. The ordinary reproducibility log is `verification_output.txt`.

The code also checks sample lengths beyond eight for the known optimal-size argument. These extra tests do not extend the optimizer census beyond length eight. The labelled census has a separate combinatorial derivation in `RESULT.md`; the orbit census relies on finite exhaustive enumeration.
