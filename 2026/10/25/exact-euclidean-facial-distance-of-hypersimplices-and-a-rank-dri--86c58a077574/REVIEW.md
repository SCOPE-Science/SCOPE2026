# Self-review

## Correctness — PASS
All proper faces of the hypersimplex are classified by coordinate fixings. For each positive-dimensional face, symmetry averaging and a sharp two-variable quadratic yield a lower bound; an explicit convex mixture of one-violation vertices attains it. Vertex faces are analyzed separately and are strictly nonoptimal in the stated non-simplex range. The remaining integer quadratic optimization is solved exactly, including parity and transition boundaries. Rational computations and independent small-dimensional convex optimization are supplementary evidence, not a substitute for the general proof.

## Originality — PASS under inspected evidence
The closest papers are Deza et al. (arXiv:2609.32440), Peña and Wirth (arXiv:2608.28971), and Ferroni and Schröter (arXiv:2310.05487). They establish general sharp bounds, calculus/lower bounds, or hypersimplex face enumeration, rather than the exact intermediate-rank face-separation metric and its minimizing-face transition. Known simplex cases are expressly excluded. Targeted searches under both “facial distance” and “pyramidal width” found no identical evaluation. Absence of a retrieved identical result is not a proof of historical priority; possible differently indexed optimization literature and incompletely accessible appendices remain residual risks.

## Mathematical value — PASS
Facial distance governs linear convergence constants for Frank–Wolfe variants. Hypersimplices are the canonical uniform-matroid base polytopes and a standard non-product \(0/1\)-polytope family. Computing their exact global invariant and identifying all minimizing face types, including a sharp transition from edges to higher-dimensional faces, supplies structural information not obtainable from general upper/lower estimates. The result is a natural infinite-family classification, rather than an arbitrary isolated computation.

## Limitations
The theorem does not cover other matroids or affine images; priority review is non-exhaustive, and independent audit is not performed. The proof and numerical checks have distinct roles: exact symbolic arguments establish generality, while finite programs supply cross-checks.

Self-review: passed. Independent audit: not yet performed.
