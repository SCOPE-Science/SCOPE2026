# Scientific review

**Correctness — PASS.** Exact-line-search away steps are strictly interior near the barycenter. Differentiating yields the cyclic product of tangent-space orthogonal coordinate-killing projections. The proof reconstructs all eigenvalues from a closed scalar recurrence, proves strict spectral contraction, and uses uniform analytic limits plus a Lambert-branch comparison for the all-dimensional limit. The included verification program passed exact symbolic checks for dimensions 3 through 8 and 70 nonlinear derivative checks. The infinite statements rely on analytical reasoning rather than finite enumeration.

**Originality — PASS (best-knowledge).** The original 2023 PolyCDwA paper specifies the algorithm and global linear-convergence theory, and its results are credited rather than restated as new. General cyclic coordinate descent/Kaczmarz equivalences, a later general triangular-Gram representation, and matching-claim mathematical research records were compared for mathematical coverage. The inspected material does not provide the full explicit isotropic-simplex sweep spectrum, the sharp local rate, or its Lambert-W limit. There remains a risk of an equivalent specialized eigenspectrum in older equiangular cyclic-projection literature.

**Value — PASS.** The theorem provides a natural complete local spectrum for a numerical optimization method, reveals oscillatory eigenmodes beginning at four vertices and a nontrivial limiting contraction factor, and supplies an exact benchmark for dimension dependence. It is not claimed to be a new global convergence theorem.

**Limitations.** Exact line search, PolyCDwA with away steps, interior local behavior, isotropic Euclidean quadratic, and exact arithmetic. A spectral-radius rate is the sharp uniform neighborhood rate but does not assert that every individual orbit realizes it. Independent scientific validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
