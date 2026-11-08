---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

The query domain consists of fixed-position pair comparisons, not comparisons of named labels. A shattered set of edges must form a forest because a cycle can be oriented as an impossible strict inequality cycle. Conversely adjacent-position queries realize all 2^(n-1) signs by direct sums of decreasing runs, proving VCdim=n-1 for every n>=1. For n=1..7 the independently re-enumerated separable concept counts 1,2,6,22,90,394,1806 and fresh exact version-space recursion independently found complete decision trees at depths 0,1,2,4,6,8,10; 2^d<=|S_n| supplies matching upper bounds. Original source stores a complete depth-ten tree in certificates.json and the inspected verifier checks its leaf witnesses; the independent depth recursion does not rely on its stored tree. Concatenating s independent seven-position decision trees under direct sums gives Ldim(S_7s)>=10s and a >=3s+1 VC gap. Finite calculations establish only the seven small cases; the all-n assertions follow from the stated structural arguments.

## originality

PASS

PASS best-of-knowledge for the exact adaptive dimension table and resulting unbounded separable-permutation adaptive/static gap; neither Schröder enumeration nor generic closure bounds alone imply those depths. The claimed novelty is not the classical separable class or the elementary forest bound. Exact historical priority in alternative comparison-learning terminology remains unchecked.

## value

PASS

The precise first strict gap n=4, exact entropy-tight adaptive dimension through n=7, and certified unbounded separation give a natural exact learning-theoretic invariant for a prominent permutation class. It is a motivated finite cutoff with an infinite structural consequence, not an arbitrary census of permutations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
