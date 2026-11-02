# Independent mathematical audit

## correctness

PASS

The theorem concerns B_n(j,k)=binom(n,k)(j/n)^k(1-j/n)^(n-k) including endpoints. Parseval independently gives r_n(x)=pi^-1 int_0^pi (1-4x(1-x)sin²(t/2))^n dt. For u=nx(1-x)>=1/2, n>=4u and the log inequality 0<=e^{-nq}-(1-q)^n<=nq²e^{-nq} (q<=1/2), plus sin(t/2) comparison and exponentially small q>1/2, give |r_n(x)-(4pi u)^-1/2|<=C u^-3/2. At j<=n/2, Le Cam binomial–Poisson TV <=j²/n yields |r_n(j/n)-e^{-2j}I0(2j)|<=4j²/n; the opposite side is symmetric. The error relative to g_{n,j} is C min(j,n-j)^-3/2 and thus summably bounded. Cutoff K=floor(n^(2/7)) makes the endpoint/bulk error O(n^-1/7). Subtracting x^-1/2+(1-x)^-1/2 from [x(1-x)]^-1/2 produces h with integrable derivative, giving sum g_{n,j}=sqrt(pi*n)/2+zeta(1/2)/sqrt(pi)+O(n^-1/2). The two endpoint rows are exactly 2 and each Poisson correction contributes a convergent sum. Independent exact rational energies for n=2,3,4,5,10 and separate stable log-gamma binomial calculations n=128,256,512,1024,2048 confirmed the predicted limit numerically. Numerical residuals at n=512,1024,2048 are 1.2756347548,1.2799016279,1.2829274156 versus C_B about 1.29025656; these finite checks do not prove the limit. No issue found in endpoint n>=1, normalization or quantifiers.

## originality

PASS

Qualified best-of-knowledge PASS after independent Resultary and public literature searches and primary full-text comparisons. Known Raşa identities cover the rowwise binomial/Poisson collision integrals, and Marco–Martínez covers Bernstein–Vandermonde singular-value numerical methods. The precise full-grid square-energy asymptotic, nonzero Poisson–Bessel plus zeta correction, and O(n^-1/7) rate were not implied by inspected statements. Search failure is not novelty proof; older Markov-chain trace or Bernstein approximation sources remain a residual risk.

## value

PASS

The squared Hilbert–Schmidt/Schatten-2 norm of the full natural Bernstein collocation matrix is a mathematically motivated total spectral-energy invariant. The normal-density bulk predicts only the sqrt(n) term; persistent Poisson endpoint layers and the singular Riemann-sum zeta term yield the independently useful exact order-one correction. This is a quantified infinite-dimensional mesh asymptotic with absolute error, not routine substitution of a known pointwise collision limit or an arbitrary finite slice. No downstream general theorem or optimized rate is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
