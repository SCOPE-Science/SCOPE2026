# Scientific assessment — exact block-Jacobi conditioning on rank-one spikes

## Correctness: PASS
The identity-plus-rank-one block reduction uses the actual square-root inverse of each exact diagonal block and preserves all complementary unit eigenvalues. The paired-eigenvalue calculation proves two-block safety. For three block energies \((s,s,t)\), symmetric and antisymmetric reductions give all eigenvalues; the critical factor identities locate every strict and equality region. A separately verified sum-of-squares certificate proves the strict \(3/2\) bound for \(t>s\), and the sequence \((s,t)=(L^2,L)\) gives the sharp limit. SymPy verifies exact factor identities and the rational witness. Numerical eigentests are consistency checks rather than proofs. The conclusions are confined to the stated positive parameters and exact symmetric scaling.

## Originality: PASS, with a specific residual risk
The 2026 BLOKS manuscript explicitly defines exact block Jacobi but the material inspected concerns approximated blocks, implementation, and experiments, not the asserted rank-one three-block phase boundary. Demmel's 2023 general scaling bounds do not by themselves imply the exact two-parameter thresholds or the sharp family-specific factor. Kolotilina's 2004 two-block eigenvalue formula explicitly covers the two-block spectral reduction, which is treated as background. His 2002 general block-scaling article could not be inspected in full and remains a concrete specialized-overlap risk; only its abstract-level scope is known. Searched research findings about weighted Jacobi damping and additive bidirectional Gauss–Seidel concern different operations and do not imply the asserted condition-number ratio. No claim of exhaustive literature coverage or independent novelty certification is made.

## Value: PASS
Recent preconditioned kernel solvers motivate choosing exact or approximate block-Jacobi diagonal blocks. The result identifies the smallest block count for a condition-number setback in a simple SPD family, gives a complete partition-energy boundary in a natural equal-pair three-block configuration, and quantifies the largest deterioration in that family. It informs partition selection and distinguishes algebraically exact local inverses from global spectral improvement. It is not a numerical experiment, a claim about randomized sketch accuracy, or a theorem about all SPD matrices.

## Scientific limitations
The sharp ratio is restricted to energies \((s,s,t)\), rather than arbitrary three-block spectra. The analysis assumes SPD rank-one perturbations of the identity, exact inverse block factors, and Euclidean spectral condition number. Prior article access constraints leave a specialized historical novelty risk. No floating-point, solver-timing, or approximate-sketch guarantee follows.

Self-review: passed. Independent audit: not yet performed.
