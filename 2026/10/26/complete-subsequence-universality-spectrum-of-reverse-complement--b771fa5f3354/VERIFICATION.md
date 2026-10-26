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

The accompanying standalone `verify_rc_universal.py` was run with Python 3 and completed:

`REVERSE_COMPLEMENT_UNIVERSALITY_PASS brute_half_words=35856 q=2:coeff_half_lengths=0..60;q=4:coeff_half_lengths=0..30;q=6:coeff_half_lengths=0..22;q=8:coeff_half_lengths=0..17`

The brute-force check evaluates actual scattered-subsequence universality against every target word in the indicated small ranges and tests the proposed central-involution index identity for each half-word. The formula-coefficient test derives Stirling/surjection coefficients, independently from the seen-mask automaton counting all half-words. The same code checks total counts, exact minimal-length witness multiplicities, and the absence of smaller witnesses over the tested finite ranges. The proof in RESULT.md, not the numerical output, establishes every alphabet and length.

There is no external mathematical verification or peer review. The self-review has passed; an independent audit has not been performed.
