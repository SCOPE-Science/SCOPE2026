---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The previously established classification of all maximal class-<=k nilpotent subsemigroups by ordered k-layer partitions is explicitly separated from the new optimization. For a fixed ordered layer vector, an element is exactly a partial injection with all arrows strictly increasing in layer number; its rank is the number of arrows. Decompose the injection into directed chains; after forgetting direction each chain is a block meeting each layer at most once, and conversely sorting block colors supplies a unique increasing chain. This is a rank-preserving bijection to colored transversal set partitions and proves the EGF coefficient formula. Recolor a marked item between two layer sizes a>=b+2 while tracking h blocks meeting both colors; the exact ratio (b+1)(a-h)/[a(b+1-h)] >=1 in each rank/block stratum, with strict inequality when h>=1. Every intermediate imbalance is improved, and rank-one strictness excludes unbalanced maximizers. An independent direct enumeration of all partial injections for ordered layers up to n=6 matched the distinct transversal-partition recurrence and coefficientwise inequalities. The enumeration is a test, not a proof for arbitrary n,k.

## originality

PASS

Qualified PASS: the 2005 Ganyushkin–Mazorchuk full preprint proves classification of maximal bounded-class nilpotent subsemigroups by ordered partitions, which is an indispensable prior hypothesis and is not claimed new. Araújo–Bentz–Konieczny Theorem 4.19 solves largest *commutative* nilpotent subsemigroup (balanced class-two null case) only. No inspected source derives the simultaneous all-rank coefficient inequality or k>=3 maxima and counts for arbitrary layered partial injections. Earlier 1994/1995 direct classification papers are not fully compared and remain a concrete priority risk.

## value

PASS

Maximal cardinality at a fixed nilpotency class is a natural extremal invariant in finite transformation semigroups. A rank-preserving chain/partition bijection and simultaneous coefficientwise inequality settle every bounded class k>=3, the complete rank polynomial and all maximizing ordered-layer shapes, beyond a k=2 textbook balancing computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
