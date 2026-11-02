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

# Reproducible checks

Run `python3 verify.py` with Python 3 using only the standard library. The direct Rule-18 update enumerates all \(2^n\) inputs for \(1\le n\le16\). For every one of the \(131070\) output words in those lengths, it checks exact agreement with the two-matching Fibonacci formula. It independently forms a four-state de Bruijn transition matrix and checks its trace for every output for \(1\le n\le11\). It also checks the unique zero-output global maximizer, second-largest fiber and equality cases for \(7\le n\le16\).

Expected terminating marker: `VERIFY_OK 131070 outputs checked; direct enumeration + formula; transfer traces for n<=11`.

The unrestricted theorem for every \(n\ge7\) is justified by the complete zero-run bijection and elementary Fibonacci inequalities in `RESULT.md`. Finite exhaustive checks are not an infinite proof. No independent audit or external verification has been performed.
