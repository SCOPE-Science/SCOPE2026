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

The proof was reconstructed from the assigned RESULT.md. A final one-block vertex is universal, so \(\gamma_P=1\). For \(v\in B_i\), all one-blocks and zero-blocks through \(A_i\) are initially observed. Any later zero-block of size at least two contains two unobserved false twins, which can never be the first forced vertex; if all later zero-blocks are singletons, successive vertices of \(B_{i+1},B_{i+2},\ldots\) force them in order. For \(v\in A_i\), \(i\ge2\), every observed later one-vertex sees at least one unobserved vertex in \(A_{i-1}\) and one in \(B_{i-1}\), so no force starts. For \(v\in A_1\), the same false-twin obstruction is exact and the singleton-block forcing chain proves sufficiency. I independently replayed the defining closure test for every connected creation sequence of orders \(2\) through \(12\): 2,047 graphs and 22,528 singleton placements, with zero criterion mismatches. The finite replay is corroborative only; the block proof establishes the infinite statement.

## originality

PASS

The closest primary work located on connected power domination proves polynomial-time solvability on threshold graphs, but the accessible primary material does not state the exact set of every optimal singleton location or its count. Since a connected threshold graph always has a universal vertex, knowing only that an optimum of size one exists does not imply which non-universal singleton vertices also work. Targeted Resultary searches returned no equivalent threshold-block classification. Full text of the closest threshold-section source was not available through the open routes tried; one authorized institutional retrieval attempt then returned an operational error and was not retried or bypassed. That is retained as a residual overlap risk rather than negative novelty evidence.

## value

PASS

The theorem gives an exact all-optima description and count for a natural graph class, refining a minimum-value/algorithmic result into a structural classification of where a single PMU can be placed. The false-twin boundary identifies precisely when non-universal optimal locations exist. This is a motivated exact invariant rather than a tiny-instance check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
