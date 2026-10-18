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

The finite statement can be regenerated from `verify.py` and `SPECTRUM.tsv` using `python3 verify.py`. The program uses prefix doubling for suffix-array order, a linear adjacent-LCP computation, exact extension-set enumeration for all LCP cores, and direct containment tests of each output. It checks the complete spectra and ten full-output digests. It also checks the sequence against a separate binary decimation recurrence, compares the complete antidictionaries to direct all-substrings enumeration at the two smallest stated levels, and tests both enumeration methods on pseudorandom finite words with a fixed seed.

All calculations are exact string operations and integer arithmetic; there are no numerical approximations or statistical estimates. The mathematical candidate-reduction argument appears in `RESULT.md`. The finite computation covers precisely the claimed integer range, not an infinite extension. Independent audit and independent validation have not been performed.
