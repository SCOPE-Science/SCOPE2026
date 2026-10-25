# Independent mathematical audit

## correctness

PASS

For the observed vertex Markov chain, a root neighbor has reset and ordinary-edge probability combined into r+a, a=(1-r)/k; direct row entropy subtraction is positive Delta=(r+a)log(r+a)-rlog r-a log a. Weighted stationary averaging yields h=B-rho Delta. The resolvent pi=r sum (1-r)^t delta_o P^t and regularity identity P^{t+1}(o,o)=P^t(o,N(o))/k give rho=kr/z(G_G(z)-1). Every closed tree walk maps injectively into closed G-walks, strictly for finite cyclic G at some t; monotone Green function gives strict finite upper bound by k-regular tree. Tree first return formula yields the explicit Green radical. For high girth g, finite and infinite tree walks agree through floor((g-1)/2); a uniform bound Delta(r)(1-r)^{m+1} goes to zero, including small r by Delta(r)->0. r downarrow0 expansion has positive coefficient 1-k/|V| in r log(1/r) so finite max exceeds log k. Independent exact-rational stationary calculations on K3,C4,K4 at rates 0.1,0.33,0.8 match observed entropy and corrected formula to 1e-13; infinite high-girth limit is analytic, not numerical.

## originality

PASS

The directly prior Wang--Chen random-walk-reset entropy model is mathematically the same, so this is not a claim to have invented the chain or basic conditional entropy formula. The claimed distinction is that their published regular-graph B_k expression counts labeled reset/hop actions instead of overlapping observed vertex destinations. The corrected collision term and strictly lower optimal universal-cover/high-girth envelope are not consequences of B_k alone. Same mathematical model full paper was not accessible during this run beyond primary abstract/metadata, so exact paper-wide comparison remains a named priority risk, not an assertion of noncoverage based on an abstract.

## value

PASS

Correcting an observed-state entropy-rate identity changes the attainable maximum on every finite regular graph; the exact universal-cover envelope and uniform large-girth extremal approximation answer a natural sharp stochastic-graph optimization problem. The theory differentiates observable vertex entropy from hidden-action entropy, with both a useful counterexample and all-k structural asymptotics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
