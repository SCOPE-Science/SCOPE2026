---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

After translating one singleton label to zero, let A be the n labels in the large part and z the other singleton. Every element of -A and z-A is an edge difference, while every nonzero difference in A-A is a nonedge difference. The induced-embedding criterion therefore makes A-A disjoint from both translates. If -a=z-b, then z=b-a is simultaneously the singleton-edge difference and a nonedge difference inside A, so the two translates are also disjoint. Since |A-A|>=n and each translate has n elements, every host has at least 3n elements. The explicit host Z_3 x Z_n with all nonzero first-coordinate differences is K_{n,n,n} and contains the required induced K_{1,1,n}. The universal argument does not rely on the finite verifier.

## originality

PASS

Fresh searches found the initiating eta paper and no stronger exact K_{1,1,n} theorem. The current public paper record lists unbalanced complete multipartite graphs among its open problems, while its abstract reports exact paths, complete bipartite graphs, selected graph values, and small double stars rather than this family. The full arXiv PDF was not retrievable in this run and the authorized institutional fallback returned a worker-unavailable error, so whole-document noncoverage is not asserted; that access gap is retained as a residual risk.

## value

PASS

The family is a natural unresolved complete-multipartite test case highlighted by the initiating problem, and the proof gives a reusable multi-neighborhood difference-set obstruction rather than an isolated computation. It closes the concrete K_{1,1,5} gap as part of an infinite family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
