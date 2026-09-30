# Independent audit — 2026-09-29

Record: `2026/09/15/027`  
Audited source tree: `b69753b9f3c03b874c60c345b8bdc2bb21258b96`  
Disposition: **repaired**

## Correctness

The Fang–Tian regularity/Morita-equivalence portion survives, but the published classification theorem did not. The original record incorrectly inferred UCT for A^alpha and A rtimes G from UCT(A) plus compactness/amenability, and it called the crossed product unital for arbitrary compact G. Fang–Tian prove simplicity, Z-stability and stable isomorphism, not this UCT permanence; in fact UCT preservation for arbitrary finite cyclic crossed products is strong enough to encode the general UCT problem. The repaired claim therefore makes UCT of the fixed-point/crossed-product Morita class an explicit additional hypothesis for rational gTR1/Elliott classification, and treats an infinite-compact-group crossed product stably rather than through a unital [1]-invariant.

## Originality

The surviving statements are a synthesis of Fang–Tian permanence and established Elliott-classification/UCT theory. The repair is mathematically important because it removes a false closure step, but it is not presented as a new general theorem.

## Scientific value

The repaired record cleanly separates what the weak tracial Rokhlin property actually supplies from the unresolved UCT input. It retains a valid conditional classification route and stable crossed-product conclusion while avoiding a claim whose proof would reach into the UCT problem.

## Limitations

- No unconditional UCT permanence theorem is supplied for the weak-tracial-Rokhlin action.
- Exact TR(A rtimes G)<=1 remains unproved.
- For infinite compact G the crossed product need not be unital, so the standard unital Elliott invariant with [1] is not used directly.
- The repaired classification conclusion is conditional on UCT for A^alpha (equivalently for the Morita-equivalent crossed product).

## Sources checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/15/027
- https://arxiv.org/abs/2508.06844
- https://arxiv.org/abs/1712.00823
- https://arxiv.org/abs/1406.1208
- https://arxiv.org/abs/1909.13382
- https://arxiv.org/abs/1507.03437
