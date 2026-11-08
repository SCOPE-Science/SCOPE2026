# Independent mathematical audit

## correctness

PASS

On the REAL Hermitian trace-norm unit ball it suffices to optimize pure signed rank-one projections. Local-unitary invariance reduces to a Schmidt rank <=2 state with u in [0,1]. In the physical 2n-dimensional operator the 2x2 entangled block has eigenvalues 1/4 +/- (1/2)sqrt(1-bu^2); remaining diagonal eigenvalues contribute exactly 1/2+cu. Therefore F_n(u)=1/2+cu+max{1/2,sqrt(1-bu^2)}, with branch optimum u_n=c/sqrt(b(b+c^2)) and exact norm .5+sqrt((4+3c^2)/(4-c^2)). On the other branch 1+cu<=1+c is strictly smaller, including n=2; duality gives same spectral norm. Product states attain 1+c, separable mixtures cannot exceed it. Independently recomputed physical partial traces/eigenspectra at 28 (n,u) configurations for n=2..8.

## originality

PASS

Best-of-knowledge PASS. The directly relevant 2023 Zhu et al. paper optimizes nuclear norms of rectangular Bloch correlation COEFFICIENT matrices, not the physical operator P_n(rho) or its real-Hermitian induced norm; it therefore does not determine this partially entangled Schmidt optimizer. A published one-body marginal projection theorem concerns linear sums rather than tensor double-centering. General operator-space or Hoeffding decomposition results may nonetheless encode the same constant.

## value

PASS

An exact physical-operator correlation-projection norm is a natural quantitative measure of centered two-body quantum correlations. Its optimal Schmidt profile changes from maximally entangled at n=2 to uniquely partially entangled for n>=3 and strictly exceeds the separable threshold, a structural entanglement-versus-product norm separation. The proof gives a full all-dimension formula, not an arbitrary finite instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
