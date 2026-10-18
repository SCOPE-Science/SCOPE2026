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
# Verification notes

Run the included script with `python3 verify_period_doubling_inr.py`. It uses only the standard Python library and contains two distinct generators of the same infinite sequence, one by direct substitution and one by valuations. Each factor comparison is exact byte-string equality.

Executed test output:

`VERIFY_OK; independent_generators=2; exhaustive_lengths=1..256; extra_lengths=18; maximum_length=8192`

The test covers all initial lengths through \(256\), eighteen larger breakpoint and scale lengths, both the first later collision position and its uniquely matched earlier start, the equality of the two word generators, and the predicted halving recurrences. It does not enumerate infinitely many lengths; the exact induction in the proof establishes the infinite result.

The manuscript distinguishes initial non-repetitive complexity from global non-repetitive complexity and acknowledges previously tabulated dyadic prefix attainment.
