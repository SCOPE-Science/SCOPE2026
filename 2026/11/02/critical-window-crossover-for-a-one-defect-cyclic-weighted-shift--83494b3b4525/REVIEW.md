# Scientific review — critical defect scaling of a finite cyclic shift

## Correctness — PASS

The numerical radius equals half the Perron root of a positive weighted cycle adjacency matrix. Reflection gives its positive cosine/cosh eigenvector, so the boundary equation is necessary and sufficient. The trigonometric branch has a unique root for each \(0\le r<1\), the hyperbolic branch for each \(r>1\), and the \(r=1\) value is exactly one. The phase formula yields the fixed subcritical asymptotic and strict size monotonicity; the exact exponential relation yields the supercritical asymptotic. Scaling \(r=1+a/n\) and the unique roots of \(z\tan(z/2)=-a\) and \(y\tanh(y/2)=a\) prove the limiting crossover. Critical computations were independently rerun with exact symbolic identities, matrix eigensolvers and arbitrary precision. No infinite conclusion depends on the finite computations.

## Originality — PASS (historical priority qualified)

Chien–Kirkland–Li–Nakazato (arXiv:2304.06050, full preprint inspected) provide determinant and numerical-range methods for general finite cyclic weighted shifts. The finite equation and Perron reduction are therefore not being claimed as novel. Their inspected general theorems, examples and permutation comparisons do not state the \(1/n\) defect-strength critical-window function with trigonometric/hyperbolic branches or the matched fixed-strength polynomial versus exponential finite-size corrections. Chang–Wang (2012) analyze optimal weight permutations rather than this scaling. Grudsky–Maximenko–Soto-González (arXiv:2308.07514, full preprint inspected) analyze a defective *Laplacian*, whose diagonal weights differ from the Hermitian part of the cyclic shift. Gorkin–Partington (2019) is related numerical-radius literature, but the original was inaccessible on the retrieval attempt. It is a residual priority risk, along with possible older periodic Jacobi defect-state asymptotics. Database similarity results about \(\ell_p\) cyclic Hessians, infinite unilateral one-weight shifts and geometric-weight finite cycles do not imply this scaling for a finite one-defect cycle. Novelty here is a bounded and qualified statement, not a claim of uniqueness.

## Value — PASS

The defect changes the Perron eigenvalue from a below-band finite-size deficit of order \(n^{-2}\) to an above-band localized eigenvalue with exponential finite-size correction. The explicit two-sided crossover is a uniform transition statement that neither fixed-strength expansion alone determines. It supplies a natural sharp Hilbert-space numerical-radius invariant and a usable boundary-layer benchmark for weakly perturbed cyclic operators, independent of a further downstream theorem.

## Boundaries

Nonnegative defect weights, real Hilbert-space Perron reduction for complex Hilbert numerical radius, and only one nonconstant edge. The \(n\to\infty\) crossover has fixed \(a\); no error-uniformity claim for arbitrary moving \(a\) or general multisite perturbations. The result has not been independently validated.

Self-review: passed. Independent audit: not yet performed.
