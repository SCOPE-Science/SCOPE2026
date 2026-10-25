---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For Cr_n=K_n,n minus a fixed matching, independent zero sets have exactly three possible structures: empty, confined to one bipartition side, or the two endpoints of a single omitted matching edge. No-zero functions have weight at least 2n; two-sided zero case also at least 2n, with n(n−1)^2 equality assignments for the matching zero pair case when n=3. In one-sided-zero case the total domination of positive vertices on the fully positive opposite side requires at least two positive vertices on the zero side, while defense requires a two-label on the opposite side; minimum n+3, attained with two one-labels on zero side and a two-defender opposite at an index among those positive two. These equality conditions give 2n(n−1) for n>=4. For n=3, three disjoint tie cases contribute 1+12+12=25. Independent all-3^(2n) enumeration for n=3,4,5,6 yielded respectively (weight,count) (6,25),(7,24),(8,40),(9,60), including label shapes. The case-split proof establishes all n>=3.

## originality

PASS

The 2019 foundational source was recovered as a full open primary PDF this run; its actual sections on graph families and bounds were compared, not merely its abstract. It does not give the matching-deleted biclique optimal label census.

## value

PASS

Removing one matching is a natural controlled perturbation of the complete-bipartite graph and tests sensitivity of a structured domination invariant. Although the scalar increases only by one, the theorem gives a complete uniform description and nontrivial optimizer multiplicity 2n(n−1), including the exceptional n=3 tie of 25 functions. This structural classification is an independently useful exact graph-invariant fact, not an unsupported tiny-gain headline.

The dated certificate retains the supplied scientific assessment, sources and limitations.
