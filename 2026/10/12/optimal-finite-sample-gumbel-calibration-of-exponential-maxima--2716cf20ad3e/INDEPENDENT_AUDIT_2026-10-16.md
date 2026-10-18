# Independent mathematical audit

## correctness

PASS

For all integers n>=1, W_n=exp(-Z_n)=n min_i exp(-X_i) has density (1-w/n)^(n-1), 0<w<n, so E exp(-tZ_n)=n^(t+1)B(t+1,n) and E Z_n=H_n-log n. Differentiating forward KL to unrestricted Gumbel(location mu, inverse scale t>0), minimizing first over mu, gives F_n(t)=1/n+(t-1)(H_n-log n)-log t+log A_n(t). Its derivative H_n-1/t-sum_{j=1}^n 1/(t+j) and strictly positive second derivative ensure the unique t_n>1; F_n' at 1 is -1/(n+1), and F_n' at infinity is H_n>0. The consecutive-n derivative comparison gives t_{n+1}<t_n, with t_1=(1+sqrt(5))/2. The mean-value theorem gives n(t_n-1)->6/pi^2; Taylor at 1 gives n^2 KL_min->1/2-3/pi^2. The support lower bound makes reverse KL infinite; no reverse-KL claim. Independent bisection at n=1,2,10,30,100,1000 verifies roots and n^2 risk approaching ~0.196036, but does not prove the all-n limits.

## originality

PASS

Best-of-knowledge original exact claim after comparison of named equivalent formulations, stronger results, exact tables and prior implications; disclosed residual literature risks.

## value

PASS

The exact unrestricted finite-sample information projection of the exponential maximum onto the two-parameter Gumbel family is a natural statistical calibration problem. The sharp loss reduction from 1/2 to 1/2-3/pi^2, uniqueness and explicit t_n equation provide a useful non-routine quantitative refinement of entropic extreme-value convergence, with sharp finite-n boundaries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
