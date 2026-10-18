---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

On a quadratic phi with Hessian H and independent equal-variance additive evaluations, literal baseline reuse gives Cov(ghat)=sigma²/h²(I+sum_a 1_Ca 1_Ca^T), while mean is Hx+b+h diag(H)/2. Exact quadratic expectation gives eta²sigma²/(2h²)[tr H+sum_a 1_Ca^T H 1_Ca], so the improvement from all-one sharing is minus eta²sigma²/h² times the signed sum of cut Hessian edges. Taking H=I+epsilon A_G with epsilon rational small enough for SPD and kappa(H)<1+delta reduces exact optimal two-baseline selection to MAX-CUT, with polynomial-size input. Euclidean gradient MSE remains h²/4 sum H_ii²+2n sigma²/h² for every partition. Independent symbolic derivation and all eight labels on a three-coordinate rational signed Hessian reproduced equality and partition invariance; the negative-edge 2D example shows forced splitting may worsen expectation.

## originality

PASS

Brekelmans et al. already derive positive cross-coordinate covariance when a forward-difference gradient reuses a common evaluation at x; this central covariance mechanism is prior. Their full paper analyzes norm gradient error and several fixed experimental designs, not the exact next-iterate H-weighted partition optimization or its signed MAX-CUT equivalence. Berahas et al. similarly treat ordinary finite differences and gradient approximation bounds. Actual Resultary and broader searches did not return an exact H-cut baseline-group design theorem. An unindexed common-random-number optimization could dominate.

## value

PASS

A natural finite-difference oracle-design choice (how to allocate r independent baseline measurements across coordinate gradients) has an exact combinatorial optimization law, with a sharp complexity boundary even for nearly isotropic SPD Hessians. It resolves the mismatch between Euclidean estimator accuracy and curvature-weighted optimization loss; the signed two-coordinate reversal makes that distinction operationally meaningful rather than a routine covariance restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
