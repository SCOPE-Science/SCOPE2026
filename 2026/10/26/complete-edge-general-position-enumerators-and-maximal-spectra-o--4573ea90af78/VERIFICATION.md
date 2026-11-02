---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Every cycle geodesic is an arc of at most m=floor(n/2) edges. Three selected edges are legal iff each cyclic gap is <=ceil(n/2); four are legal iff every adjacent pair of four gaps sums <=ceil(n/2). A hypothetical legal five-set forces 3n<=5ceil(n/2), contradiction for n>=6. Count valid gap compositions with at most one oversized gap, divide by three initial-edge markings; quartets satisfy alternating gaps (even n) or two complementary adjacent-pair sums (odd). A legal triple extends to a quartet exactly when some gap >=m; otherwise it is maximal. Each 0,1,2-set extends. These identities prove explicit A_n,B_n,M_n and n=7 purity exception. Independent geodesic-mask enumeration checked all 16,376 subsets n=3..13; finite data corroborate universal gap proof.

## originality

PASS

Best-of-knowledge: The general d-position equivalence and extremal number are prior; neither inspected paper directly counts all legal/maximal edge sets with size refinement. A stronger structural criterion could be used to derive these counts but does not state them. Prior maximum-size results are true corollaries of the audited count in the cycle case; the reverse implication is false, and the structural theorem would require nontrivial counting to recover M_n. Priority and access limits explicitly preserved.

## value

PASS

The full polynomial and inclusion-maximal size spectrum answer a motivated enumerative problem on the most basic non-tree graph, revealing exactly where legal sets are pure versus non-pure. Maximality, rather than just maximum size, is an important distinction for graph-position invariants and algorithmic counting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
