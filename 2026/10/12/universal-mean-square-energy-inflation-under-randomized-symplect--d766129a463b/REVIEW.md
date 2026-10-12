# Scientific review

## Correctness — PASS

The claim is for iid steps supported on \((0,2)\), not general symplectic solvers. Positive-cone Perron–Frobenius yields a positive-semidefinite spectral eigenmatrix, and elliptic step maps rule out rank-one eigenmatrices for both the covariance operator and its adjoint. Determinant concavity gives spectral radius at least one, while its equality case forces a common invariant quadratic form. The invariant quadratic form of any fixed symplectic Euler step is uniquely proportional to \(P_h\), distinguishing every pair of step sizes; hence nonconstant laws force a strict spectral radius larger than one. A positive-definite dual eigenmatrix provides uniform, all-directions exponential mean-square bounds. Exact rational covariance calculations, eigenpolynomial, direct finite-history enumeration and second-variation checks were replayed from the accompanying verifier. Standard cone Perron–Frobenius and determinant concavity are invoked as established facts, not novel lemmas.

## Originality — PASS, subject to residual priority risk

Full-text examination of Abdulle and Garegnani (arXiv:1801.01340, Sections 2, 7 and 9.6, especially Theorem 6 and Remarks 12–13) establishes that the work addresses random steps and finite-time geometric energy behavior, but not the universal infinite-horizon positive covariance spectral rate for all nondegenerate laws supported in the elliptic interval. Full-text readings of the adaptive-step symplectic discussion of Kaib, Quinn and Brasser (arXiv:1011.3830) and the random two-shear results of Sturman and Thiffeault (doi:10.1007/s00332-018-9497-3) found related mechanisms but neither the same random operator nor a result implying the full exact statement. Targeted published mathematical-result and primary-paper searches on invariant metrics, mean-square instability, symplectic Euler, random-step shears, and harmonic oscillators found no dominating result. This is a priority assessment, not a proof of originality. Broader random \(\mathrm{SL}(2,\mathbb R)\) product literature may contain an equivalent corollary; that remains an explicit risk.

## Value — PASS

Random time stepping is promoted to preserve symplectic geometry, but stepwise symplecticity and individual elliptic stability do not guarantee all-time mean-square energy control. The theorem gives a complete qualitative if-and-only-if classification under the natural deterministic stability interval, exact all-initial-data geometric growth, a rational witness where first-moment convergence coexists with second-moment divergence, and an informative small-jitter rate. This resolves an asymptotic reliability boundary left outside finite-horizon energy estimates and is more than a routine numeric example. The finding does not claim almost-sure divergence, practical timestep policy optimality, higher-dimensional universality or a contradiction of finite-time bounds.

Self-review: passed. Independent audit: not yet performed.
