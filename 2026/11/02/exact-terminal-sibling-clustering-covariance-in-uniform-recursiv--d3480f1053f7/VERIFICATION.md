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

# Verification and limits

The exact attachment model and the one-step change identities are written out in `RESULT.md`, including the terminal-parent event and the \(F_{n,3}\) overlap term. Algebraic substitution in the second-moment recurrences proves the candidate polynomials for all stated integer sizes after the displayed base values. The included `checker.py` uses only Python's standard library and exact integer/rational arithmetic; it exhausted all \((n-1)!\) recursive trees for each \(2\le n\le8\), tested the conditional increment identities tree by tree for \(2\le n\le7\), checked every accessible factorial moment, and tested the polynomial recurrences for \(5\le n\le200\). Its actual output was:

```
PASS: 5017 exact integer/rational assertions; n=2..8 exhaustive; polynomial recurrences n=5..200.
```

This is finite verification, not exhaustive checking of all sizes and not an independently performed audit. The infinite family is justified by the induction in `RESULT.md`. No machine formalization, central limit theorem, or historical-priority certificate is claimed.
