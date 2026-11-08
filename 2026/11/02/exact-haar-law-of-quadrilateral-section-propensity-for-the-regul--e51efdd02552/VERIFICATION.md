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

For ordered projected tetrahedron heights h1<...<h4, precisely the offset slab (h2,h3) cuts four cross-partition edges. In any of 48 congruent signed-order normal sectors, Q=(X-Y)/(X+Y) for X>=Y>=Z absolute coordinates. Put t=Y/X, s=Z/X; the spherical area density is (1+t²+s²)^(-3/2) dt ds, giving f_T(t)=12t/[pi(1+t²)sqrt(1+2t²)]. Integration yields the stated survival function for every 0<=q<=1; elementary integration gives Haar-mean 0.298746285571..., distinct from Cauchy-Steiner width-biased plane mean 0.288535543072.... Domain: nondegenerate regular tetrahedron and Haar normal, uniform intersecting offsets, generic normals; endpoints have no atom. Independently computed 100000 random projected normals: empirical mean .299585 and survival at q=.45 .24179 versus analytic .240859; this checks only finite samples, not the integral proof.

## originality

PASS

The complete Haar orientation distribution of the normalized interval of quadrilateral-producing offsets is not implied by known slicing-chamber structure, tetrahedron chord distributions, random silhouettes, or the previously known width-biased affine-plane marginal; comparison is claim/implication-based. Best-of-knowledge PASS, with residual risk from older integral-geometric stereology.

## value

PASS

Q(u) is a canonical conditional geometric probability for parallel sections; its full exact orientation law determines every threshold and exposes a substantive difference between orientation-first and invariant-affine-plane sampling. This is not a mere recomputation of one known marginal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
