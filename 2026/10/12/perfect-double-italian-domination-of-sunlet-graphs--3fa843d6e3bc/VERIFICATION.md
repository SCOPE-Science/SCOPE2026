---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For the stipulated labels 0,1,2,3, the leaf condition forces each pair to cost at least two, with (cycle,leaf)=(0,2) the only equality case. If a center and both immediate cycle neighbors are equality pairs, the center has closed-neighborhood sum two and is invalid. Thus the exceptional indices meet all n centered cyclic triples, each exceptional index serving exactly three centers; at n=3 identical sets of vertices still count as three distinct centers. The lower bound is 2n+ceil(n/3). For the upper bound give every leaf label 2 and the cycle the word (100)^q followed by nothing, 1, or 10 for residues 0, 1, or 2. In each case every centered cyclic triple contains one or two ones, so the closed sum is exactly 3 or 4 at each cycle vertex. There is no restriction at a leaf labeled 2. This verifies all n≥3 under the specified closed-neighborhood condition, not an open-neighborhood variant.

## originality

PASS

The distinct claim is the exact minimum for the closed-neighborhood interval [3,4] perfect double Italian invariant on the cycle's one-leaf corona. The strongest available same-family and general-corona comparisons use different admissibility constraints; the strongest same-invariant comparison evaluates a different graph family. None of the verified statements mechanically supplies the equality-pair obstruction and feasible construction for this invariant. This is a bounded best-of-knowledge conclusion, not proof of priority.

## value

PASS

The cycle with one leaf at each vertex is a canonical unicyclic corona, not an arbitrary finite instance. The answer is an all-orders exact benchmark for the perfect double Italian constraint and identifies the one-extra-unit-per-three-positions obstruction. A researcher comparing ordinary, restrained and perfect variants can use the exact number where the related formulas do not determine it.

The dated certificate retains the supplied scientific assessment, sources and limitations.
