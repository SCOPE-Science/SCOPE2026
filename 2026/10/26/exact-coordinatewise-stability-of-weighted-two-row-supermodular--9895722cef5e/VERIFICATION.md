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

Run `python3 checker.py` using Python 3 and only its standard library in the same extracted directory. An executed run printed `EXACT_RATIONAL_CHECKS_PASSED=12883`. The standalone program uses `fractions.Fraction`, checks rational weighted pooled isotonic projections against exhaustive contiguous-block partition minimization on small instances, reconstructs finite-cell Jacobian rows, checks row-sum sharpness and finite perturbations, and exercises equal and strongly imbalanced weight cases. These finite computations do not prove any universal quantified claim.

The mathematical proof in `RESULT.md` independently establishes the weighted square-completion reduction; the consecutive-block Jacobian formulas; the globally valid maximum row-sum bound; strict full pooling that attains the maximal local Jacobian norm at a finite pair of inputs; and the complete attainable range over positive weights. Those are analytical deductions, not assertions inferred from the checker. Numerical or exact-rational enumeration is not treated as exhaustive over arbitrary dimensions and weights.

Limits: only complete real two-row arrays, prescribed column order, finite strictly positive least-squares weights, and unweighted coordinatewise perturbation norm. The scientific review is not an independent audit.
