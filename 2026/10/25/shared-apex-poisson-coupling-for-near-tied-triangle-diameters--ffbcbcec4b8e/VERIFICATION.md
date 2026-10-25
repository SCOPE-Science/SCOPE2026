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

# Mathematical verification

The identity for the bivariate union-area exponent was checked against independent exact polygon clipping for 900 rational \(c,s,t\) cases. The integrated survival was evaluated by independent SciPy quadrature over positive thresholds for multiple \(c\) and \(\delta\) values. A 1,000-replicate experiment at \(n=700\) used exact uniform barycentric sampling and hull-pair distances for a filled isosceles triangle; observed survival values were within 0.009 of their asymptotic predictions at three positive thresholds.

To reproduce: `python verify.py` with Python 3, NumPy and SciPy. These finite checks validate formulas at tested inputs but do not themselves certify all-angle formulas or weak convergence. Proof of those statements is in `RESULT.md`.

No independent scientific audit has been performed.
