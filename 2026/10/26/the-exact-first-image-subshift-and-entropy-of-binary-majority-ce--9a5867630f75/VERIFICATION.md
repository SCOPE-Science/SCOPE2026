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

The accompanying Python 3 standard-library-only verifier reconstructs the labeled pair-state automaton from the binary majority rule. It confirms the twelve deterministic states (including sink), verifies the exact six-step pair-reset counts `110, 40, 24, 12, 8, 4, 0`, enumerates all minimal forbidden words through length seven, and compares the finite language independently against both raw input enumeration and avoidance of the six proposed exclusions through output length thirteen.

It also verifies the integer matrix identity \((M^5-2M^4+M^2-I)\mathbf1=-e_{15}\) and, by an independent exact Faddeev–LeVerrier calculation, the stated characteristic polynomial. Root values are bracketed and approximated numerically only after the algebraic identities are established.

Execution command:

```text
python3 verify.py
```

Observed output:

```text
VERIFY_OK: 12 deterministic states; reset ambiguity [110, 40, 24, 12, 8, 4, 0]; six minimal words; 14 exact block counts; exact matrix identity; lambda=1.78459893336865; h=0.57919370279722
```

The exact finite-state transition calculation proves the reset lemma for every six-letter word. The arbitrary-length forbidden-word classification follows by induction, while the recurrence and entropy follow from exact matrix multiplication and Perron theory. The finite raw-block enumerations are cross-checks, not infinite-length proofs. No independent external audit has been conducted.
