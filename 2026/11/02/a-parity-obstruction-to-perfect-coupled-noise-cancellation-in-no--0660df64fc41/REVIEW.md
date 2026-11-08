# Independent mathematical audit

## correctness

PASS

Substitution gives x_{k+1}=p(eta M)x_k+eta(eta M xi-zeta). For real normal M, polar M=QH, T=p(eta M), W_n=Σ(T^k)^T T^k commute; each scalar covariance between xi_j and Q^T zeta_j is <=sigma^2, equality forces coordinate equality a.s., so unique coupling zeta=Qxi even among non-Gaussian joints. Spectral weights give exact n and stationary contraction formulas. Zero stationary noise requires eta H=I, hence M=rQ. For orthogonal mode e^{iθ} with cosθ>0, |p(e^{iθ})|=|2cosθ-1|<1 iff cosθ<1; an odd real orthogonal matrix must have +1 or -1, monotonicity excludes -1; rotations supply all even dimensions. Conditional unbiasedness E[zeta|xi]=0 eliminates cross term. Independent 3 direct computations corroborated the analytical argument.

## originality

PASS

Gaussian OT/Procrustes polar alignment is classical; the claim assessed is its exact normal-extragradient finite/stationary reduction, unique unrestricted coupling and stable parity information boundary, not invention of Gaussian covariance alignment.

## value

PASS

Two-query stochastic algorithm design poses a meaningful information-contract question: perfect cancellation under separately Gaussian marginals need not respect conditional oracle unbiasedness. The uniquely optimal polar coupling, full weighted error and even/odd stable-cancellation obstruction are nontrivial and natural, while no claim of standard conditional-unbiased stochastic gradient improvement is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
