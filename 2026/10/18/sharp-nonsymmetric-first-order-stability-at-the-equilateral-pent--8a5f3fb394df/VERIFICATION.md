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
# Verification of the local width-distance expansion

Analytical critical checks are the smooth closure Jacobian \(\sin(\pi/3)\ne0\), the four differentiated non-constant vertex-pair distances, the edge-normal minimum-width principle, and the three-chamber max formula for \(m=\max\{\delta,\alpha,\delta-\alpha\}\). All are stated with the needed quantifiers in RESULT.md.

Run `python verify.py` using standard Python 3. The verifier independently constructs the polygon, evaluates ten vertex distances and five widths, and compares these with the predicted order-one expansions for 45 configurations in nine angular chambers/rays and five decreasing scales. It checks quadratic error bounds numerically and the algebraic linear lower bound, printing `VERIFY_OK`. Floating-point diagnostics do not establish infinitely many cases, a uniform error constant, historical priority, or a global polygon inequality.

No independent audit has been performed. The local proof has been reviewed for correctness, originality against named inspected sources, and mathematical value; remaining historical priority risk is described in REVIEW.md and AUDIT.json.
