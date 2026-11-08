---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For every finite n≥2, positive theta and every nonnegative initial vector, the explicit s,p decomposition gives s_next=a(p)s² and p_next=G(p); theta_min/2≤a≤theta_max. The separable strictly concave Phi has gradient log(theta_i(1-p_i/2)); the multiplicative update makes its gain at least ||G(p)-p||_1²/2 by the symmetric KL identity, Pinsker and bounded negative Hessian. Asymptotic regularity, finitely many face fixed points, and the ratio test for initially positive vanishing coordinates enforce the unique KKT water-filling direction p^S (including theta ties). The uniformly convergent logarithmic series defining s_*(p) obeys s_*(Gp)=a(p)s_*(p)^2, so s_m/s_*(p_m)=(s_0/s_*(p_0))^(2^m). This establishes extinction, convergence to p^S/lambda_S on the separator, or blowup with stated logarithmic rate. All finite invariant Borel probabilities concentrate on fixed points by recurrence and absence of other recurrent trajectories. Verified from actual RESULT.md e4b357..., script blob dda794...; independent 70 parameter trials ×60 projective steps matched monotonicity; no finite experiment was treated as the universal proof.

## originality

PASS

Qualified PASS: the complete original same-map journal article classifies fixed points and two-dimensional curves and includes partial n-dimensional invariant regions but does not state all-finite-dimensional projective convergence, water-filling selection, global uniformly computable separator or invariant-measure classification. The novelty claim excludes the generic homogeneity identity; a general unindexed discrete-replicator theorem remains a priority risk.

## value

PASS

The exact uniformly approximable global boundary, all-face support selection and invariant-probability classification solve a natural complete orbit-classification problem for a previously studied homogeneous operator in every finite dimension, not merely a routine computation of existing equilibria or the generic radial cocycle. No uniform convergence speed or elementary closed separator is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
