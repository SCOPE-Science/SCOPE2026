# Independent mathematical audit

## correctness

PASS

For G=(1-mu)I+mu J, A=G^1/2 and uniform omission of one of four rows, row-coordinate update is L_S=I-GD_S. Independent SymPy sum over four subsets gives the invariant covariance matrix M=((1+9mu²)/4, 3mu²-3mu/2; 3mu²/2,7mu²/2-mu), with det(I-M)=3(mu-1)(3mu+1)(3mu²+2mu-2)/8, det(I+M)=(27mu⁴+53mu²-10mu+10)/8, det M=mu(27mu³+7mu-2)/8. Schur/Jury yields spectral radius<1 for 0<=mu< (sqrt7-1)/3. Self-adjoint covariance transfer with U^t(I)=A^-1 T^t(G) A^-1 propagates this to every deterministic initial error. For mu>=mu_* positive M and Perron-Frobenius yield nonzero limit at equality/divergence above for x0=1. Separately E[B_S²] has eigenvalues (18mu²-3mu+1)/4 and (2mu²+mu+1)/4, giving one-step bound mu<=1/2, while each block has eigenvalue -2mu. Independent exact symbolic example at mu=13/25 gives 673/625>1, and mu=3/5 Perron eigenvalue >1. The special initialization conclusion is not every-start divergence.

## originality

PASS

Du & Sun, arXiv:2011.10353, §2.1.2 BRUS Algorithm 1 and Theorem 5 give exactly this unaveraged row-selection family (with absorbed m/ell scaling) and a sufficient stepsize bound corresponding to mu<1/2 here. Their theorem cannot imply sharp asymptotic mean-square convergence up to mu_* >1/2, nor isolated transient amplification in 1/2<mu<mu_*. Contrasted pseudoinverse Kaczmarz variants and Necoara averaged updates; no same frontier located. Best-of-knowledge with specialist-priority risk.

## value

PASS

A natural exact stability boundary for parallel multirow correction demonstrates stochastic stabilization even when each fixed update expands an eigenmode and a random single step can amplify mean-square error, distinguishing transient safety from long-run convergence with two algebraically sharp thresholds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
