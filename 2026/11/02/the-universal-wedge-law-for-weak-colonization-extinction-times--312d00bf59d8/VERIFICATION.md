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

# Verification evidence

Run `python3 CHECK.py` in this directory using Python 3.9 or newer. The checker requires no third-party packages. It independently implements the finite absorbing-chain recursion, the analytic edge/wedge formula, and exact rational comparisons. Its documented deterministic suite covers all labeled graphs with four and five vertices and sampled graphs with six to eight vertices, totaling 1,318 graph instances; it also checks the four-vertex tree coefficients and 51 sizes of the wedge coefficient.

The proof of infinitely many cases is in the accompanying `RESULT.md`: its backward generator identity, uniform-subset edge counting, and the positive-coefficient polynomial identity. The checker is supporting finite evidence only, not an exhaustive enumeration of graphs at all sizes and not a substitute for verifying the polynomial identity.

The numerical comparisons were executed from the bundled checker successfully. The open-source literature provides the model and context; historical-priority conclusions are conditional on inspected material. Independent external review is not performed.
