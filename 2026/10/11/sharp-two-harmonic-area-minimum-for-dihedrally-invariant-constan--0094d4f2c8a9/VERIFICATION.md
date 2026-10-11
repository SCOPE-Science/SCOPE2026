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

# Computational reproduction and limits

Run `python3 verify.py` using Python 3.10 or later and the standard library. The program prints `VERIFY_OK` if the following deterministic tests succeed: the normalized cubic critical-point formulas and positive curvature contacts for each odd order in a stated finite test set; exact endpoint/interior formula agreement for multiple rational test parameters; independent Fourier-support quadrature versus the claimed area; and comparisons with normalized feasible coefficient vectors sampled at many directions. The program requires no downloads or other files.

The full proof is analytic in arbitrary odd \(n\ge3\) and arbitrary real \(w>0\), and appears in RESULT.md. The finite tests are falsification checks only; they neither enumerate every admissible coefficient pair nor prove global optimality. The derivative-sign argument and explicit cubic maximization supply the infinite-parameter proof. No independent audit or external certification was conducted.
