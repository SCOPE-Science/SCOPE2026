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

On a loopless DAG, global directed 1-WL updates by old color and multisets of in- and out-neighbor colors, equivalent to C2 by standard counting-logic/refinement characterization. Independently enumerated EVERY upper-triangular adjacency mask (topological labelling exists for any DAG), n=1..6 mask counts 1,2,8,64,1024,32768, synchronizing colors across all same-n graphs and exactly deduplicating by directed isomorphism preserving stable colors. Recovered unlabeled DAG types 1,2,6,31,302,5984 and directed-WL/C2 buckets 1,2,6,31,302,5983, precisely one bucket with two nonisomorphic types at n6. Explicit witnesses have two oriented-transitive triangles versus a connected 6-cycle with sources/intermediate/sinks; each quotient class has two vertices, neighbor-color signatures identical while underlying connectivity proves nonisomorphism. The full exact exhaustive enumeration and finite-class completeness are independent of packaged logs and prove the n<=6 assertion; no assertion about n>=7.

## originality

PASS

Best-of-knowledge originality PASS: exact claim-versus-prior implication comparisons, including its aliases and stronger possible coverage, were made using identified primary material and the recorded semantic search. No decisive full-claim coverage was found; negative searches alone are not proof of novelty. The special-case known ingredients are explicitly credited.

## value

PASS

The onset of C2 nonidentification among directed acyclic graphs is a natural boundary for low-dimensional logic and graph-refinement methods. An exact first failure and a unique obstruction (together with class count 5983) is a meaningful finite classification distinct from routine listing of DAG counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
