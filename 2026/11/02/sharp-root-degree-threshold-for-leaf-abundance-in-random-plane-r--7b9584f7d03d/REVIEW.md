# Independent mathematical audit

## correctness

PASS

The uniform increasing ordered plane recursive tree has (2n-3)!! equiprobable insertion histories, with the exact EGF differential identity T_z=u+T/(1-T), T(z,1)=1-sqrt(1-2z). Differentiation at u=1 gives U=((1-2z)^(-1/2)-(1-2z))/3. The coefficient [z^{n-1}]T^r and ratio of [z^{n-1}]rT^{r-1}U yield E[L|R=r]=(2m+r)/3-2(r+1)(m-r)/(3(2m-r-1)), m=n-1. Subtract E L=(2m+1)/3 for bias ((r+1)^2-4m)/(3(2m-r-1)); strict increasing difference follows from positive rational expression for r<m, and zero iff m=k²,r=2k-1,k>=2. The disjoint root-gap and leaf-gap insertion events imply covariance recursion c_{t+1}=c_t+(w_{t+1}-w_t)/3, w_t=4^{t-1}/binom(2t-2,t-1), hence Cov(R,L)=(w_n-2)/3. Exact marginal second moments justify correlation ~sqrt(pi/(4-pi))/sqrt(n); all endpoints n>=3 and r=m verified. Independent exact DP through n=24 confirmed every conditional mean and covariance.

## originality

PASS

Mahmoud–Smythe–Szymański (1993) is extremely relevant: via authorized access its entire 26-page text was inspected. Section 2 gives root outdegree marginal moments and Section 3 gives leaves marginals, while Sections 5–7 analyze branch leaves conditional on branch SIZE, not the whole-tree leaf count conditional on root DEGREE. No same mixed regression, threshold r+1=2sqrt(n-1), or mixed covariance is stated there. Janson (2008) maps leaves to Stirling-permutation plateaux and root to top-level factors, but analyzed other joint triples. Acan–Hitczenko (2014) concerns counts of all nodes with fixed outdegree, not distinguished root degree. Resultary’s closest root-leaf covariance concerns uniform-parent recursive trees with covariance tending 1/2, not plane increasing trees with covariance O(sqrt n). Priority qualified against uninspected multivariate generating function literature.

## value

PASS

The distinguished root branching degree and total leaves are canonical observables in preferential attachment plane recursive trees. The sharp square-root conditional sign transition and exact neutral family provide finite-sample conditioning information unattainable from root and leaf marginals alone. Exact covariance and vanishing correlation quantify a nontrivial global-local relationship in a classical random-tree model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
