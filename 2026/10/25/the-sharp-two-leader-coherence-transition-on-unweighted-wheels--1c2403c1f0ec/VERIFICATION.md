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
# Verification and scope of checking

Run `python verify.py` with SymPy available as specified in `requirements.txt`. This program constructs the unweighted wheel Laplacian directly, deletes both selected leader rows and columns, inverts the resulting matrix over exact rationals and takes its trace. For every \(3\le n\le11\), it compares that trace with the separately derived closed formulas for the hub/rim pair and every inequivalent rim/rim separation (38 exact comparisons). It then checks strict rim-pair ordering, the exact small-wheel threshold table and the positive \(n=8\) symbolic lower bound. The successful run produced:

`VERIFY_OK 38 exact independent grounded-Laplacian trace comparisons; small-n values and positive n=8 uniform bound`

The analytical proof in `RESULT.md`, not a finite loop, establishes the full domain \(n\ge3\): the periodic resolvent is exact, the scalar convexity sign is proved for all positive reals, and the bound is increasing after its first positive integer. The program cannot independently establish novelty or certify an infinite proof. It is not an external audit.
