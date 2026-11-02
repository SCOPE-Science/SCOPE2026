# Self-review

## Correctness — PASS

The statement specifies a finite real Cartesian product of complete graphs, a positive conductance constant on each axis, the symmetrically weighted Euclidean gradient projector, and an unweighted maximum norm on those edge coordinates. The tensor-resolvent representation follows from the complete-graph Laplacian eigenvalue on a coordinate dipole. Its strictly positive heat kernel proves the signs required for summing absolute edge transfers. These sums yield the exact row formula; matrix row-sum duality gives a sign-vector extremizer. The optimization is an AM--GM inequality with a strict equality condition; comparison of the sharp row bounds proves that a smallest alphabet is optimal. A separate subtraction proves the smallest-alphabet rule for equal conductances. The single-factor and binary boundary cases are included. The independent exact rational grounded-Laplacian checker passed 24 product/weight profiles and 478 edge-row comparisons. This finite testing corroborates, rather than proves, the full infinite statement.

## Originality — PASS, with explicit residual priority risk

The closest directly examined publications are Kelner–Maymounkov (arXiv:0909.2859v1), Schild–Rao–Srivastava (arXiv:1708.01632v1), and Gurel-Gurevich–Nachmias–Sachdeva (arXiv:2605.24130v1). Their inspected theorems and examples give general electrical-routing/projection or transfer-current estimates, including parallel paths and grids, but do not state the mixed-alphabet all-axis exact formula and its sharp conductance-balancing rigidity. An exact electrical norm on complete graphs or a four-cycle is only a special case and is not claimed separately. Searching by the aliases ``transfer-current matrix'', ``electrical projection'', ``Cartesian product of complete graphs'', ``Hamming graph'', and ``edge-flow total absolute current'', including published findings archive semantic searches and available previous research claims, did not exhibit an implication covering the full theorem. This is a bounded, good-faith priority assessment rather than a claim of uniqueness; a product-graph Green-function formula in unlocated electrical-network literature remains the principal residual risk.

## Mathematical value — PASS

The theorem computes a previously non-obvious sharp endpoint stability invariant for a naturally structured infinite family of finite-dimensional graph projection operators, not a single arbitrary graph. It identifies precisely how alphabet sizes and direction conductances interact, and proves that balancing factor Laplacian rates gives the globally optimal worst-case amplification, with an iff equality condition. Exact q-ary cube scaling connects the invariant to the logarithmic electrical-localization phenomenon. The invariant is pertinent whenever electrical projections are used to route bounded edge data or study operator stability; no algorithmic runtime or general-routing competitive theorem is claimed.

## Limitations and closest coverage

The norm is for square-root-rescaled real edge coordinates, not physical edge currents under unequal conductances. Per-edge heterogeneous conductances and noncomplete factor graphs are outside scope. Existing arbitrary-graph electrical-flow literature may contain equivalent identities under a different normalization; mathematical priority has not been independently verified. The exact checker samples finitely many graphs and is not an infinite proof.

Self-review: passed. Independent audit: not yet performed.
