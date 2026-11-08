---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

From the actual balanced double-star vertex-metric RESULT.md, the zero-sum powered-distance quadratic form splits into leaf-residual, symmetric and antisymmetric sectors. The symmetric scalar coefficient f_q(p)=q3^p-(q+1)2^p-q has a unique zero p_q in (1,2] because (3/2)^p-1-2^-p is strictly increasing, with p_1=2. The antisymmetric 2x2 block has determinant qg_q(p) and g_q>0 up to p_q for q>=2 by the stated derivative and strict-concavity comparison t=2^p<2+2/q at the root. Tree-edge cut decomposition gives strict p=1 negative type, and strictness propagates below 1; above p_q an explicit symmetric vector gives positive quadratic form. The endpoint zero-sum null vector is leaves +1 and two hubs -q, yielding Gram rank 2q for q>=2 versus 2q+1 below; q=1 path has rank1 at p2. Taylor inversion gives p_q=1+[2/(3log3-2log2)]/q+O(q^-2), strictly below corresponding one-hub star exponent. Independent BFS distance matrices, sector signatures and critical null ranks confirmed q=1..6, not used to prove all q.

## originality

PASS

Doust–Weston arxiv:0705.0411 gives exact one-hub star exponent and general tree bounds; Li–Weston arxiv:0901.0695 supplies strict lower-p theorem; Caffarelli–Doust–Weston arxiv:1008.3418 treats general tree generalized roundness, and Sánchez arxiv:1108.0451 supplies a generic finite-metric determinant route. None inspected explicitly states the balanced two-hub all-q equation, nullspace, embedding dimension and asymptotic. Resultary bistar findings concern zero forcing or symmetric edge polytopes, not shortest-path powered negative type. Potential unindexed equivalent evaluation remains.

## value

PASS

The balanced double star is the simplest natural graph with two genuinely branching hubs after the exactly solved one-hub star. Its exact powered negative-type exponent, unique equality direction, Hilbert embedding rank loss and sharp q^-1 approach to one quantify an interaction between two branching clusters. The strict inequality versus each induced star proves the result is not merely a reparameterization of the star formula. This all-size structural classification is useful for metric embedding and generalized-roundness comparisons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
