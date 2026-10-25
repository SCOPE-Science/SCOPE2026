---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Spherical/Gaussian polar factorization and bivariate absolute-normal kernel yield expectation by identical edge pairs c, endpoint-sharing pairs s-2c, disjoint remainder. With d=n-1, r_d=E||g||, delta=1/3+(2sqrt3-4)/pi>0, lambda=4/3+(4-4sqrt3)/pi>0, Cov=4/pi*(d-d²/r_d²)+(delta s+lambda c)/d. For trees s=3n-4+sum_v(deg_T-1)(deg_S-1)>=3n-4, c>=0; simultaneous equality iff nonleaf sets disjoint and no common edges. Explicit n4 pair {01,02,13} & {03,12,23}, extending by leaves at 0 and 2 realizes every n. Gamma ratio gives limit 3delta-2/pi and strict negativity.

## originality

PASS

The exact angular kernel and individual-tree width-variance extremizers appear in earlier published SCOPE Resultary record, read in full; it treats one graph at a time and proves path/star self-variance extrema, not optimizing a paired labeled-tree cross-covariance with disjoint nonleaf and edge sets.

## value

PASS

The co-oriented width covariance of two shapes is a natural mixed geometric invariant; all-pair negative extremality and rigid graph-label classification reveal anticorrelation despite fixed volume and combinatorial type. This is a structural extremum, not a tiny numerical gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
