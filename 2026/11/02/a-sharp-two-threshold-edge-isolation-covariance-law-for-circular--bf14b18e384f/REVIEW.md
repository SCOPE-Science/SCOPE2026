# Independent mathematical audit

## correctness

PASS

Conditional on vertex 1 being isolated, the remaining n-1 iid uniform locations occupy the complement of its radius-r arc, a contiguous arc of length L=1-2r; the alternate circular route is >=2r and cannot create another edge. Conditional probability two other locations connect is q=1-[max(L-r,0)/L]^2 by diagonal-band area in L-by-L square. E[E|isolated]=binom(n-1,2)q and E[E]=binom(n,2)*2r; exchangeability gives exact Cov(I,E)=n(n-1)L^(n-1)[-2r+(n-2)(q-2r)/2]. Sympy independently refactored the bracket: for r<=1/3 it is r[-4+(3n+10)r-8nr^2]/[2(1-2r)^2], and for r>=1/3 it is (n-2)/2-nr. The polynomial discriminants/boundaries prove negative for n<=5, two simple zeros for n>=6 at r_- and r_+=1/2-1/n, positive between. For n=6 first factor -2r(3r-1)(4r-1)/(1-2r)^2. The expansion r=c/n yields e^(-2c)(3c^2/2-2c) for Cov/n. Source verifier exact rational geometric identities and grids are supplementary.

## originality

PASS

Prior geometric random graph papers supply isolation/connectivity asymptotics, isolated-node variance, or edge-count large deviations, not the same exact fixed-n mixed edge-isolation covariance for a HARD CIRCLE with binomial n input and the complete sign-window two-root theorem. General RGG moment formulas are a residual equivalent-formulation risk, though they do not explicitly resolve signs from inspected sources.

## value

PASS

Isolated vertices and edge count are fundamental sparse connectivity and density observables. Their covariance is always strictly negative in independent-edge G(n,p) but reverses sign over a sharply characterized spatial-radius window from n=6 onward. Both radius thresholds and sparse 4/3 scale are naturally interpretable, making the exact sign phase diagram useful rather than a gratuitous moment calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
