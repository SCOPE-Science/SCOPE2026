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

# Reproduction and proof checks

Run `python3 verify_swap.py` using Python 3. The script independently enumerates all nonempty even-length substrings and compares the number of ones in the two halves. It tests every three-marker four-gap tuple with total zeros at most 10, both special families through parameter 34 (with direct enumeration through 14), every two-marker gap triple with at most 13 zeros, and every adjacent swap in words of length at most 11 having at most two occurrences of a minority symbol. Actual execution reported PASS.

The infinite assertion depends on the proof in RESULT.md: it does not follow from enumerated cases alone. In particular, the lower-support asymptotic order follows from a per-row parity-discrepancy bound for the gap sum. This is not an independent audit or certification.
