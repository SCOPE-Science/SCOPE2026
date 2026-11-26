---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For W=aI+bJ, put R²=a²+b². Then the balanced metric operator is N R^(2−2/N) times the identity. At a scaled orthogonal matrix, left/right orthogonal invariance of entropy forces its ambient gradient to be radial (reduce by orthogonal multiplication to RI and use conjugation invariance there). The pair quotient at equal singular values is N R^(2−2/N); scaling gives the gradient (d−1)(1−1/N)W/(2R²). Combining this with the diagonal gradient gives the two ODEs with the claimed c. The boundaries 1 and the positive solution of Na(a−1)=c trap a, while B=|b| keeps its positive initial value as a lower bound and satisfies B′≤c B^(1−2/N). Thus the orbit is complete, invertible, and B diverges, since bounded B would have a positive lower bound on B′. In the clock dτ=R^(2−2/N)dt, the stable equation for a−1 has forcing ca/R²→0, so a→1; the equation for B²(a−1) has limiting damping N and forcing c, giving the stated lag. In physical time (B^(2/N))′→2c/N, hence B has the asserted equivalent. This yields the full-rank normalized direction, loss equivalent, and log coefficient −d(d−1)(N−1)/(4β), with no claim of generic behavior. Independent finite checks (`python3 review_checks/finite_checks.py 2`) compared ambient entropy directional derivatives and integrated with log(B/B₀) as clock in depths 2, 3 and 5. These are normalization and rate checks, not substitutes for the asymptotic proof.

## originality

PASS

The shared entropy and flow geometry, generic unboundedness for N>2, and unboundedness of the free energy on a static zero-loss family are prior. In the inspected sources, none gives or implies the joint quantitative asymptotics for this finite-temperature conformal-skew trajectory. The pass is for the trajectory and its rates and direction, not for the entropy formula or an assertion about generic escape.

## value

PASS

The conformal-skew family is selected by the compatibility of equal singular values and a skew perturbation of the observed diagonal, not by a numerical parameter choice. The result gives an explicit benchmark where every singular value escapes, completion loss nevertheless tends to zero at a sharp rate, and the normalized limit has full rank. In particular it supplies concrete finite-temperature depth-two trajectories without purporting to address general depth-two or generic dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
