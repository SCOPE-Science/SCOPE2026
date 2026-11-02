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

# Reproduction and boundaries

Run `python3 checker.py` with a standard Python 3 interpreter. Successful completion prints `ALL_CHECKS_OK` followed by the independently derived Dedekind counts, full-support issue-state counts, labelled frame counts and a semantic cross-check on up to three worlds.

The algorithm explicitly checks each downset against all of its members, computes the fifth Dedekind number by independent two-slice consistency, and enumerates every factive, positively introspective and negatively introspective issue-family assignment on up to three labelled worlds. It uses exact integer arithmetic throughout.

The program does **not** enumerate all larger frames, certify historical novelty, establish the infinite limit, or provide an independent external audit. For unbounded world sizes use the four-step written proof in `RESULT.md` and the classical Dedekind growth bound stated there. The six-world count is from a recurrence using the established sixth Dedekind number, not a six-world exhaustive computation.
