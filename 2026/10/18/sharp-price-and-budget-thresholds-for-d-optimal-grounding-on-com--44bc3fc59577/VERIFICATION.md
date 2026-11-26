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

Connectivity and B>0 give positive definiteness on the whole feasible simplex. The log determinant has strictly negative second derivative in every nonzero gain direction, since it is minus the squared Frobenius norm of the conjugated diagonal direction. Thus the optimizer is unique; within-class permutation invariance forces common gains without imposing a restriction. The two zero-sum class subspaces and the constant-vector two-by-two block give the stated determinant even for a singleton class. On the budget line b=(B−pa)/(tq), the endpoint derivatives simplify to pQ(t)/[Bq(B+pqt)] and R(t)/[Bt(B+pq)], where R(t)=p²(B+q)t−(B+p)(B+pq). The denominators are positive. Q has a unique positive zero when B<q² and strictly positive values for all t>0 when B≥q², including B=q². Strict decrease of the derivative makes t_lo<t_hi, gives a unique interior root between the thresholds, and puts each threshold equality at its indicated endpoint. At t=1, Q(1)=B[B+q(p+1−q)]>0 and R(1)=B[p(p−q−1)−B], giving the inclusive cutoff and star corollary. Independently checking the endpoint expressions and matrix decomposition reproduces the example; a separate symbolic and exact finite comparison confirmed the identities and 30 full-matrix determinant cases. No finite check is used to infer an unrestricted parameter theorem.

## originality

PASS

The checked work covers the D-optimal framework, continuous determinant design, and several closely matching models with other objectives or differently assigned conductances. The explicit support diagram for unrestricted grounding on unit K_{p,q}, including both price thresholds, the disappearance of the low-price regime at B=q², and the equal-price budget cutoff, was not covered by the checked specific statements or their immediate implications. No originality is assigned to generic log-det concavity, symmetrization, tree-count interpretation, or standard endpoint optimality criteria.

## value

PASS

The exact thresholds locate where a whole class goes unsupported in a natural determinant design over all independent gains. They distinguish small-budget two-sided support transitions from the high-budget disappearance of the low-price endpoint, and give a usable equal-price budget rule for stars and other unbalanced bipartite networks. This class-level support information is not supplied by an optimization routine or by analogous trace-inverse or eigenvalue designs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
