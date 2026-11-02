# Independent mathematical audit

## correctness

PASS

For uniform binary shuffles with positive fixed class sizes a,b and N=a+b, runs R=1+sum_{j=1}^{N-1} 1{X_j != X_(j+1)} and Q=sum_{t=1}^{N-1}(N*A_t-a*t)^2 give the correctly scaled two-sample CvM statistic T=Q/(ab*N^2). Conditioning on a transition at j makes its two letters a fair 01/10 orientation independent of the uniform remaining (a-1,b-1) shuffle. The hypergeometric mean and variance yield the explicit quadratic conditional influence delta_j, summing to N(N-1)(N-2ab)/6 and exact Cov(R,T)=(N-2ab)/(3N^2), negative for N>=3; N=2 has R constant. Classical Var R=2ab(2ab-N)/(N^2(N-1)), empirical finite-population Brownian-bridge convergence, and uniform integrability of T^2 give Var T->1/45 when a/N->p in (0,1), hence sqrt(N)Corr(R,T)->-sqrt(5) independently of p. Independently exhaustively enumerated all binary words for 36 positive-composition pairs with 2<=N<=9, verifying exact finite covariance. These checks do not prove all N or the functional CLT; the supplied conditional moment argument and classical bridge theorem do.

## originality

PASS

The Wald–Wolfowitz run count, Anderson two-sample CvM and its marginal distribution are classical, and the Resultary fixed-composition local-transition result already determines run-indicator covariances. None of these inspected marginal/local statements yields the exact mixed moment E[R*Q] without a conditional bridge analysis or its sharp -sqrt5 normalized correlation rate. An earlier joint calculation under different test-statistic notation remains a substantial priority risk.

## value

PASS

The exact sign and finite-size covariance quantify a nontrivial interaction between two standard distribution-free goodness-of-fit statistics, and the sample-allocation-independent -sqrt5 correlation coefficient at N^(-1/2) is a natural calibration fact for simultaneous runs/CvM inference. This is not a full joint law, but the exact mixed moment has independent statistical use.

The dated certificate retains the supplied scientific assessment, sources and limitations.
