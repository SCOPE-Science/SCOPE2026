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

The result is proved algebraically in `RESULT.md`. The standalone `verify.py` performs exact integer arithmetic and uses independent residue shortest paths to verify the stated formulas across a finite parameter grid.

Run `python3 verify.py`. Expected output:

```text
PASS: 2407 independent shortest-path checks with exact Apéry, genus, Frobenius and pseudo-Frobenius comparisons
```

The program was executed from the packaged directory and produced that output. It compares all residue representatives, evaluates the genus by Selmer's formula, identifies maximal Apéry elements through generator transitions, and, for selected small inputs, enumerates gaps directly. Those checks do not prove the universal quantifiers; the proof in `RESULT.md` supplies the infinite argument. No independent human or external mathematical audit has been performed.
