---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

For finite d>=1, B=sI-C nonsingular M-matrix with C>=0 and s>rho(C), strictly positive immigration η and t>0, the quadratic inverse Laplace equation admits an analytic branch at u=0. J=(B^T)^-1 has J_(i,j)>0 iff the directed C path i->j exists; diagonal strictly positive. Repeated implicit differentiation gives labeled-set recurrence H_i(S)=1/2 sum_l J_(i,l) sum_(nontrivial ordered position splits)H_l(S1)H_l(S minus S1), H_i({a})=J_(i,j_a). All terms nonnegative; induction with l=i proves H_i(S)>0 iff i reaches all j_a. Summation against η>0 gives exact sign/zero of every cumulant. For r>=2, Levy-Khintchine mixed cumulants equal t∫product x_(j_a)ν(dx), giving simultaneous-jump support and disjoint-group independence equivalence. Exact six-type C with links 1->4,5; 2->4,6; 3->5,6, weights 1/5 gives covariances t/25 for all three pairs but third mixed cumulant of 4,5,6 exactly zero. Independently checked exact rational derivative recurrence for these examples including κ(1,4,5)=3t/25. Source 1,588 finite checks through length four do not prove arbitrary dimension/order.

## originality

PASS

The all-order exact limiting-process common-ancestor jump hypergraph, joint-cumulant recursion and six-type pairwise-vs-threewise obstruction are a motivated specialization of known branching motifs; limiting IG process itself is attributed to Wang–Xu–Zhu.

## value

PASS

Complete combinatorial characterization of simultaneous multi-coordinate Lévy jumps at every order for a newly studied canonical coupled multitype subordinator, with a reusable finite exact cumulant recursion and a concrete six-type hypergraph that is invisible to all pairwise covariances. Independent of merely naming covariance dependence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
