---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For n>=1, m>=3 and every nonempty ballot of size <=2, q=ceil(n/3), the uniform existence criterion is 2n<5q+3. If a score-optimal three-set maximizing coverage still violates JR for candidate x, each winner has score >=s(x)>=q. With >=q wholly uncovered voters, total winner scores <=2(n-q)<3(q+1), forcing a winner with s=q. Coverage-maximal exchanges and equality n=3q force a second exchange increasing coverage, contradiction. In the converse the q singleton-x voters plus n-q pair ballots distributed evenly among ab,bc,ac give all winners scores >=q+1 and a unique non-JR score optimum. The two-seat and singleton-approval boundaries are valid with their stated quantifiers.

## originality

PASS

The exact population-wise if-and-only-if criterion for simultaneous unrestricted welfare optimum and JR under ballot size <=2 and exactly three winners was not found in inspected primary JR/welfare results. It is not equivalent to existence of a JR winner committee or to bounding price of JR; the construction shows that price can be strictly positive. An unindexed direct restricted-profile theorem remains a priority risk.

## value

PASS

The minimal number of voters and nonmonotone congruence-dependent failure profile resolve a natural fairness–utilitarian compatibility question with sharp two-seat and singleton boundary conditions; neither value nor novelty is based just on a computational example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
