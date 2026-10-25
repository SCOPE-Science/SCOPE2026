# Independent mathematical audit

## correctness

PASS

Generic Gaussian maximization fills positive coordinates in decreasing order with n,n-1,..., stopping at min(n,#positive). Thus ranks s<n have individual cone probability 2^-m/s!, and saturated rank s=n<=m has probability Pr(Bin(m,1/2)>=n)/(m!/(m-n)!). These probabilities sum over all vertex orbits to one. Layer cake on sorted Gaussian coordinates yields E h_P(G)=integral E[r(2n-r+1)/2] dt with r=min(n,Bin(m,1-Phi(t))), hence mean width 2 E h/R_m. Under n/m->rho, dominated convergence gives F(rho)=integral [rho min(rho,q(t))-min(rho,q(t))²/2]dt; for rho<.5 differentiate at z=Phi^-1(1-rho) to get erfc(z)/(2 sqrt(pi)), and for rho>=.5 the linear branch. Left W′=2phi(z), W″=2z, W‴=-2/phi(z); right W‴=0, so third derivative jump -2sqrt(2pi). Binomial CLT gives rank limit min(Z/2,tau) at n=m/2+tau sqrt(m)+o(sqrt(m), with atom 1-Phi(2tau). Independently checked direct support optimization in 1700 finite parameter/test-vector instances and finite normal-cone combinatorics; limit relies on proof not finite runs.

## originality

PASS

Best-of-knowledge originality established for the final exact claim, not for known supporting formulas: searched published Resultary records and compared actual mathematical statements, same-object literature, reductions and stronger plausible frameworks; this PASS is conditional on the explicitly documented access/priority risks.

## value

PASS

The complete geometric Gaussian normal-angle census, exact mean-width integral and a sharp third-order aspect-ratio transition are motivated invariants of the standard partial permutohedron, including a distributional critical window absent from ordinary face counting or ellipsoid descriptions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
