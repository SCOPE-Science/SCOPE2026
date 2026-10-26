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

# Reproducibility and verification

Execute `python universal_lex.py` with Python 3 and no third-party dependencies. The checker enumerates all words directly for each of 128 independent parameter triples, compares complete ordered output lists, and verifies four larger/longer instances against an independent greedy-arch index.

Expected success marker: `UNIVERSAL_LEX_LINEAR_DELAY_PASS cases=128 emitted_words=38984 high_alphabet_and_long_word_tests=4`. The proof establishes the feasibility invariant and the worst-case delay, which finite tests alone cannot certify. No independent mathematical audit has been performed.
