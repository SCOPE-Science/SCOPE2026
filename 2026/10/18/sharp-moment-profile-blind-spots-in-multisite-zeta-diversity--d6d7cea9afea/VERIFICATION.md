---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

For incidence sets A_i⊆[N], fixed sample W of k sites, binomial(Z_k,r) counts r-species groups all containing W. Thus F_r(k)=C(N,k) E C(Z_k,r)=sum_{t>=k}C(t,k) H_r(t), where H_r(t) aggregates size-t intersections of r species. Invert the triangular binomial transform to obtain H_r(t)=sum_{k>=t}(-1)^(k-t) C(k,t)F_r(k), including k=0 where Z0=S. First moment retrieves individual ranges; mean+variance gets second binomial moment hence pairwise ranges. Two explicit models with N=3,S=5 have Z1 laws (0,3,3) and (1,1,4), identical first two moments at k=1 and identical laws for k>=2 but different third factorial moment. A second N=4,S=3 model has Z1 (3,1,1,1) vs (0,2,2,2) with matching first two moments and same k>=2. For S<=2, 0/1/2-supported laws are determined by first two moments; N<=2 has at most two equiprobable site-richness outcomes. At N=3,S<=4, the sole possible triple collision in range 0..4 is (0,3,3) versus (1,1,4), and feasibility of two-site intersections excludes equal second profile. Hence minimum N+S=7 and sharp coordinatewise boundaries. Independent exact site incidence calculations reproduced both witness moment lists and the unique triple collision.

## originality

PASS

The basic binomial inversion is classical, acknowledged explicitly; the novel combined theorem asserts sharp loss-of-information boundaries for all-depth mean-and-variance profiles of common-species richness.

## value

PASS

This is a motivated identifiability limit: common-richness moments are ecological observables and exact first/second curves are commonly summarized. The smallest site-species configurations where those full profiles hide different distributions identify a natural information boundary and supply explicit sharp obstruction models. The inversion is elementary, but the minimal witnesses and boundary theorem are independently useful, not merely a known table recalculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
