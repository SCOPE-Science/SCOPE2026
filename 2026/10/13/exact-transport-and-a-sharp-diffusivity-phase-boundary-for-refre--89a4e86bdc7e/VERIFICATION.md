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

# Computational and analytical verification

The included `check.py` is the complete reproducible Python 3 source. It uses SymPy for symbolic rational identities and standard-library exact fractions for independent fixed-horizon and truncated-renewal checks. Run `python check.py` (SymPy installed). In a fresh replay, the result was:

```
PASS: 193 finite/exact checks; universal signs follow from the proof.
```

Exactly nine symbolic identities verify the speed simplification and derivative, balanced variance and derivative, endpoint variance and derivatives, and zero-refresh limits. For five rational continuation biases, two frozen-block moment functions were compared independently with all lengths from 1 through 16 (160 checks). For twelve rational bias/refresh pairs, independent geometric-tail sums were compared to the exact renewal speed and variance (24 checks). Total 193. Truncated-tail comparisons use a strict stated tolerance and are not infinite proofs. The continuum inequalities and the CLT require the analytical arguments in RESULT.md. No external or independent scientific audit has occurred.
