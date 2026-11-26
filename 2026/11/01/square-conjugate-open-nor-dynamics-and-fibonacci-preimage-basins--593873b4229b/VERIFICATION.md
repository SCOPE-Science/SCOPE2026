---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For a bipartition A⊔B the maps f and g test absence of adjacency across the partition. The polarity Y⊆f(X) iff X⊆g(Y) gives fgf=f and gfg=g. The independently variable input sides yield im F=im g × im f; the restrictions of f,g are inverses there. Hence the bijection (X,Y)↦(X,g(Y)) conjugates the image dynamics, not the full Boolean cube, to swap. Since F is involutive on that image, it is precisely the recurrent set. Fixed states are both independent and dominating, precisely maximal independent sets including all isolated vertices. Thus the counts follow from the square and its diagonal. On a path each of two output parities uses disjoint input bits; between successive sites of a parity there is one possible input edge. The parity-dependent stubs come from real path endpoints adjacent to only one site of the output parity. Ones forbid their incident edges, so zero runs separate and each requires an edge cover using internal edges and its available stubs. For length L and t stubs, the L−1+t edge bits have no adjacent pair of zeros, with 2−t endpoint edges forced when those forced edges are distinct. The remaining L−3+2t bits give F_{L−1+2t}; for L=2,t=0 the two endpoint constraints force the same edge, giving one; L=1 has counts 0,1,3, also as stated. Thus multiplication produces all one-step fibers including impossible words. Basins are disjoint unions of the attractor states’ one-step fibers because all states land in the image immediately. The all-zero/all-one basin, path maximal-independent-set recurrence and the two exponential fractions follow from the displayed run and recurrence formulas; both parities in the distinguished basin have leading numerator φ^{n+2}/5. Replay: RESULT.md lines 34–73. Both checker sources, stored outputs and VERIFICATION.md were inspected, not rerun; they are finite examples, not proof. Paths use n≥2, and the square bijection is for finite loopless undirected bipartite graphs, not closed or asynchronous NOR.

## originality

PASS

The supported distinct contribution is the complete finite-path predecessor and basin product with explicit endpoint effects. The square description is a correct direct application of the standard polarity; no separate novelty is assigned to Galois closure, the diagonal maximal-independent-set correspondence, or short recurrence. The strongest retrieved alternate formulations do not establish the same evaluated path product. An older exact-table risk remains explicit.

## value

PASS

The evaluated factorization resolves every basin size and every impossible one-step output for a natural finite dynamical system. It exposes precisely how endpoints and runs affect multiplicity, with a linear arithmetic evaluation rather than a census or mere period restriction. Its value is the complete individual-basin information, not the classical diagonal count, short recurrence, or isolated Fibonacci edge-cover identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
