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

# Reproducibility and verification

Run `python3 verify.py` with Python 3 and NumPy. The script constructs every weighted Laplacian directly from individual edge weights, checks a complete Walsh eigenbasis for uniform designs, tests the claimed optimal values and budget identities, checks eleven points on the critical optimizer segment, and tests the two universal Rayleigh bounds on nonuniform feasible designs for dimensions \(2\) through \(6\) at multiple prices and budgets. It reports `PASS: 2310 checks` on completion.

This finite sample checks independent matrix computations against the analytic formulas and identifies implementation/normalization mistakes. The unrestricted universal proof is in `RESULT.md`; its essential steps are two Walsh Rayleigh averaged upper bounds, explicit attainability, and pointwise equality conditions. No computation alone proves universal rigidity, and no external independent certification was performed.
