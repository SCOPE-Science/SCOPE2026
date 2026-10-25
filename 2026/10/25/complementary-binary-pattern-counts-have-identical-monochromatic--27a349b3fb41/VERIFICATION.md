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

# Reproduction and proof limits
Run `python3 verify.py` in a Python 3 environment with only the standard library. Successful execution prints `VERIFIED:` with the tested counts. The check reads counts from binary expansions, independently complements the patterns and reflected integer arguments, and checks the formula as an exact integer identity, not merely modulo two.

Tested: all \(240\) binary words of lengths \(2\)–\(7\) containing both digits; \(256\) test integers for each word (\(61{,}440\) point checks), and \(20\) arithmetic progressions per word (\(4{,}800\) progression reversals). Four residue moduli are compared for every progression. These finite tests do not cover unbounded lengths, starts, or differences; the full statement depends on the digitwise algebraic proof in `RESULT.md`.

No independent audit has been performed. The open-access preprint's original Problem 4 was inspected; the later journal article was not fully inspected.
