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
# Verification

The mathematical proof is contained in `RESULT.md`. The accompanying `verify.py` performs three independent finite checks:

1. It enumerates every binary relation on the labeled chains of sizes \(1,2,3,4\), tests forward confluence directly from its quantifiers, and independently tests the final-segment/weakly-increasing-row-maxima characterization.
2. It explicitly enumerates weakly increasing row-maxima sequences through \(n=10\) and checks their weighted sums against the Gaussian-binomial formula.
3. It checks both standard Gaussian-binomial recurrences through ambient size \(30\), then checks the first eight displayed frame counts.

Run:

`python3 verify.py`

Expected terminal line:

`VERIFY_OK 67010 exact assertions; exhaustive all relations through n=4`

The exhaustive relation enumeration ends at four worlds because there are \(2^{n^2}\) relations. It is a regression check for the general proof, not evidence for untested sizes. No independent audit has been performed.
