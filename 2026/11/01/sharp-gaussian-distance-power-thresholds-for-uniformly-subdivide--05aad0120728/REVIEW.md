# Review of the sharp subdivided-star Gaussian threshold

## Correctness — PASS

For each integer \(m\ge3\), the basepoint Schoenberg matrix decomposes into \(m-1\) copies of a uniformly positive two-by-two arm-difference block and one explicit branch-constant two-by-two block. The integral identity for \((r+s)^p-r^p-s^p\) proves positivity of the first block for \(1<p<2\); a strict-concavity inequality and two strictly negative derivatives prove existence and uniqueness of the exact endpoint in the prescribed interval. At the endpoint, the second block is positive semidefinite of rank one; immediately beyond it the matrix is indefinite, and above the ordinary-star bound it has a negative diagonal entry. Schoenberg's theorem and finite-space strict-negative-type monotonicity extend the classification to all lower exponents and justify the affine dimension. Subtracting the positive definite arm interaction proves strict monotonicity in arm count. Uniform Taylor expansion proves the sharp coefficient. The embedded checker passed 443 deterministic finite assertions, supporting (but not replacing) the proof.

## Originality — PASS under bounded literature comparison

The closest fully inspected primary work is Doust–Weston's arXiv:0705.0411 (ordinary star exponent and generic tree lower bounds), Li–Weston's arXiv:0901.0695 (strictness and interval principles), and Sánchez's arXiv:1108.0451 (general finite-metric criterion and complete bipartite examples). These establish background results but do not themselves state the exact equally subdivided-star root, the endpoint dimension/null vector, the strict arm-count law, or the new sharp asymptotic constant. Search results concerning curvature-distortion and Ricci-flow behavior of spider graphs study different invariants and provide no known implication. The presence of an equivalent but unindexed older tree-metric exponent calculation remains a residual risk; a negative search does not prove uniqueness.

## Mathematical value — PASS

Uniform subdivision is a natural operation on a well-studied graph-metric family. The result identifies a strict change in the all-scale Gaussian positivity cutoff under this operation, a complete endpoint embedding-rank classification, and a nontrivial asymptotic constant that differs from the unsubdivided star. The question is structural across every arm count, not a disconnected finite example or an arbitrary parameter slice. Generic finite-matrix tests would not by themselves reveal the monotone extremal law and coefficient.

## Limitations

Only uniform unit-edge two-step arms and the all-scale positivity criterion are settled. No claim is made about arbitrary spider trees. Numerical tests cover finitely many cases and an independent audit has not been performed. Historical coverage risk remains for literature not located or indexed.

Self-review: passed. Independent audit: not yet performed.
