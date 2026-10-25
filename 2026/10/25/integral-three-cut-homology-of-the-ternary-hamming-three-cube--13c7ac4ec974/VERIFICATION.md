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

## Reproducibility
Execute `python3 CHECK.py` using Python 3 and its standard library. The code checks the graph and the complete dual face lattice, all signed integral boundary compositions, two exhaustive integer unit-pivot boundary reductions, and the resulting ranks and Euler characteristic.

## Observed exact checks
The dual face vector was \((27,351,351,81)\) with no higher nonempty faces. The integer triangle boundary had \(217\) unit pivots and a zero residual, leaving \(134\) cycle generators. The tetrahedral boundary in those coordinates had \(81\) unit pivots and zero residual, leaving homology of ranks \(53\) and \(108\). The integral chain condition and degree conversion passed.

## Limits
This finite calculation is exact for \(H(3,3)\). It does not certify any dimension-uniform formula, original-complex homotopy type, or independent verification. The published results cited in the report concern related graph families but do not themselves certify this computation.
