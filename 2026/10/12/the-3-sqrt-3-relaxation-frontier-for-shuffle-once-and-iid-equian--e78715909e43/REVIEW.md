# Scientific review

## Correctness — PASS

The claim fixes a consistent, normalized three-row planar problem and an isotropic initial second moment, then compares the same number of updates at integer epoch endpoints. The tight-frame identity yields the exact IID moment recursion. The orthogonal symmetry of the three projective lines makes all six fixed-permutation epoch maps orthogonally conjugate. The characteristic trace, determinant, discriminant, and spectral-radius comparison are algebraically explicit. The sign factorization and globally positive quartic prove the unique boundary \(\eta=3-\sqrt3\) without relying on finite experiments. At the discriminant-zero point the finite-dimensional spectral-radius formula remains valid. The exact rational two-epoch witness and symbolic checker support the proof. Risks: incorrect transposition/order conventions are controlled by the explicit matrix and independent six-order checks; no claim beyond isotropic initialization is made for SS.

## Originality — PASS, qualified

The closest **same-object** precursor, Yun–Sra–Jadbabaie (arXiv:2103.07079v1, Appendix A), explicitly uses the same equiangular rank-one projectors and must receive credit. Its comparison is a spectral norm of a mean product, against fresh reshuffling, with relaxation \(\eta\le1\); it neither states nor logically yields the comparison of expected *squared* error under a once-fixed order and IID-with-replacement sampling for \(1<\eta<2\). Ahle–Bulatov–De Sa–Ré (arXiv:2609.36271v1) establish asymptotic shuffle advantages in a different high-dimensional isotropic Gaussian model. Nguyen–Phan–Kalagnanam (arXiv:2604.00260v1) study block prefix variance and order-reversal expansions, not the present exact spectral transition. Published research-record searches found related Kaczmarz residual-spike and reverse-order bias results but no matching sharp ordering. A related existing theorem concerns reshuffling for **common-Hessian** finite sums, rather than fixed-permutation heterogeneous rank-one updates. Residual risk: uncatalogued equivalent analysis of this classical three-projector product or a source not identified by current search.

## Value — PASS

The object is the smallest nontrivial redundant normalized tight frame in a plane, with normal-matrix condition number one. It was previously studied as a matrix-product ordering counterexample, and current shuffling theory motivates comparing fixed orders to IID using the physically relevant expected squared error. A sharp phase boundary separating when each method has the better exponential convergence rate, plus a two-epoch strict reversal, is a motivated structural classification rather than an arbitrary numerical slice. It demonstrates that even perfect conditioning does not preserve the shuffle-once advantage under overrelaxation. The result does not establish universal convergence orderings for larger frames.

Self-review: passed. Independent audit: not yet performed.
