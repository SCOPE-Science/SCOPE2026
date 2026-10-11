---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The determinant and singular-locus calculation was reconstructed from the displayed matrices. Differentiation factors the gradient into the two singular lines plus exactly four isolated points, and the projective Hessian has rank three at each isolated point, so they are ordinary nodes. On each line, the transverse quadratic discriminant is \(256a^2(a^2+2a+t^2+1)\), giving exactly \(t=\pm i\) as the pinch points and, after completing the square, the Whitney form \(W^2-a^2h=0\). At the line intersection the discriminant is \(256a^2b^2(1+(a+b)^2)\), yielding \(U^2-a^2b^2=0\). The 3-by-3 minors of the two symmetric matrices show that each representation has one line identically rank two and the other generically rank three with drops exactly at its two pinch points. The inspected symbolic verifier checks these identities directly.

## originality

PASS

Originality passes. Helsø's Example 9.6 gives the same quartic, its two double lines, four isolated nodes, and two nonconjugate symmetric-matrix representations whose rank-two loci differ. The inspected example does not identify Whitney pinch points, local analytic normal forms, or the precise coincidence between intrinsic pinch points and representation-specific isolated rank drops. Fresh Resultary search returned the audited theorem as the exact same-example hit and no earlier configuration-specific local stratification.

## value

PASS

The distinction between intrinsic surface singularity type and representation-dependent determinantal rank is geometrically substantive for symmetroids. Pinpointing the four Whitney pinch points and showing exactly how either symmetric representation reveals only two of them clarifies a concrete ambiguity already highlighted by the source, and the line-intersection germ completes the local stratification of the named example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
