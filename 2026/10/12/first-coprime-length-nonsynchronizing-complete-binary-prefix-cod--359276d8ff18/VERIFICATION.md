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

For the complete binary prefix codes with two through nine words, execute `python3 enumerate_trees.py` and `python3 enumerate_expansions.py`. Each enumerator must reproduce the `counts` and `nine_word_exceptions` fields of the two embedded JSON result files. The first program enumerates ordered full trees by splitting the root and tests subsets of literal decoder states. The second enumerates trees by expanding leaves and tests mergeable pairs by backwards closure, so the two constructions do not share the decisive algorithms.

All four exceptional code sets have word-length gcd one; `expansion_results.json` contains a closed, non-diagonal pair-transition certificate for each. For every listed pair, apply transitions from the actual code set on both input bits and check that the next unordered pair still appears and has distinct states. These direct checks passed for every certificate. The total number of full ordered trees in each row equals the corresponding Catalan number.

The finite enumeration establishes exact counts only for the stated range. The public literature survey cannot exclude unpublished or unindexed equivalent findings; full text of the particularly relevant 2019 source was not accessible. No independent audit has been performed.
