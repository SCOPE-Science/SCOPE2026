# Independent mathematical audit

## correctness

PASS

Reconstructed H_N=⊕_{k=0}^N D_k, dim=(N+1)(N+2)/2. P_N M_{az+bw} maps D_k to D_{k+1} for k<N and kills D_N; the (k+2)x(k+1) full-column-rank bidiagonal block has Gram diagonal A²+B² and off-diagonal a* conjugate(b), unitarily gauged to AB. The sine eigenvectors yield s_{j,r}²=A²+B²+2AB cos(pi r/j), 2<=j<=N+1, 1<=r<j, strictly positive even if A=0 or B=0. Therefore N(N+1)/2 positive singulars and N+1 zero ones, with exact extreme values. For A!=B the bounded Riemann sum gives Q/N²->(1/(2pi)) integral_0^pi f(theta)^(-p/2)dtheta for all p>0 including a zero coefficient. When A=B=c>0, t=j-r yields 2c sin(pi t/(2j)); endpoint integrability for p<1, harmonic sums for p=1, t^-p dominated convergence for p>1 give each stated constant. Summing cosecant² gives exact Q_N,2=N(N+1)(2N+7)/(36c²). In the near-balance a_N=c+tau/(2N), b_N=c-tau/(2N), fixed p>1, s²=(tau/N)²+4A_NB_N sin²(pi t/(2j)); after multiplying by N² the pointwise limit is tau²+(pi ct/u)² at j/N->u. Uniform t^-p(j/N)^p majorant validates both limit exchanges including u=0; the coth summation for p=2 is correct. Independently built full compressed matrices and checked 40 complex-parameter/N cases; the maximum singular-value discrepancy was 8.9e-16. Symbolic exact p=2 finite trace identity verified; direct balanced ratios and p=2 critical-window ratios converge numerically. These tests corroborate but are not proofs of asymptotics.

## originality

PASS

Best-of-knowledge originality survives the actual implication comparison: exact path-graph/tridiagonal eigenpairs are classical and not claimed new. The independently evaluated combined total-degree positive spectral multiset, p=1 inverse-Schatten threshold and especially the fixed-p>1 N^-1 coefficient-imbalance limit Phi_{p,c}(tau) are not supplied by the inspected closest published results. The indexed published Resultary findings were read in full and concern other polynomial multipliers, approximation objectives, or different weighted lattice shifts. Closest historical Toeplitz full texts were not accessible; this is a qualified priority risk, not evidence of coverage or grounds for automatic failure.

## value

PASS

The total-degree finite section of a bidisk Hardy linear multiplier is a natural graded Toeplitz compression with a rank-deficient Moore-Penrose inverse. Its conditioning changes sharply at equal coefficient moduli. Determining the full spectral multiset, exact inverse-square finite trace, three distinct inverse-moment growth laws, and a nontrivial mass-dependent critical-window function quantifies a mathematically motivated transition at natural scale N^-1; this is useful for benchmark inverse regularization of graded multivariable shifts. The crossover is not a gratuitous finite numeric statistic or merely a renamed tridiagonal eigenvalue identity. Value remains narrow: only linear symbols and this cutoff, no general polygon or higher-dimensional theorem asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
