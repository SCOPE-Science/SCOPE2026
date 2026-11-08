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

For n>=3,a>=1, the exact 2^n halfspace inequalities define the one-sided stretched cross-polytope. The candidate John parameters from the positive root of (n+1)c²+[2na/(a-1)-(a-1)]c-a=0 give b²=(a-c)(1+c)/n, r²=[1-2c/(a-1)]/(n-1); both facet classes are at support 1. Normalized facet contacts with orbit masses (a-c)/(a+1) and (1+c)/(a+1) have zero mean and covariance I/n, proving global John optimality. For the outer ellipsoid, two explicit branches separated at a*=(n+1)/(n-1) contain every vertex and admit nonnegative isotropic contact designs; in the second branch the -e1 pole lies strictly inside. Their log volume derivatives match at a*, but second derivative jumps by (n-1)^3/[4n(n+1)]; semiaxis limits establish the volume ratio. Independently recalculated facet and vertex support equalities across n=3,4,7 and five a values each; exact contact identities in the proof, not finite examples, certify unrestricted global uniqueness.

## originality

PASS

Qualified PASS: Henk’s general John/Löwner isotropic contact characterization is the certificate, not a claim of new general theory. Horwitz quadrilateral ellipse results address n=2, intentionally excluded from independent novelty. Existing resultary summaries on capped cubes, parity halfcubes, spiked symmetric edge polytopes have different vertex/facet systems and do not imply the one-sided orthoplex formulas or exact screening threshold. Potential unindexed asymmetric bipyramid or optimal experimental design equivalent remains.

## value

PASS

This one-axis deviation from the regular cross-polytope is a canonical minimal break of central symmetry. Giving both all-dimensional extremal ellipsoids, a contact-set phase transition that screens one vertex while retaining all John facets, and an exact non-C² volume singularity is a natural structural convex-geometric classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
