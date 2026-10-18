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

# Reproducibility and proof limits

From a directory containing `verify_congruence.py`, execute:

```
python verify_congruence.py
```

This uses only the Python standard library. On completion it prints `VERIFY_OK`. The program independently checks exact profiles using endpoint weights and direct enumeration of admissible Ferrers-block relations for parameter vectors \((1,1)\), \((1,2)\), \((2,2)\), \((2,3)\), and \((3,3)\). It also brute-forces all raw binary relations for vectors \((1,1)\), \((1,2)\), \((2,2)\), and evaluates all defining WHB axioms on the induced algebras for \((1,1)\) and \((1,2)\).

For \((2,2)\), the four coefficient counts are \(1213,70,12,1\), totaling \(1296\). For \((2,3)\), the coefficients are \(11632,309,50,8,1\), totaling \(12000\). The checker confirms these values from different representations. The endpoint formula for arbitrary factor sizes and the uniform asymptotic probability inequality are mathematical arguments in `RESULT.md`, not extrapolations from finite experiments. The quoted duality and congruence correspondence are external published premises and are not independently re-proved by the checker. No independent external audit is claimed.
