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

Run `python3 verify_phase.py` from this directory with Python 3 (standard library only). The script calculates all affine EFX inequalities for each of the seven named allocations using `fractions.Fraction`, checks their exact feasible parameter intervals, and verifies their interval union. It also enumerates all \(62{,}720\) distinguishable type-count distributions at each of the rational values \(39/2\), \(20\), and \(41/2\), finding no EFX allocation at those tested points. The exhaustive enumerations are corroboration only: they do not replace the universal argument for the entire open interval in `RESULT.md`.

Confirmed output:

```
P1: range r in [7, 13], lower_binding=[], upper_binding=[(4, 2)]
P2: range r in [11, 19], lower_binding=[(2, 1), (2, 3), (2, 4)], upper_binding=[(1, 2)]
P3: range r in [21, 23], lower_binding=[(2, 1)], upper_binding=[(1, 2)]
P4: range r in [23, 25], lower_binding=[(2, 3)], upper_binding=[(1, 2)]
P5: range r in [25, 38], lower_binding=[(2, 1)], upper_binding=[(3, 2), (4, 2)]
P6: range r in [32, 39], lower_binding=[(2, 1), (2, 4)], upper_binding=[(3, 2)]
P7: range r in [39, infinity], lower_binding=[(2, 1), (2, 3), (2, 4)], upper_binding=[]
No EFX at r=39/2: 62720 exhaustive type-count allocations checked
No EFX at r=20: 62720 exhaustive type-count allocations checked
No EFX at r=41/2: 62720 exhaustive type-count allocations checked
All exact checks passed. The nonexistence proof for every 19<r<21 is analytic, not inferred from sampling.
```

The affine interval endpoints are inclusive in the checker. The theorem assumes strictly \(r>7\); thus the interval labelled `[7,13]` in the symbolic checker contributes only \((7,13]\) to the theorem. Exact arithmetic eliminates floating-point boundary ambiguity. The checker does not certify literature priority, general chore instances, or an external independent audit.
