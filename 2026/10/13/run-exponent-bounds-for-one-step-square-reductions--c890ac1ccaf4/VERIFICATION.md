---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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
# Verification

Run `python3 verify.py`. It constructs the distinct reduction outputs directly by deletion of the second copy and finds runs by testing all factors for their least period and one-letter nonextension. For every one of the 4,094 nonempty binary words through length 11 and 3,279 nonempty ternary words through length 7, it checks that the out-degree equals the sum of run slots and that this sum is at most the sum of the integer Lyndon charges, which is at most the word length minus one. A successful run prints `CHECK_OK binary_words 4094 ternary_words 3279`.

The finite enumeration is supplementary. The universal result follows from the two-way match-interval correspondence, Fine–Wilf periodicity, and the published disjointness of the Lyndon-root start sets (see `RESULT.md`).
