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

# Reproducing the finite certificate

Run `python3 verify_palindromes.py` from the directory containing the files. It needs only Python 3's standard library. Compare its deterministic one-line JSON output byte-for-byte to `verification_output.json` after trimming no characters; the output includes a final LF.

The checker independently derives the exact 10 state-pair set from the length-256 substitution prefix, checks closure, and generates 10 coded length-128 substitution images. Their aggregate length-1 through length-18 palindrome sets yield the complete count vector, two maximal palindrome witnesses, and missing critical lengths 11 and 18. The prefix search determines the exact onset 196. A separate implementation of the source recurrence checks 4096 initial positions, and a direct 4096-letter factor scan cross-checks the finite spectrum.

These checks form a proof certificate for the infinite statement only together with the factor-cover lemma and central-palindrome reduction in `RESULT.md`. Large-prefix experiments alone would not establish a global absence result. The computation uses exact string comparisons, with no hashes or probabilistic equality tests. No external scientific validation is claimed.
