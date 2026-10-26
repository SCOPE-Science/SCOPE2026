# Self-review

## Correctness — PASS
The six mixed-difference constraints have rank four with two shared-difference relations. Those constraints exhaustively classify the twenty-two feasible active faces. Exact-rational Gram-projector calculations, reproduced in `check.py`, show that five faces and no others have maximum \(\ell^\infty\)-row norm \(7/4\). A concrete strictly complementary projection region and a matching sign perturbation prove attainability. Projection-region linearity gives the global result. The proof excludes weighted fitting and larger ground sets.

## Originality — PASS with residual priority risk
Full-text comparisons were made with Iyer–Bilmes (arXiv:1506.07329) and Bach (arXiv:1511.00394); their polyhedral and convex-extension theorems are not statements about the coordinatewise modulus of Euclidean submodular regression. Németh–Németh (arXiv:1503.08458) concerns isotonic cones defined by pairwise-order constraints. Related exact projection constants for planar cones, weighted cross-polytopes, and chains do not imply this eight-dimensional cone result. No equivalent record emerged from the mathematical searches conducted. Hidden historical overlap under different terminology remains possible; absence in a search is not a novelty certificate.

## Value — PASS
Three elements form the first case with genuinely interacting submodularity constraints. The exact sharp stability factor, twenty-two feasible active patterns, five maximizers, and two-variable baseline give a complete and reusable sensitivity benchmark for constrained denoising. This is a natural finite classification; no claim is made for arbitrary cardinalities.

## Verification and limitations
The executable rational-arithmetic checker was run successfully. Its finite enumeration certifies the full finite problem because the proof independently exhausts every possible face. The independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
