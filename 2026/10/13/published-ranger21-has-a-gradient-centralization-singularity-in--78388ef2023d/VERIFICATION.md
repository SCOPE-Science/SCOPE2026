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

Reconstructed the actual Algorithm 4, whose GC operation removes the mean of the current gradient and whose stable-decay/Norm-Loss vector divides eta_t*lambda by sqrt(mean(vhat_t)) with NO epsilon while the adaptive update has positive epsilon. For a d-coordinate row, d>=2, f(theta)=0.5||theta-b1||^2, theta_delta=c1+delta q with q centered unit vector, clipping inactive under |c-b|<tau|c|, the centered first gradient is delta q and first bias-corrected second-moment mean is delta^2/d. The norm of the regularization displacement after the update is eta_1^2*lambda*sqrt(d)*abs(||theta_delta||-1)/abs(delta). This grows as a nonzero constant /|delta| if eta_1,lambda>0 and |c|sqrt(d)!=1; at delta=0 denominator vanishes with nonzero numerator. The adaptive step tends to zero because its eps guard is positive and numerator O(delta), so cannot cancel. Symbolic independent check for d=2,c=2 returned lim(delta*displacement)=sqrt(2)*eta_1^2*lambda*(2sqrt(2)-1). Assumptions ensure nonzero scheduled first rate; default code implementations with explicit guard are not accused.

## originality

PASS

Ranger21 original arXiv Algorithm 4 was read in its printed mathematical form; it does not state this strongly convex one-step failure or inverse-distance blowup, while its denonimator omission is visibly real. The original Stable Weight Decay source and later first-party Flax version include numerical safeguards and therefore need not fail. Resultary related optimizer stability results concern different algorithms/normalizations and do not imply the published Ranger21 row-gradient-collapse singularity.

## value

PASS

A reproducible strongly convex smooth counterexample exposing unbounded/undefined first updates in a published, widely referenced optimizer equation—and distinguishing it from corrected implementations—is a motivated analysis of a concrete well-definedness defect. Its inverse-distance asymptotic is stronger than a bare 0/0 check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
