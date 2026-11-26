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

Affine normalization preserves independent uniform edge fractions and the area ratio. In cyclic order the sampled shoelace sum on the normalized quadrilateral is the ratio, since the host area is 1/2. Independently checked the moments by conditioning: set c=p+q-1, d=p-q, S=X+Z, D=X-Z, with X,Y,Z,T the independent centered Uniform[-1,1] side coordinates. The shoelace expression gives F=4(R-1/2)=C+(W+H)T+(W-H)Y with C=-dD, W=(S+cD)/2, H=dS/2+c. The joint law of (S,D) allows either sign to be flipped separately. Thus E[F]=0; in the conditional cube only C^3+2C(W^2+H^2) survives averaging over T,Y, and both terms average to zero. In the conditional fifth power, C^5 and (20/3)C^3(W^2+H^2) likewise average to zero. The remaining term is (16/3)C(W^4+W^2H^2+H^4); the only contribution after taking the (S,D) expectation is -(8/3)c^2d^2 E[S^2D^2], with E[S^2D^2]=2/5-2/9=8/45. Dividing by 4^5 gives the stated negative fifth moment. If d=0, flipping T,Y reverses F; if c=0, flipping X,Z reverses F. These transformations preserve the joint law. Off those lines the nonzero fifth moment excludes reflection symmetry. The frozen checker was inspected, not executed; the conditional-moment calculation supplies an independent exact check. Scope excludes degenerate hosts, pooled boundary sampling, and claims about a density everywhere.

## originality

PASS

Pass for the all-quadrilateral third/fifth moment result and exact full-law symmetry classification, not for the mean or parallelogram special case in isolation. The strongest same-model overlap located is confined to parallelograms; nearby boundary-sampling literature differs in model or limit and does not give the claimed obstruction or its zero locus.

## value

PASS

This solves a natural finite-distribution question on the full affine shape family: area complementation in law singles out exactly hosts with parallel opposite sides, even though usual skewness vanishes for every host. The fifth moment provides a sharp exact obstruction and the involutions explain why full symmetry, not merely a moment cancellation, holds on the two lines. The result neither assumes nor proves Euclidean reflection symmetry of the host.

The dated certificate retains the supplied scientific assessment, sources and limitations.
