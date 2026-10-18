---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

In H_n (n>=2) defined by a_i~b_j iff i<=j, no induced 2K2 occurs. Any induced path with at least five vertices contains two disjoint first/last edges inducing 2K2, so all induced paths have at most four vertices; an independent set meets each such path at most twice. Conversely, if S of size>=3 contains edge a_i b_j (i<=j), every third a_k or b_l supplies an induced 3- or 4-vertex path containing the triple using the index comparisons k<=j or k>j, l>=i or l<i; hence S fails. Thus S is monophonic position iff |S|<=2 or independent. Every independent k>=3 set is represented uniquely by k distinct increasing indices, split at B-prefix/A-suffix r=0..k, giving (k+1)C(n,k) and the complete enumerator; maximum n with n+1 canonical cuts when n>=3, while n=2 six two-sets. Fresh independent induced-path enumeration and exhaustive subsets n=2..6 (16+64+256+1024+4096 =5456 masks; generated paths 3,13,35,75,140) confirmed the exact test/polynomial. The bound for all n is structural, not based on the finite experiment.

## originality

PASS

Based on source-level and current-literature comparison, the complete surviving claim is not established by the named prior results. This is a best-of-knowledge priority judgment, not a guarantee of global novelty.

## value

PASS

The canonical twin-free bipartite chain/Ferrers graph has a natural induced-path avoidance invariant. The theorem characterizes every allowed subset and its complete cardinality polynomial, including the exceptional n=2 maximum family; the scalar maximum n alone would be weaker and potentially known. This gives a useful exact benchmark for monophonic-position counting on chain graphs, not an arbitrary tiny sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
