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
The standalone `verify.py` uses only Python 3 standard library. From its directory run `python3 verify.py`. Actual package-development replay yielded three successful lines:

`VERIFY_OK length_optima=19 construction_words=2648 palindrome_profiles=187229 literal_subsequence_checks=24387 shorter_palindromes=157360`

`ARCH_DOUBLING_OK profiles=160874 absent_witnesses=160874`

`GENERATING_FUNCTION_OK lengths=52`

Checks use literal substring-free subsequence embedding for all selected short cases; greedy arches for comprehensive palindrome candidates; exact combinatorial integer convolutions for the generating series; explicit absent-subsequence witnesses; all shorter palindromes within bounded exhaustive searches. The theorem itself rests on the derivation in `RESULT.md`, not on extrapolating finite enumeration. The published palindrome index lemma is a source premise, not independently novel. Independent scientific audit has not been performed.
