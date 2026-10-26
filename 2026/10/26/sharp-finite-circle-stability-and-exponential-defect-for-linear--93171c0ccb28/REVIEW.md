# Scientific review: sharp finite-circle spline projector stability

## Correctness — PASS

The result follows from a reconstructed finite hat Gram matrix, its explicitly periodized signed inverse, and exact integral evaluation of a piecewise-linear knot kernel. The extension from knot norms to the full operator uses convexity of kernel absolute integrals. The nonperiodic cardinal kernel has exact total absolute mass two; periodizing it gives an upper defect estimate, and fixed even/odd sign-collision windows give strictly positive lower defects at the identical geometric scale. Taking nth roots proves the optimal rate. Exact-rational finite replay over 26 circle sizes checks the recurrence, symmetry, closed inverse, small exact fractions, and stated bounds; its 1,722 assertions are supplementary, not a proof of the universal result.

## Originality — PASS within investigated evidence

Passenbrunner (arXiv:1608.06720) proves uniform boundedness for periodic spline projectors with arbitrary knot sequences, but the inspected theorem and proof do not give these finite uniform-circle constants. Oswald (arXiv:math/0611573) discusses one-dimensional upper bounds and a contrasting multivariate counterexample. Kayumov (arXiv:math/0408418) records the classical arbitrary-knot sharp bound three. The closest accessible previously established uniform bi-infinite spline norm equals two, but does not imply exact finite periodic strictness or its sharp decay rate. Published mathematical records were compared for periodic finite-dimensional spline constants, equivalent cyclic tridiagonal inverse descriptions, and finite cyclic Fourier projection results; no examined statement supplies the claimed finite-circle norm and exponential defect. Historical priority remains provisional because older periodic spline calculations and some original cited literature are not exhaustively inspected.

## Value — PASS

On a canonical finite periodic mesh, the exact maximum-norm amplification coefficient quantifies how much least-squares spline smoothing may magnify bounded perturbations. It is strictly smaller than the infinite uniform-mesh norm and the general arbitrary-knot bound. The result determines an exact finite formula, a nontrivial finite-size improvement, and its provably optimal geometric rate. No general optimal-mesh claim, second asymptotic coefficient, or uniqueness of maximizing output locations is asserted.

## Closest literature and limitations

The principal comparison is Passenbrunner's periodic-spline boundedness theorem. The arbitrary-knot 1D norm-three result and the infinite-uniform-grid norm-two claim are complementary benchmarks, not equivalent coverage. Periodic matrices may have been analyzed under different names; independent checking would be valuable. The exact formula is a finite sum, and only a sharp exponential order, not a full parity-dependent leading coefficient, is proved.

Self-review: passed. Independent audit: not yet performed.
