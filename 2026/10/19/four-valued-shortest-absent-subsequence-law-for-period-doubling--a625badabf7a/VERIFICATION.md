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

# Reproduction

Run `python3 verify.py` with Python 3 and no nonstandard dependencies. The program checks the valuation and substitution definitions independently; brute-forces all binary subsequences for short prefixes and uses independently calculated suffix-zero counts for many longer prefixes. It prints `PASS` on success.

# Proof and limitations

The all-length mathematical certificate consists of the five proofs in `RESULT.md`: valuation recurrence, the adjacent `01` fusion lemma, exact suffix criterion, terminal-gap valuation analysis, and arithmetic-density summation. No finite test is a substitute for those arguments. No external independent review, audit, or certification was performed.
