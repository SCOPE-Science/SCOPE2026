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

# Verification

The exact analytic argument is contained in `RESULT.md`, particularly the character-orthogonality identity (1), the three symmetrization inequalities (2), derivative identity (3), and the equality-characterization step. It applies to all compact abelian groups with character order at least seven or infinite order.

Run `python3 checker.py` with Python 3 and the standard library. The checker was executed against this package and produced:

```
PASS 4060 randomized finite-group cases + special orders; root= 0.7925172139743404 sharp= 2.8088401654743964
```

The program checks 3,500 random complex-coefficient cases and 560 complex extremizers over orders 7, 8, 9, 11, 16, 32 and 47. It compares direct character sums against the aperiodic-correlation identity, verifies the sharp inequality numerically, evaluates the cubic root by bisection, and checks explicit ratios for orders 4, 5 and 6. These are finite numerical checks, not an exhaustive certificate for arbitrary coefficients, character order, or compact group. The general conclusion follows from the written proof. No independent review is represented by this record.
