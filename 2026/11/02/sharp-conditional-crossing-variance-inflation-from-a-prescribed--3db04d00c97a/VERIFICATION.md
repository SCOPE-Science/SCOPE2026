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

# Verification of the crossing-variance identity

The accompanying standalone `verify.py` implements exhaustive enumeration of perfect matchings using Python 3 standard-library `fractions.Fraction` and checks the conditional first two moments of total crossings, the covariance between remaining crossings and distinguished-chord crossings, and the latter variance for every arc split at sizes \(3\le n\le7\). It also checks the unconditional crossing moments on sizes \(1\le m\le7\).

Execution command: `python verify.py`.

Observed outcome: **PASS: 194 exact assertions, 293194 enumerated matching instances, n=3..7 conditional and m=1..7 unconditional.** This is an exact check for finite sizes only, not a proof for arbitrary sizes; the finite-sum proof in `RESULT.md` covers all integers \(n\ge3\).

No external proof assistant, independent validation, or human review was performed. Originality is provisional against uninspected historical refinements of crossing-enumerating functions.
