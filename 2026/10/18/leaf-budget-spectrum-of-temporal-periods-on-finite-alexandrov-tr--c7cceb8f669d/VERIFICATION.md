---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For an order-preserving finite-tree self-map f, the stable image S=f^N[T] has f|S a finite permutation; its inverse is a positive iterate, so it is an order automorphism. The maximal set of S is an antichain of size s≤k ambient leaves. Every such tree-order automorphism is faithful on its maximal elements: for x, the maximal-descendant set M_x separates incomparable x, while the size of the inherited principal downset distinguishes comparable x. Thus order(f|S)=order of a permutation of ≤k leaves; the eventual truth-set period t divides that order. Distributing each prime-power q^{v_q(t)} to cycles divisible by it and using sum≤product for pairwise coprime factors gives λ(t)=∑q^{v_q(t)}≤k. Conversely, on EVERY fixed tree, let all non-leaves map to the root and permute chosen leaves in one disjoint cycle for each prime-power, fix other leaves, and choose one valuation leaf per cycle. The preimage truth-set sequence has exact lcm period t; t=1 from empty valuation. This proves the entire spectrum and max Landau g(k), not just a bound. Independently enumerated 34 rooted trees on ≤5 labeled increasing-parent encodings, 5,430 monotone maps, 168,950 valuations; checked k-leaf spectrum bound, period-six 5-leaf star and diamond counterexample one leaf with period two. Finite work is corroborative only.

## originality

PASS

Classical permutation order and Landau prime-power budget are acknowledged. The natural new step is that every monotone endomap of an arbitrary FIXED finite Alexandrov rooted-tree order has eventual truth-set periods constrained by just its number of leaves and every budgeted period is constructible on that very tree, irrespective of height. Vooijs–Fernández-Duque (LICS 2026) provides the topological preimage/next semantics and tree-like unravelling context but not the sharp fixed-tree period law in inspected primary full text. Geometric topological tree maps in Alsedà–Ye (1995) are a different setting from finite Alexandrov poset continuous maps. Specialized poset endomorphism monoid period theorems might overlap, so priority is qualified.

## value

PASS

This determines the exact arithmetic gaps and sharp maximum of possible temporal truth-set cycles for every fixed finite rooted Alexandrov tree, using a natural structural parameter rather than a total-size bound. The equality of spectra across different tree shapes and the sharp failure on diamond frames are motivated topological/model-theoretic distinctions, not an arbitrary finite constant or mere Landau restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
