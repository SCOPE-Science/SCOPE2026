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

# Verification and reproducibility

The theorem is proved algebraically in `RESULT.md`; numerical checks are cross-checks, not substitutes for an infinite proof.

Run `python3 verify_dynamic.py` to count **every** input word through exact subset-image dynamic programming at lengths \((n-1)^2\) and \((n-1)^2+1\) for each \(2\le n\le12\). The program checks that the shorter layer contains one reset word and that the next layer contains \(n^2-4n+7\).

Run `python3 verify_insertion.py` to construct every possible one-letter insertion into the displayed word and independently simulate each initial state for all \(2\le n\le30\). All claimed counts pass. The expected outputs, including terminal success markers, are preserved in `verification_dynamic.txt` and `verification_insertion.txt`. Execution requires only Python 3 standard library.

No computation establishes novelty relative to unread literature. Independent audit has not been performed.
