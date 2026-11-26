---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The update preserves identical colors among vertices in the same initial class and color cohort. For clique clones the only exceptional adjacency is to vertices of the same current color, which cannot be a successor. Thus a trajectory on the induced graph of one representative per cohort lifts exactly, and equality of entire representative vectors is equivalent to equality of the actual labelled states. A fresh direct adjacency replay evolved all 225 nonempty palette pairs, found the first repeated full color vector, matched the stated activation criterion in every case and recovered all six coefficient matrices. Substitution of W_i(m)W_j(n) was checked as a formal polynomial identity in the powers of 2, 3 and 4, not only for sampled sizes; the total is 4^{m+n}. The four-cycle states have disjoint sets of four along each orbit and hence N_{0,4}/4 orbits. For n>=2 a singleton clique palette 0 with independent palette {1,2} takes exactly three steps, and clones give all larger admissible sizes. For n=1,m>=2 clique palette {0,1} and independent color 2 take two steps, and the coefficient table excludes third entry. A consecutive-color edge at m=n=1 takes one step and the table excludes more. Finally B_4/4^{m+n} tends at fixed m to [W_4(m)+4W_3(m)+2W_2(m)]/4^m. Both the fixed basin and N_{3,1} have leading term 4(2^m-1)4^n for fixed m, giving the conditional limit; a full clique palette has probability tending to one as m grows, irrespective of n.

## originality

PASS

Credit exact recurrent-state and period coverage on the m=2 tripartite slice, as well as known CCA dynamics. The closest same-day Resultary record does not cover arbitrary clique size or the all-size first-entry distribution, basin criterion and fixed-core limits. The frozen finding does not claim the m=2 coarse period phenomenon as separately new. The full content is not covered by the matching specialization or the primary sources that could be checked.

## value

PASS

The complete split family has a natural clique–independent asymmetry. Classifying activity by antipodal exposure and quantifying both recurrent and transient classes give more than a three-step bound or a periodic-orbit count. In particular the persistent activity probability depends on the core, while conditional on freezing almost every initial coloring takes the full three updates for large independent sets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
