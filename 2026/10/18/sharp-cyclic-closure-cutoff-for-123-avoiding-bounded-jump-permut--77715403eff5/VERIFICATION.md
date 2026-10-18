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

# Reproduction and limits

Run `python3 verify.py` in the same directory as this document. Only Python's standard library is used. The expected four output lines appear in `verify_output.txt` and finish with `VERIFY_OK`.

The verifier uses a direct triple-loop definition of classical pattern \(123\) and a separate adjacent-difference predicate. It enumerates all permutations for \(3\le n\le8\) and \(1\le m\le4\), comparing counts with an independently coded memoized state recurrence. It also verifies the exact near-boundary counts \(1,4,35,338\) for \(m=2,3,4,5\) and no examples one length beyond the proposed boundary. The explicit formula is checked for \(2\le m\le40\), including deletion of zero, one, or two highest labels.

The all-parameter result is established in `RESULT.md` by an endpoint lemma, a cyclic closing-edge inequality, an explicit extremal construction, and equality-case rigidity. Finite tests cannot establish nonexistence outside tested parameters. No independent external audit has been performed; no result beyond the theorem's stated pattern, parameter and rooted-reading scope is verified here.
