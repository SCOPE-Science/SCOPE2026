# Independent mathematical audit

## correctness

PASS

Given K=k the support is a uniform k-subset and the labeled draw map is uniformly surjective. Identifying two positions gives collision probability S(b-1,k)/S(b,k), so E[W_i^2]=(1+(b-1)a)/(Nb) and E[W_iW_j]=(b-1)(1-a)/(N(N-1)b). Centering data and using sum y_i=0 yields the conditional coefficient [N-b+N(b-1)a]/(Nb) of unbiased s_N^2. Direct multinomial absent-cell indicators yield Cov(K,centered-mean-square)=-(b-1)/(b(N-1))((N-1)/N)^b s_N^2. Independent enumeration of all N^b=256 sequences for N=b=4, with values 0,3,8,15, reproduces four support-variance coefficients and the covariance -1323/1024; b=1, k=1 and k=b boundaries considered. Finite enumeration supplements exact all-N,b proof.

## originality

PASS

Rao–Pathak–Koltchinskii sequential bootstrap and later fixed-support variants discuss support-size randomness but change stopping rules and study asymptotics, rather than calculate the classical fixed-b ordinary bootstrap conditional mean-square and its exact covariance. These known ideas motivate the distinct conditional finite-statistic identity. Search found no exact equivalent under occupancy/surjection aliases; priority remains best-of-knowledge.

## value

PASS

Number of represented original observations is a natural effective-sample-information measure in bootstrap resampling. Exact finite conditional variance and negative covariance quantify heteroscedasticity across support strata, including nonstandard b≠N, and can inform diagnostics beyond generic asymptotic correctness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
