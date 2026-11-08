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

For n>=2, token vertices split into hub h={a1,a2}, 2n cross vertices x_(r,i), and binomial(n,2) within-large-part vertices y_(ij). Explicit adjacency makes a dominating set equivalent to a partition of columns T/S/U (0/1/2 selected x vertices), a selected within-part edge set E containing the forced clique binom(T,2), and—when h omitted—positive E-degree at every vertex of T union S plus at least one selected cross vertex. These are necessary and sufficient, so hub-including sets factor as z sum binom(n,t) z^binom(t,2)(2z+z²)^(n-t)(1+z)^(M-binom(t,2)); hub-free sets are counted via inclusion-exclusion over uncovered T/S vertices, with t>=2 vs t<=1 branch. The minimal hub count occurs only t=1 or2, yielding n(n+3)2^(n-3) (including rational-written n2=5); direct equality case analysis of |D|=n-t+u+e proves hub-free minima only n2,3,4 with counts 4,15,24, so total minima 9,33,80, n(n+3)2^(n-3) thereafter and all contain hub from n>=5. No claim for higher tokens or other domination notions.

## originality

PASS

Best-of-knowledge priority judgment after direct mathematical comparison; prior material credited and residual risks recorded. The feasibility criterion and gamma=n specialization are prior, but no ordinary domination generating polynomial or exact hub-free multiplicities were stated in the inspected primary sources. A prior general characterization could be specialized as a starting point, not a precomputed formula.

## value

PASS

For a natural family of two-token graphs whose minimum domination number has only recently been determined, the complete ordinary domination polynomial is an exact cardinality invariant useful for counting all feasible solutions. The closed optimal-set multiplicity and n=5 hub-forcing transition provide a sharp structural classification beyond the known single minimum number. Counting by forced cliques and edge-incidence degree makes it nontrivial despite an earlier feasibility lemma.

The dated certificate retains the supplied scientific assessment, sources and limitations.
