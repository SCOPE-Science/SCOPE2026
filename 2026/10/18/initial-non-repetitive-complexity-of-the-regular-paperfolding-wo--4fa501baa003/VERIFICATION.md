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

The finite regression check is provided as `verify.py`. Run `python3 verify.py` with Python 3.10 or later; no third-party packages are needed. The checker uses exact integer encodings for binary factors and compares two independent definitions of the word.

Observed output:

```
VERIFY_OK lengths_checked 337 max_n 8191 prefix_bits 25000
```

The exhaustive comparisons cover every positive length up to 320 and seventeen further lengths at dyadic boundaries and nearby transitions. The 24 distinct length-eight factors and the equal length-fifteen factors at starts 8 and 24 are also checked directly.

Finite tests do not establish the infinite theorem. The nonalternation lemma, parity separation, decimation equivalences, monotonicity, and induction appear in RESULT.md; all were checked algebraically. The available primary literature establishes related factor counts and appearance functions but not, among the inspected statements, this exact first-duplicate law. One highly relevant historical paper on canonical factor positions was inspected only at abstract level; equivalent results in its full text are a remaining literature risk.
