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

A shattered S must be independent both in M (all-one trace) and M* (all-zero trace). Conversely primal and dual independence of S permit any trace T by deleting D=S\T: dual independence yields a full-rank basis disjoint from D, then extend T in the deletion. A fully shattered depth-d query tree has no repeat along paths; for any partition E=A∪A^c follow branch label 1 inside A, 0 outside, and a witness basis bounds d≤r_M(A)+r_M*(A^c). Classical Edmonds intersection minmax equates min rank-cut to max common independent-set cardinality, hence Ldim=VCdim. The same partition yields an optimal fixed-sign membership-mistake predictor by counting 1-mistakes in A and 0-mistakes in A^c. This is an all-matroid proof, not extrapolation. Independent uniform matroid cut checks U(4,2), U(5,2), U(6,3), U(7,3), source finite enumerator inspected; loops, coloops and empty E fit.

## originality

PASS

Edmonds intersection minimax and polynomial algorithm are prior results and explicitly credited. Prior Littlestone/thicket theory defines binary tree shattering; general-dimension hardness concerns arbitrary concept classes, whereas this statement specializes to all matroid base incidence classes. No exact matching class theorem located in actual searches or published indexed record comparisons. However older graphic VC and matroid learning papers could contain equivalent formulations. The main contribution assessed is joint static/adaptive equality and simple optimal online fixed-sign learner.

## value

PASS

A natural, broad combinatorial concept class with generally different static and adaptive dimensions unexpectedly has equality, exact polynomial-time computation and a nonadaptive-sign mistake-optimal online strategy; spanning-tree specialization is concrete. Substantive structural theorem beyond merely quoting Edmonds rank minimax.

The dated certificate retains the supplied scientific assessment, sources and limitations.
