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

# Verification details

Run `python3 verification/check_medians.py` using Python 3 and its standard library. The program independently enumerates the finite binary cut minimum, compares it against the closed parity formula with rational arithmetic, tests each binary and integer-valued signal in its stated finite scopes, and checks two-step dynamics and equality witnesses. The reproduced output was:

```
PASS {'unweighted_binary': 64516, 'weighted_binary': 26908, 'real_signal': 12250, 'dynamics': 12250, 'witness': 224}
```

The proof for all sizes, all strictly positive real edge weights and all real signals is the coarea/threshold argument in RESULT.md; finite computations are not universal proofs. The statement is about a one-input variation ratio, not a two-input Lipschitz constant. No independent scientific audit has been performed. Literature comparison includes an abstract-only relevant conference source, leaving a stated originality risk.
