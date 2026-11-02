# Scientific review

## Correctness — PASS

The precise domain is a connected finite **simple cactus**, positive prices and budget, and independent nonnegative conductances. Weighted Matrix–Tree factorization partitions the polynomial into bridge factors and one-deleted-edge factors on cycles. The latter are homogeneous of degree \(\ell-1\); strict log-det concavity and injectivity of the grounded Laplacian establish uniqueness, even with asymmetric allocations and zero weights. Homogeneous budget splitting gives \(B_H=d_HB/(n-1)\). Each possible cycle face has a unique optimizer, and its one-sided KKT derivative is exactly the sum of surviving prices divided by the multiplier. This proves the sharp dominance equality and non-equality cases. The one-exception formulas are derived algebraically; exact rational determinant comparisons supplement the proof. Risk: extension to multigraphs or overlapping cycles is not proved; solver checks are finite corroborations only.

## Originality — PASS (bounded bibliographic basis)

The Matrix–Tree identity, convex log-det design and KKT conditions are established tools. Examined primary papers include Sagnol–Harman (arXiv:1307.4953, full article including block-design section) and Khosoussi–Sukhatme–Huang–Dissanayake (arXiv:1604.01116, original text including §§4.4, 5.1.2 and associated methods); Boyd (ICM 2006) supplies general spectral design context. Those treatments give general determinant design or **fixed-weight candidate-edge selection**, not a statement implying the positive-price cactus block-budget split and exact \(p_k\ge\sum_{e\ne k}p_e\) support threshold under independent continuously adjustable weights. Comparison includes alternative descriptions as D-optimal graph design, weighted spanning-tree/Matrix–Tree maximization, log-determinant Laplacian optimization, and cost-constrained edge allocation. Search and checked-results evidence is documented in the structured review. Risk: another article or textbook treatment of continuous D-optimal design on block graphs could already contain the classification; the search is not exhaustive.

## Mathematical value — PASS

The sharp dominance inequality decides **without numerical optimization** whether an optimized cycle is cut into a path; exact block-expenditure splitting holds for arbitrarily heterogeneous prices and arbitrary cactus attachment topology. The classification answers a natural D-optimal sensing/network-design support question, distinguishes the fully connected and deleted-edge regimes at a sharp price frontier, and supplies explicit unique conductances at the frontier. It is not a fixed-weight rescaling of a symmetric example and offers a reusable decomposition for cactus-structured design instances.

## Reproducibility and boundaries

`verify.py` reproduces the exact rational 12-vertex cofactor identities, the exact single-price cycle formulas, and random asymmetric design comparisons. Its finite numerical tests cannot prove infinite-family optimality; the analytical factorization, strict concavity and KKT argument do. Independent external examination has not occurred.

Self-review: passed. Independent audit: not yet performed.
