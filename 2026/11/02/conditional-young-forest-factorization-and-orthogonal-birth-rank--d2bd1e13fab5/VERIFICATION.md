---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

In the uniform independent-parent recursive tree, conditioning on the whole labeled forest of younger vertices fixes internal child-parent edges and the independent events that each component root chooses one of the i old labels; given that, choices of old parent are independent uniform. Each young component contributes its size to S_i-1 with Bernoulli(1/i), proving the product conditional PGF for all n and i, including i=1 and i=n. Each S_j,j>i is measurable from the younger forest; tower property gives E[S_i|later sizes]=n/i and pairwise zero covariances. Two-color Pólya urn yields beta-binomial variance n(n-i)(i-1)/(i^2(i+1)). Double counting ancestors gives the weighted path mean/variance; n=4 joint S2=3,S3=2 witness disproves independence. Independent exhaustive parent enumeration n=2..7 checked complete forest-stratum PGFs and mixed moments, not just marginals. All tree files and blobs reconstructed.

## originality

PASS

Best-of-knowledge distinct combined claim survives comparison with actual relevant sources; precisely prior components are credited, and inaccessible or possibly dominating material is named as a priority risk, not treated as proof of noncoverage. The new fine conditional statement is not a routine algebraic rewriting of existing global path-length mean and variance formulas.

## value

PASS

The conditional full young-forest factorization is a natural fine-grained law for birth-ranked fringe sizes, yielding a diagonal covariance matrix despite nonindependence and arbitrary deterministic birth-weighted total path variances. This supplies useful exact structural information beyond classical unweighted path length.

The dated certificate retains the supplied scientific assessment, sources and limitations.
