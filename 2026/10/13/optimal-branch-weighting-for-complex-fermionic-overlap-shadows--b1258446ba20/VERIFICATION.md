---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The physical trial and disjoint ancillary Slater state are orthonormal branches. Born probabilities weight the diagonal physical sector by lambda and ancillary sector by 1-lambda, while a cross-branch first moment scales as sqrt(lambda(1-lambda)); normalized estimator has the asserted first moment. Rescaling the exact diagonal second-moment operator of Zhao et al by 1/[4lambda(1-lambda)] gives b[1/lambda+S/(1-lambda)]-p0. S belongs to [1/(eta+1),1], so strict convexity yields lambda*=1/(1+sqrt(Sbar)); gain b(1-sqrt(Sbar))^2. The trial-equals-target Slater witness S=p0=1 requires the worst-case variance at least b/[lambda(1-lambda)]-1, attained uniquely for lambda=1/2 by the source sharp equal-weight upper bound.

## originality

PASS

Low introduced coherent ancillary augmentation and Zhao et al give the complete equal-weight source spectrum and variance, neither an arbitrary premeasurement branch probability nor its multi-target average design. Reweighted measurement changes the Born distribution as well as estimator; the new variance and opposite ensemble/minimax optimizers cannot be read directly from the equal-weight numerical bound. Similar squared-overlap shadows treat a different observable. Novelty is conditional on exact ideal-measurement assumptions, not a universal optimal quantum protocol.

## value

PASS

The exact branch-probability formula is a design rule for a reused shadow dataset across targets; it quantitatively shows when sacrificing the universal minimax choice improves ensemble-averaged complex overlap variance. The benchmark of strict gain versus unique worst-case robustness identifies a genuine experiment-design tradeoff. Calibration of Sbar remains outside scope.

The dated certificate retains the supplied scientific assessment, sources and limitations.
