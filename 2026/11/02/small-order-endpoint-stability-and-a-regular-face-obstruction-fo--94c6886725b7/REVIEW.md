# Scientific review: Euclidean Birkhoff endpoint stability

## Correctness — PASS

The proof identifies every realizable active face as a union of permutation supports and establishes the exact finite-face norm formula. Exhaustive all-subset enumeration yields 3, 49 and 7443 valid supports at orders 2, 3 and 4; 2, 6 and 42 row–column permutation orbits suffice, each evaluated using exact fractions. The unique maximizing orbit is the full support, giving \(1,16/9,9/4\). An exact 23-by-23 Gram inverse on a 72-edge regular order-twelve support yields an absolute row sum \(41/12\), exceeding the affine \(121/36\) by \(1/18\). Strict complementarity makes both upper-order row sign constructions genuine finite difference quotients. The attached verifier completed successfully.

## Originality — PASS (qualified)

The closest inspected primary work is Li–Sun–Toh (arXiv:1702.05934), which provides full-polytope generalized Jacobian formulas for any order; those are the linear-algebraic starting point, not the evaluated \(n\le4\) maximum or cyclic twelve-order counterexample. Bai–Chu–Tan (doi:10.1137/050639831) impose a prescribed entry, and Zass–Shashua (NIPS 2006) impose matrix symmetry. Queries of mathematical literature and a semantic mathematical-results index for entrywise norm, graph cycle-space aliases, and the explicit rational constants found no equivalent result. Residual priority risk remains for older technical notes or graph projector tables not indexed by these searches.

## Mathematical value — PASS

The mathematical question is whether nonnegativity constraints on a balanced-matrix least-squares projection can worsen its maximum-coordinate sensitivity relative to the affine subspace. The finding both determines all small cases up to four and proves that the apparently benign full-support dominance can fail on a regular, translation-symmetric support. It resolves a natural robustness distinction while leaving the first failing dimension and the sharp higher-order sequence open. The exact rational certificate can be independently recomputed using ordinary Python.

## Literature and scientific limitations

Inspected: author-accessible Bai–Chu–Tan manuscript §§1–3 and its publisher date record; the full Zass–Shashua proceedings paper with equation (4); and Li–Sun–Toh's preprint §§1–3 and generalized-Jacobian formulas. The first two consider modified feasible sets, while the last supplies general computational methodology without these constants. The twelve-order claim is only a strict lower bound. Independent priority and scientific validation are outstanding.

Self-review: passed. Independent audit: not yet performed.
