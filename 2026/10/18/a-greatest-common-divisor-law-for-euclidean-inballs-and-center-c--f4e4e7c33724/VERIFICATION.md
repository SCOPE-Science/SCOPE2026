---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For every p,q>=2, an intrinsic-radius-r ball satisfies X_ij>=r sqrt(1-1/pq) and adjacent Monge slacks>=2r, because projected coordinate normals have norm sqrt(1-1/pq) and mixed normals norm 2. The nonnegative Z=(X/r)-alpha dual identity has strictly positive lambda_ab=min(qa,pb)-ab and pi_ij=pq times interval overlap, so equality requires ALL slacks 2 and overlap cells Z=0. The floor-covariance/sawtooth integral yields T=(p²q²-p²-q²+g²)/6; common boundaries k/g leave g-1 parameters in [-1,1]. This proves the stated inradius, complete cube of incenters and count pq+1-g+e of tangent facets (assuming the Erickson-Kretschmann facet theorem). The p=q=n specialization matches known square radius. Independently recomputed 144 ordered p,q pairs and dual identities with exact fractions; finite checks do not prove the universal theorem.

## originality

PASS

The published square result settles p=q entirely; a square-only formula cannot determine p≠q or coprimality uniqueness. Other polytope inball records concern transportation or unrelated constraint families and do not dominate this exact Monge inball.

## value

PASS

Rectangular normalized Monge polytopes are canonical combinatorial/optimization polytopes. Their full inball and center-set topology depend discontinuously on the number of shared row/column interval boundaries gcd(p,q); this coprimality uniqueness and exact tangent-contact classification are natural genuinely new nonsquare information, not a renaming of the prior square theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
