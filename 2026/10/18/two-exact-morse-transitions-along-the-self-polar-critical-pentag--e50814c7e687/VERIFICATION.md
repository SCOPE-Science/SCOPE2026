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

# Reproducible mathematical verification

Run `python check_phase.py` using Python 3 and SymPy. The script reconstructs the five vertices, the polar edge normals, the horizontal first moment, the exact area, and diagonal second moments from the polygon formulas. It tests the signed polynomial numerator identities, calculates the resultants in the interior curve parameter, and checks both factorizations exactly. It verifies the uniqueness arguments for the eligible algebraic thresholds and uses rational interval arithmetic for physical-branch and strict-sign certificates at three separating rational samples. A complete successful run terminates with `PASS`.

Proof obligations not delegated to finite computation: the general second-variation Hessian is taken from the cited primary paper; the supporting half-space and root-uniqueness reasoning, determinant/block inertia and implicit-function reduction, and the fact that no zero outside the eliminated candidates is possible, are proved in the result document. Discrete sample values establish signs only after exact elimination ensures there are no omitted crossings. No statement of independent audit, machine-checked formal proof, or higher-order nondegenerate-boundary behavior is made.
