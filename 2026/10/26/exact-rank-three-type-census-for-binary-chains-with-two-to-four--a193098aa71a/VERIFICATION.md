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

# Verification record

The packaged code `verify.py` is standalone Python 3 standard-library code. `verification_output.txt` records a successful execution against the actual packaged version. It constructs every word with exactly \(k\in\{1,2,3,4\}\) red marks and all blue-gap parameters between zero and seven. For all 37,440 capped instances the code compares a direct prefix/suffix character implementation to independent bit-packed right-append dynamics; all match. Then it computes equivalence-class counts and shortest representatives, checking 51, 310, 1865 and 11196 signatures and sharp relative minimum lengths 13, 19, 25 and 31. The one-red row is a calibration, not part of the novel claim.

The independent implementations and finite exhaustive count are machine-replayable. The logical characterization of rank-three equivalence, the seven-point monochromatic cutoff and concatenation congruence are mathematical steps set out in `RESULT.md`; finite tests at the \(7\to8\) boundary are additional checks and not a substitute for those infinite proofs. The three- and four-marker optimum lengths are explicitly relative to fixed-marker strata.
