# Scientific review: sketched FOM positivity boundary

## Correctness — PASS

The generalized sketched Galerkin eigenvalue identity follows from the definition of the compression and an embedding-positive sketched Gram matrix. The critical bound follows from the pointwise spectral inequality \(A^2\preceq(\mu+L)A-\mu LI\), followed by an exact minimization of the turning angle. The embedding controls the bilinear discrepancy between a Krylov vector and its image under \(A\), because both vectors lie in the next Krylov space. Complex eigenvectors are permitted by complexification of the real embedding. The concrete two-row sketch realizes the exact extremal distortion and makes the one-dimensional compression zero at the stated boundary and negative beyond it. The executable standard-library verifier passed 25,308 exact-rational checks from the package's actual `verify.py`. Finite checks reinforce, rather than substitute for, the universal proof.

## Originality — PASS, subject to priority risk

Güttel and Schweitzer's original sketched FOM definition, its spectrum enclosure, and its warning that positive-real Ritz values can be lost were inspected in the full available open manuscript. Their results do not give the exact \(2\sqrt\kappa/(1+\kappa)\) universal condition nor a matching compressive construction. Cortinovis–Kressner–Nakatsukasa establish an equivalent randomized compression, but not this sharp spectral guarantee in their inspected treatment. Timsit–Grigori–Balabanov obtain a condition-number-dependent error quasi-optimality bound: controlling solver error is a different conclusion and their stated bound does not imply the precise sharp positivity frontier. Güttel–Liu–Nyman study sketched **harmonic** Ritz values with a different compression. The SPD turning-angle estimate and norm-embedding bilinear estimate are classical techniques; their use as separate lemmas is not claimed as novel. Broad perturbation or oblique-Galerkin theory might encode an equivalent consequence, so publication priority is not independently certified.

## Value — PASS

The source method evaluates matrix functions on a projected matrix whose eigenvalues determine whether reciprocal and other positive-axis-analytic functional evaluations remain well defined. A sharp, attainable embedding tolerance for guaranteeing positivity is a natural spectral design boundary, rather than a numerical example or arbitrary parameter slice. At condition number \(9\), the sharp admissible tolerance is \(3/5\), substantially larger than the direct crude enclosure's \(1/9\); at the boundary, an ordinary compressive two-row sketch produces an exact zero Ritz value. This supplies both a principled sufficient bound and an unavoidable worst-case obstruction.

## Scientific limits

There is no assertion that a particular random sketch satisfies the embedding with high probability, nor any claim about finite-precision arithmetic, nonsymmetric operators, harmonic Ritz values, solver runtime, or uniqueness of the proof's mathematical ingredients. The displayed positive-real lower bound is sufficient and may not itself be sharp away from the boundary. The literature comparison is extensive but not an independent certification of global priority.

Self-review: passed. Independent audit: not yet performed.
