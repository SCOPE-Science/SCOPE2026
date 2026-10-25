---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

In a binary cube a total mutual-visibility set is exactly a set with no distance-2 pair: a distance-2 selected pair blocks both length-2 paths between their two common neighbors, while if none exists a shortest path can greedily avoid selected internal vertices. The parity halves of Q7 are independent copies of the 64-vertex halved cube H with edges at Hamming distance 2; maximal visibility means independent domination in BOTH halves. In H a closed neighborhood has 22 vertices; independent centers distance 4 have intersection size 6, distance 6 disjoint, with triple distance-4 intersection size 1. Three independent neighborhoods cover <64; four dominate iff exactly two disjoint distance-6 pairs, giving union size 64. Fix one center, choose its distance-6 partner in 7 ways and a complementary 3+3 partition in 10 ways; gives 64*70/4=1120 quadruples per parity, hence gamma_lower=8 and 1120^2=1,254,400 labeled achievers. Independent exhaustive enumeration of all parity independent dominating 4-sets gave precisely 1120, 70 through zero. The known maximum 16 is separately supported by a length-7 simplex code and elementary distance bound, not an unproved inference from the minimum.

## originality

PASS

Best-of-knowledge distinct contribution after direct comparison with relevant same-invariant primary results, strong alternatives, indexed tables and a Resultary semantic search (minimum maximal total mutual visibility hypercube Q7 halved cube independent dominating). Known minimum values, feasibility reductions, algorithms and finite tables are credited, while the claimed additional structural enumeration is assessed separately. Unread high-relevance literature and alternative indexing are retained as residual risks, not silently treated as absence.

## value

PASS

Determines a naturally posed lower total-visibility invariant for the first nontrivial seven-dimensional cube and exactly describes and counts every extremizer. Relates the independence complex facets to binary code geometry and proves nonpurity with a sharp eight-versus-sixteen witness, a useful finite classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
