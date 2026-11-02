# Independent mathematical audit

## correctness

PASS

Root-of-unity orthogonality yields F_N=(-1)^N N P_N(z^N)/(1-z^N)^N, with P_N coefficients [t^(jN)](1+...+t^(N-1))^N. Reciprocal symmetry follows by exponent complementation. The derivative recurrence mP_(N,m+1)=((N-m)(1-w)+mNw)P_(N,m)+Nw(1-w)P'_(N,m) has alternating signs on the negative simple roots, and endpoint signs insert the left and right roots; induction gives N-1 distinct negative roots at m=N. Even N yields a unique w=-1 root by reciprocal parity; odd N has none. For fixed j, binomial/Stirling dominance yields a_(N,j)~beta_j^N/sqrt(2pi j(j+1)N) for j>=1; the j=0 exception produces the sqrt(N) prefactor. Strict logarithmic concavity of beta_j establishes separated exponential monomial rates; a uniform geometric entropy tail justifies Rouche, then Hurwitz isolates kth negative root near -a_(k-1)/a_k. This proves the fixed-k asymptotic but NOT uniformity for k growing with N. Our independent exact coefficient and negative-root isolation checks covered N=3..10 (60 checks). Minor expository slip: x log x is convex, not concave; the required concavity of its successive increments/log beta_j follows instead from decreasing second difference or a direct monotonicity proof; this does not invalidate the separation.

## originality

PASS

Qualified PASS for coupled diagonal N increasing simultaneously with Cauchy-jet order and Veronese dilation, with sharp fixed-rank exponential root prefactors. Classical real-rootedness, interlacing and reciprocal symmetry of Veronese/Ehrhart numerators are expressly prior art; Brenti–Welker and Jochemko primarily fix polynomial dimension before dilation tends to infinity. Duran treats ordinary Eulerian/Bell zeros. An older uniform Euler–Frobenius or log-concave polynomial root estimate at coupled degree/rank could dominate; explicitly retained as residual risk.

## value

PASS

PASS: locating the first persistent rings of zeros of a natural high-order Cauchy transform gives a nontrivial transition in a coupled scaling where both number of poles and jet order diverge. Exact limits 1/4,16/27,729/1024 and nonuniform prefactors distinguish ranks and are not consequences of simple negative real-rootedness. The normalisation and low-ring boundary are mathematically motivated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
