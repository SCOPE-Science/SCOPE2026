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

# Reproducibility and limits

Run `python3 verify_direct.py` and `python3 verify_templates.py` from a directory containing these two standalone files. Neither uses third-party modules or external downloads.

`verify_direct.py` independently enumerates all minimal-cardinality dominating sets for ladders of lengths five through twelve, tests the adjacent-token exchange condition and computes connected components. Its completion marker is `DIRECT_EXHAUSTIVE_LADDER_PASS`.

`verify_templates.py` implements the closed-form word templates for every integer half-length from four through twenty-six, checks domination, compares all actual token slides with the independently specified predicted adjacency list and verifies the edge counts. Its completion marker is `SYMBOLIC_TEMPLATE_AND_EXCHANGE_PASS`.

The complete infinite proof is the combinatorial argument in `RESULT.md`: degree-bound and overlap budget, forbidden double empty columns, exhaustive optimal-word classification and explicit neighbor comparison. Finite test ranges alone would not prove this infinite classification. Originality has not undergone independent scholarly review; some plausible prior full texts were inaccessible.
