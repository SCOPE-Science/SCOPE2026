---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

The normalized uniform spherical annulus has E X=0 and covariance kappa^-1 I with kappa=(d+2)(1-r^d)/(1-r^(d+2)); therefore the affine L2 projection's reproducing kernel is 1+kappa x·y. Convex symmetry of the row integral and existence of negative kernel values show precisely outer-sphere rows maximize its L-infinity norm, with sign-of-kernel extremizer. Ball-coordinate beta density and radial subtraction give the stated H_d incomplete-beta norm formula. The scaled radius S_r=kappa R_r has strictly rising lower and strictly falling upper support endpoints with density proportional to s^(d-1); its CDF has a single crossing and its mean strictly decreases. Thus it strictly dominates later radii in stop-loss order on the relevant thresholds; strict convexity of phi(s)=E(sU_1-1)_+ for s>1 proves L_d(r) strictly decreases to the sphere endpoint. Taylor at r=0 yields leading beta coefficient times r^d. Uniform radial concentration and uniform sphere-coordinate Gaussian limit give sup_r|L_d(r)/sqrt(d)-sqrt(2/pi)|->0. Independent radial/sphere quadrature checked d=2,3,4 at several radii and d=3 endpoints 253/125 and 5/3, not an all-dimensional proof.

## originality

PASS

Best-of-knowledge source comparison of exact mathematical implications, not merely titles; published SCOPE/Resultary semantic corpus queried and primary source material inspected as specifically recorded. No inspected stronger prior result covers the distinctive final claim, subject to explicitly named access and priority limitations.

## value

PASS

The sharp endpoint norm of the simplest affine least-squares projector over an annulus varies nontrivially with the concentric hole: an exact formula, rigorous monotonicity and first small-hole sensitivity supply useful design and approximation constants. Domain and invariant are natural; not a routine renamed ball/sphere constant, nor a claim about higher-degree projections or eccentric holes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
