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

Run `python3 verify.py` (Python 3 standard library only). Expected output begins `VERIFY_OK`, with exactly \(87\) candidate five-prime integers and group sizes \(71,12,3,1\), followed by the table checksum and explicit six-prime witness. All tests are exact integer arithmetic; no floating-point approximation, randomness, or network access is used.

The calculation tests every prime \(t\) within the mathematically established finite bounds for each \(s\); the proof of exhaustiveness is in `RESULT.md`. Each complement-pair list is constructed twice, by divisor factorization and direct square-root enumeration. Two distinct subset-sum algorithms verify that none of the \(87\) cases reaches the required sum. The explicit omitted pairs in the six-prime example are checked by multiplication, total sum, and direct recomputation of the retained complement-closed divisor set.

**Boundary:** This program is not an exhaustive search over all odd integers or all six-prime integers; the infinite five-prime claim relies on the abundance inequalities reducing the domain to these finite cases. Independent audit has not been performed.
