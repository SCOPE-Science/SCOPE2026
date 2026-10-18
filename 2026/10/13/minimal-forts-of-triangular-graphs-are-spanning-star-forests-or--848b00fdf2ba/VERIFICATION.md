---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For a selected edge set F in T_n=L(K_n), represent it as H=([n],F). A nonselected edge ab has exactly deg_H(a)+deg_H(b) selected neighbors; a fort therefore excludes a degree-(0,1) pair. An isolate-free minimal fort must be a minimal edge cover, precisely a spanning star forest. If H has isolates, selected degrees cannot equal 1 and a cycle exists; its edge set alone forms a nonempty fort, forcing minimality to leave exactly one cycle of length ell<n with all other original vertices isolated. Every proper nonempty subset of either listed type fails the fort condition. Standard labeled SET-of-stars and CYCLE species yield EGF exp(zu²/2+u(e^(uz)-1-uz))-1 +(e^u-1)/2[-log(1-uz)-uz-(uz)²/2], and binomial(n,3) minimum three-edge forts for n>=7. Independently tested ALL subsets for n=2..6 by direct triangular graph adjacency and all nonempty proper subsets; recovered 1,3,11,60,308 and n5/n6 size distributions. Source reported n7=1659 but the n7 2^21 brute force was not independently rerun; the all-order structural proof, not an experiment, supports the theorem.

## originality

PASS

Minimal-fort theory is established prior work (Cameron et al.). Becker et al. calculate all minimal forts for different graph families and their general hypergraph perspective, while Afzali et al. report a scalar failed zero forcing number on Johnson graphs. Neither the inspected full fort-count paper nor a scalar extremal formula implies the star-forest/proper-cycle shape classification and all-size EGF for T_n. The directly relevant Johnson article was inaccessible in full, which is preserved as a substantive priority risk, not automatic rejection.

## value

PASS

All inclusion-minimal forts of the canonical line graph L(K_n)=Johnson J(n,2) are classified geometrically, and their exact labeled size distribution is computable via a closed EGF. This is substantially richer than a previously studied minimum or failed-forcing scalar and provides explicit input for zero-forcing/fort-cover models at every order.

The dated certificate retains the supplied scientific assessment, sources and limitations.
