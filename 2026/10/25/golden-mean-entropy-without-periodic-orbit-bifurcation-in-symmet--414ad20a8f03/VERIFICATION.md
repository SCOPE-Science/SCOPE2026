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

The standalone script `checks/verify.py` uses Python and SymPy for exact polynomial algebra and rational/integer arithmetic. Its recorded output is `checks/verify-output.txt`. The checker computes both transition matrices and characteristic polynomials, enumerates true fixed points of the circle map through periods one to fourteen, verifies the exact boundary-address corrections to the traces, and independently compares symmetric interior-hole periodic counts through period twelve. It also constructs the common refinement graph, computes its strongly connected components, and checks affine six-return branches and the two boundary three-cycles.

All exact finite checks passed at packaging. The analytic argument in `RESULT.md` is required for claims covering all positive periods, all interior parameters, entropy, Hausdorff dimension, and the uniqueness of the full new periodic orbit set. No finite computation can replace those steps, and no independent mathematical validation has been performed.
