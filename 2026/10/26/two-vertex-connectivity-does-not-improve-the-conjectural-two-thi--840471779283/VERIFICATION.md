---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For n>=6 the crossing-transposition sum of K_{2,n-2} is C(S_n)-C(S_2)-C(S_{n-2}); on each S_2×S_{n-2} branch of Specht lambda it has scalar equal to sum of the removed two Young-diagram contents minus c(alpha), with alpha=(2) horizontal strip or (1,1) vertical strip. Optimizing two-box Pieri scores yields 2 for tau=(2,2,1^{n-4}), 6-n for sigma=(2^{n/2}) when n even and 7-n for sigma=(2^{(n-1)/2},1) when n odd. Consequently lambda_min(tau)=2n-6, lambda_min(sigma)=3n-10 even or 3n-11 odd, with ratio 2/3+positive O(1/n). Independently enumerated all valid two-box Pieri removals for n=6..30 and confirmed scores; no full group representation construction needed to reconstruct the general content proof. K_{2,n-2} remains connected after any one vertex deletion, hence is genuinely 2-vertex-connected. The result is an upper obstruction on any uniform constant, not proof of Alon lower conjecture.

## originality

PASS

Alon proves conjectural comparison in selected graph classes and demonstrates 2/3 optimality via star graphs, which have cut vertices. The present witness family K_{2,n-2} stays two-vertex-connected while ratios approach 2/3, so the obstruction has strictly stronger graph-class scope than the star example. Exact K_{2,n-2} Specht minima may exist in older complete-bipartite interchange literature and remain the main risk.

## value

PASS

A natural strengthening of a sharp spectral comparison conjecture is to impose 2-vertex-connectivity to remove star-type bottlenecks. This explicit infinite 2-connected bipartite family rules out such an improved size-independent constant, a motivated negative boundary theorem. It is not a proof of the conjectured bound itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
