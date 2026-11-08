# Independent mathematical audit

## correctness

PASS

The RRT growth transition is exhaustive: Δ(U,S)=(1,0) with q, (0,1) with pU/n, (0,-1) with pS/n, else (0,0). From it E S_n=ns+(p-s)R_n for s=pq/(1+p); Var U=npq; total covariance gives c_{n+1}=(1-p/n)c_n+(1+p)alpha+(b/n)R_n with alpha=pq(p²+2p-1)/(1+p)² and b=2p³q/(1+p). Dividing d_n=c_n-n alpha by R_n telescopes to c_n=n alpha+R_n[-pq-alpha+b sum_{j=1}^{n-1}(j-p)^(-1)]. Initial c1=-pq matches. Gamma asymptotic R_n~n^(-p)/Gamma(1-p) and harmonic H~log n imply one sign flip at sqrt(2)-1 and positive critical decay b n^(-p)log n/Gamma(1-p). Centered martingale recursion B=[[0,0],[p,-p]] has bounded propagator M(t)=[[1,0],[1-t^p,t^p]]; conditional covariance -> G with entries pq,-q s,p(q+s)-s²; Lindeberg follows from bounded increments; integrate M G M^T to get displayed Σ and independence only for Gaussian limit at the critical p. Independently enumerated all trees/site outcomes through n=5 at three rational p; exact covariances match formula. No finite-size sign universality or actual-count independence asserted.

## originality

PASS

PASS qualified: Gu and Yuan use precisely X_n(0) closed and X_n(1) open singleton counts, give the transition and singleton LLN; Janson supplies general small-urn Gaussian and variance theory. The specialized all-n closed-versus-singleton covariance identity, exact finite-size correction and critical n^(-p)log n cancellation were not located in those primary statements. Generic covariance machinery might imply a special case after explicit calculation, a genuine residual literature risk.

## value

PASS

Closed sites and survivor singleton clusters are two natural coupled observables in vertex-percolation fragmentation of recursive trees. The explicit all-size covariance reveals a non-obvious negative/positive correlation phase transition and a fine positive vanishing covariance at the exact zero-Gaussian-correlation threshold. This structural dependence law is useful beyond a generic CLT or first-moment law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
